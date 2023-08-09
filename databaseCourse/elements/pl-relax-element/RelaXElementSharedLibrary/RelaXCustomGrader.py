from difflib import SequenceMatcher
import requests

# weights for input and oututbased grading
outputScoreWeight = 0.85
inputScoreWeight = 0.15

#threshold for how close input matching needs to be for a correct answer
#above which the student is given a score of 100%
threshold = 0.75


# Uses Python's SequenceMatcher library to check the
# similarity between the correct answer and the student's
# submitted answer.
def customGrader(data):
    
    feedback = True
    
    if (data['params']['feedback'] is False):
        feedback = False
        data['params']['queryFeedback'] = "Your instructor has disabled feedback for this question."
    
    outputScore = gradeQuery(data, feedback)
    inputScore = 0
    
    submittedAnswer = data['submitted_answers']['RelaXEditor']
    correctAnswer = data['correct_answers']['RelaXEditor']
    
    # Strips both of whitespace
    stripSA = submittedAnswer.strip()
    stripCA = correctAnswer.strip()
    
    # Normalize and split the strings into lists of words
    wordsSA = sorted(stripSA.split())
    wordsCA = sorted(stripCA.split())
    
    # Uses the sequence checker to check similatiry between
    # the submission and answer. It returns a number between
    # 0 and 1. 1 means the strings are identical and 0 is
    # the strings are entirely different.
    similarity = similar(wordsSA, wordsCA)

    # If the similarity between the submission and answer
    # is above the threshold, the student is given full credit
    if outputScore == 1:
        inputScore = 1
    elif similarity > threshold:
        inputScore = 1
    # Otherwise, the student is given a grade that reflective of
    # how close they are. The function linearly maps (0, $threshhold)
    # onto (0, 1) such that is the student gets exactly $threshold
    # they receive a score of 1 (full credit) and if they get a
    # similarity of 0 they recieve a score of 0. 
    else:
        inputScore = similarity / threshold
        
    if type(outputScore) == str:
        global outputScoreWeight
        outputScoreWeight = 0.15
        global inputScoreWeight
        inputScoreWeight = 0.85
        if (feedback):
            data['params']['queryFeedback'] = "Query was unable to execute. Scoring done through input matching. <br>"
            data['params']['queryFeedback'] += f"Input Score: {inputScore*100:.2f}% <br>"
            data['params']['queryFeedback'] += f"Execution Penalty: {outputScoreWeight*100:.2f}% <br>"
        outputScore = 0
        
    totalScore = outputScore * outputScoreWeight + inputScore * inputScoreWeight
    
    totalScore = max(totalScore, 0)
        
    return totalScore


# Returns the similarity between two strings.
# 1 means that the strings are identical.
# 0 means the strings are entirely different.
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def gradeQuery(data, feedback):
    
    score = 0
    
    # grading weight for each component of statement
    orderWeight = 0.05
    rowWeight = 0.20
    colWeight = 0.25
    valueMatchWeight = 0.50


    # change to and test 'db_initialize_insert_backend'
    #print(data['params']['database'])
    #print(data['params']['db_initialize_create'])
    db = data['params']['database']

    submittedAnswer = data['submitted_answers']['RelaXEditor']
    correctAnswer = data['correct_answers']['RelaXEditor']

    #url = f"http://relaxAPI:3001/index"
    url = data['params']['url']
    #print(url)

    # Construct the data to be sent in the POST request
    data_to_send = {
    "database": db,
    "submittedAnswer": submittedAnswer,
    "correctAnswer": correctAnswer
    }
    
    try:

        response = requests.get(url, json=data_to_send)

        # Assuming the server returns JSON data containing the processed result
        response_data = response.json()

        # Process the response data as needed
        queriedSA = response_data.get('queriedSA', None)
        queriedCA = response_data.get('queriedCA', None)

    except Exception as e:
        print("Error:", str(e))
        return "error"
    

    if ('error' in queriedSA or 'error' in queriedCA):
        return "error"
        
    #row matching
    rowData = rowMatch(queriedSA['rows'], queriedCA['rows'])
    rowScore = rowData['score']
    totalRowsSA = rowData['totalRowsSA']
    totalRowsCA = rowData['totalRowsCA']

    

    #col matching
    colData = colMatch(queriedSA['schema']['_names'], queriedCA['schema']['_names'])
    colScore = colData['score']
    totalColsSA = colData['totalColsSA']
    totalColsCA = colData['totalColsCA']
    missingCols = colData['missingCols']
    
    #value matching
    valueData = valueMatch(queriedSA['rows'], queriedCA['rows'])
    valueScore = valueData['score']
    totalValuesSA = valueData['totalValuesSA']
    totalValuesCA = valueData['totalValuesCA']
    
    
    #order matching
    orderScore = orderMatch(queriedSA['rows'], queriedCA['rows'])
    order = "Correct" if orderScore == 1 else "Incorrect"
    
    if (feedback):
        data['params']['queryFeedback'] = "<em>Category: [actual / expected]</em>  <br>"
        addFeedback(data, "rows", totalRowsSA, totalRowsCA)
        addFeedback(data, "columns", totalColsSA, totalColsCA)
        if missingCols:
            data['params']['queryFeedback'] += f"missing columns: {missingCols}<br>"
        addFeedback(data, "values", totalValuesSA, totalValuesCA)
        addFeedback(data, "order", order, "Correct")

    
    score = (rowScore * rowWeight) + (colScore * colWeight) + (valueScore * valueMatchWeight) + (orderScore * orderWeight)
    score = round(score, 2)
    return score

# HELPERS ----------------------------------------------------------------------------------------------------------------------
# scores the difference in the number of rows between both outputs
def rowMatch(rowsSA, rowsCA):
    
    #taken from SQL customgrader

    
    totalRowsSA = 0
    totalRowsCA = 0
    
    expectedRowsCA = len(rowsCA)
    totalRowsCA += expectedRowsCA
    
    rowCountSA = len(rowsSA)
    totalRowsSA += rowCountSA
    
    if (totalRowsCA != 0):
        missingRows = abs(totalRowsCA - rowCountSA)
        correctRows = totalRowsCA - missingRows
        rowScore = correctRows / totalRowsCA
    elif (totalRowsCA == 0 and totalRowsSA == 0):
        rowScore = 1
    else:
        rowScore = 0
    
    #if not (rowsCA or rowsSA): rowScore = 1
    #if not rowsSA or not rowsSA[0]: rowScore = 0
    
    rowData = {
        'score': rowScore,
        'totalRowsSA': totalRowsSA,
        'totalRowsCA': totalRowsCA
    }
    
    
    return rowData
    
    
# scores the difference in the number of columns between both outputs
def colMatch(colsSA, colsCA):
    
    totalColsSA = 0
    totalColsCA = len(colsCA)
    missingColsList = []
    
    #+1 point for each correct column
    for col in colsCA:
        if col in colsSA:
            totalColsSA += 1
        else:
            missingColsList.append(col)
            
    missingCols = abs(totalColsCA - totalColsSA)
    correctCols = totalColsCA - missingCols
    colScore = correctCols / totalColsCA
    
    colData = {
        'score': colScore,
        'totalColsSA': totalColsSA,
        'totalColsCA': totalColsCA,
        "missingCols": missingColsList
    }
    
    return colData

# scores how much the values match between the expected ans and the actual ans
def valueMatch(valueSA, valueCA):
    
    totalValuesSA = 0
    totalValuesCA = len(valueCA)
    commonValues = 0
    
    for row in valueSA:
        if row in valueCA:
            commonValues += 1

    if totalValuesCA != 0:
        missingVals = abs(totalValuesCA - commonValues)
        correctVals = totalValuesCA - missingVals
        valueScore = correctVals / totalValuesCA
    elif totalValuesCA == 0 and totalValuesSA == 0:
        valueScore = 1
    
    totalValuesSA = commonValues
    
    valueData = {
        'score': valueScore,
        'totalValuesSA': totalValuesSA,
        'totalValuesCA': totalValuesCA
    }
    
    return valueData

# checks if rows are ordered the same direction as the correct answer
def orderMatch(valueSA, valueCA):
    
    numRowsSA = len(valueSA)
    numRowsCA = len(valueCA)
    
    # if either list is empty, return 1
    if numRowsSA == 0 or numRowsCA == 0:
        return 1

    # if either list has 1 row, return 1 if it's a match, otherwise 0
    if numRowsSA == 1 or numRowsCA == 1:
        for rowCA in valueCA:
            if rowCA in valueSA:
                return 1
        return 0
    
    try:
        return checkOrder(valueSA, valueCA)
    except:
        return 0

#helper function for ordermatch
def checkOrder(valueSA, valueCA):
    
    # Convert rows to tuples for comparison
    valueCA_tuples = [tuple(row) for row in valueCA]
    valueSA_tuples = [tuple(row) for row in valueSA]

    # if ascending
    if valueCA_tuples[0] < valueCA_tuples[-1]:
        if valueSA_tuples[0] < valueSA_tuples[-1]:
            return 1
        else:
            return 0
    # if descending
    elif valueCA_tuples[0] > valueCA_tuples[-1]:
        if valueSA_tuples[0] > valueSA_tuples[-1]:
            return 1
        else:
            return 0
    


def addFeedback(data, category, submitted, correct):
    data['params']['queryFeedback'] += f"{category} : [{submitted} / {correct}] <br>"
from difflib import SequenceMatcher
import requests

# weights for input and oututbased grading
outputScoreWeight = 0.85
inputScoreWeight = 0.15

# if query can't execute, receive penalty
executionFailPenalty = 0.5

#threshold for how close input matching needs to be for a correct answer
#above which the student is given a score of 100%
threshold = 0.75


# Uses Python's SequenceMatcher library to check the
# similarity between the correct answer and the student's
# submitted answer.
def customGrader(data):
    
    
    outputScore = gradeQuery(data)
    inputScore = 0
    
    if outputScore == 0:
        global outputScoreWeight
        outputScoreWeight = 0.15
        global inputScoreWeight
        inputScoreWeight = 0.85
    
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
    if similarity > threshold:
        inputScore = 1
    # Otherwise, the student is given a grade that reflective of
    # how close they are. The function linearly maps (0, $threshhold)
    # onto (0, 1) such that is the student gets exactly $threshold
    # they receive a score of 1 (full credit) and if they get a
    # similarity of 0 they recieve a score of 0. 
    else:
        inputScore = similarity / threshold
        
    return (outputScore * outputScoreWeight + inputScore * inputScoreWeight)


# Returns the similarity between two strings.
# 1 means that the strings are identical.
# 0 means the strings are entirely different.
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def gradeQuery(data):
    
    score = 0
    feedback = True
    
    # grading weight for each component of statement
    orderWeight = 0.05
    rowWeight = 0.10
    colWeight = 0.25
    valueMatchWeight = 0.6
    
    db = data['params']['database']
    submittedAnswer = data['submitted_answers']['RelaXEditor']
    correctAnswer = data['correct_answers']['RelaXEditor']

    host_ip = "localhost"
    url = f"http://{host_ip}:3000/ra_autoGrader"

    # Construct the data to be sent in the POST request
    data_to_send = {
    "database": db,
    "submittedAnswer": submittedAnswer,
    "correctAnswer": correctAnswer
    }
    
    try:
        
        # print("Url:", url)
        # print("Data: ",data_to_send)

        response = requests.get(url, json=data_to_send)
        
        # print("Response: ", response)
        # print("Response status code:", response.status_code)
        # print("Response text:", response.text)

        # Assuming the server returns JSON data containing the processed result
        response_data = response.json()
        
        #print("Response data: ", response_data)

        # Process the response data as needed
        queriedSA = response_data.get('queriedSA', None)
        queriedCA = response_data.get('queriedCA', None)


        print("QueriedSA:", queriedSA)
        print("QueriedCA:", queriedCA)

    except Exception as e:
        print("Error:", str(e))
        return score
    
    if ('error' in queriedSA or 'error' in queriedCA):
        return score
        
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
    orderScore = 0
    
    if (feedback):
        data['params']['feedback'] = "<em>Category: [actual / expected]</em>  <br>"
        addFeedback(data, "rows", totalRowsSA, totalRowsCA)
        addFeedback(data, "columns", totalColsSA, totalColsCA)
        if missingCols:
            data['params']['feedback'] += f"Missing columns: {missingCols}<br>"
        addFeedback(data, "values", totalColsSA, totalValuesCA)
        addFeedback(data, "order", "desc", "asc")

    
    score = (rowScore * rowWeight) + (colScore * colWeight) + (valueScore * valueMatchWeight) + orderScore
    score = round(score, 2)
    return score

# HELPERS ----------------------------------------------------------------------------------------------------------------------
# scores the difference in the number of rows between both outputs
def rowMatch(rowsSA, rowsCA):
    
    totalRowsSA = 0
    totalRowsCA = 0
    
    expectedRowsCA = len(rowsCA)
    totalRowsCA += expectedRowsCA
    
    #taken from SQL customgrader
    if not (rowsCA or rowsSA): return 1
    if not rowsSA or not rowsSA[0]: return 0
    
    rowCountSA = len(rowsSA)
    totalRowsSA += rowCountSA
    
    missingRows = abs(totalRowsCA - totalRowsSA)
    correctRows = totalRowsCA - missingRows
    rowScore = correctRows / totalRowsCA
    
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
    for x in colsCA:
        if x in colsSA:
            totalColsSA += 1
        else:
            missingColsList.append(x)
            
    
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
    
    #+1 point for each correct value
    for x in valueCA:
        if x in valueSA:
            totalValuesSA += 1
            
    missingVals = abs(totalValuesCA - totalValuesSA)
    correctVals = totalValuesCA - missingVals
    valueScore = correctVals / totalValuesCA
    
    valueData = {
        'score': valueScore,
        'totalValuesSA': totalValuesSA,
        'totalValuesCA': totalValuesCA
    }
    
    return valueData

def addFeedback(data, category, submitted, correct):
    data['params']['feedback'] += f"{category} : [{submitted} / {correct}] <br>"

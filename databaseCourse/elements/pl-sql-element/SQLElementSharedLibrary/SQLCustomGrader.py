from difflib import SequenceMatcher
import sqlite3
import os

# Uses Python's SequenceMatcher library to check the
# similarity between the correct answer and the student's
# submitted answer.
def customGrader(data):
    # weights for input and oututbased grading
    data['params']['feedback'] = ""
    outputScoreWeight = 0.85
    inputScoreWeight = 0.15

    # Grabs the student answer from data
    submittedAnswer = data['submitted_answers']['SQLEditor']

    # Grabs the solution from data
    correctAnswer = data['correct_answers']['SQLEditor']
    
    # Strips both of whitespace
    stripSA = submittedAnswer.strip()
    stripCA = correctAnswer.strip()

    # # Normalize and split the strings into lists of words
    wordsSA = sorted(stripSA.split())
    wordsCA = sorted(stripCA.split())

    questionType = data["params"]["html_params"]["questionType"]

    outputScore = 0
    inputScore = 0

    if os.path.exists("ans.db"):
        os.remove("ans.db")
    if os.path.exists("ans2.db"):
        os.remove("ans2.db")

    # if student makes a typo, the grading is shifted so that the input is weighted more than the output
    # partial grading for lab 2 - Create Questions
    if(questionType == "create"):
        try:
            outputScore += gradeCreateQuestion(data,correctAnswer,submittedAnswer)
        except sqlite3.OperationalError as e:
            if "syntax error" in str(e).lower():
                outputScoreWeight = 0.15
                inputScoreWeight = 0.85
    
    # partial grading for lab 2 - Insert Questions
    if(questionType == "insert"):
        try:
            outputScore += gradeInsertQuestion(data,correctAnswer,submittedAnswer)
        except sqlite3.OperationalError as e:
            if "syntax error" in str(e).lower():
                outputScoreWeight = 0.15
                inputScoreWeight = 0.85

    # partial grading for lab 2 - Update Questions
    if(questionType == "update"):
        try:
            outputScore += gradeUpdateQuestion(data,correctAnswer,submittedAnswer)
        except sqlite3.OperationalError as e:
            if "syntax error" in str(e).lower():
                outputScoreWeight = 0.15
                inputScoreWeight = 0.85

    # partial grading for lab 2 - Delete Questions
    if(questionType == "delete"):
        try:
            outputScore += gradeDeleteQuestion(data,correctAnswer,submittedAnswer)
        except sqlite3.OperationalError as e:
            if "syntax error" in str(e).lower():
                outputScoreWeight = 0.15
                inputScoreWeight = 0.85

    # partial grading for lab 2 - Create Questions
    if(questionType == "query"):
        try:
            outputScore += gradeQueryQuestion(data,correctAnswer,submittedAnswer)
        except sqlite3.OperationalError as e:
            if "syntax error" in str(e).lower():
                outputScoreWeight = 0.15
                inputScoreWeight = 0.85


    # Uses the sequence checker to check similatiry between
    # the submission and answer. It returns a number between
    # 0 and 1. 1 means the strings are identical and 0 is
    # the strings are entirely different.
    similarity = similar(wordsSA, wordsCA)

    # The similarity threshold above which the student is given
    # 100% score
    threshold = 0.75

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
    grade = (inputScoreWeight*inputScore) + (outputScoreWeight*outputScore)
    grade = round(grade,2)
    return grade

# Returns the similarity between two strings.
# 1 means that the strings are identical.
# 0 means the strings are entirely different.
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

# QUERY------------------------------------------------------------------------------------------------------------------------
# grades the response for a query question
def gradeQueryQuestion(data,correctAnswer,submittedAnswer):
    # grading weight for each component of statement
    orderWeight = 0.05
    rowWeight = 0.10
    colWeight = 0.25
    valueMatchWeight = 0.6

    # gets outputs in proper formatting
    arr = getExpectedAndActualQueryResults(data,correctAnswer,submittedAnswer)

    expectedAns = arr[0]
    actualAns = arr[1]

    # row matching + column matching
    rowScore = rowMatch(expectedAns,actualAns)
    colScore = colMatch(expectedAns,actualAns)

    # value matching
    valueMatchScore = valueMatch(expectedAns,actualAns)

    # order matching
    orderScore = 0
    if len(expectedAns) == 0 or len(actualAns) == 0:
        return 1
    if rowScore == 1 and colScore ==1:
        if expectedAns[0] == actualAns[0] and expectedAns[-1] == actualAns[-1]:
            orderScore = 1
        
    addFeedback(data,"Rows",round(rowScore,2))
    addFeedback(data,"Columns",round(colScore,2))
    addFeedback(data,"Values",round(valueMatchScore,2))
    addFeedback(data,"Order",round(orderScore,2))

    score = (rowWeight*rowScore) + (valueMatchWeight*valueMatchScore) + (colWeight*colScore) + (orderWeight*orderScore)
    score = round(score,2)
    return score

# {}, str, str => (,)
# takes in data variable, correct ans, submitted ans, runs the queries and returns the output in proper formatting
# compares query results of solution and submission
def getExpectedAndActualQueryResults(data,correctAnswer,submittedAnswer):
    con = sqlite3.connect("ans.db")
    cur  = con.cursor()
    
    # formats database initialization from string to SQL
    commands = data['params']['db_initialize_create'].replace('\n', '').replace('\t', '')
    commands += data['params']['db_initialize_insert_backend'].replace('\n', '').replace('\t', '')
    
    # db initialization
    cur.executescript(commands)
    con.commit()

    # format solution from string to code and execute + fetch results
    expectedCode = correctAnswer.replace('\n', ' ').replace('\t', ' ')
    expectedAns = cur.execute(expectedCode).fetchall()
    
    # format submission from string to code and execute + fetch results
    studentCode = submittedAnswer.replace('\n', ' ').replace('\t', ' ')
    actualAns = cur.execute(studentCode).fetchall()
    
    return (expectedAns,actualAns)

# CREATE------------------------------------------------------------------------------------------------------------------------
# grades create questions
def gradeCreateQuestion(data,correctAnswer,submittedAnswer):
    # gets output in proper formatting
    arr = getExpectedAndActualCreateResults(correctAnswer,submittedAnswer)

    expectedAns = arr[0]
    actualAns = arr[1]

    # value matching
    valueMatchScore = valueMatch(expectedAns,actualAns)

    addFeedback(data,"Values",round(valueMatchScore,2))

    score = valueMatchScore
    score = round(score,2)
    return score

# str, str => (,)
# takes in data variable, correct ans, submitted ans, runs the queries and returns the output in proper formatting
# compares table metadate from (tables created by solution) and (tables created by submission)
def getExpectedAndActualCreateResults(correctAnswer,submittedAnswer):
    con = sqlite3.connect("ans.db")
    cur  = con.cursor()

# correct answer execution
    # formatting from string to SQL + execution
    expectedCode = correctAnswer.replace('\n', ' ').replace('\t', ' ')
    cur.executescript(expectedCode)
    con.commit()

    # get all tables that the solution creates
    tables = cur.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
    tablesCleaned = [item[0] for item in tables]

    # gets the schema info and metadata for each table in the db after running the solution
    expectedAns = []
    for table in tablesCleaned:
        expectedAns += cur.execute("PRAGMA table_info(" + table + ")").fetchall()
        expectedAns += cur.execute("PRAGMA foreign_key_list(" + table + ")").fetchall()

# submitted answer execution
    conTwo = sqlite3.connect("ans2.db")
    curTwo  = conTwo.cursor()

    # formatting submission from string to SQL + execution
    studentCode = submittedAnswer.replace('\n', ' ').replace('\t', ' ')
    curTwo.executescript(studentCode)
    conTwo.commit()

    # gets all tables that the submission creates
    tables = curTwo.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
    tablesCleaned = [item[0] for item in tables]

    # get metadatae on tables created by submission
    actualAns = []
    for table in tablesCleaned:
        actualAns += curTwo.execute("PRAGMA table_info(" + table + ")").fetchall()
        actualAns += curTwo.execute("PRAGMA foreign_key_list(" + table + ")").fetchall()

    return (expectedAns,actualAns)

# INSERT------------------------------------------------------------------------------------------------------------------------
# all or nothing grading for insert questions
def gradeInsertQuestion(data,correctAnswer,submittedAnswer):
    # gets output in proper formatting
    arr = getExpectedAndActualInsertResults(data,correctAnswer,submittedAnswer)

    expectedAns = arr[0]
    actualAns = arr[1]

    # value matching
    valueMatchScore = valueMatch(expectedAns,actualAns)

    addFeedback(data,"Values",round(valueMatchScore,2))

    score = valueMatchScore
    score = round(score,2)
    return score

# {}, str, str => (,)
# takes in data variable, correct ans, submitted ans, runs the queries and returns the output in proper formatting
# compares (DB after executing solution inserts) to (DB after submission inserts)
def getExpectedAndActualInsertResults(data,correctAnswer,submittedAnswer):
    con = sqlite3.connect("ans.db")
    cur  = con.cursor()
    
    # formats db initialization code from string to SQL and executes
    commands = data['params']['db_initialize_create'].replace('\n', '').replace('\t', '')
    commands += data['params']['db_initialize_insert_backend'].replace('\n', '').replace('\t', '')
    cur.executescript(commands)
    con.commit()

    # gets all tables
    tables = cur.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
    tablesCleaned = [item[0] for item in tables]

    # formats solution from string to SQL
    expectedCode = correctAnswer.replace('\n', ' ').replace('\t', ' ')
    
    # executes solution and gets updated DB after all the inserts
    cur.executescript(expectedCode)
    expectedAns = []
    for table in tablesCleaned:
        expectedAns += cur.execute("SELECT * FROM " + table).fetchall()

    # re-initialize db
    conTwo = sqlite3.connect("ans2.db")
    curTwo  = conTwo.cursor()
    curTwo.executescript(commands)
    conTwo.commit()

    # format submission from string to SQL
    studentCode = submittedAnswer.replace('\n', ' ').replace('\t', ' ')

    # executes submission and gets updated DB after all the inserts
    curTwo.executescript(studentCode)
    actualAns = []
    for table in tablesCleaned:
        actualAns += curTwo.execute("SELECT * FROM " + table).fetchall()
        
    return (expectedAns,actualAns)

# UPDATE------------------------------------------------------------------------------------------------------------------------
# grades update question
def gradeUpdateQuestion(data,correctAnswer,submittedAnswer):
    # gets output in proper formatting
    arr = getExpectedAndActualUpdateResults(data,correctAnswer,submittedAnswer)
    expectedAns = arr[0]
    actualAns = arr[1]
    originalDb = arr[2]

    # checks the value match of the updates
    updateMatchVal = updateMatch(data,expectedAns,actualAns,originalDb)

    return updateMatchVal

# compares the differences between (db after running solution update code) and (db after running submission update code)
def updateMatch(data,expectedAns,actualAns,originalDb):
    rowMatchWeight = 0.5
    valMatchWeight = 0.5
    # finds the rows that have been updated when running solution
    expectedUpdatedRows = [row for row in expectedAns if row not in originalDb]
    # finds the rows that have been updated when running submission
    actualUpdatedRows = [row for row in actualAns if row not in originalDb]
    # row matching and value matching
    rowMatchScore = rowMatch(expectedUpdatedRows,actualUpdatedRows)
    valMatchScore = valueMatch(expectedUpdatedRows,actualUpdatedRows)

    addFeedback(data,"Rows",round(rowMatchScore,2))
    addFeedback(data,"Values",round(valMatchScore,2))

    score = (rowMatchScore*rowMatchWeight) + (valMatchScore*valMatchWeight)
    return score

# {}, str, str => (,)
# takes in data variable, correct ans, submitted ans, runs the queries and returns the output in proper formatting
# gives us the db when initialized, after running solution, and then after running submission for comparison of all 3
def getExpectedAndActualUpdateResults(data,correctAnswer,submittedAnswer):
    con = sqlite3.connect("ans.db")
    cur  = con.cursor()
    
    # formats db initialization code from string to SQL and executes
    commands = data['params']['db_initialize_create'].replace('\n', '').replace('\t', '')
    commands += data['params']['db_initialize_insert_backend'].replace('\n', '').replace('\t', '')
    cur.executescript(commands)
    con.commit()

    # gets all tables in db
    tables = cur.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
    tablesCleaned = [item[0] for item in tables]

    # defines the original db by fetching all its tables and rows
    originalDb = []
    for table in tablesCleaned:
        originalDb += cur.execute("SELECT * FROM " + table).fetchall()

    # executes solution
    expectedCode = correctAnswer.replace('\n', ' ').replace('\t', ' ')
    cur.executescript(expectedCode)

    # gets the database after executing the solution
    expectedAns = []
    for table in tablesCleaned:
        expectedAns += cur.execute("SELECT * FROM " + table).fetchall()
    
    # re-initialize db
    conTwo = sqlite3.connect("ans2.db")
    curTwo  = conTwo.cursor()
    curTwo.executescript(commands)
    conTwo.commit()

    # format and execute submission
    studentCode = submittedAnswer.replace('\n', ' ').replace('\t', ' ')
    curTwo.executescript(studentCode)
    conTwo.commit()

    # gets the database after executing the submission
    actualAns = []
    for table in tablesCleaned:
        actualAns += curTwo.execute("SELECT * FROM " + table).fetchall()
        
    return (expectedAns,actualAns,originalDb)

# DELETE------------------------------------------------------------------------------------------------------------------------
# grades delete questions
def gradeDeleteQuestion(data,correctAnswer,submittedAnswer):
    # gets output in proper formatting
    arr = getExpectedAndActualDeleteResults(data,correctAnswer,submittedAnswer)

    expectedAns = arr[0]
    actualAns = arr[1]
    originalDb = arr[2]

    # value matching
    deleteMatchScore = deleteMatch(data,expectedAns,actualAns,originalDb)

    score = deleteMatchScore
    score = round(score,2)
    return score

# compares the differences between (db after running solution update code) and (db after running submission update code)
def deleteMatch(data,dbAfterSolution,dbAfterSubmission,originalDb):
    rowMatchWeight = 0.5
    valMatchWeight = 0.5

    # finds the rows that have been updated when running solution
    expectedDeletedRows = [row for row in originalDb if row not in dbAfterSolution]

    # finds the rows that have been updated when running submission
    actualDeletedRows = [row for row in originalDb if row not in dbAfterSubmission]

    # row matching and value matching
    rowMatchScore = rowMatch(expectedDeletedRows,actualDeletedRows)
    valMatchScore = valueMatch(expectedDeletedRows,actualDeletedRows)

    addFeedback(data,"Rows",round(rowMatchScore,2))
    addFeedback(data,"Values",round(valMatchScore,2))

    score = (rowMatchScore*rowMatchWeight) + (valMatchScore*valMatchWeight)
    return score

# {}, str, str => (,)
# takes in data variable, correct ans, submitted ans, runs the queries and returns the output in proper formatting
# gives us the db when initialized, after running solution, and then after running submission for comparison of all 3
def getExpectedAndActualDeleteResults(data,correctAnswer,submittedAnswer):
    con = sqlite3.connect("ans.db")
    cur  = con.cursor()
    
    # formats db initialization code from string to SQL and executes
    commands = data['params']['db_initialize_create'].replace('\n', '').replace('\t', '')
    commands += data['params']['db_initialize_insert_backend'].replace('\n', '').replace('\t', '')
    cur.executescript(commands)
    con.commit()

    # gets all tables in db
    tables = cur.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
    tablesCleaned = [item[0] for item in tables]

    # defines the original db by fetching all its tables and rows
    originalDb = []
    for table in tablesCleaned:
        originalDb += cur.execute("SELECT * FROM " + table).fetchall()

    # executes solution
    expectedCode = correctAnswer.replace('\n', ' ').replace('\t', ' ')
    cur.executescript(expectedCode)

    # gets the database after executing the solution
    expectedAns = []
    for table in tablesCleaned:
        expectedAns += cur.execute("SELECT * FROM " + table).fetchall()

    # re-initialize db
    conTwo = sqlite3.connect("ans2.db")
    curTwo  = conTwo.cursor()
    curTwo.executescript(commands)
    conTwo.commit()
    
    # format and execute submission
    studentCode = submittedAnswer.replace('\n', ' ').replace('\t', ' ')
    curTwo.executescript(studentCode)
    conTwo.commit()

    # gets all tables in db
    tables = curTwo.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
    tablesCleaned = [item[0] for item in tables]
    
    # gets the database after executing the submission
    actualAns = []
    for table in tablesCleaned:
        actualAns += curTwo.execute("SELECT * FROM " + table).fetchall()
    return (expectedAns,actualAns,originalDb)

# HELPERS ----------------------------------------------------------------------------------------------------------------------
# scores the difference in the number of rows between both outputs
def rowMatch(expectedAns,actualAns):
    expectedTotal = 0
    actualTotal = 0

    if not (actualAns or expectedAns): return 1
    if not actualAns or not actualAns[0]: return 0

    expectedRowCount = len(expectedAns)
    expectedTotal += expectedRowCount

    actualRowCount = len(actualAns)
    actualTotal += actualRowCount

    # for each row that the submitted answer has that is more or less than the expected answer, a point is deducted
    rowGrade = abs(expectedTotal - actualTotal)
    rowScore = (expectedTotal - rowGrade)/expectedTotal
    return rowScore

# scores the difference in the number of columns between both outputs
def colMatch(expectedAns,actualAns):
    expectedTotal = 0
    actualTotal = 0

    if not (actualAns or expectedAns): return 1
    if not actualAns or not actualAns[0]: return 0

    expectedColumnCount = len((expectedAns[0]))
    expectedTotal += expectedColumnCount
    
    actualColumnCount = len(actualAns[0])
    actualTotal += actualColumnCount

    # for each column that the submitted answer has that is more or less than the expected answer, a point is deducted
    colGrade = abs(expectedTotal - actualTotal)
    colScore = (expectedTotal - colGrade)/expectedTotal
    return colScore

# scores how much the values match between the expected ans and the actual ans
def valueMatch(expectedAns,actualAns):
    valueMatchExpectedTotal = len(expectedAns)
    valueMatchActualTotal = 0

    if valueMatchExpectedTotal == 0 and len(actualAns) == 0:
        return 1
    if valueMatchExpectedTotal == 0 and len(actualAns) != 0:
        return 0

    # +1 point per row of exact values matched
    for x in actualAns:
        if x in expectedAns:
            valueMatchActualTotal += 1

    matchScore = valueMatchActualTotal / valueMatchExpectedTotal
    return matchScore

def addFeedback(data, category, categoryScore):
    data['params']['feedback'] += f"{category} : {(round((categoryScore*100),2))}"+"%<br>"
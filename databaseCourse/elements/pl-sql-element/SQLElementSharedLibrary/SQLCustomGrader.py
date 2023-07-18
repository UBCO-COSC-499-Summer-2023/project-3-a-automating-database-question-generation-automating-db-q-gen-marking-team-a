from difflib import SequenceMatcher
import sqlite3
import os

# Uses Python's SequenceMatcher library to check the
# similarity between the correct answer and the student's
# submitted answer.
def customGrader(data):
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

    if not wordsSA: return 0

    questionType = data["params"]["html_params"]["questionType"]

    outputScore = 0
    inputScore = 0
    outputScoreWeight = 0.85
    inputScoreWeight = 0.15

    if os.path.exists("ans.db"):
        os.remove("ans.db")
    if os.path.exists("ans2.db"):
        os.remove("ans2.db")

    # partial grading for lab 2 - Create Questions
    if(questionType == "create"):
        outputScore += gradeCreateQuestion(data,correctAnswer,submittedAnswer)
    
    # partial grading for lab 2 - Insert Questions
    if(questionType == "insert"):
        outputScore += gradeInsertQuestion(data,correctAnswer,submittedAnswer)

    # partial grading for lab 2 - Update Questions
    if(questionType == "update"):
        outputScore += gradeUpdateQuestion(data,correctAnswer,submittedAnswer)

    # partial grading for lab 2 - Delete Questions
    if(questionType == "delete"):
        outputScore += gradeDeleteQuestion(data,correctAnswer,submittedAnswer)

    # partial grading for lab 2 - Create Questions
    if(questionType == "query"):
        outputScore += gradeQueryQuestion(data,correctAnswer,submittedAnswer)
    
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
    # rowColWeight = 0.3
    # number of rows is affected by things like WHERE
    # number of columns is usually what the user SELECTs
    orderWeight = 0.05
    rowWeight = 0.10
    colWeight = 0.25
    valueMatchWeight = 0.6

    arr = getExpectedAndActualQueryResults(data,correctAnswer,submittedAnswer)

    expectedAns = arr[0]
    actualAns = arr[1]

    # row + column matching
    # rowColScore = rowColMatch(expectedAns,actualAns)
    rowScore = rowMatch(expectedAns,actualAns)
    colScore = colMatch(expectedAns,actualAns)

    # value matching
    valueMatchScore = valueMatch(expectedAns,actualAns)

    # order matching
    orderScore = 0
    if rowScore == 1 and colScore ==1:
        if expectedAns[0] == actualAns[0] and expectedAns[-1] == actualAns[-1]:
            orderScore = 1

    score = (rowWeight*rowScore) + (valueMatchWeight*valueMatchScore) + (colWeight*colScore) + (orderWeight*orderScore)
    score = round(score,2)
    return score

def getExpectedAndActualQueryResults(data,correctAnswer,submittedAnswer):
    con = sqlite3.connect("ans.db")
    cur  = con.cursor()
    # print(data['params']['db_initialize'])
    commands = data['params']['db_initialize_create'].replace('\n', '').replace('\t', '')
    commands += data['params']['db_initialize_insert_backend'].replace('\n', '').replace('\t', '')
    # print(commands)
    cur.executescript(commands)
    con.commit()
    expectedCode = correctAnswer.replace('\n', ' ').replace('\t', ' ')
    # print("formatted correct ans",expectedCode)
    # print("correctans",correctAnswer)
    expectedAns = cur.execute(expectedCode).fetchall()
    # print("solution:",expectedAns)
    studentCode = submittedAnswer.replace('\n', ' ').replace('\t', ' ')
    actualAns = cur.execute(studentCode).fetchall()
    # print("submitted",actualAns)
    return (expectedAns,actualAns)

# CREATE------------------------------------------------------------------------------------------------------------------------
def gradeCreateQuestion(data,correctAnswer,submittedAnswer):
    arr = getExpectedAndActualCreateResults(data,correctAnswer,submittedAnswer)
    print(arr[0])
    print(arr[1])

    expectedAns = arr[0]
    actualAns = arr[1]

    # value matching
    valueMatchScore = valueMatch(expectedAns,actualAns)

    score = valueMatchScore
    score = round(score,2)
    return score

def getExpectedAndActualCreateResults(data,correctAnswer,submittedAnswer):
    con = sqlite3.connect("ans.db")
    cur  = con.cursor()

    expectedCode = correctAnswer.replace('\n', ' ').replace('\t', ' ')
    cur.executescript(expectedCode)
    con.commit()

    tables = cur.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
    tablesCleaned = [item[0] for item in tables]

    expectedAns = []
    for table in tablesCleaned:
        expectedAns += cur.execute("PRAGMA table_info(" + table + ")").fetchall()
        expectedAns += cur.execute("PRAGMA foreign_key_list(" + table + ")").fetchall()
    # -----------------------
    conTwo = sqlite3.connect("ans2.db")
    curTwo  = conTwo.cursor()

    studentCode = submittedAnswer.replace('\n', ' ').replace('\t', ' ')
    curTwo.executescript(studentCode)
    conTwo.commit()

    tables = curTwo.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
    tablesCleaned = [item[0] for item in tables]

    actualAns = []
    for table in tablesCleaned:
        actualAns += curTwo.execute("PRAGMA table_info(" + table + ")").fetchall()
        actualAns += curTwo.execute("PRAGMA foreign_key_list(" + table + ")").fetchall()

    return (expectedAns,actualAns)

# INSERT------------------------------------------------------------------------------------------------------------------------
# all or nothing
def gradeInsertQuestion(data,correctAnswer,submittedAnswer):
    arr = getExpectedAndActualInsertResults(data,correctAnswer,submittedAnswer)

    expectedAns = arr[0]
    actualAns = arr[1]

    # value matching
    valueMatchScore = valueMatch(expectedAns,actualAns)

    score = valueMatchScore
    score = round(score,2)
    return score

def getExpectedAndActualInsertResults(data,correctAnswer,submittedAnswer):
    con = sqlite3.connect("ans.db")
    cur  = con.cursor()
    # print(data['params']['db_initialize'])
    commands = data['params']['db_initialize_create'].replace('\n', '').replace('\t', '')
    # print(commands)

    cur.executescript(commands)
    con.commit()

    tables = cur.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
    tablesCleaned = [item[0] for item in tables]

    expectedCode = correctAnswer.replace('\n', ' ').replace('\t', ' ')
    # print("formatted correct ans",expectedCode)
    # print("correctans",correctAnswer)
    cur.executescript(expectedCode)
    expectedAns = []
    for table in tablesCleaned:
        expectedAns += cur.execute("SELECT * FROM " + table).fetchall()
    print("solution:",expectedAns)

    cur.executescript(commands)
    con.commit()
    studentCode = submittedAnswer.replace('\n', ' ').replace('\t', ' ')
    cur.executescript(studentCode)
    actualAns = []
    for table in tablesCleaned:
        actualAns += cur.execute("SELECT * FROM " + table).fetchall()
    print("submitted",actualAns)
    return (expectedAns,actualAns)

# UPDATE------------------------------------------------------------------------------------------------------------------------
def gradeUpdateQuestion(data,correctAnswer,submittedAnswer):
    arr = getExpectedAndActualDeleteOrUpdateResults(data,correctAnswer,submittedAnswer)

    expectedAns = arr[0]
    actualAns = arr[1]
    originalDb = arr[2]

    # value matching
    deleteMatchScore = deleteorUpdateMatch(expectedAns,actualAns,originalDb)

    score = deleteMatchScore
    score = round(score,2)
    return score

# DELETE------------------------------------------------------------------------------------------------------------------------
def gradeDeleteQuestion(data,correctAnswer,submittedAnswer):
    arr = getExpectedAndActualDeleteOrUpdateResults(data,correctAnswer,submittedAnswer)

    expectedAns = arr[0]
    actualAns = arr[1]
    originalDb = arr[2]

    # value matching
    deleteMatchScore = deleteorUpdateMatch(expectedAns,actualAns,originalDb)

    score = deleteMatchScore
    score = round(score,2)
    return score

def deleteorUpdateMatch(dbAfterSolution,dbAfterSubmission,originalDb):
    rowMatchWeight = 1
    valMatchWeight = 0

    expectedDeletedRows = [row for row in originalDb if row not in dbAfterSolution]
    actualDeletedRows = [row for row in originalDb if row not in dbAfterSubmission]
    print("EXPECTED",expectedDeletedRows)
    print("ACTUAL",actualDeletedRows)
    rowMatchScore = rowMatch(expectedDeletedRows,actualDeletedRows)
    valMatchScore = 0

    if(len(expectedDeletedRows) != 0):
        rowMatchWeight = 0.5
        valMatchWeight = 0.5
        valMatchScore = similar(expectedDeletedRows,actualDeletedRows)

    score = (rowMatchScore*rowMatchWeight) + (valMatchScore*valMatchWeight)
    return score

def getExpectedAndActualDeleteOrUpdateResults(data,correctAnswer,submittedAnswer):
    con = sqlite3.connect("ans.db")
    cur  = con.cursor()
    # print(data['params']['db_initialize'])
    commands = data['params']['db_initialize_create'].replace('\n', '').replace('\t', '')
    # print(commands)

    cur.executescript(commands)
    con.commit()

    tables = cur.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
    tablesCleaned = [item[0] for item in tables]
    originalDb = []
    for table in tablesCleaned:
        originalDb += cur.execute("SELECT * FROM " + table).fetchall()

    print(originalDb)

    expectedCode = correctAnswer.replace('\n', ' ').replace('\t', ' ')
    # print("formatted correct ans",expectedCode)
    # print("correctans",correctAnswer)
    print(expectedCode)
    cur.executescript(expectedCode)
    con.commit()
    expectedAns = []
    for table in tablesCleaned:
        expectedAns += cur.execute("SELECT * FROM " + table).fetchall()
    print("solution:",expectedAns)

    cur.executescript(commands)
    con.commit()
    studentCode = submittedAnswer.replace('\n', ' ').replace('\t', ' ')
    cur.executescript(studentCode)
    con.commit()
    tables = cur.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
    tablesCleaned = [item[0] for item in tables]
    actualAns = []
    for table in tablesCleaned:
        actualAns += cur.execute("SELECT * FROM " + table).fetchall()
    print("submitted",actualAns)
    return (expectedAns,actualAns,originalDb)

# HELPERS ----------------------------------------------------------------------------------------------------------------------
def rowMatch(expectedAns,actualAns):
    expectedTotal = 0
    actualTotal = 0
    expectedRowCount = len(expectedAns)
    expectedTotal += expectedRowCount
    # print(expectedTotal,expectedColumnCount,expectedRowCount)

    if not (actualAns or expectedAns): return 1
    if not actualAns: return 0

    actualRowCount = len(actualAns)
    actualTotal += actualRowCount
    # print(actualTotal,actualColumnCount,actualRowCount)

    rowGrade = abs(expectedTotal - actualTotal)
    rowScore = (expectedTotal - rowGrade)/expectedTotal
    return rowScore

def colMatch(expectedAns,actualAns):
    expectedTotal = 0
    actualTotal = 0
    expectedColumnCount = len((expectedAns[0]))
    expectedTotal += expectedColumnCount
    # print(expectedTotal,expectedColumnCount,expectedRowCount)

    if not (actualAns or expectedAns): return 1
    if not actualAns: return 0

    actualColumnCount = len((actualAns[0]))
    actualTotal += actualColumnCount
    # print(actualTotal,actualColumnCount,actualRowCount)

    colGrade = abs(expectedTotal - actualTotal)
    colScore = (expectedTotal - colGrade)/expectedTotal
    return colScore

def valueMatch(expectedAns,actualAns):
    valueMatchExpectedTotal = len(expectedAns)
    valueMatchActualTotal = 0
    for x in actualAns:
        if x in expectedAns:
            valueMatchActualTotal += 1

    matchScore = valueMatchActualTotal / valueMatchExpectedTotal
    return matchScore
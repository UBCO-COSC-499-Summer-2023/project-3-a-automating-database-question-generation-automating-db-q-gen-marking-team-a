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

    questionType = data["params"]["html_params"]["questionType"]

    outputScore = 0

    if os.path.exists("ans.db"):
        os.remove("ans.db")

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
        return 1
    # Otherwise, the student is given a grade that reflective of
    # how close they are. The function linearly maps (0, $threshhold)
    # onto (0, 1) such that is the student gets exactly $threshold
    # they receive a score of 1 (full credit) and if they get a
    # similarity of 0 they recieve a score of 0. 
    else:
        return similarity / threshold


# Returns the similarity between two strings.
# 1 means that the strings are identical.
# 0 means the strings are entirely different.
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def gradeQueryQuestion(data,correctAnswer,submittedAnswer):
    rowColWeight = 0.3
    valueMatchWeight = 0.7

    arr = getExpectedAndActualQueryResults(data,correctAnswer,submittedAnswer)

    expectedAns = arr[0]
    actualAns = arr[1]

    # row + column matching---------------------------------------------
    rowColScore = rowColMatch(expectedAns,actualAns)

    # value matching-----------------------------------------------------
    valueMatchScore = valueMatch(expectedAns,actualAns)

    # order matching-----------------------------------------------------
    score = (rowColWeight*rowColScore) + (valueMatchWeight*valueMatchScore)
    score = round(score,2)

    print("total",score)
    return score

def getExpectedAndActualQueryResults(data,correctAnswer,submittedAnswer):
    con = sqlite3.connect("ans.db")
    cur  = con.cursor()
    # print(data['params']['db_initialize'])
    commands = data['params']['db_initialize'].replace('\n', '').replace('\t', '')
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


def rowColMatch(expectedAns,actualAns):
    if not actualAns[0] and not expectedAns[0]: return 1
    if not actualAns[0]: return 0

    expectedTotal = 0
    actualTotal = 0
    expectedRowCount = len(expectedAns)
    expectedColumnCount = len((expectedAns[0]))
    expectedTotal += expectedRowCount + expectedColumnCount
    # print(expectedTotal,expectedColumnCount,expectedRowCount)

    actualRowCount = len(actualAns)
    actualColumnCount = len((actualAns[0]))
    actualTotal += actualRowCount + actualColumnCount
    # print(actualTotal,actualColumnCount,actualRowCount)

    colrowGrade = abs(expectedTotal - actualTotal)
    rowColScore = (expectedTotal - colrowGrade)/expectedTotal
    return rowColScore

def valueMatch(expectedAns,actualAns):
    if not actualAns[0] and not expectedAns[0]: return 1
    if not actualAns[0]: return 0
    
    valueMatchExpectedTotal = len(expectedAns)
    valueMatchActualTotal = 0
    # value matching-----------------------------------------------------
    for x in actualAns:
        if x in expectedAns:
            valueMatchActualTotal += 1

    matchScore = valueMatchActualTotal / valueMatchExpectedTotal
    return matchScore

def gradeCreateQuestion(data,correctAnswer,submittedAnswer):
    print(correctAnswer,submittedAnswer)
    return 1

# all or nothing
def gradeInsertQuestion(data,correctAnswer,submittedAnswer):
    print(correctAnswer,submittedAnswer)
    return 1

def gradeUpdateQuestion(data,correctAnswer,submittedAnswer):
    print(correctAnswer,submittedAnswer)
    return 1

def gradeDeleteQuestion(data,correctAnswer,submittedAnswer):
    print(correctAnswer,submittedAnswer)
    return 1
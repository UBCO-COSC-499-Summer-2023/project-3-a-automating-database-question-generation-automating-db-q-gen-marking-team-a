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

    if os.path.exists("ans.db"):
        os.remove("ans.db")
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
    expectedAns = cur.execute(expectedCode)
    print("solution:",expectedAns.fetchall())
    studentCode = submittedAnswer.replace('\n', ' ').replace('\t', ' ')
    actualAns = cur.execute(studentCode)
    print("submitted",actualAns.fetchall())
    # # Normalize and split the strings into lists of words
    wordsSA = sorted(stripSA.split())
    wordsCA = sorted(stripCA.split())
    
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
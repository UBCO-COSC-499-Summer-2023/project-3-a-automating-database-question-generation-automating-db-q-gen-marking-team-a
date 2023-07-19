from difflib import SequenceMatcher
import requests
from relational_algebra import Relation, Selection, Projection, CrossProduct, ThetaJoin
from relational_algebra.formulas.Formula import Formula


# Uses Python's SequenceMatcher library to check the
# similarity between the correct answer and the student's
# submitted answer.
def customGrader(data):
    
    host_ip = "142.231.78.234"
    url = f"http://{host_ip}:4000/index"
    data = {"Car": "BMW", "Testing": "API"}

    request = requests.post(url,data=data)
    print(request.status_code)
    print(request.text)
  
    #execQuery()
    
    # Grabs the student answer from data
    submittedAnswer = data['submitted_answers']['RelaXEditor']

    # Grabs the solution from data
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

def evaluate_ra_query(query, sql_con=None):
    pass

# Example usage:
def execQuery():
    # Create relations R and S (same as previous example)
    relation_R = Relation(name="R")
    relation_R.add_attributes(["a", "b", "c"])
    relation_R.add_rows([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ])

    relation_S = Relation(name="S")
    relation_S.add_attributes(["b", "c", "d"])
    relation_S.add_rows([
        [2, 3, 4],
        [5, 6, 7],
        [8, 9, 10],
    ])

    # Evaluate the query
    #result = evaluate_ra_query(query, sql_con=None)

    # Display the result
    print("Attributes:", relation_R.attributes)
    print("Rows:", relation_R.rows)

from difflib import SequenceMatcher
import relational_algebra as ra

#print(dir(ra))
#print(help(ra.Selection))


# Uses Python's SequenceMatcher library to check the
# similarity between the correct answer and the student's
# submitted answer.
def customGrader(data):
    
    query = "π a R"
    db = data['params']['database']
    dbArray = db.split(";")
    dataset = []
    
    relation = ra.Relation(name="R")
    relation.add_attributes(["a", "b", "c"])
    relation.add_rows([
	    [1, 2, 3],
	    [4, 5, 6],
	    [7, 8, 9],
    ])
    
    b = ra.Relation(name="S")
    b.add_attributes(["d", "b", "c"])
    b.add_rows([
	    [1, 2, 3],
	    [4, 5, 6],
	    [7, 8, 9],
    ])
    
    answer = ra.evaluate(query)
    
    print(answer)
    
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
from difflib import SequenceMatcher

# Here we can choose the grading method
# For now, there's only a strict string match
def customGrader(data):

    # Calls the appropraite grader for the question
    if data['params']['grader'] == 'SQLEditor':
        stringMatchSQL(data)
    elif data['params']['grader'] == 'RAEditor':
        stringMatchRA(data)


# Basic string matching for SQL text
def stringMatchSQL(data):
    # Grabs the student answer from data
    submittedAnswer = data['submitted_answers']['SQLEditor']

    # Grabs the solution from data
    correctAnswer = data['correct_answers']['SQLEditor']
    
    # Strips both of whitespace
    stripSA = submittedAnswer.strip()
    stripCA = correctAnswer.strip()
    
    # Normalize and split the strings into lists of words
    wordsSA = sorted(stripSA.split())
    wordsCA = sorted(stripCA.split())
    

    # Check if the sorted lists of words are equal
    
    similarityPercentage = similar(wordsSA, wordsCA)
    threshold = 0.75

    if similarityPercentage > threshold:
        data["score"] = 1
    else:
        data["score"] = similarityPercentage / threshold
    


# Basic string matching for RA text
def stringMatchRA(data):
    # Grabs the student answer from data
    submittedAnswer = data['submitted_answers']['RAEditor']

    # Grabs the solution from data
    correctAnswer = data['correct_answers']['RAEditor']
    
    # Strips both of whitespace
    stripSA = submittedAnswer.strip()
    stripCA = correctAnswer.strip()
    
    # Normalize and split the strings into lists of words
    wordsSA = sorted(stripSA.split())
    wordsCA = sorted(stripCA.split())
    
    

    # Check if the sorted lists of words are equal
    if wordsSA == wordsCA:
        data["score"] = 1
    else:
        data["score"] = 0
        
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()
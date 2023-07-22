from difflib import SequenceMatcher
import requests


# Uses Python's SequenceMatcher library to check the
# similarity between the correct answer and the student's
# submitted answer.
def customGrader(data):
    
    try:
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
        
        print("Url:", url)
        print("Data: ",data_to_send)

        response = requests.get(url, json=data_to_send)
        
        print("Response: ", response)
        print("Response status code:", response.status_code)
        print("Response text:", response.text)

        # Assuming the server returns JSON data containing the processed result
        response_data = response.json()
        
        print("Response data: ", response_data)

        # Process the response data as needed
        queriedSA = response_data.get('queriedSA', None)
        queriedCA = response_data.get('queriedCA', None)


        print("QueriedSA:", queriedSA)
        print("QueriedCA:", queriedCA)

    except Exception as e:
        print("Error:", str(e))
        raise e
    

    
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

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

        host_ip = "192.168.1.66"
        url = f"http://{host_ip}:4000/index"

        # Construct the data to be sent in the POST request
        data_to_send = {
            "db": db,
            "submittedAnswer": submittedAnswer,
            "correctAnswer": correctAnswer
        }

        response = requests.post(url, data=data_to_send)

        # Assuming the server returns JSON data containing queriedSA and queriedCA
        response_data = response.json()

        queriedSA = response_data.get('queriedSA', None)
        queriedCA = response_data.get('queriedCA', None)

        print("Response status code:", response.status_code)
        print("Response text:", response.text)
        print("QueriedSA:", queriedSA)
        print("QueriedCA:", queriedCA)

    except KeyError as e:
        # Handle the case when the required keys are missing in the 'data' dictionary
        print("KeyError:", e)
        return 0.0
    except ValueError as e:
        # Handle the case when the response does not contain valid JSON data
        print("ValueError:", e)
        return 0.0
    
    # db = data['params']['database']
    
    # # Grabs the student answer from data
    # submittedAnswer = data['submitted_answers']['RelaXEditor']

    # # Grabs the solution from data
    # correctAnswer = data['correct_answers']['RelaXEditor']
    
    
    # host_ip = "192.168.1.66"
    # url = f"http://{host_ip}:4000/index"
    # data = {"Car": "BMW", "Testing": "API"}

    # request = requests.post(url,data=data)
    # print(request.status_code)
    # print(request.text)
    

    
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

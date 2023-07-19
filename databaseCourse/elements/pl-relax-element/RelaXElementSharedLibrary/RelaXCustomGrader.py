from difflib import SequenceMatcher

import subprocess
import json
import os




# Uses Python's SequenceMatcher library to check the
# similarity between the correct answer and the student's
# submitted answer.
def customGrader(data):
    # JavaScript code to set the environment and execute exec_relalg_bundle.js
    js_code = """
    const fs = require('fs');
    
    // Read relalg_bundle.js content as a string
    const relalgBundleCode = fs.readFileSync('relalg_bundle.js', 'utf8');

    // Execute relalg_bundle.js code
    eval(relalgBundleCode);

    // Import the necessary functions and objects from relalg_bundle
    const executeRelalg = relalg_bundle.executeRelalg;
    const Relation = relalg_bundle.Relation;

    // Read exec_relalg_bundle.js content as a string
    const execRelalgCode = fs.readFileSync('exec_relalg_bundle.js', 'utf8');

    // Execute exec_relalg_bundle.js code
    eval(execRelalgCode);
    """

    # Call node with the inline JavaScript code
    command = ['node', '-e', js_code]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode != 0:
        raise Exception(stderr.decode())
    
    print("Process: ", process)
    print("Stdout : " , stdout.decode())
    print("Stderr : " , stderr.decode())

    # Continue with the rest of your customGrader function if needed
    #for i, result in enumerate(results):
    #    print(f"Result {i+1}: {result}")
    
    
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
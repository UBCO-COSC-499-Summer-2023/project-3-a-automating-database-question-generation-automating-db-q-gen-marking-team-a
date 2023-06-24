import json
import chevron
import lxml.html
import prairielearn as pl

import SQLElementSharedLibrary.SQLCustomGrader as grader
import SQLElementSharedLibrary.SQLAutogenerator as autogen

# Note to devs:
# It seems you cannot modify params or correct answers from generate().
# That must be done in prepare().
def generate(element_html, data):
    pass


# Prepares the question by filling data with necessary parameters
def prepare(element_html, data):
    '''
	Given an element_html and a dictionary data, this function extracts the answer from the element and 
	sets it as the correct answer in the data dictionary. If the element has a database attribute, its contents
	are read and added to the data dictionary as a list of strings. 

	Parameters:
	- element_html (string): A string containing the HTML of an element.
	- data (dict): A dictionary to which the correct answer and database contents will be added.

	Return:
	- None
	'''

    # Grabs the answer from the question's question.html file
    element = lxml.html.fragment_fromstring(element_html)    
    correctAnswer = pl.inner_html(element[1])

    # Sets the correct answer
    data['correct_answers']['SQLEditor'] = correctAnswer

    # Grabs the path to the database file
    # Only used in static questions
    databaseFilePath = pl.get_string_attrib(element, 'database', '')

    # If there is a database file, read and loads its contents
    if databaseFilePath:
        databaseFile = open(databaseFilePath,"r")

        # Reads the database as an array over lines of a string
        data['params']['db_initialize'] = databaseFile.read().splitlines()
        
        databaseFile.close() 

    # Loads quesiton parameters into data
    questionRandom = pl.get_boolean_attrib(element, 'random', False)
    questionType = pl.get_string_attrib(element, 'questionType', 'query')
    questionDifficulty = pl.get_string_attrib(element, 'difficulty', 'normal')
    questionMaxGrade = pl.get_float_attrib(element, 'maxGrade', 1)
    questionMarkerFeedback = pl.get_boolean_attrib(element, 'markerFeedback', False)

    data['params']['html_params'] = {
        'random': questionRandom,
        'questionType': questionType,
        'difficulty': questionDifficulty,
        'maxGrade': questionMaxGrade,
        'markerFeedback': questionMarkerFeedback
    }

    # If if is a randomised question, generate the question
    # data['params']['html_params']['random']
    if questionRandom:
        autogen.autogenerate(data)


# Renders the element
def render(element_html, data):
    '''
    Renders the question, submission and answer into PrairieLearn.
    This function is called by PrairieLearn during the page load.
    
    Keyword arguments:
    :param element_html: The element HTML
    :param data: The data
    :return: The HTML you want rendered
    '''
    
    # Grabs the student's submitted answer
    element = lxml.html.fragment_fromstring(element_html)
    submittedAnswer = data['submitted_answers'].get('SQLEditor', '')
    
    # Grabs the correct answer from the data variable
    correctAnswer = data['correct_answers']['SQLEditor']
    
    # Grabs the string to initialize the database.
    # The join command turns an array of strings into a single string.
    # The get returns the entry if it exists or an empty string otherwise.
    dbInit = ''.join(data['params'].get('db_initialize', ''))
     
    # This renders the question into PL
    if data['panel'] == 'question':  
        
        html_params = {
            'question': True,
            'db_initialize': dbInit
        }
    
        with open('pl-sql-element.mustache', 'r', encoding='utf-8') as f:
            html = chevron.render(f, html_params)
        
    # This renders the users submitted answer into the "Submitted answer" box in PL
    elif data['panel'] == 'submission':

        
        html_params = {
            'submission': True,
            'studentSubmission': submittedAnswer
        }
        

        
        with open('pl-sql-submission.mustache', 'r', encoding='utf-8') as f:
            html = chevron.render(f, html_params)
    
    # This renders the correct answer into the "Correct answer" box in PL
    # This will not be displayed on the student page unless a showCorrectAnswer: True 
    # is specified in the info.json file.
    elif data['panel'] == 'answer':
        
        html_params = {
            'answer': True,
            'correctAnswer': correctAnswer
        }
        with open('pl-sql-answer.mustache', 'r', encoding='utf-8') as f:
            html = chevron.render(f, html_params).strip()
    
    return html

def parse(element_html, data):
    pass

# Used to grade the student submission
def grade(element_html, data):
    '''
	Grades the student's submission and places the student's score and other feedback into data.
	
	:param element_html: HTML element of the submission.
	:type element_html: str
	:param data: Dictionary containing the submission data.
	:type data: dict
	
	:returns: None
	'''
 
    # Grades the student's submission
    studentScore = grader.customGrader(data)
    
    # Places the student's score and other feedback into data.
    # Score cannot be directly modified in the element folder,
    # rather it must be placed within partial scores.
    # Updating final score is done automatically by PrairieLearn
    # based upon the partial scores.
    
    data['partial_scores']['SQLEditor'] = {
        'score': studentScore,
        'weight': 1,
        'feedback': "",
        'marker_feedback': ""
    }

def test(element_html, data):
    pass
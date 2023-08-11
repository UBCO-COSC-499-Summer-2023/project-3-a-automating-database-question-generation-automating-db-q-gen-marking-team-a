import json
import chevron
import lxml.html
import html
import prairielearn as pl

import RelaXElementSharedLibrary.RelaXCustomGrader as grader
import RelaXElementSharedLibrary.RelaXAutogenerator as autogen

# This allows DroneCI to see the RASQLib module
import sys
sys.path.append('/databaseCourse/serverFilesCourse/RASQLib')
sys.path.append('/drone/src/databaseCourse/serverFilesCourse/')

from RASQLib import textDatabaseHandler as db

# url to the relax API for backend grading
RELAXAPI_URL = 'http://relaxAPI:3001/index'

def generate(element_html, data):
    pass
    


def prepare(element_html, data):
    data['params']['grader'] = 'RelaXEditor'

    data['params']['db_initialize_create'] = ''
    data['params']['db_initialize_create_backend'] = ''
    element = lxml.html.fragment_fromstring(element_html)
    
    # If there is a database file, read and loads its contents
    databaseFilePath = pl.get_string_attrib(element, 'database', '')
    database = ''
    if databaseFilePath:
        with open(databaseFilePath,"r") as databaseFile:
           database += databaseFile.read()
    
    data['params']['database'] = database    
    
    # parameter whether to show feedback or not
    feedback = pl.get_boolean_attrib(element, 'feedback', False)
    data['params']['feedback'] = feedback
    
    # storing the actual feedback
    data['params']['queryFeedback'] = ''

    #get the url to execute relax from backend
    #url = pl.get_string_attrib(element, 'url', '') #obsolete, now taken from global variable
    data['params']['url'] = RELAXAPI_URL
    
    #get the correct answer from question.html
    correctAnswer = lxml.html.fromstring(pl.inner_html(element[0])).text_content()
    data['correct_answers']['RelaXEditor'] = correctAnswer



    # Grabs the path to the database file
    # Only used in static questions
    databaseFilePath = pl.get_string_attrib(element, 'database', '')
    # Note to devs:
    # Notice the strings in the pl.get_... are lowercase despite
    # the html parameters being uppercase. I have no clue why
    # this is, but the pl.get_... will fail to find the corresponding
    # parameter if their string is uppercase. Hence all lowercase
    questionRandom = pl.get_boolean_attrib(element, 'random', False)

    data['params']['html_params'] = {
        'random': questionRandom,
        'expectedOutput' : pl.get_boolean_attrib(element, "expectedoutput", True)
    }
    # If there is a database file, read and loads its contents
    data['params']['db_initialize'] = ''
    if databaseFilePath:
        with open(databaseFilePath,"r") as databaseFile:
           data['params']['db_initialize'] = databaseFile.read()
        data['params']['html_params']['expectedOutput'] = ''
        data['params']['db_initialize_create_backend'] = data['params']['db_initialize']
        
    
    # Loads quesiton parameters into data
    #



    if questionRandom:
        attribDict = {
            "numClauses": pl.get_integer_attrib(element, "numclauses", 1),
            "orderBy": pl.get_boolean_attrib(element, "orderby", False),
            "groupBy": pl.get_boolean_attrib(element, "groupby", False),
            "numJoins": pl.get_integer_attrib(element, "numjoins", 0),
            "antiJoin": pl.get_boolean_attrib(element, "antijoin", False),
            "semiJoin": pl.get_boolean_attrib(element, "semijoin", False),
            "outerJoin": pl.get_boolean_attrib(element, "outerjoin", False)
        }
        data['params']['attrib_dict'] = attribDict
        data['params']['outputGuarantee'] = pl.get_boolean_attrib(element, "outputguarantee", True)

    # If if is a randomised question, generate the question
    if questionRandom:
        autogen.autogenerate(data)
        database = data['params']['db_initialize_create']
        # print(database)
        data['params']['database'] = database

    if not pl.get_boolean_attrib(element, "expectedoutput", True):
        data['params']['html_params']['expectedOutput'] = ''        




def render(element_html, data):
    # Gets the element data from the HTML
    element = lxml.html.fragment_fromstring(element_html)

    # Gets each element from the questionHTML
    submittedAnswer = data['submitted_answers'].get('RelaXEditor','')
    correctAnswer = data['correct_answers'].get('RelaXEditor', '')
    giveFeedback = data['params']['feedback']


    # NOTE: the database is loaded into the data
    # variable during the `prepare()` function,
    # when it called `autogenerate()`



    # This renders the question into PL
    if data['panel'] == 'question':
        #data['params']['html_params']['expectedOutput'] = autogen.createPreview(data)
        if 'questionText' not in data['params'].keys():
            data['params']['questionText'] = ""
        # setting the paramaters
        html_params = {
            'database' : data['params']['database'],
            'questionText' : data['params']['questionText'],
            'previousSubmission' : submittedAnswer,
            'expectedOutput' : data['params']['html_params']['expectedOutput']
        }
            # Opens and renders mustache file into the question html
        with open('pl-relax-element.mustache', 'r', encoding='utf-8') as f:
            html = chevron.render(f, html_params)


    elif data['panel'] == 'submission':
        if giveFeedback:
            try:
                queryFeedback = data['partial_scores']['RelaXEditor'].get('feedback', None)
            except KeyError:
                queryFeedback = ''
        else:
            queryFeedback = "Your instructor has disabled feedback for this question."
  
        html_params = {
            'submission': True,
            'submissionAnswer': submittedAnswer,
            'feedback' : queryFeedback
        }
        
        with open('pl-relax-submission.mustache', 'r', encoding='utf-8') as f:
            html = chevron.render(f, html_params)

    # This renders the correct answer into the "Correct answer" box in PL
    # This will not be displayed on the student page unless a showCorrectAnswer: True 
    # is specified in the info.json file.
    elif data['panel'] == 'answer':
        html_params = {
            'answer': True,
            'correctAnswer': correctAnswer
        }
        with open('pl-relax-answer.mustache', 'r', encoding='utf-8') as f:
            html = chevron.render(f, html_params).strip()


    return html

def parse(element_html, data):
    pass

def grade(element_html, data):
    # Grades the student's submission
    studentScore = grader.customGrader(data)
    # Places the student's score and other feedback into data.
    # Score cannot be directly modified in the element folder,
    # rather it must be placed within partial scores.
    # Updating final score is done automatically by PrairieLearn
    # based upon the partial scores.
    
    data['partial_scores']['RelaXEditor'] = {
        'score': studentScore,
        'weight': 1,
        'feedback': data['params']['queryFeedback'],
        'marker_feedback': ""
    }
    

def test(element_html, data):
    pass
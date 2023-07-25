import json
import chevron
import lxml.html
import html
import prairielearn as pl

import RelaXElementSharedLibrary.RelaXCustomGrader as grader
import RelaXElementSharedLibrary.RelaXAutogenerator as autogen

# This allows DroneCI to see the RASQLib module
import sys
sys.path.append('/drone/src/databaseCourse/serverFilesCourse/')

from RASQLib import textDatabaseHandler as db

def generate(element_html, data):
    pass
    


def prepare(element_html, data):
    data['params']['grader'] = 'RelaXEditor'
    element = lxml.html.fragment_fromstring(element_html)
    
    # If there is a database file, read and loads its contents
    databaseFilePath = pl.get_string_attrib(element, 'database', '')
    database = ''
    if databaseFilePath:
        with open(databaseFilePath,"r") as databaseFile:
           database += databaseFile.read()
    
    data['params']['database'] = database
    
    #prepare the feedback parameter
    data['params']['feedback'] = ''
    
    #get the url to execute relax from backend
    url = pl.get_string_attrib(element, 'url', '')
    data['params']['url'] = url
    
    #get the correct answer from question.html
    correctAnswer = lxml.html.fromstring(pl.inner_html(element[0])).text_content()
    data['correct_answers']['RelaXEditor'] = correctAnswer



    # Grabs the path to the database file
    # Only used in static questions
    databaseFilePath = pl.get_string_attrib(element, 'database', '')

    # If there is a database file, read and loads its contents
    data['params']['db_initialize'] = ''
    if databaseFilePath:
        with open(databaseFilePath,"r") as databaseFile:
           data['params']['db_initialize'] = databaseFile.read()
        

    
    # Loads quesiton parameters into data
    #
    # Note to devs:
    # Notice the strings in the pl.get_... are lowercase despite
    # the html parameters being uppercase. I have no clue why
    # this is, but the pl.get_... will fail to find the corresponding
    # parameter if their string is uppercase. Hence all lowercase
    questionRandom = pl.get_boolean_attrib(element, 'random', False)

    data['params']['html_params'] = {
        'random': questionRandom
    }

    # If if is a randomised question, generate the question
    if questionRandom:
        autogen.autogenerate(data)



def render(element_html, data):
    # Gets the element data from the HTML
    element = lxml.html.fragment_fromstring(element_html)

    # Gets each element from the questionHTML
    submittedAnswer = data['submitted_answers'].get('RelaXEditor','')
    correctAnswer = data['correct_answers'].get('RelaXEditor', '')



    # NOTE: the database is loaded into the data
    # variable during the `prepare()` function,
    # when it called `autogenerate()`



    # This renders the question into PL
    if data['panel'] == 'question':
        # setting the paramaters
        html_params = {
            'database' : data['params']['db_initialize']
        }
            # Opens and renders mustache file into the question html
        with open('pl-relax-element.mustache', 'r', encoding='utf-8') as f:
            html = chevron.render(f, html_params)


    elif data['panel'] == 'submission':
  
        html_params = {
            'submission': True,
            'submissionAnswer': submittedAnswer,
            'feedback' : data['params']['feedback']
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
        'feedback': "test1",
        'marker_feedback': "marker test1"
    }
    

def test(element_html, data):
    pass
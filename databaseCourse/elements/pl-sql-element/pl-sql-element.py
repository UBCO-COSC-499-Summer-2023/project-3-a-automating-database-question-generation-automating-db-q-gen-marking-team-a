import json
import chevron
import lxml.html
import prairielearn as pl

import RASQLCustomGrader as grader

# Note to devs:
# It seems you cannot modify params or correct answers from generate().
# That must be done in prepare().
def generate(element_html, data):
    pass

def prepare(element_html, data):

    # TODO
    #   Remove this param when we seperate grader into SQL and DDL; it will no longer be needed
    data['params']['grader'] = 'SQLEditor'

    # Grabs the answer from the question's question.html file
    element = lxml.html.fragment_fromstring(element_html)    
    correctAnswer = pl.inner_html(element[1])

    # Sets the correct answer
    data['correct_answers']['SQLEditor'] = correctAnswer


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

def grade(element_html, data):

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

import json
import chevron
import lxml.html
import html
import prairielearn as pl
import RelaXElementSharedLibrary.RelaXCustomGrader as grader
import RelaXElementSharedLibrary.RelaXAutogenerator as autogen

def generate(element_html, data):
    pass
    


def prepare(element_html, data):
    data['params']['grader'] = 'RelaXEditor'
    element = lxml.html.fragment_fromstring(element_html)
    
    correctAnswer = lxml.html.fromstring(pl.inner_html(element[0])).text_content()
    data['correct_answers']['RelaXEditor'] = correctAnswer

def render(element_html, data):
    # # Gets the element data from the HTML
    element = lxml.html.fragment_fromstring(element_html)
    # # Gets each element from the questionHTML
    submittedAnswer = data['submitted_answers'].get('RelaXEditor','')
    correctAnswer = data['correct_answers'].get('RelaXEditor', '')
    databaseFilePath = pl.get_string_attrib(element, 'database', '')

    # If there is a database file, read and loads its contents
    database = ''
    if databaseFilePath:
        with open(databaseFilePath,"r") as databaseFile:
           database += databaseFile.read()
    else:
        table1 = autogen.Table()
        print(table1.toString())
        database+=table1.toString()
    # This renders the question into PL
    if data['panel'] == 'question':
        # setting the paramaters
        html_params = {
            'database' : database,
        }
            # Opens and renders mustache file into the question html
        with open('pl-relax-element.mustache', 'r', encoding='utf-8') as f:
            html = chevron.render(f, html_params)


    elif data['panel'] == 'submission':
  
        html_params = {
            'submission': True,
            'submissionAnswer': submittedAnswer,
        }
        
        with open('pl-relax-submission.mustache', 'r', encoding='utf-8') as f:
            html = chevron.render(f, html_params)

    # This renders the correct answer into the "Correct answer" box in PL
    # This will not be displayed on the student page unless a showCorrectAnswer: True 
    # is specified in the info.json file.
    elif data['panel'] == 'answer':
        
        #print("correctAnswer:", correctAnswer)
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
        'feedback': "",
        'marker_feedback': ""
    }

def test(element_html, data):
    pass
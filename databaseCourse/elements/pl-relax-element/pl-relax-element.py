import json
import chevron
import lxml.html
import prairielearn as pl

'''
def prepare():
    pass '''

def render(element_html, data):
    # Gets the element data from the HTML
    element = lxml.html.fragment_fromstring(element_html)
    # Gets each element from the questionHTML
    questionText = pl.inner_html(element[0])
    database = pl.inner_html(element[1])


    submittedAnswer = data['submitted_answers'].get('RelaXEditor','')
    correctAnswer = data['correct_answers']["RelaXEditor"]
    print("CA",correctAnswer)
    print("SA",submittedAnswer)
    # This renders the question into PL
    print("data is  ",data)
    if data['panel'] == 'question':  
        # setting the paramaters
        html_params = {
            'answer': True,
            'submission': True,
            'questionText' : questionText,
            'database' : database,
            'studentSubmission': submittedAnswer,
            'correctAnswer': correctAnswer
        }
            # Opens and renders mustache file into the question html
        with open('pl-relax-element.mustache', 'r') as f:
            html = chevron.render(f, html_params)

    elif data['panel'] == 'submission':

        
        html_params = {
            'submission': True,
            'studentSubmission': submittedAnswer
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
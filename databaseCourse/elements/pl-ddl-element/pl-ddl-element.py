import json
import chevron
import lxml.html
import prairielearn as pl


def render(element_html, data):
    '''
    Renders the question, submission and answer into PrairieLearn.
    This function is called by PrairieLearn during the page load.
    
    Keyword arguments:
    :param element_html: The element HTML
    :param data: The data
    :return: The HTML you want rendered
    '''
    
    element = lxml.html.fragment_fromstring(element_html)
    submittedAnswer = data['submitted_answers'].get('SQLEditor','')
    correctAnswer = data['correct_answers']['SQLEditor']
     
    # This renders the question into PL
    if data['panel'] == 'question':  
        z = pl.inner_html(element[0])
        html_params = {
            'questionText' : z,
            'generateDb' : ''.join(data["params"]["ddl"])
        }
    
        with open('pl-ddl-element.mustache', 'r') as f:
            html = chevron.render(f, html_params)
        
    # This renders the users submitted answer into the "Submitted answer" box in PL
    elif data['panel'] == 'submission':
        html = submittedAnswer
    
    # This renders the correct answer into the "Correct answer" box in PL
    # This will not be displayed on the student page unless a showCorrectAnswer: True 
    # is specified in the info.json file.
    elif data['panel'] == 'answer':
        html = correctAnswer
    
    return html

def snake_case_to_camel_case(s):
    return ''.join(x.capitalize() or '_' for x in s.split('_'))


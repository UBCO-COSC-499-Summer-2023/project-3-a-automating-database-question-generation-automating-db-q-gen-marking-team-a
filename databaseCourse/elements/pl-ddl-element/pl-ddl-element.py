import json
import chevron
import lxml.html
import prairielearn as pl

def prepare(element_html, data):
        element = lxml.html.fragment_fromstring(element_html)
        data['params']['oldAnswer'] = None
        data['params']['feedback'] = None
        data['params']['answer'] = pl.inner_html(element[1])



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
    data['params']['oldAnswer'] = data['submitted_answers'].get('c', '')
     
    # This renders the question into PL
    if data['panel'] == 'question':  
        z = pl.inner_html(element[0])
        html_params = {
            'questionText' : z
        }
    
        with open('pl-ddl-element.mustache', 'r', encoding='utf-8') as f:
            html = chevron.render(f, html_params)
        
    # This renders the users submitted answer into the "Submitted answer" box in PL
    elif data['panel'] == 'submission':

        
        html_params = {
            'submission': True,
            'studentSubmission': data['params']['oldAnswer'],
        }
        

        
        with open('pl-ddl-submission.mustache', 'r', encoding='utf-8') as f:
            html = chevron.render(f, html_params)
    
    # This renders the correct answer into the "Correct answer" box in PL
    # This will not be displayed on the student page unless a showCorrectAnswer: True 
    # is specified in the info.json file.
    elif data['panel'] == 'answer':
        
        html = pl.inner_html(element[1])
    
    return html


# Not working as of June 16
def grade(element_html, data):
    
    element = lxml.html.fragment_fromstring(element_html)

    
    submittedAnswer = data['submitted_answers'].get('c', '')
    correctAnswer = pl.inner_html(element[1])

    
    # Check if the submitted answer is correct
    if submittedAnswer == correctAnswer:
        data["partial_scores"]["ddl_answer"]["score"] = 1
    else:
        data["partial_scores"]["ddl_answer"]["score"] = 0.5

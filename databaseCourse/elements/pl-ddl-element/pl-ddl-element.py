import json
import chevron
import lxml.html
import prairielearn as pl

def prepare(element_html, data):
        element = lxml.html.fragment_fromstring(element_html)
        data['params']['submission'] = None




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
        
        data['params']['submission'] = data['submitted_answers'].get('c', '')
        
        html_params = {
            'submission': data['params']['submission'],
        }
        
        print(html_params)
        
        with open('pl-ddl-submission.mustache', 'r', encoding='utf-8') as f:
            html = chevron.render(f, html_params)
    
    # This renders the correct answer into the "Correct answer" box in PL
    # This will not be displayed on the student page unless a showCorrectAnswer: True 
    # is specified in the info.json file.
    elif data['panel'] == 'answer':
        correctAnswer = pl.inner_html(element[1])
        html = correctAnswer
    
    return html
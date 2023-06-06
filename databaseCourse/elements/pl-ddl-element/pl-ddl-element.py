import json
import chevron
import lxml.html
import prairielearn as pl

def render(element_html, data):
    element = lxml.html.fragment_fromstring(element_html)

    if data['panel'] == 'question':        
        html_params = {
            "question": True,
        }
        with open('pl-ddl-element.mustache', 'r', encoding='utf-8') as f:
            html = chevron.render(f, html_params).strip()

    
    #html = chevron.render('Hello, {{ mustache }}!', {'mustache': 'World'})
    
    return html
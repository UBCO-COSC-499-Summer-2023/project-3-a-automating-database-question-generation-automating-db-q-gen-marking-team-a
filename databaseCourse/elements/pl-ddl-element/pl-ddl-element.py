import json
import chevron
import lxml.html
import prairielearn as pl

def render(element_html, data):
    element = lxml.html.fragment_fromstring(element_html)
    
    """
    if data['panel'] == 'question':        
        html_params = {
            'question_data': data['params']['question_data'],
        }
        with open('ddl-element.mustache', 'r', encoding='utf-8') as f:
            html = chevron.render(f, html_params).strip()
    """
    
    z = pl.inner_html(element[0])
    
    html = chevron.render('{{ mustache }}!', {'mustache': z})
    
    return html
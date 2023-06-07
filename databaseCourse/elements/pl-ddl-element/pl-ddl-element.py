import json
import chevron
import lxml.html
import prairielearn as pl

def render(element_html, data):
    element = lxml.html.fragment_fromstring(element_html)
     
    z = pl.inner_html(element[0])
    html_params = {
        'questionText' : z
    }
    
    with open('pl-ddl-element.mustache', 'r') as f:
        html = chevron.render(f, html_params)
    
    return html
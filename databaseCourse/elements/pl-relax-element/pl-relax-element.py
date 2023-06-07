import json
import chevron
import lxml.html
import prairielearn as pl


'''def prepare():


    return'''

def render(element_html, data):
    element = lxml.html.fragment_fromstring(element_html)
    
    z = pl.inner_html(element)
    html_params = {
        'questionText' : z
    }
    with open('pl-relax-element.mustache', 'r') as f:
        html = chevron.render(f, html_params)
    return html


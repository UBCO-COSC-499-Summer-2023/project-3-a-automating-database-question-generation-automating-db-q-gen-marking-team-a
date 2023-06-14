import json
import chevron
import lxml.html
import prairielearn as pl


def prepare():

    
    return

def hello_orld_new():

    return lkjhkjl

def render(element_html, data):
    element = lxml.html.fragment_fromstring(element_html)

    questionText = pl.inner_html(element[0])
    relaxFile = pl.inner_html(element[1])

    html_params = {
        'questionText' : questionText,
        'relaxFile' : relaxFile
    }
    with open('pl-relax-element.mustache', 'r') as f:
        html = chevron.render(f, html_params)
    return html


import json
import chevron
import lxml.html
import prairielearn as pl


'''def prepare():

    
    return'''

def render(element_html, data):
    # Gets the element data from the HTML
    element = lxml.html.fragment_fromstring(element_html)
    # Gets each element from the questionHTML
    questionText = pl.inner_html(element[0])
    relaxFile = pl.inner_html(element[1])

    # setting the paramaters
    html_params = {
        'questionText' : questionText,
        'relaxFile' : relaxFile
    }
    # Opens and renders mustache file into the question html
    with open('pl-relax-element.mustache', 'r') as f:
        html = chevron.render(f, html_params)

    return html


import unittest

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# example uiTestFile to show how you can automate ui tests, configure the ui test classes/files 
# and tests
class TestSample(unittest.TestCase):

    # tests that the page loaded ,when PL docker container is up, has title which contains
    # "PrairieLearn" in it
    def test_page_name(self):
        baseUrl = 'http://google.ca/'
        options = Options()
        options.add_argument('--headless')
        driver = webdriver.Firefox(options=options)
        driver.get(baseUrl)
        assert 'Gjhghgggfg' in driver.title
        driver.quit()

if __name__ == '__main__':
    unittest.main()
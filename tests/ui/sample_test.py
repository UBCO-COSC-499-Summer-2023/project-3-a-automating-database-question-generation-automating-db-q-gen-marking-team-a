import unittest

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# example uiTestFile to show how you can automate ui tests, configure the ui test classes/files 
# and tests
class TestSample(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options)


    # tests that the page loaded ,when PL docker container is up, has title which contains
    # "PrairieLearn" in it
    def testPageName(self):
        baseUrl = 'http://google.ca/'
        self.driver.get(baseUrl)
        assert 'Google' in self.driver.title
        print(self.driver.title)
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
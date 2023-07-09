import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

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
        baseUrl = 'http://localhost:3000/'
        driver = self.driver
        driver.get(baseUrl)
        assert 'PrairieLearn' in self.driver.title
        print(self.driver.title)
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()


# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# options = Options()
# options.page_load_strategy = 'normal'
# driver = webdriver.Chrome(options=options)
# driver.get("http://www.google.com")
# driver.quit()
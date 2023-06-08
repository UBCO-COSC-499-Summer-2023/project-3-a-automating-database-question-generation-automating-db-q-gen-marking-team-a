import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# example uiTestFile to show how you can automate ui tests, configure the ui test classes/files 
# and tests
class SampleTest(unittest.TestCase):

    # tests that the page loaded ,when PL docker container is up, has title which contains
    # "PrairieLearn" in it
    def test_page_name(self):
        # currently using firefox due to issues with chrome on my machine
        # set to webdriver.Chrome() or Edge() or any supported browser of your choice
        browser = webdriver.Firefox()

        browser.get('http://localhost:3000/')
        print(browser.title)
        assert 'PrairieLearn' in browser.title
        # elem = browser.find_element(By.NAME, 'p')  # Find the search box
        # elem.send_keys('seleniumhq' + Keys.RETURN)
        browser.quit()

if __name__ == '__main__':
    unittest.main()
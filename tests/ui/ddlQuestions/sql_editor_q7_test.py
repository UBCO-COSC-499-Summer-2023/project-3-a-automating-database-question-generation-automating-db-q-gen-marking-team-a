import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import chromedriver_binary

# example uiTestFile to show how you can automate ui tests, configure the ui test classes/files 
# and tests
class TestSqlEditorDDLQ7(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options)
        self.baseUrl = "http://localhost:3000/pl/course_instance/1/instructor/question/25/preview"

    # tests that the home page of PL loads properly
    def testPrairieLearnLoad(self):
        baseUrl = 'http://localhost:3000/'
        driver = self.driver
        driver.get(baseUrl)
        self.assertIn("PrairieLearn",driver.title)
        print(self.driver.title)
  
    def test_sqlExecuteButtonClick(self):
        # Test name: sqlExecuteButtonClick
        # Step # | name | target | value
        # 1 | open | http://localhost:3000/pl/course_instance/1/instructor/question/36/preview | 
        self.driver.get(self.baseUrl)
        # 2 | setWindowSize | 1536x824 | 
        self.driver.set_window_size(1536, 824)
        # 3 | click | id=execute | 
        self.driver.find_element(By.ID, "execute").click()
    
    def test_sqlExecuteQuery(self):
        # Test name: sqlExecuteQuery
        # Step # | name | target | value
        # 1 | open | http://localhost:3000/pl/course_instance/1/instructor/question/36/preview | 
        self.driver.get(self.baseUrl)
        # 2 | setWindowSize | 1536x824 | 
        self.driver.set_window_size(1536, 824)
        # 3 | runScript | window.scrollTo(0,354.3999938964844) | 
        self.driver.execute_script("window.scrollTo(0,354.3999938964844)")
        # 4 | runScript | window.scrollTo(0,354.3999938964844) | 
        self.driver.execute_script("window.scrollTo(0,354.3999938964844)")
        # 5 | type | css=.CodeMirror textarea | SELECT * FROM customer
        self.driver.find_element(By.CSS_SELECTOR, ".CodeMirror textarea").send_keys("SELECT * FROM customer")
        # 6 | click | id=execute | 
        self.driver.find_element(By.ID, "execute").click()
    
    def test_sqlOutputTableColumnSortByClick(self):
        # Test name: sqlOutputTableColumnSortByClick
        # Step # | name | target | value
        # 1 | open | http://localhost:3000/pl/course_instance/1/instructor/question/36/preview | 
        self.driver.get(self.baseUrl)
        # 2 | setWindowSize | 1536x824 | 
        self.driver.set_window_size(1536, 824)
        # 3 | runScript | window.scrollTo(0,354.3999938964844) | 
        self.driver.execute_script("window.scrollTo(0,354.3999938964844)")
        # 4 | runScript | window.scrollTo(0,354.3999938964844) | 
        self.driver.execute_script("window.scrollTo(0,354.3999938964844)")
        # 5 | runScript | window.scrollTo(0,354.3999938964844) | 
        self.driver.execute_script("window.scrollTo(0,354.3999938964844)")
        # 6 | type | css=.CodeMirror textarea | SELECT * FROM customer
        self.driver.find_element(By.CSS_SELECTOR, ".CodeMirror textarea").send_keys("SELECT * FROM customer")
        # 7 | click | id=execute | 
        self.driver.find_element(By.ID, "execute").click()
        # 8 | click | css=th:nth-child(2) | 
        self.driver.find_element(By.CSS_SELECTOR, "th:nth-child(2)").click()
        # 9 | click | css=th:nth-child(3) | 
        self.driver.find_element(By.CSS_SELECTOR, "th:nth-child(3)").click()

if __name__ == '__main__':
    unittest.main()
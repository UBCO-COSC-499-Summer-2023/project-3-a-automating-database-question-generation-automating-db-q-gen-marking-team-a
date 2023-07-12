import unittest
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
class TestSqlEditor(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options)

    # tests that the home page of PL loads properly
    def testPrairieLearnLoad(self):
        baseUrl = 'http://localhost:3000/'
        driver = self.driver
        driver.get(baseUrl)
        self.assertIn("PrairieLearn",driver.title)
        print(self.driver.title)
    
    def test_sqlEditorDbSchemaClickAddTableName(self):
        # Test name: sqlEditorDbSchemaClickAddTableName
        # Step # | name | target | value
        # 1 | open | http://localhost:3000/ | 
        self.driver.get("http://localhost:3000/")
        # 2 | setWindowSize | 1532x816 | 
        self.driver.set_window_size(1532, 816)
        # 3 | click | linkText=Summer 2023 | 
        self.driver.find_element(By.LINK_TEXT, "Summer 2023").click()
        # 4 | click | linkText=Homework For Writing SQL Queries | 
        self.driver.find_element(By.LINK_TEXT, "Homework For Writing SQL Queries").click()
        # 5 | click | css=tr:nth-child(2) a | 
        schema = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,"tr:nth-child(2) a"))
        )
        schema.click()
        # 6 | click | id=btn-" + tableName + " | 
        tableName = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.ID, "btn-\" + tableName + \""))
        )
        tableName.click()

    def test_sqlEditorDbSchemaClickAddColumn(self):
        # Test name: sqlEditorDbSchemaClickAddColumn
        # Step # | name | target | value
        # 1 | open | http://localhost:3000/ | 
        self.driver.get("http://localhost:3000/")
        # 2 | setWindowSize | 1532x816 | 
        self.driver.set_window_size(1532, 816)
        # 3 | click | linkText=Summer 2023 | 
        self.driver.find_element(By.LINK_TEXT, "Summer 2023").click()
        # 4 | click | linkText=Homework For Writing SQL Queries | 
        self.driver.find_element(By.LINK_TEXT, "Homework For Writing SQL Queries").click()
        # 5 | click | css=tr:nth-child(2) a | 
        # self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) a").click()
        schema = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,"tr:nth-child(2) a"))
        )
        schema.click()
        # 6 | click | xpath=//span[@onclick="addColumnToEditor('customer', 'cid')"] | 
        # self.driver.find_element(By.XPATH, "//span[@onclick=\"addColumnToEditor(\'customer\', \'cid\')\"]").click()
        schemaCol = WebDriverWait(self.driver,10).until(
            EC._element_if_visible((By.XPATH, "//span[@onclick=\"addColumnToEditor(\'customer\', \'cid\')\"]"))
        )
        schemaCol.click()
    
    def test_sqlEditorExecuteButtonClick(self):
        # Test name: sqlEditorExecuteButtonClick
        # Step # | name | target | value
        # 1 | open | http://localhost:3000/ | 
        self.driver.get("http://localhost:3000/")
        # 2 | setWindowSize | 1532x816 | 
        self.driver.set_window_size(1532, 816)
        # 3 | click | linkText=Summer 2023 | 
        self.driver.find_element(By.LINK_TEXT, "Summer 2023").click()
        # 4 | click | linkText=Homework For Writing SQL Queries | 
        self.driver.find_element(By.LINK_TEXT, "Homework For Writing SQL Queries").click()
        # 5 | click | css=tr:nth-child(2) a | 
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) a").click()
        # 6 | click | id=execute | 
        self.driver.find_element(By.ID, "execute").click()
    
    def test_sqlEditorExecuteQuery(self):
        # Test name: sqlEditorExecuteQuery
        # Step # | name | target | value
        # 1 | open | http://localhost:3000/ | 
        self.driver.get("http://localhost:3000/")
        # 2 | setWindowSize | 1532x816 | 
        self.driver.set_window_size(1532, 816)
        # 3 | click | css=tr:nth-child(1) > td:nth-child(2) | 
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) > td:nth-child(2)").click()
        # 4 | click | linkText=Summer 2023 | 
        self.driver.find_element(By.LINK_TEXT, "Summer 2023").click()
        # 5 | click | linkText=Homework For Writing SQL Queries | 
        self.driver.find_element(By.LINK_TEXT, "Homework For Writing SQL Queries").click()
        # 6 | click | css=tr:nth-child(2) a | 
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) a").click()
        # 7 | runScript | window.scrollTo(0,358.3999938964844) | 
        self.driver.execute_script("window.scrollTo(0,358.3999938964844)")
        # 8 | runScript | window.scrollTo(0,358.3999938964844) | 
        self.driver.execute_script("window.scrollTo(0,358.3999938964844)")
        # 9 | runScript | window.scrollTo(0,358.3999938964844) | 
        self.driver.execute_script("window.scrollTo(0,358.3999938964844)")
        # 10 | type | css=.CodeMirror textarea | SELECT * FROM customer
        self.driver.find_element(By.CSS_SELECTOR, ".CodeMirror textarea").send_keys("SELECT * FROM customer")
        # 11 | click | id=execute | 
        self.driver.find_element(By.ID, "execute").click()
    
    def test_sqlEditorOutputTableColumnSortByClick(self):
        # Test name: sqlEditorOutputTableColumnSortByClick
        # Step # | name | target | value
        # 1 | open | http://localhost:3000/ | 
        self.driver.get("http://localhost:3000/")
        # 2 | setWindowSize | 1532x816 | 
        self.driver.set_window_size(1532, 816)
        # 3 | click | linkText=Summer 2023 | 
        self.driver.find_element(By.LINK_TEXT, "Summer 2023").click()
        # 4 | click | linkText=Homework For Writing SQL Queries | 
        self.driver.find_element(By.LINK_TEXT, "Homework For Writing SQL Queries").click()
        # 5 | click | css=tr:nth-child(2) a | 
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) a").click()
        # 6 | runScript | window.scrollTo(0,358.3999938964844) | 
        self.driver.execute_script("window.scrollTo(0,358.3999938964844)")
        # 7 | runScript | window.scrollTo(0,358.3999938964844) | 
        self.driver.execute_script("window.scrollTo(0,358.3999938964844)")
        # 8 | type | css=.CodeMirror textarea | SELECT * FROM customer
        self.driver.find_element(By.CSS_SELECTOR, ".CodeMirror textarea").send_keys("SELECT * FROM customer")
        # 9 | click | id=execute | 
        self.driver.find_element(By.ID, "execute").click()
        # 10 | click | css=th:nth-child(2) | 
        self.driver.find_element(By.CSS_SELECTOR, "th:nth-child(2)").click()
        # 11 | click | css=th:nth-child(2) | 
        self.driver.find_element(By.CSS_SELECTOR, "th:nth-child(2)").click()
        # 12 | click | css=th:nth-child(3) | 
        self.driver.find_element(By.CSS_SELECTOR, "th:nth-child(3)").click()
        # 13 | click | css=th:nth-child(3) | 
        self.driver.find_element(By.CSS_SELECTOR, "th:nth-child(3)").click()
        # 14 | doubleClick | css=th:nth-child(3) | 
        element = self.driver.find_element(By.CSS_SELECTOR, "th:nth-child(3)")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        # 15 | click | css=th:nth-child(4) | 
        self.driver.find_element(By.CSS_SELECTOR, "th:nth-child(4)").click()
        # 16 | click | css=th:nth-child(4) | 
        self.driver.find_element(By.CSS_SELECTOR, "th:nth-child(4)").click()
        # 17 | doubleClick | css=th:nth-child(4) | 
        element = self.driver.find_element(By.CSS_SELECTOR, "th:nth-child(4)")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        # 18 | click | css=th:nth-child(5) | 
        self.driver.find_element(By.CSS_SELECTOR, "th:nth-child(5)").click()
        # 19 | click | css=th:nth-child(5) | 
        self.driver.find_element(By.CSS_SELECTOR, "th:nth-child(5)").click()
        # 20 | doubleClick | css=th:nth-child(5) | 
        element = self.driver.find_element(By.CSS_SELECTOR, "th:nth-child(5)")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        # 21 | click | css=th:nth-child(1) | 
        self.driver.find_element(By.CSS_SELECTOR, "th:nth-child(1)").click()
        # 22 | click | css=th:nth-child(1) | 
        self.driver.find_element(By.CSS_SELECTOR, "th:nth-child(1)").click()
        # 23 | doubleClick | css=th:nth-child(1) | 
        element = self.driver.find_element(By.CSS_SELECTOR, "th:nth-child(1)")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
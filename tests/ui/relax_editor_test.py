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

# Question 1 ----------------------------------------------------------------------------------------------------------------------------------
class TestRelaxEditorQ1(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options)
        self.baseUrl = "http://localhost:3000/pl/course_instance/1/instructor/question/31/preview"

    def test_relaxClickAddTableName(self):
        # Test name: relaxClickAddTableName
        # Step # | name | target | value
        # 1 | open | http://localhost:3000/pl/course_instance/1/instructor/question/31/preview | 
        self.driver.get(self.baseUrl)
        # 2 | setWindowSize | 1536x816 | 
        self.driver.set_window_size(1536, 816)
        # 3 | click | id=btn-Customer | 
        self.driver.find_element(By.ID, "btn-Customer").click()

    def test_relaxExecuteButton(self):
        # Test name: relaxExecuteButton
        # Step # | name | target | value
        # 1 | open | http://localhost:3000/pl/course_instance/1/instructor/question/31/preview | 
        self.driver.get(self.baseUrl)
        # 2 | setWindowSize | 1536x816 | 
        self.driver.set_window_size(1536, 816)
        # 3 | click | id=execute | 
        self.driver.find_element(By.ID, "execute").click()
    
    def test_relaxExecuteQuery(self):
        # Test name: relaxExecuteQuery
        # Step # | name | target | value
        # 1 | open | http://localhost:3000/pl/course_instance/1/instructor/question/31/preview | 
        self.driver.get(self.baseUrl)
        # 2 | setWindowSize | 1536x816 | 
        self.driver.set_window_size(1536, 816)
        # 3 | click | css=#popWrapper_i4m1hevx8hm > span | 
        self.driver.find_element(By.CSS_SELECTOR, "#popWrapper_i4m1hevx8hm > span").click()
        # 4 | type | css=.CodeMirror textarea |  cid Customer 
        self.driver.find_element(By.CSS_SELECTOR, ".CodeMirror textarea").send_keys(" cid Customer ")
        # 5 | click | css=#popWrapper_wrwiiwklzc > span | 
        self.driver.find_element(By.CSS_SELECTOR, "#popWrapper_wrwiiwklzc > span").click()
        # 6 | type | css=.CodeMirror textarea |  
        self.driver.find_element(By.CSS_SELECTOR, ".CodeMirror textarea").send_keys(" ")
        # 7 | click | id=btn-Shipment | 
        self.driver.find_element(By.ID, "btn-Shipment").click()
        # 8 | click | id=execute | 
        self.driver.find_element(By.ID, "execute").click()
    
    def test_relaxQuestionAccess(self):
        # Test name: relaxQuestionAccess
        # Step # | name | target | value
        # 1 | open | http://localhost:3000/ | 
        self.driver.get("http://localhost:3000/")
        # 2 | setWindowSize | 1536x816 | 
        self.driver.set_window_size(1536, 816)
        # 3 | click | linkText=Summer 2023 | 
        self.driver.find_element(By.LINK_TEXT, "Summer 2023").click()
        # 4 | click | linkText=Homework For Relational Algebra | 
        self.driver.find_element(By.LINK_TEXT, "Homework For Relational Algebra").click()
        # 5 | click | css=tr:nth-child(2) a | 
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) a").click()
    
    def test_relaxClickTreeLeaves(self):
        # Test name: relaxClickTreeLeaves
        # Step # | name | target | value
        # 1 | open | http://localhost:3000/pl/course_instance/1/instructor/question/31/preview | 
        self.driver.get(self.baseUrl)
        # 2 | setWindowSize | 1536x816 | 
        self.driver.set_window_size(1536, 816)
        # 3 | click | css=#popWrapper_i4m1hevx8hm > span | 
        self.driver.find_element(By.CSS_SELECTOR, "#popWrapper_i4m1hevx8hm > span").click()
        # 4 | type | css=.CodeMirror textarea |  cid 
        self.driver.find_element(By.CSS_SELECTOR, ".CodeMirror textarea").send_keys(" cid ")
        # 5 | click | id=btn-Customer | 
        self.driver.find_element(By.ID, "btn-Customer").click()
        # 6 | type | css=.CodeMirror textarea |  
        self.driver.find_element(By.CSS_SELECTOR, ".CodeMirror textarea").send_keys(" ")
        # 7 | click | css=#popWrapper_jgzn81np8i > span | 
        self.driver.find_element(By.CSS_SELECTOR, "#popWrapper_jgzn81np8i > span").click()
        # 8 | type | css=.CodeMirror textarea |  
        self.driver.find_element(By.CSS_SELECTOR, ".CodeMirror textarea").send_keys(" ")
        # 9 | click | id=btn-Shipment | 
        self.driver.find_element(By.ID, "btn-Shipment").click()
        # 10 | click | id=execute | 
        self.driver.find_element(By.ID, "execute").click()
        # 11 | click | xpath=//div[@id='button-⨝']/span/span | 
        self.driver.find_element(By.XPATH, "//div[@id=\'button-⨝\']/span/span").click()
        # 12 | click | css=#button-\&pi\; > span | 
        self.driver.find_element(By.CSS_SELECTOR, "#button-\\&pi\\; > span").click()
        # 13 | click | css=li:nth-child(2) > #button-_inlineRelation8 | 
        self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(2) > #button-_inlineRelation8").click()
        # 14 | click | id=button-_inlineRelation8 | 
        self.driver.find_element(By.ID, "button-_inlineRelation8").click()

    def test_relaxSortOutputTableByColumn(self):
        # Test name: relaxSortOutputTableByColumn
        # Step # | name | target | value
        # 1 | open | http://localhost:3000/pl/course_instance/1/instructor/question/31/preview | 
        self.driver.get(self.baseUrl)
        # 2 | setWindowSize | 1536x816 | 
        self.driver.set_window_size(1536, 816)
        # 3 | click | css=#popWrapper_i4m1hevx8hm > span | 
        self.driver.find_element(By.CSS_SELECTOR, "#popWrapper_i4m1hevx8hm > span").click()
        # 4 | type | css=.CodeMirror textarea |  cid Customer
        self.driver.find_element(By.CSS_SELECTOR, ".CodeMirror textarea").send_keys(" cid Customer")
        # 5 | click | id=execute | 
        self.driver.find_element(By.ID, "execute").click()
        # 6 | click | css=th | 
        self.driver.find_element(By.CSS_SELECTOR, "th").click()
        # 7 | click | css=th | 
        self.driver.find_element(By.CSS_SELECTOR, "th").click()
        # 8 | click | css=th | 
        self.driver.find_element(By.CSS_SELECTOR, "th").click()
        # 9 | click | css=th | 
        self.driver.find_element(By.CSS_SELECTOR, "th").click()
        # 10 | doubleClick | css=th | 
        element = self.driver.find_element(By.CSS_SELECTOR, "th")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        # 11 | click | css=th | 
        self.driver.find_element(By.CSS_SELECTOR, "th").click()
        # 12 | click | css=.CodeMirror-line > span | 
        self.driver.find_element(By.CSS_SELECTOR, ".CodeMirror-line > span").click()
        # 13 | type | css=.CodeMirror textarea | ,city
        self.driver.find_element(By.CSS_SELECTOR, ".CodeMirror textarea").send_keys(",city")
        # 14 | click | id=execute | 
        self.driver.find_element(By.ID, "execute").click()
        # 15 | click | css=th:nth-child(2) | 
        self.driver.find_element(By.CSS_SELECTOR, "th:nth-child(2)").click()
        # 16 | click | css=th:nth-child(2) | 
        self.driver.find_element(By.CSS_SELECTOR, "th:nth-child(2)").click()
        # 17 | click | css=th:nth-child(2) | 
        self.driver.find_element(By.CSS_SELECTOR, "th:nth-child(2)").click()
        # 18 | click | css=th:nth-child(2) | 
        self.driver.find_element(By.CSS_SELECTOR, "th:nth-child(2)").click()
        # 19 | doubleClick | css=th:nth-child(2) | 
        element = self.driver.find_element(By.CSS_SELECTOR, "th:nth-child(2)")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
    
    def test_relaxClickOperationProjection(self):
        # Test name: relaxClickOperationProjection
        # Step # | name | target | value
        # 1 | open | http://localhost:3000/pl/course_instance/1/instructor/question/31/preview | 
        self.driver.get(self.baseUrl)
        # 2 | setWindowSize | 1536x816 | 
        self.driver.set_window_size(1536, 816)
        # 3 | click | css=#popWrapper_i4m1hevx8hm > span | 
        self.driver.find_element(By.CSS_SELECTOR, "#popWrapper_i4m1hevx8hm > span").click()

    def test_relaxClickOperationAnd(self):
        # Test name: relaxClickOperation_And
        # Step # | name | target | value
        # 1 | open | http://localhost:3000/pl/course_instance/1/instructor/question/31/preview | 
        self.driver.get(self.baseUrl)
        # 2 | setWindowSize | 1536x816 | 
        self.driver.set_window_size(1536, 816)
        # 3 | click | css=#popWrapper_lv4upm1exe > span | 
        self.driver.find_element(By.CSS_SELECTOR, "#popWrapper_lv4upm1exe > span").click()
    
    def test_relaxClickOperationAntiJoin(self):
        # Test name: relaxClickOperation_AntiJoin
        # Step # | name | target | value
        # 1 | open | http://localhost:3000/pl/course_instance/1/instructor/question/31/preview | 
        self.driver.get(self.baseUrl)
        # 2 | setWindowSize | 1536x816 | 
        self.driver.set_window_size(1536, 816)
        # 3 | click | css=#popWrapper_ntphproh2gh > span | 
        self.driver.find_element(By.CSS_SELECTOR, "#popWrapper_ntphproh2gh > span").click()
    
    def test_relaxClickOperationAssignment(self):
        # Test name: relaxClickOperation_Assignment
        # Step # | name | target | value
        # 1 | open | http://localhost:3000/pl/course_instance/1/instructor/question/31/preview | 
        self.driver.get(self.baseUrl)
        # 2 | setWindowSize | 1536x816 | 
        self.driver.set_window_size(1536, 816)
        # 3 | click | css=#popWrapper_aq5dkivxzhk > span | 
        self.driver.find_element(By.CSS_SELECTOR, "#popWrapper_aq5dkivxzhk > span").click()
    
    def test_relaxClickOperationCrossJoin(self):
        # Test name: relaxClickOperation_CrossJoin
        # Step # | name | target | value
        # 1 | open | http://localhost:3000/pl/course_instance/1/instructor/question/31/preview | 
        self.driver.get(self.baseUrl)
        # 2 | setWindowSize | 1536x816 | 
        self.driver.set_window_size(1536, 816)
        # 3 | click | css=#popWrapper_bcy1hzhtzbq > span | 
        self.driver.find_element(By.CSS_SELECTOR, "#popWrapper_bcy1hzhtzbq > span").click()
    
    def test_relaxClickOperationDivision(self):
        # Test name: relaxClickOperation_Division
        # Step # | name | target | value
        # 1 | open | http://localhost:3000/pl/course_instance/1/instructor/question/31/preview | 
        self.driver.get(self.baseUrl)
        # 2 | setWindowSize | 1536x816 | 
        self.driver.set_window_size(1536, 816)
        # 3 | click | css=#popWrapper_ytckmx1p4tk > span | 
        self.driver.find_element(By.CSS_SELECTOR, "#popWrapper_ytckmx1p4tk > span").click()
    
    def test_relaxClickOperationUnion(self):
        # Test name: relaxClickOperation_Union
        # Step # | name | target | value
        # 1 | open | http://localhost:3000/pl/course_instance/1/instructor/question/31/preview | 
        self.driver.get(self.baseUrl)
        # 2 | setWindowSize | 1536x816 | 
        self.driver.set_window_size(1536, 816)
        # 3 | click | css=#popWrapper_o60hh3goasp > span | 
        self.driver.find_element(By.CSS_SELECTOR, "#popWrapper_o60hh3goasp > span").click()
    
    def test_relaxClickOperationSubtraction(self):
        # Test name: relaxClickOperation_Subtraction
        # Step # | name | target | value
        # 1 | open | http://localhost:3000/pl/course_instance/1/instructor/question/31/preview | 
        self.driver.get(self.baseUrl)
        # 2 | setWindowSize | 1536x816 | 
        self.driver.set_window_size(1536, 816)
        # 3 | click | css=#popWrapper_2131akj8rbn > span | 
        self.driver.find_element(By.CSS_SELECTOR, "#popWrapper_2131akj8rbn > span").click()
    
    def test_relaxClickOperationSlComment(self):
        # Test name: relaxClickOperation_SlComment
        # Step # | name | target | value
        # 1 | open | http://localhost:3000/pl/course_instance/1/instructor/question/31/preview | 
        self.driver.get(self.baseUrl)
        # 2 | setWindowSize | 1536x816 | 
        self.driver.set_window_size(1536, 816)
        # 3 | click | css=#popWrapper_r2u4dj6ind > span | 
        self.driver.find_element(By.CSS_SELECTOR, "#popWrapper_r2u4dj6ind > span").click()
    
    def test_relaxClickOperationSemiRightJoin(self):
        # Test name: relaxClickOperation_SemiRightJoin
        # Step # | name | target | value
        # 1 | open | http://localhost:3000/pl/course_instance/1/instructor/question/31/preview | 
        self.driver.get(self.baseUrl)
        # 2 | setWindowSize | 1536x816 | 
        self.driver.set_window_size(1536, 816)
        # 3 | click | css=#popWrapper_h8t7el4tebi > span | 
        self.driver.find_element(By.CSS_SELECTOR, "#popWrapper_h8t7el4tebi > span").click()
    
    def test_relaxClickOperationSemiLeftJoin(self):
        # Test name: relaxClickOperation_SemiLeftJoin
        # Step # | name | target | value
        # 1 | open | http://localhost:3000/pl/course_instance/1/instructor/question/31/preview | 
        self.driver.get(self.baseUrl)
        # 2 | setWindowSize | 1536x816 | 
        self.driver.set_window_size(1536, 816)
        # 3 | click | css=#popWrapper_7lmq0e5lt2k > span | 
        self.driver.find_element(By.CSS_SELECTOR, "#popWrapper_7lmq0e5lt2k > span").click()
    
    def test_relaxClickOperationSelection(self):
        # Test name: relaxClickOperation_Selection
        # Step # | name | target | value
        # 1 | open | http://localhost:3000/pl/course_instance/1/instructor/question/31/preview | 
        self.driver.get(self.baseUrl)
        # 2 | setWindowSize | 1536x816 | 
        self.driver.set_window_size(1536, 816)
        # 3 | click | css=#popWrapper_zk54ccpfgr9 > span | 
        self.driver.find_element(By.CSS_SELECTOR, "#popWrapper_zk54ccpfgr9 > span").click()
    
    def test_relaxClickOperationRightArrow(self):
        # Test name: relaxClickOperation_RightArrow
        # Step # | name | target | value
        # 1 | open | http://localhost:3000/pl/course_instance/1/instructor/question/31/preview | 
        self.driver.get(self.baseUrl)
        # 2 | setWindowSize | 1536x816 | 
        self.driver.set_window_size(1536, 816)
        # 3 | click | css=#popWrapper_r4e8qivo9x > span | 
        self.driver.find_element(By.CSS_SELECTOR, "#popWrapper_r4e8qivo9x > span").click()
    
    def test_relaxClickOperationOuterRightJoin(self):
        # Test name: relaxClickOperation_OuterRightJoin
        # Step # | name | target | value
        # 1 | open | http://localhost:3000/pl/course_instance/1/instructor/question/31/preview | 
        self.driver.get(self.baseUrl)
        # 2 | setWindowSize | 1536x816 | 
        self.driver.set_window_size(1536, 816)
        # 3 | click | css=#popWrapper_wrwiiwklzc > span | 
        self.driver.find_element(By.CSS_SELECTOR, "#popWrapper_wrwiiwklzc > span").click()
    
    def test_relaxClickOperationRenameRelationColumns(self):
        # Test name: relaxClickOperation_RenameRelationColumns
        # Step # | name | target | value
        # 1 | open | http://localhost:3000/pl/course_instance/1/instructor/question/31/preview | 
        self.driver.get(self.baseUrl)
        # 2 | setWindowSize | 1536x816 | 
        self.driver.set_window_size(1536, 816)
        # 3 | click | css=#popWrapper_opmskf8udx > span | 
        self.driver.find_element(By.CSS_SELECTOR, "#popWrapper_opmskf8udx > span").click()
    
    def test_relaxClickOperationOuterLeftJoin(self):
        # Test name: relaxClickOperation_OuterLeftJoin
        # Step # | name | target | value
        # 1 | open | http://localhost:3000/pl/course_instance/1/instructor/question/31/preview | 
        self.driver.get(self.baseUrl)
        # 2 | setWindowSize | 1536x816 | 
        self.driver.set_window_size(1536, 816)
        # 3 | click | css=#popWrapper_99cz04sajcd > span | 
        self.driver.find_element(By.CSS_SELECTOR, "#popWrapper_99cz04sajcd > span").click()
    
    def test_relaxClickOperationOuterFullJoin(self):
        # Test name: relaxClickOperation_OuterFullJoin
        # Step # | name | target | value
        # 1 | open | http://localhost:3000/pl/course_instance/1/instructor/question/31/preview | 
        self.driver.get(self.baseUrl)
        # 2 | setWindowSize | 1536x816 | 
        self.driver.set_window_size(1536, 816)
        # 3 | click | css=#popWrapper_xzmnvtls6zk > span | 
        self.driver.find_element(By.CSS_SELECTOR, "#popWrapper_xzmnvtls6zk > span").click()
    
    def test_relaxClickOperationOrderBy(self):
        # Test name: relaxClickOperation_OrderBy
        # Step # | name | target | value
        # 1 | open | http://localhost:3000/pl/course_instance/1/instructor/question/31/preview | 
        self.driver.get(self.baseUrl)
        # 2 | setWindowSize | 1536x816 | 
        self.driver.set_window_size(1536, 816)
        # 3 | click | css=#popWrapper_rm8nadc63ta > span | 
        self.driver.find_element(By.CSS_SELECTOR, "#popWrapper_rm8nadc63ta > span").click()
    
    def test_relaxClickOperationOr(self):
        # Test name: relaxClickOperation_Or
        # Step # | name | target | value
        # 1 | open | http://localhost:3000/pl/course_instance/1/instructor/question/31/preview | 
        self.driver.get(self.baseUrl)
        # 2 | setWindowSize | 1536x816 | 
        self.driver.set_window_size(1536, 816)
        # 3 | click | css=#popWrapper_wihrg7pw86c > span | 
        self.driver.find_element(By.CSS_SELECTOR, "#popWrapper_wihrg7pw86c > span").click()
    
    def test_relaxClickOperationNotEqual(self):
        # Test name: relaxClickOperation_NotEqual
        # Step # | name | target | value
        # 1 | open | http://localhost:3000/pl/course_instance/1/instructor/question/31/preview | 
        self.driver.get(self.baseUrl)
        # 2 | setWindowSize | 1536x816 | 
        self.driver.set_window_size(1536, 816)
        # 3 | click | css=#popWrapper_qfox1fuq55 > span | 
        self.driver.find_element(By.CSS_SELECTOR, "#popWrapper_qfox1fuq55 > span").click()
    
    def test_relaxClickOperationNot(self):
        # Test name: relaxClickOperation_Not
        # Step # | name | target | value
        # 1 | open | http://localhost:3000/pl/course_instance/1/instructor/question/31/preview | 
        self.driver.get(self.baseUrl)
        # 2 | setWindowSize | 1536x816 | 
        self.driver.set_window_size(1536, 816)
        # 3 | click | css=#popWrapper_mx0q4np8lms > span | 
        self.driver.find_element(By.CSS_SELECTOR, "#popWrapper_mx0q4np8lms > span").click()
    
    def test_relaxClickOperationNaturalJoin(self):
        # Test name: relaxClickOperation_NaturalJoin
        # Step # | name | target | value
        # 1 | open | http://localhost:3000/pl/course_instance/1/instructor/question/31/preview | 
        self.driver.get(self.baseUrl)
        # 2 | setWindowSize | 1536x816 | 
        self.driver.set_window_size(1536, 816)
        # 3 | click | css=#popWrapper_jgzn81np8i > span | 
        self.driver.find_element(By.CSS_SELECTOR, "#popWrapper_jgzn81np8i > span").click()
    
    def test_relaxClickOperationMlComment(self):
        # Test name: relaxClickOperation_MlComment
        # Step # | name | target | value
        # 1 | open | http://localhost:3000/pl/course_instance/1/instructor/question/31/preview | 
        self.driver.get(self.baseUrl)
        # 2 | setWindowSize | 1536x816 | 
        self.driver.set_window_size(1536, 816)
        # 3 | click | css=#popWrapper_2znla6h967q > span | 
        self.driver.find_element(By.CSS_SELECTOR, "#popWrapper_2znla6h967q > span").click()
    
    def test_relaxClickOperationLessThanOrEqual(self):
        # Test name: relaxClickOperation_LessThanOrEqual
        # Step # | name | target | value
        # 1 | open | http://localhost:3000/pl/course_instance/1/instructor/question/31/preview | 
        self.driver.get(self.baseUrl)
        # 2 | setWindowSize | 1536x816 | 
        self.driver.set_window_size(1536, 816)
        # 3 | click | css=#popWrapper_tc2rsc59fbq > span | 
        self.driver.find_element(By.CSS_SELECTOR, "#popWrapper_tc2rsc59fbq > span").click()
    
    def test_relaxClickOperationLeftArrow(self):
        # Test name: relaxClickOperation_LeftArrow
        # Step # | name | target | value
        # 1 | open | http://localhost:3000/pl/course_instance/1/instructor/question/31/preview | 
        self.driver.get(self.baseUrl)
        # 2 | setWindowSize | 1536x816 | 
        self.driver.set_window_size(1536, 816)
        # 3 | click | css=#popWrapper_vqmsrbz4lhh > span | 
        self.driver.find_element(By.CSS_SELECTOR, "#popWrapper_vqmsrbz4lhh > span").click()
    
    def test_relaxClickOperationIntersection(self):
        # Test name: relaxClickOperation_Intersection
        # Step # | name | target | value
        # 1 | open | http://localhost:3000/pl/course_instance/1/instructor/question/31/preview | 
        self.driver.get(self.baseUrl)
        # 2 | setWindowSize | 1536x816 | 
        self.driver.set_window_size(1536, 816)
        # 3 | click | css=#popWrapper_q8ve1atlpu > span | 
        self.driver.find_element(By.CSS_SELECTOR, "#popWrapper_q8ve1atlpu > span").click()
    
    def test_relaxClickOperationInsertDate(self):
        # Test name: relaxClickOperation_InsertDate
        # Step # | name | target | value
        # 1 | open | http://localhost:3000/pl/course_instance/1/instructor/question/31/preview | 
        self.driver.get(self.baseUrl)
        # 2 | setWindowSize | 1536x816 | 
        self.driver.set_window_size(1536, 816)
        # 3 | click | css=.fa-calendar-alt > path | 
        self.driver.find_element(By.CSS_SELECTOR, ".fa-calendar-alt > path").click()
    
    def test_relaxClickOperationInlineRelation(self):
        # Test name: relaxClickOperation_InlineRelation
        # Step # | name | target | value
        # 1 | open | http://localhost:3000/pl/course_instance/1/instructor/question/31/preview | 
        self.driver.get(self.baseUrl)
        # 2 | setWindowSize | 1536x816 | 
        self.driver.set_window_size(1536, 816)
        # 3 | click | css=#popWrapper_2aod06t35hu > span | 
        self.driver.find_element(By.CSS_SELECTOR, "#popWrapper_2aod06t35hu > span").click()
    
    def test_relaxClickOperationGroupBy(self):
        # Test name: relaxClickOperation_GroupBy
        # Step # | name | target | value
        # 1 | open | http://localhost:3000/pl/course_instance/1/instructor/question/31/preview | 
        self.driver.get(self.baseUrl)
        # 2 | setWindowSize | 1536x816 | 
        self.driver.set_window_size(1536, 816)
        # 3 | click | css=#popWrapper_yelfh6roevh > span | 
        self.driver.find_element(By.CSS_SELECTOR, "#popWrapper_yelfh6roevh > span").click()
    
    def test_relaxClickOperationGreaterThanOrEqual(self):
        # Test name: relaxClickOperation_GreaterThanOrEqual
        # Step # | name | target | value
        # 1 | open | http://localhost:3000/pl/course_instance/1/instructor/question/31/preview | 
        self.driver.get(self.baseUrl)
        # 2 | setWindowSize | 1536x816 | 
        self.driver.set_window_size(1536, 816)
        # 3 | click | css=#popWrapper_3ixqdjahm8v > span | 
        self.driver.find_element(By.CSS_SELECTOR, "#popWrapper_3ixqdjahm8v > span").click()
    
    def test_relaxClickOperationEqual(self):
        # Test name: relaxClickOperation_Equal
        # Step # | name | target | value
        # 1 | open | http://localhost:3000/pl/course_instance/1/instructor/question/31/preview | 
        self.driver.get(self.baseUrl)
        # 2 | setWindowSize | 1536x816 | 
        self.driver.set_window_size(1536, 816)
        # 3 | click | css=#popWrapper_iwcqg10p7gn > span | 
        self.driver.find_element(By.CSS_SELECTOR, "#popWrapper_iwcqg10p7gn > span").click()


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()    
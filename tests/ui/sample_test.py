from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class TestSample(unittest.TestCase):

    def setUp(self):

        driver = webdriver.Chrome(ChromeDriverManager().install())


    def testPageName(self):
        baseUrl = 'http://pl:3000/'
        driver = self.driver
        driver.get(baseUrl)
        assert 'PrairieLearn' in driver.title
        print(driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

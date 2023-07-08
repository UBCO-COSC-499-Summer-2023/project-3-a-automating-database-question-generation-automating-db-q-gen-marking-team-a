import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class TestSample(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')  # Add this line to avoid sandbox issues
        options.add_argument('--disable-dev-shm-usage')  # Add this line to avoid /dev/shm usage
        self.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=options)

    def testPageName(self):
        baseUrl = 'http://pl:3000/'  # Update the URL to use the service name defined in docker-compose.yml
        driver = self.driver
        driver.get(baseUrl)
        assert 'PrairieLearn' in self.driver.title
        print(self.driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

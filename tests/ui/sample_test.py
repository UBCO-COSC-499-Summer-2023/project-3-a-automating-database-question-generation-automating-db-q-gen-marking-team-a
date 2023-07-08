import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class TestSample(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        # Set the path to the ChromeDriver executable
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--window-size=1920,1080')
        chrome_options.add_argument('--disable-infobars')
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-setuid-sandbox')
        chrome_options.add_argument('--remote-debugging-port=9222')
        chrome_options.add_argument('--disable-blink-features=BlockCredentialedSubresources')
        chrome_options.add_argument('--disable-web-security')

        # Use webdriver_manager to manage ChromeDriver
        chrome_driver_path = ChromeDriverManager().install()
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

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

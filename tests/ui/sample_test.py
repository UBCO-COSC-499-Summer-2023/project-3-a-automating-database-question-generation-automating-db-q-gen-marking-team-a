import os
import shutil
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class TestSample(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        # Specify the directory where the ChromeDriver binary will be moved
        chromedriver_dir = '/usr/local/bin'

        # Set the path to the ChromeDriver executable
        chromedriver_path = '/usr/bin/chromedriver'

        # Move the ChromeDriver binary to the specified directory
        shutil.move(chromedriver_path, chromedriver_dir)

        # Set the permissions of the ChromeDriver binary
        os.chmod(os.path.join(chromedriver_dir, 'chromedriver'), 0o755)

        # Now the ChromeDriver binary should be in a directory in the system's PATH
        self.driver = webdriver.Chrome(options=options)

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

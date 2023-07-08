import os
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class TestSample(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')  # Add this line to avoid sandbox issues
        options.add_argument('--disable-dev-shm-usage')  # Add this line to avoid /dev/shm usage
        options.add_argument('--disable-gpu')  # Add this line to disable GPU usage
        options.add_argument('--window-size=1920,1080')  # Add this line to set the window size
        options.add_argument('--disable-infobars')  # Add this line to disable infobars
        options.add_argument('--disable-extensions')  # Add this line to disable extensions
        options.add_argument('--disable-dev-shm-usage')  # Add this line to disable /dev/shm usage
        options.add_argument('--no-sandbox')  # Add this line to avoid sandbox issues

        # Set the path to the ChromeDriver executable
        options.add_argument('--webdriver=/usr/bin/chromedriver')

        self.driver = webdriver.Chrome(options=options)

    def testPageName(self):
        baseUrl = 'http://pl:3000/'  # Update the URL to use the service name defined in docker-compose.yml
        driver = self.driver
        driver.get(baseUrl)
        assert 'PrairieLearn' in self.driver.title
        print(self.driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    # Print the contents of /usr/bin directory
    print("Contents of /usr/bin directory:")
    print(os.listdir('/usr/bin'))

    unittest.main()

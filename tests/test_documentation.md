# Testing Documentation
-Tests will be modularized

- To run any test-file(ui/unit/integration/anything) just enter the following into your terminalonce you're in the appropriate directory: 
"python -m unittest testfilename.py"
    - ex. "python -m unittest tests/ui/sample.py"

## Unit Testing
- Using Python's Unittest framework to cover python code

## UI Testing
- "pip install selenium" to ensure all ui tests run.
- Automated using Python's Unittest framework
- If you haven't used Selenium for UI testing before, know that once you run a UI test file, it will open up a browser (depending on what you set in the testfile), and start executing the test in front of you. You do not need to do anything while this happens. But to avoid this you can also run the tests in headless mode.

## CI/CD
- configure your drone.yml file and then once it's hooked up to Drone using Scott's instructions, you're good to go

## Selenium
- Selenium is pretty useful for ui testing, and can be done in different languages.
- In this project, we wrote it in python so the instructions will be for that:
1. pip install selenium
2. Download webdriver for whatever browser you decide to do your ui tests on primarily
3. Download the Selenium IDE on a browser (makes writing UI tests SIGNIFICANTLY easier)
4. From there, once you have your application running on your localhost, open Selenium IDE and set it up
5. Create a test and specify the base-url (ex. localhost:3000/menu/item)
    - your base-url does not need to be the same for all tests, but unless you specify, Selenium IDE will use the same for all
6. Click record and this will open up the link you specified on a browser and starts recording anything you do on the page
    - scroll, click, type, etc.
7. Once you're done recording a test, stop recording from the IDE and you will see your test appear there
8. From here you can just export the test to whatever language options they give you
    - Note that you can modify these tests in the code
9. Make your test file and use unittest or any unit testing framework to automate your UI tests 
10. Define your setup function to contain your browser setup for the UI tests
11. Add your test methods from Selenium and make sure you also add a teardown function to close the webdrivers, etc.

* Our group was unsuccessful with running our UI tests on Drone - we kept running into chromedriver issues and other problems that took up
a lot of our time just for it to not end up working in the end. If you find yourself running into similar issues with Drone, we suggest you don't waste more time on it. Write all your UI tests, run them locally and treat the integration of selenium tests into Drone as your very last priority, if that.

* Sometimes if you have stuff that takes time to load, tests that involve that stuff will pass when you run them on the Selenium IDE, but have a chance of failing when you run your testfile itself - this is because you need to add code to wait for those things to load before interacting with them
import unittest
from SQLElementSharedLibrary.SQLAutogenerator import *

class AutogeneratorTest(unittest.TestCase):

    # autogenerate Tests------------------------------------------------------------------------------------------------------------------
    # case1 : enter an invalid difficulty
    def testAutogenerateInvalidDifficultyReturnsNone(self):
        data = {'params':{'html_params':{'random':{},'questionType':{},'difficulty':{}}}}

        result = autogenerate(data)

        self.assertIsNone(result)
    



if __name__ == '__main__':
    unittest.main()
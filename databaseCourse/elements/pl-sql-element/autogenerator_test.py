import unittest
from SQLElementSharedLibrary.SQLAutogenerator import *

class AutogeneratorTest(unittest.TestCase):

    # autogenerate Tests------------------------------------------------------------------------------------------------------------------
    # case1 : enter an invalid difficulty
    def testAutogenerateInvalidDifficultyReturnsNone(self):
        data = {'params':{'html_params':{'random':{},'questionType':{},'difficulty':{}}}}

        result = autogenerate(data)

        self.assertIsNone(result)
    
    # case2 : valid type and difficulty = create , easy
    def testAutogenerateCreateType(self):
        initialAns = '\n    '
        data = {'params':{'html_params':{'questionType':"create",'difficulty':"easy"}},
                'correct_answers':{'SQLEditor': initialAns}}
        
        self.assertEqual(len(data['correct_answers']['SQLEditor']),len(initialAns))
        
        autogenerate(data)
        
        self.assertGreater(len(data['correct_answers']['SQLEditor']),len(initialAns))
        actualQuestionType = data['params']['questionString'].split()[0]
        self.assertEqual(actualQuestionType,"Create")

if __name__ == '__main__':
    unittest.main()
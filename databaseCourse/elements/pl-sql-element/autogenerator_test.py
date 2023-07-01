import unittest
from parameterized import parameterized
from SQLElementSharedLibrary.SQLAutogenerator import *

class AutogeneratorTest(unittest.TestCase):

    # autogenerate() Tests------------------------------------------------------------------------------------------------------------------
    # case1 : enter an invalid difficulty
    def testAutogenerateInvalidDifficultyReturnsNone(self):
        data = {'params':{'html_params':{'random':{},'questionType':{},'difficulty':{}}}}

        result = autogenerate(data)

        self.assertIsNone(result)

    # case 2: valid inputs return correct questions
    @parameterized.expand([
            ["create","easy","create"],
            ["insert","easy","insert"],
            ["update","easy","change"],
            ["delete","easy","delete"],
            ["query","easy","select"],
            ["create","medium","create"],
            ["insert","medium","insert"],
            ["update","medium","change"],
            ["delete","medium","delete"],
            ["query","medium","select"],
            ["create","hard","create"],
            ["insert","hard","insert"],
            # ["update","hard","change"], #not implemented yet
            # ["delete","hard","delete"], #not implemented yet
            ["query","hard","select"]
            ])
    def test_autogenerate(self,testType,difficulty,keyWord):
        initialAns = "\n"
        db_initalize = ""
        data = {'params':{'html_params':{'questionType':testType,'difficulty':difficulty},
                          'db_initialize':db_initalize},
                'correct_answers':{'SQLEditor': initialAns}}
        
        autogenerate(data)
        print("start",data['correct_answers']['SQLEditor'],"end")
        
        self.assertGreater(len(data['correct_answers']['SQLEditor']),len(initialAns))
        actualQuestionType = ''.join(data['params']['questionString']).lower()
        self.assertIn(keyWord,actualQuestionType)

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    unittest.main()
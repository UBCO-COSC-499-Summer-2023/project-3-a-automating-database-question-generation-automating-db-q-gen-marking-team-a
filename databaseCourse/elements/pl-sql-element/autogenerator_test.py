import unittest
from parameterized import parameterized
from SQLElementSharedLibrary.SQLAutogenerator import *

class AutogeneratorTest(unittest.TestCase):

    # DONE
#---# autogenerate() Tests------------------------------------------------------------------------------------------------------------------
    # case1 : enter an invalid difficulty
    def testAutogenerateInvalidDifficultyReturnsNone(self):
        data = {'params':{'html_params':{'random':{},'questionType':{},'difficulty':{}}}}

        result = autogenerate(data)

        self.assertIsNone(result)

    # case 2: valid inputs return correct questions - testing each type with each difficulty here
    @parameterized.expand([
            # questionType , difficulty, keyword to check in question, 
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
        if testType == "query":
            print("start",data['params']['questionString'],"end")
        
        self.assertGreater(len(data['correct_answers']['SQLEditor']),len(initialAns))
        actualQuestionType = ''.join(data['params']['questionString']).lower()
        self.assertIn(keyWord,actualQuestionType)
    
    # TODO
    # generate*QuestionType*() Tests------------------------------------------------------------------------------------------------------------------
    
#---# generateCreate() Test(s)
#---# generateInsert() Test(s)
#---# generateUpdate() Test(s)
#---# generateDelete() Test(s)
#---# generateQuery() Test(s)

    # TODO
    # *questionType*Statement() Tests------------------------------------------------------------------------------------------------------------------

#---# createStatement() Test(s)
#---# insertStatement() Test(s)
#---# updateStatement() Test(s)
#---# deleteStatement() Test(s)
#---# queryStatement() Test(s)

    # TODO
    # helper functions Tests------------------------------------------------------------------------------------------------------------------

#---# conditionalStatement Test(s)

#---# relativeFilePath Test(s)

#---# getReferencedDatabasesSet Test(s)
#---# getReferencedDatabaseDictionary Test(s)

#---# loadSchemas Test(s)
#---# loadAllSchema Test(s)

#---# loadNoisyData Test(s)
#---# loadAllNoisyData Test(s)
#---# loadTrimmedDatabase Test(s)

#---# generateRow Test(s)
#---# generateRows Test(s)

#---# generateNoisyData Test(s)
#---# generateNoisyInteger Test(s)
#---# generateNoisyChar Test(s)
#---# generateNoisyVarchar Test(s)

#---# generateRandomDate Test(s)
#---# generateRandomDateTime Test(s)

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    unittest.main()
import unittest
from parameterized import parameterized
from SQLElementSharedLibrary.SQLAutogenerator import *

class AutogenerateTest(unittest.TestCase):

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
            # TODO
            # ["update","hard","change"], #not implemented yet
            # ["delete","hard","delete"], #not implemented yet
            ["query","hard","select"]
            ])
    def testAutogenerateReturnsCorrectQuestionType(self,testType,difficulty,keyWord):
        initialAns = "\n"
        db_initalize = ""
        data = {'params':{'html_params':{'questionType':testType,'difficulty':difficulty},
                          'db_initialize':db_initalize},
                'correct_answers':{'SQLEditor': initialAns}}
        
        autogenerate(data)
        
        self.assertGreater(len(data['correct_answers']['SQLEditor']),len(initialAns))
        actualQuestionType = ''.join(data['params']['questionString']).lower()
        self.assertIn(keyWord,actualQuestionType)
    
    # TODO
    # generate*QuestionType*() Tests------------------------------------------------------------------------------------------------------------------
#---# generateCreate() - already tested & covered in AutogenerateTest class
#---# generateInsert() - already tested & covered in AutogenerateTest class
#---# generateDelete() Test(s) - already tested & covered in AutogenerateTest class
class QuestionGenerationTest(unittest.TestCase):
#---# generateUpdate() Test(s)
    # Does not use a conditional clause
    def testGenerateUpdateDoesNotReturnConditionalClauseWhenEasy(self):
        testType = "Update"
        db_initialize = ""
        initialAns = ""
        difficulty = "easy"
        data = {'params':{'html_params':{'questionType':testType,'difficulty':difficulty},
                          'db_initialize':db_initialize},
                'correct_answers':{'SQLEditor': initialAns}}
        
        generateUpdate(data,difficulty)

        actualQuestionType = ''.join(data['params']['questionString']).lower()
        self.assertNotIn("where",actualQuestionType)

    # Uses a conditional clause when medium
    def testGenerateUpdateReturnsConditionalClauseWhenMedium(self):
        testType = "Update"
        db_initialize = ""
        initialAns = ""
        difficulty = "medium"
        data = {'params':{'html_params':{'questionType':testType,'difficulty':difficulty},
                          'db_initialize':db_initialize},
                'correct_answers':{'SQLEditor': initialAns}}
        
        generateUpdate(data,difficulty)

        actualQuestionType = ''.join(data['params']['questionString']).lower()
        self.assertIn("where",actualQuestionType)
    
    # case for hard difficulty

    # TODO
#---# generateQuery() Test(s)
    # joins == 0, clauses == 0
    # def testGenerateQueryReturnsEasyQuestion(self):
    #     testType = "query"
    #     db_initialize = ""
    #     initialAns = ""
    #     difficulty = "medium"
    #     data = {'params':{'html_params':{'questionType':testType,'difficulty':difficulty},
    #                       'db_initialize':db_initialize},
    #             'correct_answers':{'SQLEditor': initialAns}}
        
    #     generateQuery(data,difficulty)
    #     print(data)

    #     actualQuestionType = ''.join(data['params']['questionString']).lower()
    #     self.assertIn("where",actualQuestionType)
    # joins != 0, clauses == 0
    # joins != 0, clauses != 0

    # TODO
    # *questionType*Statement() Tests------------------------------------------------------------------------------------------------------------------
class QuestionTypeStatementsTest(unittest.TestCase):

#---# createStatement() Test(s)
    # all databases are properly parsed into creating a create statement
    @parameterized.expand([
        ["airport"],
        ["airplane"],
        ["passenger"],
        ["flight"]
    ])
    def testCreateStatementReturnsStatementWithAllColumns(self,databaseFile):
        database = db.load(relativeFilePath(databaseFile))
        dbName = database.name

        result = createStatement(database)
        
        self.assertIn("CREATE",result)
        self.assertNotIn("INSERT",result)
        self.assertNotIn("UPDATE",result)
        self.assertNotIn("DELETE",result)
        self.assertNotIn("SELECT",result)
        self.assertIn(dbName,result)
        for key in database.columns:
            self.assertIn(key,result)
            self.assertIn(database.columns[key]["unit"],result)

#---# insertStatement() Test(s)
    # valid input -> valid output
    def testInsertStatementReturnsCorrectTableNameAndValuesInStatement(self):
        dbName = "airport"
        row = [9,8,0]
        database = db.load(relativeFilePath(dbName))

        result = insertStatement(database,row)

        self.assertIn(dbName,result)
        for x in row:
            self.assertIn(str(x),result)
        self.assertIn("INSERT",result)
        self.assertNotIn("CREATE",result)
        self.assertNotIn("UPDATE",result)
        self.assertNotIn("DELETE",result)
        self.assertNotIn("SELECT",result)

#---# updateStatement() Test(s)
    # with conditional
    def testUpdateStatementWithConditional(self):
        dbName = "airport"
        database = db.load(relativeFilePath(dbName))
        updateCol= "province"
        updateVal = "Alberta"
        conditionalCol = updateCol
        conditionalVal = "Ontario"

        result = updateStatement(database,updateCol,updateVal,conditionalCol,conditionalVal)

        self.assertIn("UPDATE",result)
        self.assertIn("WHERE",result)
        self.assertNotIn("CREATE",result)
        self.assertNotIn("INSERT",result)
        self.assertNotIn("DELETE",result)
        self.assertNotIn("SELECT",result)

    # without conditional
    def testUpdateStatementWithoutConditional(self):
        dbName = "airport"
        database = db.load(relativeFilePath(dbName))
        updateCol = "province"
        updateVal = "Alberta"

        result = updateStatement(database,updateCol,updateVal)

        self.assertIn("UPDATE",result)
        self.assertNotIn("WHERE",result)
        self.assertNotIn("CREATE",result)
        self.assertNotIn("INSERT",result)
        self.assertNotIn("DELETE",result)
        self.assertNotIn("SELECT",result)
        
#---# deleteStatement() Test(s)
    # with a condition
    def testDeleteStatementWithConditional(self):
        dbName = "airport"
        database = db.load(relativeFilePath(dbName))
        col = "province"
        condition = "Alberta"

        result = deleteStatement(database,col,condition)

        self.assertIn("DELETE",result)
        self.assertIn("WHERE",result)
        self.assertNotIn("CREATE",result)
        self.assertNotIn("INSERT",result)
        self.assertNotIn("UPDATE",result)
        self.assertNotIn("SELECT",result)

    # without a condition
    def testDeleteStatementWithoutConditional(self):
        dbName = "airport"
        database = db.load(relativeFilePath(dbName))

        result = deleteStatement(database)

        self.assertIn("DELETE",result)
        self.assertNotIn("WHERE",result)
        self.assertNotIn("CREATE",result)
        self.assertNotIn("INSERT",result)
        self.assertNotIn("UPDATE",result)
        self.assertNotIn("SELECT",result)

#---# queryStatement() Test(s)

    # TODO
    # helper functions Tests------------------------------------------------------------------------------------------------------------------
class HelperFnsTest(unittest.TestCase):
    def emptyTest(self):
        pass
#---# conditionalStatement() Test(s)

#---# relativeFilePath() Test(s)

#---# getReferencedDatabasesSet() Test(s)
#---# getReferencedDatabaseDictionary() Test(s)

#---# loadSchemas() Test(s)
#---# loadAllSchema() Test(s)

#---# loadNoisyData() Test(s)
#---# loadAllNoisyData() Test(s)
#---# loadTrimmedDatabase() Test(s)

#---# generateRow() Test(s)
#---# generateRows() Test(s)

#---# generateNoisyData() Test(s)
#---# generateNoisyInteger() Test(s)
#---# generateNoisyChar() Test(s)
#---# generateNoisyVarchar() Test(s)

#---# generateRandomDate() Test(s)
#---# generateRandomDateTime() Test(s)

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    unittest.main()
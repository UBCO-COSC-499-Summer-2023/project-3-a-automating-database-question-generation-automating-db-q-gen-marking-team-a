import unittest
from parameterized import parameterized
from SQLElementSharedLibrary.SQLAutogenerator import *

class AutogenerateTest(unittest.TestCase):

    # DONE
#---# autogenerate() Tests------------------------------------------------------------------------------------------------------------------
    # case1 : enter an invalid difficulty
    def testAutogenerateInvalidDifficultyReturnsNone(self):
        data = {'params':{'html_params':{'random':{},'questionType':{},'difficulty':'not valid difficulty'}}}

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
            # TODO: needs to be implemented
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
    def testGenerateQueryReturnsEasyQuestion(self):
        testType = "query"
        db_initialize = ""
        initialAns = ""
        difficulty = "medium"
        data = {'params':{'html_params':{'questionType':testType,'difficulty':difficulty},
                          'db_initialize':db_initialize},
                'correct_answers':{'SQLEditor': initialAns}}
        
        generateQuery(data,difficulty)

        actualQuestionType = ''.join(data['params']['questionString']).lower()
        self.assertIn("select the columns",actualQuestionType)
    # joins != 0, clauses == 0
    # joins != 0, clauses != 0

    # *questionType*Statement() Tests------------------------------------------------------------------------------------------------------------------
class QuestionTypeStatementsTest(unittest.TestCase):

#---# createStatement() Test(s)
    # all tables are properly parsed into creating a create statement
    @parameterized.expand([
        ["airport"],
        ["airplane"],
        ["passenger"],
        ["flight"]
    ])
    def testCreateStatementReturnsStatementWithAllColumns(self,tableFile):
        table = db.Table(tableFile)
        tableName = table.name

        result = createStatement(table)
        
        # Can't test UPDATE not in tables for all tables
        # since the clause "ON UPDATE CASCADE" would
        # erroneously fail the test
        #self.assertNotIn("UPDATE",result)

        # Similarly, DELETE is untestable due to the 
        # clause "ON DELETE SET NULL"
        #self.assertNotIn("DELETE",result)

        self.assertIn("CREATE",result)
        self.assertNotIn("INSERT",result)
        self.assertNotIn("SELECT",result)
        self.assertIn(tableName,result)
        for key in table.columns:
            self.assertIn(key,result)
            self.assertIn(table.columns[key]["unit"],result)

#---# insertStatement() Test(s)
    # valid input -> valid output
    def testInsertStatementReturnsCorrectTableNameAndValuesInStatement(self):
        tableName = "airport"
        row = [9,8,0]
        table = db.Table(tableName)

        result = insertStatement(table,row)

        self.assertIn(tableName,result)
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
        tableName = "airport"
        table = db.Table(tableName)
        updateCol= "province"
        updateVal = "Alberta"
        conditionalCol = updateCol
        conditionalVal = "Ontario"

        result = updateStatement(table,updateCol,updateVal,conditionalCol,conditionalVal)

        self.assertIn("UPDATE",result)
        self.assertIn("WHERE",result)
        self.assertNotIn("CREATE",result)
        self.assertNotIn("INSERT",result)
        self.assertNotIn("DELETE",result)
        self.assertNotIn("SELECT",result)

    # without conditional
    def testUpdateStatementWithoutConditional(self):
        tableName = "airport"
        table = db.Table(tableName)
        updateCol = "province"
        updateVal = "Alberta"

        result = updateStatement(table,updateCol,updateVal)

        self.assertIn("UPDATE",result)
        self.assertNotIn("WHERE",result)
        self.assertNotIn("CREATE",result)
        self.assertNotIn("INSERT",result)
        self.assertNotIn("DELETE",result)
        self.assertNotIn("SELECT",result)
        
#---# deleteStatement() Test(s)
    # with a condition
    def testDeleteStatementWithConditional(self):
        tableName = "airport"
        table = db.Table(tableName)
        col = "province"
        condition = "Alberta"

        result = deleteStatement(table,col,condition)

        self.assertIn("DELETE",result)
        self.assertIn("WHERE",result)
        self.assertNotIn("CREATE",result)
        self.assertNotIn("INSERT",result)
        self.assertNotIn("UPDATE",result)
        self.assertNotIn("SELECT",result)

    # without a condition
    def testDeleteStatementWithoutConditional(self):
        tableName = "airport"
        table = db.Table(tableName)

        result = deleteStatement(table)

        self.assertIn("DELETE",result)
        self.assertNotIn("WHERE",result)
        self.assertNotIn("CREATE",result)
        self.assertNotIn("INSERT",result)
        self.assertNotIn("UPDATE",result)
        self.assertNotIn("SELECT",result)

    # TODO: not fully implemented yet
#---# queryStatement() Test(s)
    # no foreignkeys
    # def testQueryStatementWithoutForeignKeys(self):
    #     tableName = "airport"
    #     table = db.Table(tableName)
    #     keyMap = {"airport"}
    #     foreignKeyMap = {}
    #     selectedColumns = []
    #     clauses = None

    #     result = queryStatement(table,keyMap,foreignKeyMap,selectedColumns,clauses)
        
    # helper functions Tests------------------------------------------------------------------------------------------------------------------
class HelperFnsTest(unittest.TestCase):
#---# conditionalStatement() Test(s)
    def testConditionalStatementReturnsStatementWithWhere(self):
        column = ""
        condition = ""

        result = conditionalStatement(column,condition)

        self.assertIn("WHERE",result)

#---# getReferencedTablesSet() Test(s)
    # has referenced tables
    def testGetReferencedTablesSetGetsAllReferencedDbs(self):
        tableName = "flight"
        referenced = ["airplane","airport","passenger"]
        table = db.Table(tableName)

        result = getReferencedTables(table, unique=True)

        self.assertIsInstance(result,dict)
        for x in result:
            self.assertIn(x.name,referenced)

    # has no referenced tables
    def testGetReferencedTablesSetGetsAllZeroReferencedDbs(self):
        tableName = "airport"
        referenced = ["airplane","airport","passenger"]
        table = db.Table(tableName)

        result = getReferencedTables(table, unique=True)

        self.assertIsInstance(result,dict)
        for x in result:
            self.assertNotIn(x.name,referenced)

#---# getReferencedTableDictionary() Test(s)
    # has referenced tables
    def testGetReferencedTablesDictionaryGetsAllReferencedDbs(self):
        tableName = "flight"
        referenced = ["airplane","airport","passenger"]
        table = db.Table(tableName)

        result = getReferencedTables(table, unique=False)

        self.assertIsInstance(result,dict)
        for x in result:
            self.assertIn(x,referenced)

    # has no referenced tables
    def testGetReferencedTablesDictionaryGetsAllZeroReferencedDbs(self):
        tableName = "airport"
        referenced = ["airplane","airport","passenger"]
        table = db.Table(tableName)

        result = getReferencedTables(table, unique=False)

        self.assertIsInstance(result,dict)
        for x in result:
            self.assertNotIn(x,referenced)

#---# loadSchemas() Test(s)
    # all tables are added to db init 
    def testLoadSchemasAddsTablesToDbInit(self):
        testType = "Update"
        db_initialize = ""
        initialAns = ""
        difficulty = "easy"
        data = {'params':{'html_params':{'questionType':testType,'difficulty':difficulty},
                          'db_initialize':db_initialize},
                'correct_answers':{'SQLEditor': initialAns}}
        tableOne = "airport"
        tableAirport = db.Table(tableOne)
        tableTwo = "flight"
        tableFlight = db.Table(tableTwo)
        tableThree = "airplane"
        tableAirplane = db.Table(tableThree)
        tables = {tableOne: tableAirport, tableThree: tableAirplane}

        self.assertEqual(len(data['params']['db_initialize']),0)

        loadSchemas(data,tableFlight,tables)

        self.assertIn(tableOne,data['params']['db_initialize'])
        self.assertIn(tableTwo,data['params']['db_initialize'])
        self.assertIn(tableThree,data['params']['db_initialize'])

    # no tables are added to db init when input is empty
    def testLoadSchemasAddsNoTablesToDbInit(self):
        testType = "Update"
        db_initialize = ""
        initialAns = ""
        difficulty = "easy"
        data = {'params':{'html_params':{'questionType':testType,'difficulty':difficulty},
                          'db_initialize':db_initialize},
                'correct_answers':{'SQLEditor': initialAns}}
        table = None
        tables = []

        self.assertEqual(len(data['params']['db_initialize']),0)

        loadSchemas(data,table,tables)

        self.assertEqual(len(data['params']['db_initialize']),0)

#---# loadAllSchema() Test(s)
    # table with no other referenced tables
    def testLoadAllSchemaAddsTableWithNoReferencesToDbInit(self):
        testType = "Update"
        db_initialize = ""
        initialAns = ""
        difficulty = "easy"
        data = {'params':{'html_params':{'questionType':testType,'difficulty':difficulty},
                          'db_initialize':db_initialize},
                'correct_answers':{'SQLEditor': initialAns}}
        tableOne = "airport"
        tableAirport = db.Table(tableOne)

        self.assertEqual(len(data['params']['db_initialize']),0)

        loadAllSchema(data,tableAirport)

        self.assertIn(tableOne,data['params']['db_initialize'])
    
    # table with other referenced tables
    def testLoadAllSchemaAddsTableWithReferencesToDbInit(self):
        testType = "Update"
        db_initialize = ""
        initialAns = ""
        difficulty = "easy"
        data = {'params':{'html_params':{'questionType':testType,'difficulty':difficulty},
                          'db_initialize':db_initialize},
                'correct_answers':{'SQLEditor': initialAns}}
        tableOne = "flight"
        tableAirport = db.Table(tableOne, random=False)

        self.assertEqual(len(data['params']['db_initialize']),0)

        loadAllSchema(data,tableAirport)

        self.assertIn(tableOne,data['params']['db_initialize'])
        self.assertIn("airplane",data['params']['db_initialize'])
        self.assertIn("airport",data['params']['db_initialize'])

#---# loadTrimmedTable() Test(s)
    # returns a table with a number of columns that we know will work
    def testLoadTrimmedTableReturnsValidTableWhenGivenValidSize(self):
        columnCount = 3

        result = loadTrimmedTable(columnCount, 0)

        self.assertIsNotNone(result)
    
    # doesnt return a table because 0 columns isn't possible
    def testLoadTrimmedTableReturnsNoTableWhenGivenSizeZero(self):
        columnCount = 0

        result = loadTrimmedTable(columnCount, 0)

        self.assertIsNone(result)
    
    # doesn't return a table if no tables have enough columns
    def testLoadTrimmedTableReturnsNoTableWhenGivenInvalidSize(self):
        columnCount = 200
        
        result = loadTrimmedTable(columnCount, 0)

        self.assertIsNone(result)
    
    # returns a table with a number of joins that we know will work
    def testLoadTrimmedTableReturnsValidTableWhenGivenValidSize(self):
        joins = 2

        result = loadTrimmedTable(1, joins)

        self.assertIsNotNone(result)

    # doesn't return a table if the number of joins is invalid
    def testLoadTrimmedTableReturnsNoTableWhenGivenJoinsZero(self):
        joins = -1

        result = loadTrimmedTable(1, joins)

        self.assertIsNone(result)

    # doesn't return a table if no tables have enough columns
    def testLoadTrimmedTableReturnsNoTableWhenGivenInvalidJoins(self):
        joins = 200
        
        result = loadTrimmedTable(1, joins)

        self.assertIsNone(result)


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    unittest.main()
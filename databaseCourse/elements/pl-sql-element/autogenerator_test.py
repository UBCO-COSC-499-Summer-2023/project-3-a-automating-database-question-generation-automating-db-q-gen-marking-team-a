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
            # ["query","hard","select"]
            ])
    def testAutogenerateReturnsCorrectQuestionType(self,testType,difficulty,keyWord):
        initialAns = "\n"
        db_initialize = ""
        data = {'params':{'html_params':{'questionType':testType,'difficulty':difficulty,'expectedOutput':False},
                    'db_initialize_create':db_initialize, 
                    'db_initialize_insert_frontend':db_initialize, 
                    'db_initialize_insert_backend':db_initialize},
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
                        'db_initialize_create':db_initialize, 
                        'db_initialize_insert_frontend':db_initialize, 
                        'db_initialize_insert_backend':db_initialize},
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
                        'db_initialize_create':db_initialize, 
                        'db_initialize_insert_frontend':db_initialize, 
                        'db_initialize_insert_backend':db_initialize},
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
        data = {'params':{'html_params':{'questionType':testType,'difficulty':difficulty,'expectedOutput':False},
                        'db_initialize_create':db_initialize, 
                        'db_initialize_insert_frontend':db_initialize, 
                        'db_initialize_insert_backend':db_initialize},
                'correct_answers':{'SQLEditor': initialAns}}
        
    #     generateQuery(data,difficulty)

    #     actualQuestionType = ''.join(data['params']['questionString']).lower()
    #     self.assertIn("select the columns",actualQuestionType)
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
        table = db.Table(tableFile, random=False)
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
        table = db.Table(tableName, random=False)

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
        table = db.Table(tableName, random=False)
        updateCol= "province"
        updateVal = "Alberta"
        conditionalCol = updateCol
        conditionalVal = "Ontario"

        result = updateStatement(table,updateCol,updateVal,{conditionalCol: {'value': conditionalVal, 'connector': 'OR', 'comparator': '='}})

        self.assertIn("UPDATE",result)
        self.assertIn("WHERE",result)
        self.assertNotIn("CREATE",result)
        self.assertNotIn("INSERT",result)
        self.assertNotIn("DELETE",result)
        self.assertNotIn("SELECT",result)

    # without conditional
    def testUpdateStatementWithoutConditional(self):
        tableName = "airport"
        table = db.Table(tableName, random=False)
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
        table = db.Table(tableName, random=False)
        col = "province"
        condition = "Alberta"

        result = deleteStatement(table, {col: {'value': condition, 'connector': 'OR', 'comparator': '='}})

        self.assertIn("DELETE",result)
        self.assertIn("WHERE",result)
        self.assertNotIn("CREATE",result)
        self.assertNotIn("INSERT",result)
        self.assertNotIn("UPDATE",result)
        self.assertNotIn("SELECT",result)

    # without a condition
    def testDeleteStatementWithoutConditional(self):
        tableName = "airport"
        table = db.Table(tableName, random=False)

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



    # Parameterized CREATE Tests------------------------------------------------------------------------------------------------------------------
class ParameterizedCreateTests(unittest.TestCase):
    
    # Describes how many times each test should be run.
    # Since we're testing random generation, we need
    # a sufficient sample size to catch edge cases
    sampleSize = 50

    # Declares and sets defaults
    data = {
        'params': {
            'html_params': {
                'random': True,
                'questionType': 'create',
                'difficulty': None,
                'maxGrade': 3,
                'markerFeedback': True,
                'expectedOutput': False
            }
        },
        'correct_answers': {
            'SQLEditor': ''
        }
    }



    # Parameters for CREATE to test various cases
    @parameterized.expand([
            # columns, joins, primaryKeys, notNulls, uniques, cascades, nullOnDeletes
            [data, 5, 2, 1, 1, 1, 1, 1, sampleSize],  # A bit of everything
            [data, 3, 0, 0, 0, 0, 0, 0, sampleSize],  # Minimum values
            [data, 5, 1, 4, 0, 0, 0, 0, sampleSize],
            [data, 5, 4, 1, 0, 0, 0, 0, sampleSize],
            [data, 5, 5, 0, 0, 0, 5, 5, sampleSize],  # Max foreign clauses
            [data, 5, 0, 1, 4, 4, 0, 0, sampleSize],  # Max other clauses
            [data, 10, 7, 0, 0, 0, 0, 0, sampleSize]   # Lots of column and tables
            ])
    
    def testParameterizedCreate(self,data,columns,joins,primaryKeys,isNotNull,isUnique,isOnUpdateCascade,isOnDeleteSetNull,sampleSize):        
        data['params']['html_params']['columns'] = columns
        data['params']['html_params']['joins'] = joins

        data['params']['html_table_clauses'] = {
            'primaryKeys': primaryKeys,
            'isNotNull': isNotNull,
            'isUnique': isUnique,
            'isOnUpdateCascade': isOnUpdateCascade,
            'isOnDeleteSetNull': isOnDeleteSetNull
        }

        for i in range(sampleSize):

            # Sets values to be empty
            data['params']['questionString'] = ''
            data['params']['db_initialize_create'] = ''
            data['params']['db_initialize_insert_frontend'] = ''
            data['params']['db_initialize_insert_backend'] = ''
            data['correct_answers']['SQLEditor'] = ''

            autogenerate(data)

            self.assertIn("CREATE",data['correct_answers']['SQLEditor'])
            self.assertNotIn("WHERE",data['correct_answers']['SQLEditor'])
            #self.assertNotIn("DELETE",data['correct_answers']['SQLEditor']) 'ON DELETE SET NULL'
            self.assertNotIn("INSERT",data['correct_answers']['SQLEditor'])
            #self.assertNotIn("UPDATE",data['correct_answers']['SQLEditor']) 'ON UPDATE CASCADE'
            self.assertNotIn("SELECT",data['correct_answers']['SQLEditor'])

            self.assertGreater(len(data['params']['questionString']), 0)

            self.assertEqual(len(data['params']['db_initialize_insert_frontend']), 0)
            self.assertEqual(len(data['params']['db_initialize_insert_backend']), 0)

    # Parameterized INSERT Tests------------------------------------------------------------------------------------------------------------------
class ParameterizedInsertTests(unittest.TestCase):
    
    # Describes how many times each test should be run.
    # Since we're testing random generation, we need
    # a sufficient sample size to catch edge cases
    sampleSize = 5

    # Declares and sets defaults
    data = {
        'params': {
            'html_params': {
                'random': True,
                'questionType': 'insert',
                'difficulty': None,
                'maxGrade': 3,
                'markerFeedback': True,
                'expectedOutput': False
            }
        },
        'correct_answers': {
            'SQLEditor': ''
        }
    }

    # Parameters for CREATE to test various cases
    @parameterized.expand([
            # columns, joins
            [data, 5, 2, sampleSize],   # A bit of everything
            [data, 3, 0, sampleSize],   # Minimum values
            [data, 10, 7, sampleSize]    # Max values
            ])
    
    def testParameterizedInsert(self,data,columns,joins,sampleSize):        
        data['params']['html_params']['columns'] = columns
        data['params']['html_params']['joins'] = joins

        for i in range(sampleSize):

            # Sets values to be empty
            data['params']['questionString'] = ''
            data['params']['db_initialize_create'] = ''
            data['params']['db_initialize_insert_frontend'] = ''
            data['params']['db_initialize_insert_backend'] = ''
            data['correct_answers']['SQLEditor'] = ''

            autogenerate(data)

            self.assertIn("INSERT",data['correct_answers']['SQLEditor'])
            self.assertNotIn("WHERE",data['correct_answers']['SQLEditor'])
            self.assertNotIn("DELETE",data['correct_answers']['SQLEditor'])
            self.assertNotIn("CREATE",data['correct_answers']['SQLEditor'])
            self.assertNotIn("UPDATE",data['correct_answers']['SQLEditor'])
            self.assertNotIn("SELECT",data['correct_answers']['SQLEditor'])

            self.assertGreater(len(data['params']['questionString']), 0)
            self.assertGreater(len(data['params']['db_initialize_create']), 0)
            self.assertGreater(len(data['params']['db_initialize_insert_frontend']), 0)
            self.assertGreater(len(data['params']['db_initialize_insert_backend']), 0)


    # Parameterized UPDATE Tests------------------------------------------------------------------------------------------------------------------
class ParameterizedUpdateTests(unittest.TestCase):
    
    # Describes how many times each test should be run.
    # Since we're testing random generation, we need
    # a sufficient sample size to catch edge cases
    sampleSize = 5

    # Declares and sets defaults
    data = {
        'params': {
            'html_params': {
                'random': True,
                'questionType': 'update',
                'difficulty': None,
                'maxGrade': 3,
                'markerFeedback': True,
                'expectedOutput': False
            }
        },
        'correct_answers': {
            'SQLEditor': ''
        }
    }

    # Parameters for CREATE to test various cases
    @parameterized.expand([
            # columns, joins, conditionals, subquery
            [data, 5, 2, 2, False, sampleSize],   # A bit of everything
            [data, 5, 2, 2, True, sampleSize],   # A bit of everything
            [data, 3, 0, 0, False, sampleSize],   # Min, without subquery
            [data, 3, 1, 0, False, sampleSize],   # Min, with subquery
            [data, 10, 5, 5, False, sampleSize],   # Max, Without subquery
            [data, 10, 5, 5, True, sampleSize]   # Max, with subquery
            ])
    
    def testParameterizedUpdate(self,data,columns,joins,conditionals,subquery,sampleSize):        
        data['params']['html_params']['columns'] = columns
        data['params']['html_params']['joins'] = joins

        data['params']['html_query_clauses'] = {
            'conditional': conditionals,
            'useSubquery': subquery
        }

        for i in range(sampleSize):

            # Sets values to be empty
            data['params']['questionString'] = ''
            data['params']['db_initialize_create'] = ''
            data['params']['db_initialize_insert_frontend'] = ''
            data['params']['db_initialize_insert_backend'] = ''
            data['correct_answers']['SQLEditor'] = ''

            autogenerate(data)

            self.assertIn("UPDATE",data['correct_answers']['SQLEditor'])
            self.assertNotIn("DELETE",data['correct_answers']['SQLEditor'])
            self.assertNotIn("CREATE",data['correct_answers']['SQLEditor'])
            self.assertNotIn("INSERT",data['correct_answers']['SQLEditor'])

            if subquery or conditionals:
                self.assertIn("WHERE",data['correct_answers']['SQLEditor'])
            else:
                self.assertNotIn("WHERE",data['correct_answers']['SQLEditor'])

            if subquery:
                self.assertIn("SELECT",data['correct_answers']['SQLEditor'])
            else:
                self.assertNotIn("SELECT",data['correct_answers']['SQLEditor'])

            self.assertGreater(len(data['params']['questionString']), 0)
            self.assertGreater(len(data['params']['db_initialize_create']), 0)
            self.assertGreater(len(data['params']['db_initialize_insert_frontend']), 0)
            self.assertGreater(len(data['params']['db_initialize_insert_backend']), 0)


    # Parameterized UPDATE Tests------------------------------------------------------------------------------------------------------------------
class ParameterizedDeleteTests(unittest.TestCase):
    
    # Describes how many times each test should be run.
    # Since we're testing random generation, we need
    # a sufficient sample size to catch edge cases
    sampleSize = 5

    # Declares and sets defaults
    data = {
        'params': {
            'html_params': {
                'random': True,
                'questionType': 'delete',
                'difficulty': None,
                'maxGrade': 3,
                'markerFeedback': True,
                'expectedOutput': False
            }
        },
        'correct_answers': {
            'SQLEditor': ''
        }
    }

    # Parameters for CREATE to test various cases
    @parameterized.expand([
            # columns, joins, conditionals, subquery
            [data, 5, 2, 2, False, sampleSize],   # A bit of everything
            [data, 5, 2, 2, True, sampleSize],   # A bit of everything
            [data, 3, 0, 0, False, sampleSize],   # Min, without subquery
            [data, 3, 1, 0, False, sampleSize],   # Min, with subquery
            [data, 10, 5, 5, False, sampleSize],   # Max, Without subquery
            [data, 10, 5, 5, True, sampleSize]   # Max, with subquery
            ])
    
    def testParameterizedDelete(self,data,columns,joins,conditionals,subquery,sampleSize):        
        data['params']['html_params']['columns'] = columns
        data['params']['html_params']['joins'] = joins

        data['params']['html_query_clauses'] = {
            'conditional': conditionals,
            'useSubquery': subquery
        }

        for i in range(sampleSize):

            # Sets values to be empty
            data['params']['questionString'] = ''
            data['params']['db_initialize_create'] = ''
            data['params']['db_initialize_insert_frontend'] = ''
            data['params']['db_initialize_insert_backend'] = ''
            data['correct_answers']['SQLEditor'] = ''

            autogenerate(data)

            self.assertIn("DELETE",data['correct_answers']['SQLEditor'])
            self.assertNotIn("UPDATE",data['correct_answers']['SQLEditor'])
            self.assertNotIn("CREATE",data['correct_answers']['SQLEditor'])
            self.assertNotIn("INSERT",data['correct_answers']['SQLEditor'])

            if subquery or conditionals:
                self.assertIn("WHERE",data['correct_answers']['SQLEditor'])
            else:
                self.assertNotIn("WHERE",data['correct_answers']['SQLEditor'])

            if subquery:
                self.assertIn("SELECT",data['correct_answers']['SQLEditor'])
            else:
                self.assertNotIn("SELECT",data['correct_answers']['SQLEditor'])

            self.assertGreater(len(data['params']['questionString']), 0)
            self.assertGreater(len(data['params']['db_initialize_create']), 0)
            self.assertGreater(len(data['params']['db_initialize_insert_frontend']), 0)
            self.assertGreater(len(data['params']['db_initialize_insert_backend']), 0)

        
    # helper functions Tests------------------------------------------------------------------------------------------------------------------
class HelperFnsTest(unittest.TestCase):
#---# conditionalStatement() Test(s)
    def testConditionalStatementReturnsStatementWithWhere(self):
        column = ""
        condition = ""

        result = conditionalStatement(column,condition)

        self.assertIn("WHERE",result)

        
        
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
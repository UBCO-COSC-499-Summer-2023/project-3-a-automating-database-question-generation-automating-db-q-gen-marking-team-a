import unittest
#from parameterized import parameterized
from SQLElementSharedLibrary.textDatabaseHandler import *

# Tests the helper functions
class TableHelperFunctionsTest(unittest.TestCase):
    
    #---# relativeFilePath() Test(s)
    def testRelativeFilePathReturnsFilePathWithFileName(self):
        file = "random"

        result = relativeFilePath(file)

        self.assertEqual(f"./SQLElementSharedLibrary/randomTables/{file}.txt",result)



    # Tests getStaticSchema()
    # Case: file is found
    def testGetStaticSchemaFileIsFound(self):
        tableName = 'airport'
        schema = getStaticSchema(tableName)

        self.assertIsNotNone(schema)

    # Case: file is not found
    def testGetStaticSchemaFileIsNotFound(self):
        tableName = 'noSuchTable'
        schema = getStaticSchema(tableName)

        self.assertIsNone(schema)



    # Tests the getAllTableFiles() function
    # This test isn't really needed since it is implicitly
    # tested through other test functions
    def testGetAllTableFiles(self):
        tableList = getAllTableFiles()

        self.assertGreater(len(tableList), 0)

    

    # Tests the getRandomTableNames() function
    # This test isn't really needed since it is implicitly
    # tested through other test functions
    def testGetRandomTableNames(self):
        randomNames = getRandomTableNames()

        self.assertGreater(len(randomNames), 0)



# Tests the table object
class TableTest(unittest.TestCase):
    


    # Tests load()
    # This one does not need to be tested since it is
    # integration tested with Table instantiation



    # Tests object instantiation, thus the load() function
    # Case: filepath is correct
    def testStaticTableGeneration(self):
        tableName = 'flight'
        table = Table(tableName,random=False)

        self.assertIsNotNone(table)



    # Tests random object instantiation
    # Case: Default parameters
    def testRandomTableDefaultParameters(self):
        table = Table()

        self.assertIsNotNone(table)
        self.assertGreater(len(list(table.columns)), 0)
        self.assertIsNotNone(table.getKeyMap())

    # Case: Valid columns and valid joins
    def testRandomTableValidColumnsValidJoins(self):
        tableName = 'randomTable'
        columns = 3
        joins = 1
        table = Table(tableName, columns, joins)

        self.assertEqual(len(table.columns), columns)
        self.assertEqual(len(table.getKeyMap()), joins)

    # Case: Valid columns and invalid joins
    def testRandomTableValidColumnsInvalidJoins(self):
        tableName = 'randomTable'
        columns = 3
        joins = -1
        table = Table(tableName, columns, joins)

        self.assertEqual(len(list(table.columns)), 0)

    # Case: Invalid columns and valid joins
    def testRandomTableInvalidColumnsValidJoins(self):
        tableName = 'randomTable'
        columns = -1
        joins = 1
        table = Table(tableName, columns, joins)

        self.assertEqual(len(list(table.columns)), 0)

    # Case: Invalid columns and invalid joins
    def testRandomTableInvalidColumnsInvalidJoins(self):
        tableName = 'randomTable'
        columns = -1
        joins = -1
        table = Table(tableName, columns, joins)

        self.assertEqual(len(list(table.columns)), 0)
    
    # Case: more joins than columns
    def testRandomTableMoreJoinsThanColumns(self):
        tableName = 'randomTable'
        columns = 4
        joins = 5
        table = Table(tableName, columns, joins)

        self.assertEqual(len(list(table.columns)), 0)



    # Tests parseColumnsFromFile()
    # This one does not need to be tested since it is
    # integration tested with Table instantiation



    # Tests parseRange()
    # Case: a string, not a range, is provided
    def testParseRangeStringNotRange(self):
        table = Table('randomTable')
        
        string = 'this is not a range'
        returnedRange = table.parseRange(string)

        self.assertEqual(string, returnedRange)

    # Case: range has two components
    def testParseRangeTwoComponents(self):
        table = Table('randomTable')
        
        string = '3-5'
        trueRange = range(3, 6)
        returnedRange = table.parseRange(string)

        self.assertEqual(trueRange, returnedRange)

    # Case: range has three components
    def testParseRangeThreeComponents(self):
        table = Table('randomTable')
        
        string = '20-30-5'
        trueRange = range(20, 31, 5)
        returnedRange = table.parseRange(string)

        self.assertEqual(trueRange, returnedRange)

    # Case: range has four components
    # The fourth component should be ignored
    def testParseRangeThreeComponents(self):
        table = Table('randomTable')
        
        string = '7-10-3-1'
        trueRange = range(7, 11, 3)
        returnedRange = table.parseRange(string)

        self.assertEqual(trueRange, returnedRange)



    # Tests getKeyMap()
    # Case: table has no relations
    def testGetKeyMapWhenTableHasNoRelations(self):
        tableName = 'airport'
        table = Table(tableName, random=False)

        keyMap = table.getKeyMap()
        self.assertEqual(len(keyMap), 0)

    # Case: table has at least one relation
    def testGetKeyMapWhenTableHasAtleastOneRelation(self):
        tableName = 'flight'
        table = Table(tableName, random=False)

        keyMap = table.getKeyMap()
        self.assertGreater(len(keyMap), 0)



    # Tests getSchema()
    # Case: table is unmodified from file Schema
    def testGetSchemaWhenTableIsUnmodified(self):
        tableName = 'flight'
        table = Table(tableName, random=False)
        tableSchema = table.getSchema()

        unmodifiedSchema = getStaticSchema(tableName)

        # Strips all whitespace from both strings
        tableSchemaStripped = ''.join([word.strip() for word in tableSchema])
        unmodifiedSchemaStripped = ''.join([word.strip() for word in unmodifiedSchema])

        self.assertEqual(tableSchemaStripped, unmodifiedSchemaStripped)


    # Case: table is modified from Schema
    def testGetSchemaWhenTableIsModified(self):
        tableName = 'flight'
        table = Table(tableName, random=False)
        table.columns.pop('departAirport')
        tableSchema = table.getSchema().split('\n')

        # To check if the table was correctly modified, 
        # count the number of foreign keys in the table.
        # We know that if we 'departAirport' from 'flight',
        # then there will be two foreign key left:
        # 'arriveAirport' and 'airplaneId'
        fks = 0
        for line in tableSchema:
            if 'FOREIGN KEY' in line:
                fks += 1

        self.assertEqual(fks, 2)



if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    unittest.main()
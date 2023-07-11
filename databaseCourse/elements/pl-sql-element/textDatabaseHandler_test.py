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
    # Case: path is correct
    def testGetAllTableFilesReturnsPathsIfFilesFound(self):
        path = './SQLElementSharedLibrary/randomTables/'
        tableList = getAllTableFiles(path)

        self.assertIsNotNone(tableList)

    # Case: path is not corret
    def testGetAllTableFilesReturnsNoneIfFilesNotFound(self):
        path = './not/a/path/'
        tableList = getAllTableFiles(path)

        self.assertFalse(tableList)



# Tests the table object
class TableTest(unittest.TestCase):
    


    # Tests load()
    # This one does not need to be tested since it is
    # integration tested with Table instantiation



    # Tests object instantiation, thus the load() function
    # Case: filepath is correct
    def testStaticTableGeneration(self):
        tableName = 'flight'
        table = Table(tableName)

        self.assertIsNotNone(table)

    ''' ! Functions does not yet exists !
    # Tests random object instantiation
    # Case: Valid columns and valid joins
    def testRandomTableValidColumnsValidJoins(self):
        tableName = 'randomTable'
        columns = 3
        joins = 1
        table = Table(tableName, columns, joins)

        self.assertEqual(len(table.columns), columns)
        self.assertEqual(len(table.getKeyMap()), joins)
    '''

    # Case: Valid columns and invalid joins
    def testRandomTableValidColumnsInvalidJoins(self):
        tableName = 'randomTable'
        columns = 3
        joins = -1
        table = Table(tableName, columns, joins)

        self.assertIsNone(table.columns)

    # Case: Invalid columns and valid joins
    def testRandomTableInvalidColumnsValidJoins(self):
        tableName = 'randomTable'
        columns = -1
        joins = 1
        table = Table(tableName, columns, joins)

        self.assertIsNone(table.columns)

    # Case: Invalid columns and invalid joins
    def testRandomTableInvalidColumnsInvalidJoins(self):
        tableName = 'randomTable'
        columns = -1
        joins = -1
        table = Table(tableName, columns, joins)

        self.assertIsNone(table.columns)
    
    # Case: more joins than columns
    def testRandomTableMoreJoinsThanColumns(self):
        tableName = 'randomTable'
        columns = 4
        joins = 5
        table = Table(tableName, columns, joins)

        self.assertIsNone(table.columns)



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
        range = range(3, 6)
        returnedRange = table.parseRange(string)

        self.assertEqual(range, returnedRange)

    # Case: range has three components
    def testParseRangeThreeComponents(self):
        table = Table('randomTable')
        
        string = '20-30-5'
        range = range(20, 31, 5)
        returnedRange = table.parseRange(string)

        self.assertEqual(range, returnedRange)

    # Case: range has four components
    # The fourth component should be ignored
    def testParseRangeThreeComponents(self):
        table = Table('randomTable')
        
        string = '7-10-3-1'
        range = range(7, 11, 3)
        returnedRange = table.parseRange(string)

        self.assertEqual(range, returnedRange)



    # Tests getKeyMap()
    # Case: table has no relations
    def testGetKeyMapWhenTableHasNoRelations(self):
        tableName = 'airport'
        table = Table(tableName)

        keyMap = table.getKeyMap()
        self.assertEqual(len(keyMap), 0)

    # Case: table has at least one relation
    def testGetKeyMapWhenTableHasAtleastOneRelation(self):
        tableName = 'flight'
        table = Table(tableName)

        keyMap = table.getKeyMap()
        self.assertGreater(len(keyMap), 0)



    # Tests getSchema()
    # Case: table is unmodified from file Schema
    def testGetSchemaWhenTableIsUnmodified(self):
        tableName = 'flight'
        table = Table(tableName)
        tableSchema = table.getSchema()

        unmodifiedSchema = getStaticSchema(tableName)

        # Strips all whitespace from both strings
        tableSchemaStripped = ''.join([word.strip() for word in tableSchema])
        unmodifiedSchemaStripped = ''.join([word.strip() for word in unmodifiedSchema])

        self.assertEqual(tableSchemaStripped, unmodifiedSchemaStripped)


    # Case: table is modified from Schema
    def testGetSchemaWhenTableIsUnmodified(self):
        tableName = 'flight'
        table = Table(tableName)
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
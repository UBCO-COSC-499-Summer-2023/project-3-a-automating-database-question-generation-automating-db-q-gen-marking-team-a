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



    # Tests getStaticDDL()
    # Case: file is found
    def testGetStaticDDLFileIsFound(self):
        tableName = 'airport'
        schema = getStaticSchema(tableName)

        self.assertIsNotNone(schema)

    # Case: file is not found
    def testGetStaticDDLFileIsNotFound(self):
        tableName = 'noSuchTable'
        schema = getStaticSchema(tableName)

        self.assertIsNone(schema)



    # Tests the load() function
    # Case: file is found
    def testLoadReturnsTableFileIsFound(self):
        tableName = 'airport'
        table = load(tableName)

        self.assertIsNotNone(table)

    # Case: file is not found
    ''' ! Function does not yet exists !
    def testLoadReturnsNoneFileIsNotFound(self):
        tableName = 'noSuchTable'
        table = load(f"./SQLElementSharedLibrary/randomTables/{tableName}.txt")

        self.assertEqual(table.name, tableName)
    '''



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
    
    # Tests static object instantiation
    # Case: filepath is correct
    def testStaticTableGeneration(self):
        table = Table()

        self.assertIsNotNone(table)

    # Case: the table is random
    ''' ! Function does not yet exists !
    def testRandomTableGeneration(self):
        tableName = 'randomTable'
        table = Table(tableName)

        self.assertIsNotNone(table)
    '''



    ''' ! Functions does not yet exists !
    # Tests random object instantiation
    # Case: Valid columns and valid joins
    def testRandomTableValidColumnsValidJoins(self):
        tableName = 'randomTable'
        columns = 3
        joins = 1
        table = load(tableName, columns, joins)

        self.assertEqual(len(table.columns), columns)
        self.assertAlmostEqual(len(table.getKeyMap()), joins)

    # Case: Valid columns and invalid joins
    def testRandomTableValidColumnsInvalidJoins(self):
        tableName = 'randomTable'
        columns = 3
        joins = -1
        table = load(tableName, columns, joins)

        self.assertIsNone(table)

    # Case: Invalid columns and valid joins
    def testRandomTableInvalidColumnsValidJoins(self):
        tableName = 'randomTable'
        columns = -1
        joins = 1
        table = load(tableName, columns, joins)

        self.assertIsNone(table)

    # Case: Invalid columns and invalid joins
    def testRandomTableInvalidColumnsInvalidJoins(self):
        tableName = 'randomTable'
        columns = -1
        joins = -1
        table = load(tableName, columns, joins)

        self.assertIsNone(table)
    '''



    # Tests getKeyMap()
    # Case: table has no relations
    def testGetKeyMapWhenTableHasNoRelations(self):
        tableName = 'airport'
        table = load(tableName)

        keyMap = table.getKeyMap()
        self.assertEquals(len(keyMap), 0)

    # Case: table has at least one relation
    def testGetKeyMapWhenTableHasAtleastOneRelation(self):
        tableName = 'flight'
        table = load(tableName)

        keyMap = table.getKeyMap()
        self.assertGreater(len(keyMap), 0)



    # Tests getDDL()
    # Case: table is unmodified from file DDL
    ''' ! Function does not yet exists !
    def testGetDDLWhenTableIsUnmodified(self):
        tableName = 'flight'
        table = load(f"./SQLElementSharedLibrary/randomTables/{tableName}.txt")
        tableDDL = table.getDDL()

        unmodifiedDDL = getDDL(f"./SQLElementSharedLibrary/randomTables/{tableName}.txt")

        self.assertEqual(tableDDL, unmodifiedDDL)
    '''


    # Case: table is modified from DDL
    ''' ! Function does not yet exists !
    def testGetDDLWhenTableIsUnmodified(self):
        tableName = 'flight'
        table = load(f"./SQLElementSharedLibrary/randomTables/{tableName}.txt")
        table.columns.pop('departAirport')
        tableDDL = table.getDDL().split('\n')

        # To check if the table was correctly modified, 
        # count the number of foreign keys in the table
        fks = 0
        for line in tableDDL:
            if 'FOREIGN KEY' in line:
                fks += 1

        self.assertEqual(fks, 1)
    '''



if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    unittest.main()
import unittest
#from parameterized import parameterized
from SQLElementSharedLibrary.textDatabaseHandler import *

# Tests the helper functions
class TableHelperFunctionsTest(unittest.TestCase):
    
    # We're NOT testing the getDDL() funciton since it is
    # depricated in favour of an Table object-specific function that
    # returns the current DDL, not the DDL from a file.

    # Tests the load() function
    # Case: file is found
    def testLoadReturnsTableIfFileIsFound(self):
        tableName = 'airport'
        table = load(f"./SQLElementSharedLibrary/randomDatabases/{tableName}.txt")

        self.assertIsNotNone(table)

    # Case: file is not found
    ''' ! Function does not yet exists !
    def testLoadReturnsNoneIfFileIsNotFound(self):
        tableName = 'noSuchTable'
        table = load(f"./SQLElementSharedLibrary/randomDatabases/{tableName}.txt")

        self.assertEqual(table.name, tableName)
    '''



    # Tests the getAllDatabaseFiles() function
    # Case: path is correct
    def testGetAllDatabaseFilesReturnsPathsIfFilesFound(self):
        path = './SQLElementSharedLibrary/randomDatabases/'
        tableList = getAllDatabaseFiles(path)

        self.assertIsNotNone(tableList)

    # Case: path is not corret
    def testGetAllDatabaseFilesReturnsNoneIfFilesNotFound(self):
        path = './not/a/path/'
        tableList = getAllDatabaseFiles(path)

        self.assertFalse(tableList)



# Tests the table object
class TableTest(unittest.TestCase):
    
    # Tests static object instantiation
    # Case: filepath is correct
    def testStaticTableGeneration(self):
        tableName = 'airport'
        table = Database(f"./SQLElementSharedLibrary/randomDatabases/{tableName}.txt")

        self.assertIsNotNone(table)

    # Case: the table is random
    ''' ! Function does not yet exists !
    def testRandomTableGeneration(self):
        tableName = 'randomTable'
        table = Database(tableName)

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
        table = load(f"./SQLElementSharedLibrary/randomDatabases/{tableName}.txt")

        keyMap = table.getKeyMap()
        self.assertEquals(len(keyMap), 0)

    # Case: table has at least one relation
    def testGetKeyMapWhenTableHasAtleastOneRelation(self):
        tableName = 'flight'
        table = load(f"./SQLElementSharedLibrary/randomDatabases/{tableName}.txt")

        keyMap = table.getKeyMap()
        self.assertGreater(len(keyMap), 0)



    # Tests getDDL()
    # Case: table is unmodified from file DDL
    ''' ! Function does not yet exists !
    def testGetDDLWhenTableIsUnmodified(self):
        tableName = 'flight'
        table = load(f"./SQLElementSharedLibrary/randomDatabases/{tableName}.txt")
        tableDDL = table.getDDL()

        unmodifiedDDL = getDDL(f"./SQLElementSharedLibrary/randomDatabases/{tableName}.txt")

        self.assertEqual(tableDDL, unmodifiedDDL)
    '''


    # Case: table is modified from DDL
    ''' ! Function does not yet exists !
    def testGetDDLWhenTableIsUnmodified(self):
        tableName = 'flight'
        table = load(f"./SQLElementSharedLibrary/randomDatabases/{tableName}.txt")
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
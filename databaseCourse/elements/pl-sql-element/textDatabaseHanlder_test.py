import unittest
#from parameterized import parameterized
from SQLElementSharedLibrary.textDatabaseHandler import *

# Tests the helper functions
class TableHelperFunctionsTest(unittest.TestCase):
    
    # We're NOT testing the getDDL() funciton since it should
    # be depricated in favour of an object-specific function that
    # returns the current DDL, not the DDL from a file. Those tests
    # will be implemented later, just prior to the creation of
    # said function.

    # Tests the load() function
    # Case: file is found
    def testLoadReturnsTableIfFileIsFound(self):
        tableName = 'airport'
        table = load(f"./SQLElementSharedLibrary/randomDatabases/{tableName}.txt")

        self.assertIsNotNone(table)

    # Case: file is not found
    def testLoadReturnsNoneIfFileIsNotFound(self):
        tableName = '-1'
        table = load(f"./SQLElementSharedLibrary/randomDatabases/{tableName}.txt")

        self.assertIsNone(table)



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
    def testStaticTableGenerationWithCorrectFilePath(self):
        tableName = 'airport'
        table = Database(f"./SQLElementSharedLibrary/randomDatabases/{tableName}.txt")

        self.assertIsNotNone(table)

    # No need to test the incorrect case, since the prior load()
    # test covers that case.


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



    # Tests random object instantiation
    # Case: Valid columns and valid joins
    # TODO

    # Case: Valid columns and invalid joins
    # TODO

    # Case: Invalid columns and valid joins
    # TODO

    # Case: Invalid columns and invalid joins
    # TODO



if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    unittest.main()
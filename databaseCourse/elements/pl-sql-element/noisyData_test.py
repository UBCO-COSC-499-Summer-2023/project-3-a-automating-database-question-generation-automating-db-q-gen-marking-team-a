import unittest
#from parameterized import parameterized
from SQLElementSharedLibrary.SQLNoisyData import *
from SQLElementSharedLibrary.textDatabaseHandler import Table

class NoisyDataGenerationTests(unittest.TestCase):
    
    # Test generateColumns
    # Case: number of rows are specified
    def testGenerateColumnsSpecifiedQuantity(self):
        cols = 5
        rows = 7
        table = Table('', cols)

        data = generateColumns(table, rows)

        self.assertEqual(len(list(data.values())), cols)
        self.assertEqual(len(list(data.values())[0]), rows)

    # Case: number of rows are unspecified
    def testGeneratedColumnsUnspecifiedQuantity(self):
        cols = 5
        table = Table('', cols)

        data = generateColumns(table)

        self.assertEqual(len(list(data.values())), cols)
        self.assertEqual(len(list(data.values())[0]), 1)

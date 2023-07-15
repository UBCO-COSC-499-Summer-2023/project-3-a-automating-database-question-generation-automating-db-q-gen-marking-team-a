import unittest
#from parameterized import parameterized
from SQLElementSharedLibrary.SQLNoisyData import *
from SQLElementSharedLibrary.textDatabaseHandler import Table

class NoisyDataGenerationTests(unittest.TestCase):
    

    # Tests generateNoisyData()
    # This covers integration testing for all functions of
    # the form `generateNoisy{Type}()`.
    # Case: key is an integer
    def testGenerateNoisyDataKeyIsInteger(self):
        cols=1
        key = 'colName'
        qty = 25
        constraint = {
            key: {
                'unit': 'INTEGER',
                'unitOther': None
            }
        }
        table = Table('', columns=cols, constraints=constraint)

        data = generateNoisyData(table, key, qty)

        # Checks data type
        self.assertTrue(isinstance(data[0], int))

        # Checks range
        self.assertGreater(data[0], 0)
        self.assertLessEqual(data[0], 1000)

        # Checks quantity
        self.assertEqual(len(data), qty)

        # Checks whether each element is unique
        dataSet = (datum for datum in data)
        self.assertEqual(len(dataSet), len(data))

    # Case: key is a decimal
    def testGenerateNoisyDataKeyIsDecimal(self):
        cols=1
        key = 'colName'
        qty = 25
        totalDigits = 9
        decimalDigits = 2
        constraint = {
            key: {
                'unit': 'DECIMAL',
                'unitOther': f"{totalDigits},{decimalDigits}"
            }
        }
        table = Table('', columns=cols, constraints=constraint)

        data = generateNoisyData(table, key, qty)

        # Checks data type
        self.assertTrue(isinstance(data[0], float))

        # Checks range
        self.assertLessEqual(len(str(data[0])), totalDigits + 1)
        self.assertLessEqual(len(str(int(data[0]))), totalDigits - decimalDigits)
        self.assertLessEqual(len(str(data[0])[str(data[0]).find('.') + 1:]), decimalDigits)

        # Checks quantity
        self.assertEqual(len(data), qty)

        # Checks whether each element is unique
        dataSet = (datum for datum in data)
        self.assertEqual(len(dataSet), len(data))

    # Case: key is a char
    def testGenerateNoisyDataKeyIsChar(self):
        cols=1
        key = 'colName'
        qty = 25
        length = 5
        constraint = {
            key: {
                'unit': 'CHAR',
                'unitOther': length
            }
        }
        table = Table('', columns=cols, constraints=constraint)

        data = generateNoisyData(table, key, qty)

        # Checks data type
        self.assertTrue(isinstance(data[0], int))

        # Checks range
        self.assertEqual(len(data[0]), 5)

        # Checks quantity
        self.assertEqual(len(data), qty)

        # Checks whether each element is unique
        dataSet = (datum for datum in data)
        self.assertEqual(len(dataSet), len(data))

    # Case: key is a varchar
    def testGenerateNoisyDataKeyIsVarchar(self):
        cols=1
        key = 'colName'
        qty = 25
        length = 5
        constraint = {
            key: {
                'unit': 'VARCHAR',
                'unitOther': length
            }
        }
        table = Table('', columns=cols, constraints=constraint)

        data = generateNoisyData(table, key, qty)

        # Checks data type
        self.assertTrue(isinstance(data[0], int))

        # Checks range
        self.assertLessEqual(len(data[0]), 5)
        self.assertGreater(len(data[0]), 0)

        # Checks quantity
        self.assertEqual(len(data), qty)

        # Checks whether each element is unique
        dataSet = (datum for datum in data)
        self.assertEqual(len(dataSet), len(data))

    # Case: key is a date
    def testGenerateNoisyDataKeyIsDate(self):
        cols=1
        key = 'colName'
        qty = 25
        constraint = {
            key: {
                'unit': 'DATE',
                'unitOther': None
            }
        }
        table = Table('', columns=cols, constraints=constraint)

        data = generateNoisyData(table, key, qty)

        # Checks data type
        self.assertTrue(isinstance(data[0], int))

        # Checks quantity
        self.assertEqual(len(data), qty)

        # Checks whether each element is unique
        dataSet = (datum for datum in data)
        self.assertEqual(len(dataSet), len(data))

    # Case: key is a datetime
    def testGenerateNoisyDataKeyIsDatetime(self):
        cols=1
        key = 'colName'
        qty = 25
        constraint = {
            key: {
                'unit': 'DATETIME',
                'unitOther': None
            }
        }
        table = Table('', columns=cols, constraints=constraint)

        data = generateNoisyData(table, key, qty)

        # Checks data type
        self.assertTrue(isinstance(data[0], int))

        # Checks quantity
        self.assertEqual(len(data), qty)

        # Checks whether each element is unique
        dataSet = (datum for datum in data)
        self.assertEqual(len(dataSet), len(data))



    # Tests generateColumns()
    # Case: number of rows are specified
    def testGenerateColumnsSpecifiedQuantity(self):
        cols = 5
        rows = 7
        table = Table('', columns=cols)

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

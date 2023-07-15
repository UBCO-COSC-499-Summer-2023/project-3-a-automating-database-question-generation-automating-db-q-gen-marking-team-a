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
        key = 'colName'
        qty = 25
        constraint = {
            key: {
                'unit': 'INTEGER',
                'unitOther': None
            }
        }
        table = Table('', constraints=constraint)

        data = generateNoisyData(table, key, qty)

        # Checks quantity
        self.assertEqual(len(data), qty)

        # Checks each entry
        dataSet = []
        for datum in data:

            # Checks data type
            self.assertTrue(isinstance(datum, int))

            # Checks range
            self.assertGreater(datum, 0)
            self.assertLessEqual(datum, 1000)

            # Checks uniqueness
            self.assertNotIn(datum, dataSet)
            dataSet.append(datum)

        # Checks if each element is unique
        self.assertEqual(len(dataSet), len(data))

    # Case: key is a decimal
    def testGenerateNoisyDataKeyIsDecimal(self):
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
        table = Table('', constraints=constraint)

        data = generateNoisyData(table, key, qty)

        # Checks quantity
        self.assertEqual(len(data), qty)

        # Checks each entry
        dataSet = []
        for datum in data:

            # Checks data type
            self.assertTrue(isinstance(datum, float))

            # Checks range
            self.assertLessEqual(len(str(datum)), totalDigits + 1)
            self.assertLessEqual(len(str(int(datum))), totalDigits - decimalDigits)
            self.assertLessEqual(len(str(datum)[str(datum).find('.') + 1:]), decimalDigits)

            # Checks uniqueness
            self.assertNotIn(datum, dataSet)
            dataSet.append(datum)

        # Checks if each element is unique
        self.assertEqual(len(dataSet), len(data))

    # Case: key is a char
    def testGenerateNoisyDataKeyIsChar(self):
        key = 'colName'
        qty = 25
        length = 5
        constraint = {
            key: {
                'unit': 'CHAR',
                'unitOther': length
            }
        }
        table = Table('', constraints=constraint)

        data = generateNoisyData(table, key, qty)

        # Checks quantity
        self.assertEqual(len(data), qty)

        # Checks each entry
        dataSet = []
        for datum in data:

            # Checks data type
            self.assertTrue(isinstance(datum, str))

            # Checks range
            self.assertEqual(len(datum), 5)

            # Checks uniqueness
            self.assertNotIn(datum, dataSet)
            dataSet.append(datum)

        # Checks if each element is unique
        self.assertEqual(len(dataSet), len(data))

    # Case: key is a varchar
    def testGenerateNoisyDataKeyIsVarchar(self):
        key = 'colName'
        qty = 25
        length = 5
        constraint = {
            key: {
                'unit': 'VARCHAR',
                'unitOther': length
            }
        }
        table = Table('', constraints=constraint)

        data = generateNoisyData(table, key, qty)

        # Checks quantity
        self.assertEqual(len(data), qty)

        # Checks each entry
        dataSet = []
        for datum in data:

            # Checks data type
            self.assertTrue(isinstance(datum, str))

            # Checks range
            self.assertLessEqual(len(datum), 5)

            # Checks uniqueness
            self.assertNotIn(datum, dataSet)
            dataSet.append(datum)

        # Checks if each element is unique
        self.assertEqual(len(dataSet), len(data))

    # Case: key is a date
    def testGenerateNoisyDataKeyIsDate(self):
        key = 'colName'
        qty = 25
        constraint = {
            key: {
                'unit': 'DATE',
                'unitOther': None
            }
        }
        table = Table('', constraints=constraint)

        data = generateNoisyData(table, key, qty)

        # Checks quantity
        self.assertEqual(len(data), qty)

        # Checks each entry
        dataSet = []
        for datum in data:

            # Checks data type
            self.assertTrue(isinstance(datum, str))

            # Checks uniqueness
            self.assertNotIn(datum, dataSet)
            dataSet.append(datum)

        # Checks if each element is unique
        self.assertEqual(len(dataSet), len(data))

    # Case: key is a datetime
    def testGenerateNoisyDataKeyIsDatetime(self):
        key = 'colName'
        qty = 25
        constraint = {
            key: {
                'unit': 'DATETIME',
                'unitOther': None
            }
        }
        table = Table('', constraints=constraint)

        data = generateNoisyData(table, key, qty)

        # Checks quantity
        self.assertEqual(len(data), qty)

        # Checks each entry
        dataSet = []
        for datum in data:

            # Checks data type
            self.assertTrue(isinstance(datum, str))

            # Checks uniqueness
            self.assertNotIn(datum, dataSet)
            dataSet.append(datum)

        # Checks if each element is unique
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

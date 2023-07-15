import unittest
#from parameterized import parameterized
from SQLElementSharedLibrary.SQLNoisyData import *
from SQLElementSharedLibrary.textDatabaseHandler import Table

# Tests the primary functions
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

            # Prepares uniqueness check
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

            # Prepares uniqueness check
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
            self.assertEqual(len(datum), length)

            # Prepares uniqueness check
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
            self.assertLessEqual(len(datum), length)

            # Prepares uniqueness check
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

            # Prepares uniqueness check
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

            # Prepares uniqueness check
            self.assertNotIn(datum, dataSet)
            dataSet.append(datum)

        # Checks if each element is unique
        self.assertEqual(len(dataSet), len(data))
    
    # Case: key is mapped to a file
    def testGenerateNoisyDataKeyIsMappedToFile(self):
        key = 'firstName'
        qty = 25
        length = 35
        constraint = {
            key: {
                'unit': 'VARCHAR',
                'unitOther': length
            }
        }
        table = Table('', constraints=constraint)

        data = generateNoisyData(table, key, qty)
        firstNames = readLines('firstNames')

        # Checks quantity
        self.assertEqual(len(data), qty)

        # Checks each entry
        dataSet = []
        for datum in data:

            # Checks data type
            self.assertTrue(isinstance(datum, str))

            # Checks range
            self.assertLessEqual(len(datum), length)

            # Checks if item was loaded from a file
            self.assertIn(datum, firstNames)

            # Prepares uniqueness check
            self.assertNotIn(datum, dataSet)
            dataSet.append(datum)

        # Checks if each element is unique
        self.assertEqual(len(dataSet), len(data))



# Tests the helper functions
class NoisyDataHelperTests(unittest.TestCase):

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

    

    # Tests getColumnToFileMap()
    # Case: default path
    def testGetColumnToFileMapDefaultPath(self):
        mapping = getColumnToFileMap()

        self.assertIsNotNone(mapping)
        self.assertGreater(len(mapping), 0)

    # Case: incorrect path
    def testGetColumnToFileMapDefaultPath(self):
        mapping = getColumnToFileMap('a/bad/path/')

        self.assertIsNone(mapping)


    
    # Does not test getRelativeFilePath().
    # It is already integration tested.



    # Tests readLines()
    # Case: file is found
    def testReadLinesFileIsFound(self):
        lines = readLines('firstNames')

        self.assertIsNotNone(lines)
        self.assertGreater(len(lines), 0)

    # Case: file is not found
    def testReadLinesFileIsFound(self):
        lines = readLines('badFileName')

        self.assertIsNone(lines)



    # Tests isUnique()
    # Case: key in table is unique
    def testIsUniqueIsUnique(self):
        table = Table('flight', random=False)
        key = 'number'

        unique = isUnique(table, key)

        self.assertTrue(unique)

    # Case: key in table is not unique
    def testIsUniqueIsNotUnique(self):
        table = Table('flight', random=False)
        key = 'arrivalDate'

        unique = isUnique(table, key)

        self.assertFalse(unique)
    


    # Tests popRandom()
    def testPopRandom(self):
        numberOfValues = 100
        originalValues = range(numberOfValues)

        poppedValues = []
        for i in range(numberOfValues):
            value = popRandom(originalValues)

            self.assertIsNotNone(value)
            self.assertNotIn(value, poppedValues)

            poppedValues.append(value)
        
        self.assertEqual(len(poppedValues), numberOfValues)
    


    # Tests popRandom()
    def testSelectRandom(self):
        numberOfValues = 100
        originalValues = range(numberOfValues)

        selectedValues = []
        for i in range(numberOfValues):
            value = popRandom(originalValues)

            self.assertIsNotNone(value)

            selectedValues.append(value)
        
        self.assertEqual(len(selectedValues), numberOfValues)

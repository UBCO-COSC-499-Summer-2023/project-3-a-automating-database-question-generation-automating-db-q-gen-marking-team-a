import unittest
from parameterized import parameterized
from SQLElementSharedLibrary.SQLAutogenerator import *

    # Parameterized CREATE Tests------------------------------------------------------------------------------------------------------------------
class ParameterizedCreateTests(unittest.TestCase):
    
    # Describes how many times each test should be run.
    # Since we're testing random generation, we need
    # a sufficient sample size to catch edge cases
    sampleSize = 100

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

import unittest
from parameterized import parameterized
from SQLElementSharedLibrary.SQLAutogenerator import *

    # Parameterized UPDATE Tests------------------------------------------------------------------------------------------------------------------
class ParameterizedUpdateTests(unittest.TestCase):
    
    # Describes how many times each test should be run.
    # Since we're testing random generation, we need
    # a sufficient sample size to catch edge cases
    sampleSize = 100

    # Declares and sets defaults
    data = {
        'params': {
            'html_params': {
                'random': True,
                'questionType': 'update',
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
            # columns, joins, conditionals, subquery
            [data, 5, 2, 2, False, sampleSize],   # A bit of everything
            [data, 5, 2, 2, True, sampleSize],   # A bit of everything
            [data, 3, 0, 0, False, sampleSize],   # Min, without subquery
            [data, 3, 1, 0, False, sampleSize],   # Min, with subquery
            [data, 10, 5, 5, False, sampleSize],   # Max, Without subquery
            [data, 10, 5, 5, True, sampleSize]   # Max, with subquery
            ])
    
    def testParameterizedUpdate(self,data,columns,joins,conditionals,subquery,sampleSize):        
        data['params']['html_params']['columns'] = columns
        data['params']['html_params']['joins'] = joins

        data['params']['html_query_clauses'] = {
            'conditional': conditionals,
            'useSubquery': subquery
        }

        for i in range(sampleSize):

            # Sets values to be empty
            data['params']['questionString'] = ''
            data['params']['db_initialize_create'] = ''
            data['params']['db_initialize_insert_frontend'] = ''
            data['params']['db_initialize_insert_backend'] = ''
            data['correct_answers']['SQLEditor'] = ''

            autogenerate(data)

            self.assertIn("UPDATE",data['correct_answers']['SQLEditor'])
            self.assertNotIn("DELETE",data['correct_answers']['SQLEditor'])
            self.assertNotIn("CREATE",data['correct_answers']['SQLEditor'])
            self.assertNotIn("INSERT",data['correct_answers']['SQLEditor'])

            if subquery or conditionals:
                self.assertIn("WHERE",data['correct_answers']['SQLEditor'])
            else:
                self.assertNotIn("WHERE",data['correct_answers']['SQLEditor'])

            if subquery:
                self.assertIn("SELECT",data['correct_answers']['SQLEditor'])
            else:
                self.assertNotIn("SELECT",data['correct_answers']['SQLEditor'])

            self.assertGreater(len(data['params']['questionString']), 0)
            self.assertGreater(len(data['params']['db_initialize_create']), 0)
            self.assertGreater(len(data['params']['db_initialize_insert_frontend']), 0)
            self.assertGreater(len(data['params']['db_initialize_insert_backend']), 0)
databaseCourse/elements/pl-sql-element/parameter_create_test.py
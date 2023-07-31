import unittest
from parameterized import parameterized
from SQLElementSharedLibrary.SQLAutogenerator import *

    # Parameterized INSERT Tests------------------------------------------------------------------------------------------------------------------
class ParameterizedInsertTests(unittest.TestCase):
    
    # Describes how many times each test should be run.
    # Since we're testing random generation, we need
    # a sufficient sample size to catch edge cases
    sampleSize = 100

    # Declares and sets defaults
    data = {
        'params': {
            'html_params': {
                'random': True,
                'questionType': 'insert',
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
            # columns, joins
            [data, 5, 2, sampleSize],   # A bit of everything
            [data, 3, 0, sampleSize],   # Minimum values
            [data, 10, 7, sampleSize]    # Max values
            ])
    
    def testParameterizedInsert(self,data,columns,joins,sampleSize):        
        data['params']['html_params']['columns'] = columns
        data['params']['html_params']['joins'] = joins

        for i in range(sampleSize):

            # Sets values to be empty
            data['params']['questionString'] = ''
            data['params']['db_initialize_create'] = ''
            data['params']['db_initialize_insert_frontend'] = ''
            data['params']['db_initialize_insert_backend'] = ''
            data['correct_answers']['SQLEditor'] = ''

            autogenerate(data)

            self.assertIn("INSERT",data['correct_answers']['SQLEditor'])
            self.assertNotIn("WHERE",data['correct_answers']['SQLEditor'])
            self.assertNotIn("DELETE",data['correct_answers']['SQLEditor'])
            self.assertNotIn("CREATE",data['correct_answers']['SQLEditor'])
            self.assertNotIn("UPDATE",data['correct_answers']['SQLEditor'])
            self.assertNotIn("SELECT",data['correct_answers']['SQLEditor'])

            self.assertGreater(len(data['params']['questionString']), 0)
            self.assertGreater(len(data['params']['db_initialize_create']), 0)
            self.assertGreater(len(data['params']['db_initialize_insert_frontend']), 0)
            self.assertGreater(len(data['params']['db_initialize_insert_backend']), 0)

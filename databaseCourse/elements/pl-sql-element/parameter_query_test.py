import unittest
from parameterized import parameterized
from SQLElementSharedLibrary.SQLAutogenerator import *

    # Parameterized UPDATE Tests------------------------------------------------------------------------------------------------------------------
class ParameterizedQueryTests(unittest.TestCase):
    
    # Describes how many times each test should be run.
    # Since we're testing random generation, we need
    # a sufficient sample size to catch edge cases
    sampleSize = 100

    # Declares and sets defaults
    data = {
        'params': {
            'html_params': {
                'random': True,
                'questionType': 'query',
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
            # columns, joins, conditional, useSubquery, columnsToSelect, orderBy, groupBy, having, limit, isDistinct
            [data, 5, 2, 2, False, 5, 1, 1, 1, 5, True, sampleSize],   # A bit of everything
            [data, 5, 2, 2, True, 5, 1, 1, 1, 5, True, sampleSize],   # A bit of everything, and a subquery
            [data, 3, 1, 0, False, 0, 0, 0, 0, 0, False, sampleSize],   # Min, without subquery
            [data, 3, 1, 0, True, 0, 0, 0, 0, 0, False, sampleSize],   # Min, with subquery
            [data, 10, 4, 4, False, 10, 4, 4, 4, 5, False, sampleSize], # Max, without subquery
            [data, 10, 4, 4, True, 10, 4, 4, 4, 5, False, sampleSize],    # Max, with subquery
            ])
    
    def testParameterizedQuery(self,data,columns,joins,conditionals,subquery,columnsToSelect,orderBy,groupBy,having,limit,isDistinct,sampleSize):        
        data['params']['html_params']['columns'] = columns
        data['params']['html_params']['joins'] = joins

        data['params']['html_query_clauses'] = {
            'conditional': conditionals,
            'useSubquery': subquery,
            'columnsToSelect': columnsToSelect,
            'orderBy': orderBy,
            'groupBy': groupBy,
            'having': having,
            'limit': limit,
            'with': 0,
            'isDistinct': isDistinct
        }


        for i in range(sampleSize):

            # Sets values to be empty
            data['params']['questionString'] = ''
            data['params']['db_initialize_create'] = ''
            data['params']['db_initialize_insert_frontend'] = ''
            data['params']['db_initialize_insert_backend'] = ''
            data['correct_answers']['SQLEditor'] = ''

            autogenerate(data)

            self.assertIn("SELECT",data['correct_answers']['SQLEditor'])
            self.assertNotIn("UPDATE",data['correct_answers']['SQLEditor'])
            self.assertNotIn("CREATE",data['correct_answers']['SQLEditor'])
            self.assertNotIn("INSERT",data['correct_answers']['SQLEditor'])
            self.assertNotIn("DELETE",data['correct_answers']['SQLEditor'])

            if subquery or conditionals:
                self.assertIn("WHERE",data['correct_answers']['SQLEditor'])
            else:
                self.assertNotIn("WHERE",data['correct_answers']['SQLEditor'])

            self.assertGreater(len(data['params']['questionString']), 0)
            self.assertGreater(len(data['params']['db_initialize_create']), 0)
            self.assertGreater(len(data['params']['db_initialize_insert_frontend']), 0)
            self.assertGreater(len(data['params']['db_initialize_insert_backend']), 0)

        
import unittest
import random as rand
from parameterized import parameterized

# This allows DroneCI to see the RASQLib module
import sys
sys.path.append('databaseCourse/elements/pl-relax-element/')
from RelaXElementSharedLibrary.RelaXAutogenerator import *


# Tests RelaX autogen queries
class AutogenerateQueryTest(unittest.TestCase):
    
    # Describes how many times each test should be run.
    # Since we're testing random generation, we need
    # a sufficient sample size to catch edge cases.
    sampleSize = 30


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
            'RelaXEditor': ''
        }
    }

    # Parameters for RelaX question.
    # These are passed into the function header for all
    # functions of this class. Each tuple corresponds to 
    # a test case
    @parameterized.expand([
            # data, numJoins, numClauses, orderBy, groupBy, antiJoin, outerJoin, semiJoin
            [data, 3, 0, 0, True, False, False, False, False, sampleSize],
            [data, 3, 1, 0, False, False, False, False, False, sampleSize],
            [data, 3, 2, 0, False, False, False, False, False, sampleSize],
            [data, 3, 3, 0, True, True, False, False, False, sampleSize],

            [data, 3, 0, 1, False, False, False, False, False, sampleSize],
            [data, 3, 1, 1, False, True, False, False, False, sampleSize], # A very simple query
            [data, 3, 2, 1, False, False, False, False, False, sampleSize],
            [data, 3, 3, 1, True, False, False, False, False, sampleSize],

            [data, 3, 0, 2, False, True, False, False, False, sampleSize], # A simple query
            [data, 3, 1, 2, True, True, False, False, False, sampleSize], # A simple query
            [data, 3, 2, 2, True, False, False, False, False, sampleSize], # A simple query
            [data, 3, 3, 2, False, False, False, False, False, sampleSize], # A complex query
            
            [data, 3, 0, 3, False, False, False, False, False, sampleSize], # A very weird query
            [data, 3, 1, 3, False, True, False, False, False, sampleSize], # A very weird query
            [data, 3, 2, 3, False, False, False, False, False, sampleSize], # A very weird query
            [data, 3, 3, 3, True, False, False, False, False, sampleSize],  # A very weird query

            [data, 3, 0, 0, True, False, False, False, True, sampleSize],
            [data, 3, 1, 0, False, False, False, True, False, sampleSize],
            [data, 3, 2, 0, False, False, True, False, False, sampleSize],
            [data, 3, 3, 0, True, True, True, True, True, sampleSize],

            [data, 3, 0, 0, True, False, False, False, True, sampleSize],
            [data, 3, 0, 1, False, False, False, True, False, sampleSize],
            [data, 3, 0, 2, False, False, True, False, False, sampleSize],
            [data, 3, 0, 3, True, True, True, True, True, sampleSize],

            [data, 1, 0, 0, True, False, False, False, True, sampleSize],
            [data, 3, 0, 1, False, False, False, True, False, sampleSize],
            [data, 2, 0, 2, False, False, True, False, False, sampleSize],
            [data, 3, 0, 3, True, True, True, True, True, sampleSize]

        ])

    
    # The real value in this test is not what the assert statements
    # cover, but the error message of when it crashes
    def testRelaXQuery(self,data,projectedColumns,numJoins,numClauses,orderBy,groupBy,antiJoin,outerJoin,semiJoin,sampleSize):        
        data['params']['attrib_dict'] = {
            "projectedColumns": projectedColumns,
            "numClauses": numClauses,
            "orderBy": orderBy,
            "groupBy": groupBy,
            "numJoins": numJoins,
            "antiJoin": antiJoin,
            "semiJoin": semiJoin,
            "outerJoin": outerJoin,
        }

        for i in range(sampleSize):

            # Sets values to be empty
            data['params']['questionText'] = ''
            data['params']['db_initialize_create'] = ''
            data['params']['db_initialize_create_backend'] = ''
            data['correct_answers']['RelaXEditor'] = ''

            # Generates the question
            autogenerate(data, outputGuaranteed=False)

            # Asserts
            self.assertGreater(len(data['params']['db_initialize_create']), 0)
            self.assertGreater(len(data['params']['db_initialize_create_backend']), 0)
            self.assertGreater(len(data['correct_answers']['RelaXEditor']), 0)

            self.assertIn("π" if not groupBy else "γ", data['correct_answers']['RelaXEditor'])
            
            if numClauses:
                self.assertIn("σ", data['correct_answers']['RelaXEditor'])


            print(data['correct_answers']['RelaXEditor'])

        print("\n\n")
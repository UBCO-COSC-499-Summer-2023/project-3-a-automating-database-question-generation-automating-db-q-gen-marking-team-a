import unittest
import random as rand
from parameterized import parameterized
from RelaXElementSharedLibrary.RelaXAutogenerator import *

class AutogenerateTest(unittest.TestCase):

    def testAutogenerateTablesRelaX(self):
        for i in range(100):
            columns = rand.randint(4, 7)
            joins = rand.randint(2, 5)
            rows = rand.randint(5, 15)
            database = db.Database(isSQL=False, columns=columns, joins=joins, rows=rows)
            if database is None:
                print("Error: database is None")

    
#     def testAutogenerateJoinedTablesCollection(self):
#         for i in range(10):
#             columns = rand.randint(4, 7)
#             joins = rand.randint(2, 5)
#             rows = rand.randint(5, 15)
#             database = db.Database(isSQL=False, columns=columns, joins=joins, rows=rows)
#             numJoins = joins-1
            
            
#             graph = {}
#             for table in database.tableSet:
#                 connections = []
#                 for column in database.tableSet[table].columns:
#                     if database.tableSet[table].columns[column]['references']:
#                         connections.append(database.tableSet[table].columns[column]['references'])
#                 graph[table] = connections

#             for j in range(10):
#                 table = rand.choice(list(database.tableSet.keys()))
#                 subgraph = randomSubgraph(graph=graph, n=numJoins)
#                 if len(subgraph) != (numJoins+1):
#                     print(f"Error: {len(subgraph)} != {numJoins+1}")
                    
# #AutogenerateTest.testAutogenerateJoinedTablesCollection()


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
            [data, 1, 1, False, True, False, False, False, sampleSize], # A very simple query
            [data, 2, 2, True, False, False, False, False, sampleSize], # A simple query
            [data, 3, 2, False, False, False, False, False, sampleSize], # A complex query
            [data, 0, 3, False, False, False, False, False, sampleSize], # A very weird query
            #[data, 0, 0, False, False, False, False, False, sampleSize]
        ])

    
    # The real value in this test is not what the assert statements
    # cover, but the error message of when it crashes
    def testRelaXQuery(self,data,numJoins,numClauses,orderBy,groupBy,antiJoin,outerJoin,semiJoin,sampleSize):        
        data['params']['attrib_dict'] = {
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
            autogenerate(data, testing=True)

            # Asserts
            self.assertGreater(len(data['params']['db_initialize_create']), 0)
            self.assertGreater(len(data['params']['db_initialize_create_backend']), 0)
            self.assertGreater(len(data['correct_answers']['RelaXEditor']), 0)

            self.assertIn("π" if not groupBy else "γ", data['correct_answers']['RelaXEditor'])
            
            if numClauses:
                self.assertIn("σ", data['correct_answers']['RelaXEditor'])


            print(data['correct_answers']['RelaXEditor'])
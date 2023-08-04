import unittest
import random as rand
#from parameterized import parameterized
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

    
    def testAutogenerateJoinedTablesCollection():
        for i in range(10):
            columns = rand.randint(4, 7)
            joins = rand.randint(2, 5)
            rows = rand.randint(5, 15)
            database = db.Database(isSQL=False, columns=columns, joins=joins, rows=rows)
            numJoins = joins-1
            
            
            graph = {}
            for table in database.tableSet:
                connections = []
                for column in database.tableSet[table].columns:
                    if database.tableSet[table].columns[column]['references']:
                        connections.append(database.tableSet[table].columns[column]['references'])
                graph[table] = connections

            for j in range(10):
                table = rand.choice(list(database.tableSet.keys()))
                subgraph = randomSubgraph(graph=graph, n=numJoins)
                if len(subgraph) != (numJoins+1):
                    print(f"Error: {len(subgraph)} != {numJoins+1}")
                    
AutogenerateTest.testAutogenerateJoinedTablesCollection()
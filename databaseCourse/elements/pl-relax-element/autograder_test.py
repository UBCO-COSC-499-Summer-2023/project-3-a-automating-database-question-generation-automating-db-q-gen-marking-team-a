import unittest
from parameterized import parameterized
from RelaXElementSharedLibrary.RelaXCustomGrader import *

class CustomGraderTest(unittest.TestCase):
    

    # rowmatch
    # 0 due to empty
    def testRowMatchReturnsZeroWhenEmpty(self):
        submittedAns = []
        correctAns = [[1,2,3]]

        result = rowMatch(submittedAns, correctAns)

        self.assertEqual(result['score'],0)
    # 0.5
    def testRowMatchReturnsHalfWhenHalfMatches(self):
        submittedAns = [[1,2,3]]
        correctAns = [[1,2,3],[4,5,6]]

        result = rowMatch(submittedAns, correctAns)

        self.assertEqual(result['score'],0.5)
    # 1
    def testRowMatchReturnsOneWhenAllMatch(self):
        submittedAns = [(1,2,3)]
        correctAns = [(1,2,3)]

        result = rowMatch(submittedAns, correctAns)

        self.assertEqual(result['score'],1)

    # valmatch
    # 0 when empty
    def testValMatchReturnsZeroWhenEmpty(self):
        submittedAns = [()]
        correctAns = [(1,2,3)]

        result = valueMatch(submittedAns, correctAns)

        self.assertEqual(result['score'],0)
    # 0 when non empty
    def testValMatchReturnsZeroWhenNoMatches(self):
        submittedAns = [(0,5,9)]
        correctAns = [(1,2,3,4)]

        result = valueMatch(submittedAns, correctAns)

        self.assertEqual(result['score'],0)
    
    def testValMatchReturnsZeroWhenExtraMatches(self):
        submittedAns = [(1,2,3,4,5,6)]
        correctAns = [(1,2,3)]
        
        result = valueMatch(submittedAns, correctAns)
        
        self.assertEqual(result['score'],0)
        
    # 0.5
    def testValMatchReturnsHalfWhenHalfMatches(self):
        submittedAns = [(1,2,3),(0,2,3)]
        correctAns = [(1,2,3),(1,9,8)]

        result = valueMatch(submittedAns,correctAns)

        self.assertEqual(result['score'],0.5)
    # 1
    def testValMatchReturnsOneWhenAllMatch(self):
        submittedAns = [(1,2,3)]
        correctAns = [(1,2,3)]

        result = valueMatch(submittedAns, correctAns)

        self.assertEqual(result['score'],1)
        
    
    # col match
    # 0 due to empty
    def testColMatchReturnsZeroWhenEmpty(self):
        submittedAns = []
        correctAns = [[1,2,3]]

        result = colMatch(submittedAns, correctAns)

        self.assertEqual(result['score'],0)
    # 0.5
    def testColMatchReturnsHalfWhenHalfMatches(self):
        submittedAns = ["name"]
        correctAns = ["name", "state"]

        result = colMatch(submittedAns, correctAns)

        self.assertEqual(result['score'],0.5)
        self.assertEqual(result['missingCols'], [("state")])
    # 1
    def testColMatchReturnsOneWhenAllMatch(self):
        submittedAns = [[1,2,3,4]]
        correctAns = [[1,2,3,4]]

        result = colMatch(submittedAns, correctAns)

        self.assertEqual(result['score'],1)
        
    def testOrderMatchReturnsOneWhenEmpty(self):
        submittedAns = []
        correctAns = [[1,2,3]]
        
        result = orderMatch(submittedAns, correctAns)
        
        self.assertEqual(result,1)
        
    def testOrderMatchReturnsOneWhenOneRow(self):
        submittedAns = [[1,2,3]]
        correctAns = [[1,2,3], [4,5,6]]
        
        result = orderMatch(submittedAns, correctAns)
        
        self.assertEqual(result,1)
        
    def testOrderMatchReturnsOneBothAscending(self):
        submittedAns = [[1,2,3],[7,8,9]]
        correctAns = [[1,2,3],[4,5,6]]
        
        result = orderMatch(submittedAns, correctAns)
        
        self.assertEqual(result,1)
        
    def testOrderMatchReturnsOneBothDescending(self):
        submittedAns = [[7,8,9],[1,2,3]]
        correctAns = [[4,5,6], [1,2,3]]
        
        result = orderMatch(submittedAns, correctAns)
        
        self.assertEqual(result,1)
        
    def testOrderMatchReturnsZeroWhenNoMatches(self):
        submittedAns = [[9,8,7], [6,5,4], [3,2,1]]
        correctAns = [[1,2,3],[4,5,6]]
        
        result = orderMatch(submittedAns, correctAns)
        
        self.assertEqual(result,0)
        
    def testAddFeedback(self):
        data = {}
        data['params'] = {}
        data['params']['queryFeedback'] = ''
        
        addFeedback(data, "rows", 2, 4)
        
        self.assertEqual(data['params']['queryFeedback'], 'rows : [2 / 4] <br>')
        
        
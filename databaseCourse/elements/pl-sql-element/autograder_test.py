import unittest
from parameterized import parameterized
from SQLElementSharedLibrary.SQLCustomGrader import *

class CustomGraderTest(unittest.TestCase):
    # 100%
    def testCustomGraderReturnsHundredWhenStringMatch(self):
        data = {'params':{'html_params':{'questionType':'','difficulty':''}},
                'submitted_answers':{'SQLEditor':"SELECT * FROM airport"},
                'correct_answers':{'SQLEditor':"SELECT * FROM airport"}}
        
        result = customGrader(data)

        self.assertEqual(result, 100)

    # 0%
    def testCustomGraderReturnsZeroWhenNoStringMatch(self):
        data = {'params':{'html_params':{'questionType':'','difficulty':''}},
                'submitted_answers':{'SQLEditor':""},
                'correct_answers':{'SQLEditor':"SELECT * FROM airport"}}
        
        result = customGrader(data)

        self.assertEqual(result,0)

    # rowmatch
    # 0 due to empty
    def testRowMatchReturnsZeroWhenEmpty(self):
        actualAns = []
        expectedAns = [(1,2,3)]

        result = rowMatch(expectedAns,actualAns)

        self.assertEqual(result,0)
    # 0.5
    def testRowMatchReturnsHalfWhenHalfMatches(self):
        actualAns = [(1,9,3)]
        expectedAns = [(1,2,3),(4,5,6)]

        result = rowMatch(expectedAns,actualAns)

        self.assertEqual(result,0.5)
    # 1
    def testRowMatchReturnsOneWhenAllMatch(self):
        actualAns = [(1,2,9)]
        expectedAns = [(1,2,3)]

        result = rowMatch(expectedAns,actualAns)

        self.assertEqual(result,1)

    # valmatch
    # 0 when empty
    def testValMatchReturnsZeroWhenEmpty(self):
        actualAns = [()]
        expectedAns = [(1,2,3)]

        result = valueMatch(expectedAns,actualAns)

        self.assertEqual(result,0)
    # 0 when non empty
    def testValMatchReturnsZeroWhenNoMatches(self):
        actualAns = [(1,2,9)]
        expectedAns = [(1,2,3)]

        result = valueMatch(expectedAns,actualAns)

        self.assertEqual(result,0)
    # 0.5
    def testValMatchReturnsHalfWhenHalfMatches(self):
        actualAns = [(1,2,3),(1,9,0)]
        expectedAns = [(1,2,3),(1,9,8)]

        result = valueMatch(expectedAns,actualAns)

        self.assertEqual(result,0.5)
    # 1
    def testValMatchReturnsOneWhenAllMatch(self):
        actualAns = [(1,2,3)]
        expectedAns = [(1,2,3)]

        result = valueMatch(expectedAns,actualAns)

        self.assertEqual(result,1)

    # col match
    # 0 due to empty
    def testColMatchReturnsZeroWhenEmpty(self):
        actualAns = [()]
        expectedAns = [(1,2,3)]

        result = colMatch(expectedAns,actualAns)

        self.assertEqual(result,0)
    # 0.5
    # SQLite3 returns single value tuples as (x,) and not as (x)
    def testColMatchReturnsHalfWhenHalfMatches(self):
        actualAns = [(1,)]
        expectedAns = [(1,2,)]

        result = colMatch(expectedAns,actualAns)

        self.assertEqual(result,0.5)
    # 1
    def testColMatchReturnsOneWhenAllMatch(self):
        actualAns = [(1,2,9)]
        expectedAns = [(1,2,3)]

        result = colMatch(expectedAns,actualAns)

        self.assertEqual(result,1)
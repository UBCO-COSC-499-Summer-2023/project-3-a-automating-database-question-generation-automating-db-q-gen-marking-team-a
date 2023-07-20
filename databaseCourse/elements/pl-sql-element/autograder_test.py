import unittest
from parameterized import parameterized
from SQLElementSharedLibrary.SQLCustomGrader import *

class CustomGraderTest(unittest.TestCase):
    # 0 similarity
    def testAutograderReturnsZeroWhenNoSimilarities(self):
        data = {'params':{'html_params':{'questionType':'' ,'difficulty':''}},
                'submitted_answers':{'SQLEditor':""},
                'correct_answers':{'SQLEditor':"SELECT * FROM Airport"}}
    
        result = customGrader(data)

        self.assertEqual(0,result)
    
    # 100% similarity
    def testAutograderReturnsOneWhenExactMatch(self):
        data = {'params':{'html_params':{'questionType':'' ,'difficulty':''}},
                'submitted_answers':{'SQLEditor':"SELECT * from Airport"},
                'correct_answers':{'SQLEditor':"SELECT * FROM Airport"}}
    
        result = customGrader(data)

        self.assertEqual(1,result)
    
    # 75% similarity
    def testAutograderReturnsOneWhenAboveThresholdMatch(self):
        data = {'params':{'html_params':{'questionType':'' ,'difficulty':''}},
                'submitted_answers':{'SQLEditor':"SELECT * FROM"},
                'correct_answers':{'SQLEditor':"SELECT * FROM Airport"}}
    
        result = customGrader(data)

        self.assertEqual(0.15,result)
    
    # 50% similarity
    def testAutograderReturnsDecimalWhenBelowThresholdMatch(self):

        data = {'params':{'html_params':{'questionType':'' ,'difficulty':''}},
                'submitted_answers':{'SQLEditor':"SELECT *"},
                'correct_answers':{'SQLEditor':"SELECT * FROM Airport"}}
    
        result = customGrader(data)

        self.assertGreaterEqual(result,0)
        self.assertLessEqual(result,1)
    
    # valueMatch
    # 0 - no matches
    def testValueMatchReturnsZeroWhenNoValuesMatch(self):
        expectedAns = [(7,8,9),(1,4,2)]
        actualAns = [(1,2,3),(4,5,6)]

        res = valueMatch(expectedAns,actualAns)

        self.assertEqual(res,0)
    # 0 - empty
    # def testValueMatchReturnsZeroWhenEmpty(self):
    # # 0.5
    # def testValueMatchReturnsHalfWhenHalfValuesMatch(self):
    # # 1
    # def testValueMatchReturnsOneWhenAllValuesMatch(self):

    # colMatch
    # same
    # 1 over
    # 1 less
    # 0

    # rowMatch
    # same
    # 1 over
    # 1 less
    # 0
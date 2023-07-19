import unittest
from parameterized import parameterized
from SQLCustomGrader import *

class CustomGraderTest(unittest.TestCase):
    # 0 similarity
    def testAutograderReturnsZeroWhenNoSimilarities(self):
        data = {'submitted_answers':{'SQLEditor':""},
                'correct_answers':{'SQLEditor':"SELECT * FROM Airport"}}
    
        result = customGrader(data)

        self.assertEqual(0,result)
    
    # 100% similarity
    def testAutograderReturnsOneWhenExactMatch(self):
        data = {'submitted_answers':{'SQLEditor':"SELECT * from Airport"},
                'correct_answers':{'SQLEditor':"SELECT * FROM Airport"}}
    
        result = customGrader(data)

        self.assertEqual(1,result)
    
    # 75% similarity
    def testAutograderReturnsOneWhenAboveThresholdMatch(self):
        data = {'submitted_answers':{'SQLEditor':"SELECT * FROM"},
                'correct_answers':{'SQLEditor':"SELECT * FROM Airport"}}
    
        result = customGrader(data)

        self.assertEqual(1,result)
    
    # 50% similarity
    def testAutograderReturnsDecimalWhenBelowThresholdMatch(self):
        data = {'submitted_answers':{'SQLEditor':"SELECT *"},
                'correct_answers':{'SQLEditor':"SELECT * FROM Airport"}}
    
        result = customGrader(data)

        self.assertGreaterEqual(result,0)
        self.assertLessEqual(result,1)
    
    # more cases for matching depending on threshold changes in the futre as well as more detailed grading

    # exact same
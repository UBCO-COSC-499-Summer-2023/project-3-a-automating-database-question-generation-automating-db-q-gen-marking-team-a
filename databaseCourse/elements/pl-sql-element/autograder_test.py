import unittest
from unittest.mock import Mock,patch
from parameterized import parameterized
from SQLElementSharedLibrary.SQLCustomGrader import *

class CustomGraderTest(unittest.TestCase):
    # # 0 similarity
    # def testAutograderReturnsZeroWhenNoSimilarities(self):
    #     data = {'submitted_answers':{'SQLEditor':""},
    #             'correct_answers':{'SQLEditor':"SELECT * FROM Airport"}}
    
    #     result = customGrader(data)

    #     self.assertEqual(0,result)
    
    # # 100% similarity
    # def testAutograderReturnsOneWhenExactMatch(self):
    #     data = {'submitted_answers':{'SQLEditor':"SELECT * from Airport"},
    #             'correct_answers':{'SQLEditor':"SELECT * FROM Airport"}}
    
    #     result = customGrader(data)

    #     self.assertEqual(1,result)
    
    # # 75% similarity
    # def testAutograderReturnsOneWhenAboveThresholdMatch(self):
    #     data = {'submitted_answers':{'SQLEditor':"SELECT * FROM"},
    #             'correct_answers':{'SQLEditor':"SELECT * FROM Airport"}}
    
    #     result = customGrader(data)

    #     self.assertEqual(1,result)
    
    # # 50% similarity
    # def testAutograderReturnsDecimalWhenBelowThresholdMatch(self):
    #     data = {'submitted_answers':{'SQLEditor':"SELECT *"},
    #             'correct_answers':{'SQLEditor':"SELECT * FROM Airport"}}
    
    #     result = customGrader(data)

    #     self.assertGreaterEqual(result,0)
    #     self.assertLessEqual(result,1)
    
    # case for perfect match - 1/1
    @patch('SQLElementSharedLibrary.SQLCustomGrader.getExpectedAndActualQueryResults',return_value=([("Yo",1,2)],[("Yo",1,2)]))
    def testAutoGraderOutputGradingQuery(self,getExpectedAndActualQueryResult):
        data = {
                "params":{"db_initalize":"CREATE TABLE Airport(name int)"}
                }

        res = gradeQueryQuestion(data,"","")

        self.assertEqual(1.0,res)

    # case for imperfect match - 0/1
    @patch('SQLElementSharedLibrary.SQLCustomGrader.getExpectedAndActualQueryResults',return_value=([],[("Yo",1,2)]))
    @patch('SQLElementSharedLibrary.SQLCustomGrader.rowColMatch',return_value=0)
    @patch('SQLElementSharedLibrary.SQLCustomGrader.valueMatch',return_value=0)
    def testAutoGraderOutputGradingQuery2(self,getExpectedAndActualQueryResult,rowColMatch,valueMatch):
        data = {
                "params":{"db_initalize":"CREATE TABLE Airport(name int)"}
                }

        res = gradeQueryQuestion(data,"","")

        self.assertEqual(0,res)

    
    # more cases for matching depending on threshold changes in the futre as well as more detailed grading

    # exact same
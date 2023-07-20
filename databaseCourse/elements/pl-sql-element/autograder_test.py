import unittest
from unittest.mock import Mock,patch
from parameterized import parameterized
from SQLElementSharedLibrary.SQLCustomGrader import *

class CustomGraderTest(unittest.TestCase):

    # Grade Query Question
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
    @patch('SQLElementSharedLibrary.SQLCustomGrader.rowMatch',return_value=0)
    @patch('SQLElementSharedLibrary.SQLCustomGrader.valueMatch',return_value=0)
    @patch('SQLElementSharedLibrary.SQLCustomGrader.colMatch',return_value=0)
    def testAutoGraderOutputGradingQuery2(self,getExpectedAndActualQueryResult,rowMatch,colMatch,valueMatch):
        data = {
                "params":{"db_initalize":"CREATE TABLE Airport(name int)"}
                }

        res = gradeQueryQuestion(data,"","")

        self.assertEqual(0,res)

    # valueMatch
    # 0 - no matches
    def testValueMatchReturnsZeroWhenNoValuesMatch(self):
        expectedAns = [(7,8,9),(1,4,2)]
        actualAns = [(1,2,3),(4,5,6)]

        res = valueMatch(expectedAns,actualAns)

        self.assertEqual(res,0)
    # 0 - empty
    def testValueMatchReturnsZeroWhenEmpty(self):
        expectedAns = [(1,2,3),(4,5,6)]
        actualAns = []

        res = valueMatch(expectedAns,actualAns)

        self.assertEqual(res,0)
    # 0.5
    def testValueMatchReturnsHalfWhenHalfValuesMatch(self):
        expectedAns = [(7,8,9),(1,2,3)]
        actualAns = [(1,2,3),(4,5,6)]

        res = valueMatch(expectedAns,actualAns)

        self.assertEqual(res,0.5)
    # 1
    def testValueMatchReturnsOneWhenAllValuesMatch(self):
        expectedAns = [(4,5,6),(1,2,3)]
        actualAns = [(1,2,3),(4,5,6)]

        res = valueMatch(expectedAns,actualAns)

        self.assertEqual(res,1)

    # colMatch
    # same
    def testColMatchReturnsOneWhenSameNumberofCols(self):
        expectedAns = [(4,5,6),(1,2,3)]
        actualAns = [(1,2,3),(4,5,6)]

        res = colMatch(expectedAns,actualAns)

        self.assertEqual(res,1)

    # 1 over
    def testColMatchReturnsOneLessWhenOneMoreCol(self):
        expectedAns = [(4,5),(1,2)]
        actualAns = [(1,2,3),(4,5,6)]

        res = colMatch(expectedAns,actualAns)

        self.assertEqual(res,0.5)

    # 1 less
    def testColMatchReturnsOneLessWhenOneLessCol(self):
        expectedAns = [(4,5,6,7),(1,2,9,8)]
        actualAns = [(1,2),(4,4)]

        res = colMatch(expectedAns,actualAns)

        self.assertEqual(res,0.5)

    # 0
    def testColMatchReturnsZeroWhenEmpty(self):
        expectedAns = [(4,5),(1,2)]
        actualAns = [()]

        res = colMatch(expectedAns,actualAns)

        self.assertEqual(res,0)

    # rowMatch
    def testRowMatchReturnsOneWhenSameNumberofRows(self):
        expectedAns = [(4,5,6),(1,2,3)]
        actualAns = [(1,2,3),(4,5,6)]

        res = rowMatch(expectedAns,actualAns)

        self.assertEqual(res,1)

    # 1 over
    def testRowMatchReturnsOneLessWhenOneMoreRow(self):
        expectedAns = [(4,5),(1,2)]
        actualAns = [(1,2,3),(4,5,6),(9,8)]

        res = rowMatch(expectedAns,actualAns)

        self.assertEqual(res,0.5)

    # 1 less
    def testRowMatchReturnsOneLessWhenOneLessRow(self):
        expectedAns = [(4,5),(6,7)]
        actualAns = [(1,2)]

        res = rowMatch(expectedAns,actualAns)

        self.assertEqual(res,0.5)

    # 0
    def testRowMatchReturnsZeroWhenEmpty(self):
        expectedAns = [(4,5),(1,2)]
        actualAns = [()]

        res = rowMatch(expectedAns,actualAns)

        self.assertEqual(res,0)
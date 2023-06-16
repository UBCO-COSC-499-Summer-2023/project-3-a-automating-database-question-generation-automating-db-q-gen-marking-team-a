# -*- coding: utf-8 -*-
from randomgeneration import *

# unit test is whitebox testing, namely, test every unit of file "randomgeneration.py"
# there are several main parts needed to be tested:
# function of generating strong/weak entities
# function of generating 1-1/1-N/M-N relationships
# funciton of generating question that is to generate entities and their relationships by integrating the above 2 functions
# Therefore, this unit-test will focus on the 3 main units
# (1) buildEntity
# (2) buildRelationship
# (3) generate_question


import unittest


class Test_generate_random(unittest.TestCase):
    # @unittest.skip('Some reason')
    def setUp(self):
        self.name = "Tom"
        self.identifyingEntity = None
        self.minattr = 3
        self.maxattr = 6
        self.strong_entity = buildEntity(self.name, self.identifyingEntity, self.minattr, self.maxattr)
        [self.name, self.key, self.ppk, self.attr, self.identifyingEntity] = self.strong_entity  # unpack

        self.e1 = buildEntity("Tom", None)  # strong entity
        self.e2 = buildEntity("David", None)  # strong entity
        self.e3 = buildEntity("Jack", None)  # strong entity
        self.e4 = buildEntity("Lee", "Tom")  # weak entity
        self.e5 = buildEntity("Andy", "David")  # weak entity
        self.e6 = buildEntity("Henry", "Jack")  # weak entity

        self.setting_values = {
            "MIN_STRONG_ENTITY": 3, "MAX_STRONG_ENTITY": 6,
            "MIN_WEAK_ENTITY": 1, "MAX_WEAK_ENTITY": 3,
            "MIN_11_RELATIONSHIP": 2, "MAX_11_RELATIONSHIP": 5,
            "MIN_1N_RELATIONSHIP": 2, "MAX_1N_RELATIONSHIP": 5,
            "MIN_MN_RELATIONSHIP": 2, "MAX_MN_RELATIONSHIP": 4
        }
        self.data = {}
        self.data['params'] = self.setting_values
        self.result = generate_question(8888, self.data)
        self.question = self.result['question'].strip().split("\n")
        self.answer = self.result['answer'].strip().split("\n")
        # calculate the number of entities in question
        self.strong_entities_question, self.weak_entities_question, self.relationship_question = 0, 0, 0
        for keys in self.question:
            if " is identified by its association with " in keys or " exists dependent on " in keys:
                self.weak_entities_question += 1

            if " is identified by " in keys or " has key " in keys:
                self.strong_entities_question += 1

            if " is connected with one " in keys or " has multiple relationships with " in keys:
                self.relationship_question += keys.count(" is connected with one ")
                self.relationship_question += keys.count(" has multiple relationships with ")

        # print( strong_entities_question, weak_entities_question, relationship_question//2 )
        # calculate the number of entities & relationships in answer
        self.strong_entities_answer, self.weak_entities_answer, self.relationship_answer = [], [], []
        for keys in self.answer:
            if "{PK}" in keys:
                self.strong_entities_answer.append(keys)
            elif "{PPK}" in keys:
                self.weak_entities_answer.append(keys)
            else:
                self.relationship_answer.append(keys)

    def tearDown(self):
        self.name = "Tom"
        self.identifyingEntity = None
        self.minattr = 3
        self.maxattr = 6


    def test_strong_assertGreater(self):
        self.assertGreater(len(self.key), 0, "no primary key generated for strong entity")

    def test_weak_assertGreater(self):
        self.name = "Jack"
        self.identifyingEntity = "Tom"
        self.minattr = 2
        self.maxattr = 5
        self.assertGreater(len(self.key), 0, "no primary key generated for strong entity")

    def test_strong_assertEqual(self):
        self.assertEqual(len(self.ppk), 0, "there is partial primary key generated for strong entity")

    def test_weak_assertEqual(self):
        self.name = "Jack"
        self.identifyingEntity = "Tom"
        self.minattr = 2
        self.maxattr = 5
        self.assertEqual(len(self.ppk), 0, "there is partial primary key generated for strong entity")

    def test_strong_assertGreaterEqual_len_attr(self):
        self.assertGreaterEqual(len(self.attr), self.minattr, "too few attribute(s) generated for strong entity")

    def test_weak_assertGreaterEqual_len_attr(self):
        self.name = "Jack"
        self.identifyingEntity = "Tom"
        self.minattr = 2
        self.maxattr = 5
        self.assertGreaterEqual(len(self.attr), self.minattr, "too few attribute(s) generated for strong entity")

    def test_strong_assertGreaterEqual_maxattr(self):
        self.assertGreaterEqual(self.maxattr, len(self.attr), "too many attribute(s) generated for strong entity")

    def test_weak_assertGreaterEqual_maxattr(self):
        self.name = "Jack"
        self.identifyingEntity = "Tom"
        self.minattr = 2
        self.maxattr = 5
        self.assertGreaterEqual(self.maxattr, len(self.attr), "too many attribute(s) generated for strong entity")

    def test_buildRelationship_1(self):
        [_, _, card1, card2, attr] = buildRelationship(self.e1, self.e4, 0)  # 1-1
        f = "1..1" == card1 and "1..1" == card2
        self.assertTrue(f, "no 1-1 relationship generated for 2 entities")
        # print(_, _, card1, card2, attr)

    def test_buildRelationship_2(self):
        [_, _, card1, card2, attr] = buildRelationship(self.e1, self.e4, 0)  # 1-1
        f = "1..1" == card1 and "1..1" == card2
        self.assertTrue(f, "no 1-1 relationship generated for 2 entities")
        # print(_, _, card1, card2, attr)

    def test_buildRelationship_3(self):
        [_, _, card1, card2, attr] = buildRelationship(self.e1, self.e4, 0)  # 1-1
        f = "1..1" == card1 and "1..1" == card2
        self.assertTrue(f, "no 1-1 relationship generated for 2 entities")
        # print(_, _, card1, card2, attr)

    def test_generate_question_strong(self):
        self.assertEqual(len(self.strong_entities_answer), self.strong_entities_question, "number of strong entities does not match")

    def test_generate_question_weak(self):
        self.assertEqual(len(self.weak_entities_answer), self.weak_entities_question, "number of weak entities does not match")

    def test_generate_question(self):
        self.assertEqual(len(self.relationship_answer), self.relationship_question//2, "number of relationships does not match")

    # @unittest.skip('Some reason')
    def test_generate_random(self):
        data = {}
        question_data = generate_random(data)
        self.assertEqual(len(question_data), 4, "the returned data is not valid")
        return


unittest.main(argv=[''], verbosity=2, exit=False)


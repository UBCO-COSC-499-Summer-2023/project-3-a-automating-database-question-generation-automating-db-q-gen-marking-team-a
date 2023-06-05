# -*- coding: utf-8 -*-

from randomgeneration import *
import unittest
from unittest import TestCase


# integration test is blackbox testing, namely, test the whole application of file "randomgeneration.py"
# the main interface of file "randomgeneration.py":
# generate_random(data),
# it returns the generated entities & relationships, and pack them in list question & answer
# Therefore, this integration-test will focus on the 3 main units
# (1) data structure: the returned data should contain 4 elements:
# "question", "answer", "maximum_attempts", "penalty_type"
# (2) data values: the returned 4 elements have their valid values,
# such as not empty for list question & answer
# (3) data detail: the returned elements (list question & answer) should contain consistent data
# such as,
# the same number of strong/weak entities, relationships
# the numbers of strong/weak entities, relationships match the setting-values


class test_generate_random_integration(unittest.TestCase):
    def setUp(self):
        self.data = {}
        self.MIN_STRONG_ENTITY=5
        self.MAX_STRONG_ENTITY=9
        self.MIN_WEAK_ENTITY=3
        self.MAX_WEAK_ENTITY=6
        self.MIN_11_RELATIONSHIP=3
        self.MAX_11_RELATIONSHIP=7
        self.MIN_1N_RELATIONSHIP=3
        self.MAX_1N_RELATIONSHIP=6
        self.MIN_MN_RELATIONSHIP=3
        self.MAX_MN_RELATIONSHIP=5

        self.setting_values = {
            "MIN_STRONG_ENTITY": self.MIN_STRONG_ENTITY,
            "MAX_STRONG_ENTITY": self.MAX_STRONG_ENTITY,
            "MIN_WEAK_ENTITY": self.MIN_WEAK_ENTITY,
            "MAX_WEAK_ENTITY": self.MAX_WEAK_ENTITY,
            "MIN_11_RELATIONSHIP": self.MIN_11_RELATIONSHIP,
            "MAX_11_RELATIONSHIP": self.MAX_11_RELATIONSHIP,
            "MIN_1N_RELATIONSHIP": self.MIN_1N_RELATIONSHIP,
            "MAX_1N_RELATIONSHIP": self.MAX_1N_RELATIONSHIP,
            "MIN_MN_RELATIONSHIP": self.MIN_MN_RELATIONSHIP,
            "MAX_MN_RELATIONSHIP": self.MAX_MN_RELATIONSHIP
        }
        self.data['params'] = self.setting_values
        # get data
        self.question_data = generate_random(self.data)

        # range of strong entities
        self.MIN_STRONG_ENTITY = self.data['params']["MIN_STRONG_ENTITY"]
        self.MAX_STRONG_ENTITY = self.data['params']["MAX_STRONG_ENTITY"]
        # range of weak entities
        self.MIN_WEAK_ENTITY = self.data['params']["MIN_WEAK_ENTITY"]
        self.MAX_WEAK_ENTITY = self.data['params']["MAX_WEAK_ENTITY"]
        # range of 1-1 relationships
        self.MIN_11_RELATIONSHIP = self.data['params']["MIN_11_RELATIONSHIP"]
        self.MAX_11_RELATIONSHIP = self.data['params']["MAX_11_RELATIONSHIP"]
        # range of 1-N relationships
        self.MIN_1N_RELATIONSHIP = self.data['params']["MIN_1N_RELATIONSHIP"]
        self.MAX_1N_RELATIONSHIP = self.data['params']["MAX_1N_RELATIONSHIP"]
        # range of M-N relationships
        self.MIN_MN_RELATIONSHIP = self.data['params']["MIN_MN_RELATIONSHIP"]
        self.MAX_MN_RELATIONSHIP = self.data['params']["MAX_MN_RELATIONSHIP"]
        #
        self.question = self.question_data["question"].split("\n")
        self.strong_entities_question, self.weak_entities_question, self.relationship_question = 0, 0, 0
        for it in self.question:
            if " is identified by its association with " in it or " exists dependent on " in it:
                self.weak_entities_question += 1
            elif " is identified by " in it or " has key " in it:
                self.strong_entities_question += 1
            if " is connected with one " in it or " has multiple relationships with " in it:
                self.relationship_question += it.count(" is connected with one ")
                self.relationship_question += it.count(" has multiple relationships with ")
        self.relationship_question = self.relationship_question // 2
        #
        self.answer = self.question_data["answer"].split("\n")
        self.strong_entities_answer, self.weak_entities_answer, self.relationships_11_answer, self.relationships_1N_answer, self.relationships_MN_answer = 0, 0, 0, 0, 0
        for it in self.answer:
            if "{PK}" in it:
                self.strong_entities_answer += 1
            elif "{PPK}" in it:
                self.weak_entities_answer += 1
            else:
                if it.count("1..1") == 2:
                    self.relationships_11_answer += 1
                elif it.count("1..1") == 1 and it.count("1..*") == 1:
                    self.relationships_1N_answer += 1
                elif it.count("1..*") == 2:
                    self.relationships_MN_answer += 1
        self.relationship_answer = self.relationships_11_answer + self.relationships_1N_answer + self.relationships_MN_answer

    def test_questions_data_question(self):
        assert len(self.question_data["question"]) > 0, "question element should not be empty"

    def test_questions_data_answer(self):
        assert len(self.question_data["answer"]) > 0, "answer element should not be empty"

    def test_question_data_max_attempt(self):
        assert self.question_data["maximum_attempts"] == 7, "maximum_attempts element should equal to 7"

    def test_question_data_penalty_type(self):
        assert self.question_data["penalty_type"] == 0, "penalty_type element should equal to 0"

    def test_whole01(self):
        print("Test case function for the whole 01: data structure")
        assert len(self.question_data) == 4, "question_data should contain 4 elements"
        elements = ["question", "answer", "maximum_attempts", "penalty_type"]
        for ele in elements:
            assert ele in self.question_data, "question_data should contain element " + ele

    def test_min_strong(self):
        assert self.strong_entities_answer >= self.MIN_STRONG_ENTITY, "too few strong entities generated"

    def test_max_strong(self):
        assert self.strong_entities_answer <= self.MAX_STRONG_ENTITY, "too many strong entities generated"

    def test_min_weak(self):
        assert self.weak_entities_answer >= self.MIN_WEAK_ENTITY, "too few weak entities generated"

    def test_max_weak(self):
        assert self.weak_entities_answer <= self.MAX_WEAK_ENTITY, "too many weak entities generated"

    def test_min_11(self):
        assert self.relationships_11_answer >= self.MIN_11_RELATIONSHIP, "too few 1-1 relationships generated"

    def test_max_11(self):
        assert self.relationships_11_answer <= self.MAX_11_RELATIONSHIP, "too many 1-1 relationships generated"

    def test_min_1n(self):
        assert self.relationships_1N_answer >= self.MIN_1N_RELATIONSHIP, "too few 1-N relationships generated"

    def test_max_1n(self):
        assert self.relationships_1N_answer <= self.MAX_1N_RELATIONSHIP, "too many 1-N relationships generated"

    def test_min_MN(self):
        assert self.relationships_MN_answer >= self.MIN_MN_RELATIONSHIP, "too few M-N relationships generated"

    def test_max_MN(self):
        assert self.relationships_MN_answer <= self.MAX_MN_RELATIONSHIP, "too many M-N relationships generated"

    def test_strong_en(self):
        assert self.strong_entities_question == self.strong_entities_answer, "the number of strong entities in question & answer should macth"

    def test_weak_en(self):
        assert self.weak_entities_question == self.weak_entities_answer, "the number of weak entities in question & answer should macth"

    def test_relationship_question(self):
        assert self.relationship_question == self.relationship_answer, "the number of relationships in question & answer should macth"


unittest.main(argv=[''], verbosity=2, exit=False)

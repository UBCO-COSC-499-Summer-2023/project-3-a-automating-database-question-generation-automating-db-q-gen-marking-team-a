import unittest
from randomgeneration import *


class test(unittest.TestCase):

    def test_whole01(self):
        data = {}

        length = 4
        items_list = ["question", "answer", "maximum_attempts", "penalty_type"]

        for i in range(0, 10):
            question_data = generate_random(data)

            self.assertEqual(length, len(question_data))

            for it in items_list:
                fg = it in question_data
                self.assertTrue(fg)

    def test_whole02(self):
        data = {}

        for i in range(0, 10):
            question_data = generate_random(data)

            question = question_data['question'].strip().split("\n")
            answer = question_data['answer'].strip().split("\n")
            attempts = question_data['maximum_attempts']
            penalty = question_data['penalty_type']

            self.assertEqual(attempts, 7)
            self.assertEqual(penalty, 0)

            # parse list question
            ppk_marks = [" is identified by its association with ", " exists dependent on "]
            key_marks = [" is identified by ", " has key "]
            strong_entities_question, weak_entities_question, relationships_question = [], [], []

            for it in question:
                if ppk_marks[0] in it or ppk_marks[1] in it:
                    weak_entities_question.append(it)
                elif key_marks[0] in it or key_marks[1] in it:
                    strong_entities_question.append(it)
                else:
                    relationships_question.append(it)

            # parse list answer
            strong_entities_answer, weak_entities_answer, relationships_answer = [], [], []
            for it in answer:
                if "{PK}" in it:
                    strong_entities_answer.append(it)
                elif "{PPK}" in it:
                    weak_entities_answer.append(it)
                else:
                    relationships_answer.append(it)

            # entity check
            self.assertEqual(len(strong_entities_question), len(strong_entities_answer))
            self.assertEqual(len(weak_entities_question), len(weak_entities_answer))

            # relationship check
            self.assertGreaterEqual(len(relationships_answer), len(relationships_question))

            # relationships in list question == that in list answer
            relationship_marks = [
                " may be related to at most one ", " has at most one connection with ",
                " must be related to exactly one ", " is connected with one ",
                " may be related to many ", " has multiple relationships with ", " has zero or more connections with ",
                " must be related to at least one but possibly many ", "is associated with one or more "
            ]

            # for strong entities in list question
            offset1 = 0
            for it in strong_entities_question:
                for rs in relationship_marks:
                    if rs in it:
                        offset1 += it.count(rs)

            # for weak entities in list question
            offset2 = 0
            for it in weak_entities_question:
                for rs in relationship_marks:
                    if rs in it:
                        offset2 += it.count(rs)

            offset1 = offset1 // 2  # because relationship occurs in pair, so divived by 2
            offset2 = offset2 // 2  # because relationship occurs in pair, so divived by 2

            # whether there is redundancy in list answer
            redundancy_number = 0
            tmp_set = set()
            for it in answer:
                if it not in tmp_set:
                    tmp_set.add(it)
                else:
                    redundancy_number += 1

            self.assertEqual(len(relationships_answer) - redundancy_number,
                             len(relationships_question) + offset1 + offset2)

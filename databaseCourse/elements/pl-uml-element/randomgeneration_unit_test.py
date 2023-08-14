import unittest
from randomgeneration import *


class test(unittest.TestCase):

    def test_basic(self):
        data = {}
        question_data = generate_random(data)

        length = 4

        question = question_data['question'].split("\n")
        answer = question_data['answer'].split("\n")
        attempts = 7
        penalty = 0

        self.assertEqual(length, len(question_data))

        self.assertEqual(attempts, question_data['maximum_attempts'])
        self.assertEqual(penalty, question_data['penalty_type'])
        self.assertGreater(len(question), 0)
        self.assertGreater(len(answer), len(question))

    def test_detailed(self):
        data = {}
        question_data = generate_random(data)

        question = question_data['question'].split("\n")
        answer = question_data['answer'].split("\n")

        # for question
        tmp_set = set()
        for it in question:
            if it not in tmp_set:
                tmp_set.add(it.strip())
            else:
                print("redundancy in question: ", it, ", remove it")

        if len(tmp_set) != len(question):
            question = list(tmp_set)

        # for answer
        tmp_set = set()
        for it in answer:
            if it not in tmp_set:
                tmp_set.add(it.strip())
            else:
                print("redundancy in answer: ", it, ", remove it")

        if len(tmp_set) != len(answer):
            answer = list(tmp_set)

        # parse list question
        ppk_marks = [" is identified by its association with ", " exists dependent on "]
        key_marks = [" is identified by ", " has key "]
        strong_entities_question, weak_entities_question, relationships_question = [], [], []
        for it in question:
            flag = False
            for m in ppk_marks:
                if m in it:
                    weak_entities_question.append(it)
                    flag = True
                    break

            if flag:
                continue

            for m in key_marks:
                if m in it:
                    strong_entities_question.append(it)
                    flag = True
                    break

            if flag:
                continue

            relationships_question.append(it)

        self.assertEqual(len(question),
                         len(strong_entities_question) + len(weak_entities_question) + len(relationships_question))

        # parse list answer
        strong_entities_answer, weak_entities_answer, relationships_answer = [], [], []
        for it in answer:
            if "{PK}" in it:
                strong_entities_answer.append(it)
            elif "{PPK}" in it:
                weak_entities_answer.append(it)
            else:
                relationships_answer.append(it)

        self.assertEqual(len(answer),
                         len(strong_entities_answer) + len(weak_entities_answer) + len(relationships_answer))

        # entity check
        self.assertEqual(len(strong_entities_question), len(strong_entities_answer))
        self.assertEqual(len(weak_entities_question), len(weak_entities_answer))

        # relationship check
        self.assertGreaterEqual(len(relationships_answer), len(relationships_question))

        # relationships in list question == that in list answer
        relationship_marks = []
        relationship_marks += [" may be related to at most one ", " has at most one connection with "]
        relationship_marks += [" must be related to exactly one ", " is connected with one "]
        relationship_marks += [" may be related to many ", " has multiple relationships with ",
                               " has zero or more connections with "]
        relationship_marks += [" must be related to at least one but possibly many ", "is associated with one or more "]

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
        self.assertEqual(len(relationships_answer), len(relationships_question) + offset1 + offset2)

#!/usr/bin/python
# -*- coding: utf-8 -*-

from unittest import TestCase
from randomgrader import setMaxGrade, setMarkingCriteria, mark_answer


class test(TestCase):

    # Set up a question, a student answer, and grading parameters to use in each test
    def setUp(self):
        self.correct_entity_name = 0.2
        self.correct_attributes = 0.1
        self.correct_primary_keys = 0.2
        self.extra_entities = 0.25
        self.correct_weak_entities = 0.5
        self.correct_relationship_entities = 0.5
        self.correct_cardinality = 0.25
        self.extra_relationship = 0.25
        self.MAXIMUM_GRADE = 10

        self.marking_criteria = {
            'correct_entity_name': self.correct_entity_name,
            'correct_attributes': self.correct_attributes,
            'correct_primary_keys': self.correct_primary_keys,
            'extra_entity': self.extra_entities,
            'correct_weak_entity': self.correct_weak_entities,
            'correct_relationship_entity': self.correct_relationship_entities,
            'correct_cardinality': self.correct_cardinality,
            'extra_relationship': self.extra_relationship,
            }

        self.student_answer = \
            '''[Tank|number {PK};name;volume;color]
            [Fish|id {PK};name;color;weight]
            [Species|id {PK};name;preferredFood]
            [Event|date {PPK};note]
            [Tank]1..1 - 0..*[Fish]
            [Fish]1..* - 1..1[Species]
            [Fish]1..1 - 0..*[Event]
            [Fish]0..* - 1..*[Fish]
            [Fish]1..* - 0..*[Event]'''

        self.question_template = {
            'id': 6,
            'title': 'fishstore',
            'created_by': 1,
            'question_template': 1,
            'maximum_grade': self.MAXIMUM_GRADE,
            'other_marking_criteria': {
                'correct_entity_name': self.correct_entity_name,
                'correct_attributes': self.correct_attributes,
                'correct_primary_keys': self.correct_primary_keys,
                'extra_entity': self.extra_entities,
                'correct_weak_entity': self.correct_weak_entities,
                'correct_relationship_entity': self.correct_relationship_entities,
                'correct_cardinality': self.correct_cardinality,
                'extra_relationship': self.extra_relationship,
                },
            'custom_css': '',
            'question': '''Construct a database design in UML for a fish store where:
A fish store maintains a number of [aquaria (tanks)](tank), each with a [number](number), [name](name), [volume](volume) and [color](color).
Each [tank](tank) contains a number of [fish](fish), each with an [id](id), [name](name), [color](color), and [weight](weight).
Each [fish](fish) is of a particular [species](species), which has a [id](id), [name](name), and [preferred food](preferredFood).
Each individual [fish](fish) has a number of [events](event) in its life, involving a [date](date) and a [note](note) relating to the event.
''',
            'answers': [{'answer': '''[Tank|number {PK};name;volume;color]
[Fish|id {PK};name;color;weight]
[Species|id {PK};name;preferredFood]
[Event|date {PPK};note]
[Tank]1..1 - 0..*[Fish]
[Fish]1..* - 1..1[Species]
[Fish]1..1 - 0..*[Event]
[Fish]0..* - 1..*[Fish]
[Fish]1..* - *[Event]
'''}],
            }


    # Set everything back to default values between tests
    def tearDown(self):
        setMaxGrade(10)
        setMarkingCriteria(
            0.2,
            0.1,
            0.2,
            0.25,
            0.5,
            0.5,
            0.25,
            0.25,
            )


    # Testing default parameters with a correct answer
    def test_correct_answer(self):
        grade = mark_answer(self.question_template.get('question'),
                            self.question_template.get('answers'),
                            self.student_answer)

        self.assertEqual(grade.get('mark'), 10)


    # Testing bad input which result in default parameters with a correct answer
    def test_bad_input(self):
        setMaxGrade(-1)
        setMarkingCriteria(
            'a',
            'b',
            'c',
            'abc',
            -1,
            0,
            1,
            2,
            )
        grade = mark_answer(self.question_template.get('question'),
                            self.question_template.get('answers'),
                            self.student_answer)

        self.assertEqual(grade.get('mark'), 10)


    # Testing modified parameters with a correct answer
    def test_different_max_grade(self):
        setMaxGrade(20)

        grade = mark_answer(self.question_template.get('question'),
                            self.question_template.get('answers'),
                            self.student_answer)

        self.assertEqual(grade.get('mark'), 20)


    # Testing partially correct answers with default grading criteria
    def test_partial_answer(self):
        self.student_answer = \
            '''[Tank]
            [Fish]
            [Species]
            [Event]
            [Tank]1..1 - 0..*[Fish]
            [Fish]1..* - 1..1[Species]
            [Fish]1..1 - 0..*[Event]
            [Fish]0..* - 1..*[Fish]
            [Fish]1..* - 0..*[Event]'''

        grade = mark_answer(self.question_template.get('question'),
                            self.question_template.get('answers'),
                            self.student_answer)

        self.assertEqual(grade.get('mark'), 8)


    # Testing if modified grading criteria works properly with partially correct answers
    def test_different_grading_criteria(self):
        setMarkingCriteria(
            1,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            )

        self.student_answer = \
            '''[tank|number {PK};name;volume;color]
            [fish|id {PK};name;color;weight]
            [species|id {PK};name;preferredFood]
            [event|date {PPK};note]
            [tank]1..1 - 0..*[fish]
            [fish]1..* - 1..1[species]
            [fish]1..1 - 0..*[event]
            [fish]0..* - 1..*[fish]
            [fish]1..* - 0..*[event]'''

        grade = mark_answer(self.question_template.get('question'),
                            self.question_template.get('answers'),
                            self.student_answer)

        self.assertEqual(grade.get('mark'), 0)

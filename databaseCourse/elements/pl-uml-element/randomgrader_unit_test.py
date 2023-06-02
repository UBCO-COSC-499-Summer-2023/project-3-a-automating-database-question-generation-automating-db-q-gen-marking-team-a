#!/usr/bin/python
# -*- coding: utf-8 -*-
from unittest import TestCase
from randomgrader import *


class test(TestCase):

    def setUp(self):
        self.MAXIMUM_GRADE = 10

    def tearDown(self):
        setMaxGrade(10)

    # setMaxGrade(...) sets the maximum amount of points possible for this question to its parameter
    # testing if function correctly changes the `MAXIMUM_GRADE` variable

    # Set normal value
    def test_setMaxGrade01(self):
        maxgrade = 20
        self.assertEqual(setMaxGrade(20), maxgrade)


    # Set small value
    def test_setMaxGrade02(self):
        maxgrade = 0.1
        self.assertEqual(setMaxGrade(0.1), maxgrade)


    # Set big value
    def test_setMaxGrade03(self):
        maxgrade = 1000.1
        self.assertEqual(setMaxGrade(1000.1), maxgrade)


    # Set invalid value - string
    def test_setMaxGrade04(self):
        maxgrade = 10
        self.assertEqual(setMaxGrade('5'), maxgrade)


    # Set invalid value - zero
    def test_setMaxGrade05(self):
        maxgrade = 10
        self.assertEqual(setMaxGrade(0), maxgrade)


    # Set invalid value - negative
    def test_setMaxGrade06(self):
        maxgrade = 10
        self.assertEqual(setMaxGrade(-1), maxgrade)



    # setMarkingCriteria(...) sets the relative weights of each part of the question to each of the parameters
    # testing if all parameters are correctly set after calling function

    # Set normal value
    def test_setMarkingCriteria01(self):
        markingcriteria = {
            'correct_entity_name': 0.33,
            'correct_attributes': 0.33,
            'correct_primary_keys': 0.33,
            'extra_entity': 0.33,
            'correct_weak_entity': 0.33,
            'correct_relationship_entity': 0.33,
            'correct_cardinality': 0.33,
            'extra_relationship': 0.33,
            }
        self.assertEqual(setMarkingCriteria(
            0.33,
            0.33,
            0.33,
            0.33,
            0.33,
            0.33,
            0.33,
            0.33,
            ), markingcriteria)


    # Set small and big values
    def test_setMarkingCriteria02(self):
        markingcriteria = {
            'correct_entity_name': 0.1,
            'correct_attributes': 0.01,
            'correct_primary_keys': 0.001,
            'extra_entity': 0.0001,
            'correct_weak_entity': 0.9999,
            'correct_relationship_entity': 0.999,
            'correct_cardinality': 0.99,
            'extra_relationship': 0.9,
            }
        self.assertEqual(setMarkingCriteria(
            0.1,
            0.01,
            0.001,
            0.0001,
            0.9999,
            0.999,
            0.99,
            0.9,
            ), markingcriteria)


    # Set invalid values - all parameters
    def test_setMarkingCriteria03(self):
        markingcriteria = {
            'correct_entity_name': 0.2,
            'correct_attributes': 0.1,
            'correct_primary_keys': 0.2,
            'extra_entity': 0.25,
            'correct_weak_entity': 0.5,
            'correct_relationship_entity': 0.5,
            'correct_cardinality': 0.25,
            'extra_relationship': 0.25,
            }
        self.assertEqual(setMarkingCriteria(
            'a',
            'b',
            'c',
            'abc',
            -1,
            0,
            1,
            2,
            ), markingcriteria)


    # Set invalid values - only some parameters
    def test_setMarkingCriteria04(self):
        markingcriteria = {
            'correct_entity_name': 0.33,
            'correct_attributes': 0.33,
            'correct_primary_keys': 0.33,
            'extra_entity': 0.33,
            'correct_weak_entity': 0.5,
            'correct_relationship_entity': 0.5,
            'correct_cardinality': 0.25,
            'extra_relationship': 0.25,
            }
        self.assertEqual(setMarkingCriteria(
            0.33,
            0.33,
            0.33,
            0.33,
            'a',
            'b',
            -999,
            999,
            ), markingcriteria)



    # convert(...) converts the student's answer into a dictionary divided into gradeable parts
    # testing if function correctly creates dictionaries of student answers

    # Set diagram with relationships
    def test_convert01(self):
        er_dict = {'entities': [{
            'entity_name': 'Fish',
            'primary_key': [],
            'partial_primary_key': [],
            'attributes': [],
            }, {
            'entity_name': 'Species',
            'primary_key': [],
            'partial_primary_key': [],
            'attributes': [],
            }, {
            'entity_name': 'Tank',
            'primary_key': [],
            'partial_primary_key': [],
            'attributes': [],
            }], 'relationships': [{'entities': ['Fish', 'Species'],
                                  'Fish': '', 'Species': ''}]}

        self.assertEqual(convert('''[Fish]
            [Species]
            [Tank]
            [Fish] - [Species]'''),
                         er_dict)


    # Set diagram with cardinalities
    def test_convert02(self):
        er_dict = {'entities': [{
            'entity_name': 'Tank',
            'primary_key': [],
            'partial_primary_key': [],
            'attributes': [],
            }, {
            'entity_name': 'Fish',
            'primary_key': [],
            'partial_primary_key': [],
            'attributes': [],
            }, {
            'entity_name': 'Species',
            'primary_key': [],
            'partial_primary_key': [],
            'attributes': [],
            }, {
            'entity_name': 'Event',
            'primary_key': [],
            'partial_primary_key': [],
            'attributes': [],
            }], 'relationships': [{'entities': ['Fish', 'Tank'],
                                  'Tank': '0..1', 'Fish': '0..*'}]}

        self.assertEqual(convert('''[Tank]
            [Fish]
            [Species]
            [Event]
            [Tank]0..1 - 0..*[Fish]'''),
                         er_dict)


    # Set diagram with attributes
    def test_convert03(self):
        er_dict = {'entities': [{
            'entity_name': 'Tank',
            'primary_key': [],
            'partial_primary_key': [],
            'attributes': ['name', 'number', 'volume'],
            }, {
            'entity_name': 'Fish',
            'primary_key': [],
            'partial_primary_key': [],
            'attributes': ['color', 'id', 'name'],
            }, {
            'entity_name': 'Species',
            'primary_key': [],
            'partial_primary_key': [],
            'attributes': ['id', 'name', 'preferredFood'],
            }, {
            'entity_name': 'Color',
            'primary_key': [],
            'partial_primary_key': [],
            'attributes': [],
            }], 'relationships': [{'entities': ['Color', 'Fish'],
                                  'Color': '', 'Fish': ''},
                                  {'entities': ['Fish', 'Species'],
                                  'Species': '', 'Fish': ''}]}

        self.assertEqual(convert('''[Tank|number;name;volume]
            [Fish|id;name;color]
            [Species|id;name;preferredFood]
            [Color]
            [Color] - [Fish]
            [Species] - [Fish]'''),
                         er_dict)



    # mark_answer(...) grades a student's answer depending on the relative grading criterias
    # testing if different student answers get graded correctly according to grading criteria

    # Mark correct answer
    def test_mark_answer01(self):
        question = 'question'
        answer = \
            [{'answer': '''[Tank|number {PK};name;volume;color]
                    [Fish|id {PK};name;color;weight]
                    [Species|id {PK};name;preferredFood]
                    [Event|date {PPK};note]
                    [Tank]1..1 - 0..*[Fish]
                    [Fish]1..* - 1..1[Species]
                    [Fish]1..1 - 0..*[Event]
                    [Fish]0..* - 1..*[Fish]
                    [Fish]1..* - *[Event]'''}]

        stu_answer = \
            '''[Tank|number {PK};name;volume;color]
            [Fish|id {PK};name;color;weight]
            [Species|id {PK};name;preferredFood]
            [Event|date {PPK};note]
            [Tank]1..1 - 0..*[Fish]
            [Fish]1..* - 1..1[Species]
            [Fish]1..1 - 0..*[Event]
            [Fish]0..* - 1..*[Fish]
            [Fish]1..* - 0..*[Event]'''
        self.assertEqual(mark_answer(question, answer,
                         stu_answer).get('mark'), 10)


    # Mark partially correct answer
    def test_mark_answer02(self):
        question = 'question'
        answer = \
            [{'answer': '''[Tank|number {PK};name;volume;color]
                    [Fish|id {PK};name;color;weight]
                    [Species|id {PK};name;preferredFood]
                    [Event|date {PPK};note]
                    [Tank]1..1 - 0..*[Fish]
                    [Fish]1..* - 1..1[Species]
                    [Fish]1..1 - 0..*[Event]
                    [Fish]0..* - 1..*[Fish]
                    [Fish]1..* - *[Event]'''}]

        stu_answer = \
            '''[Tank]
            [Fish]
            [Species]
            [Event]
            [Tank]1..1 - 0..*[Fish]
            [Fish]1..* - 1..1[Species]
            [Fish]1..1 - 0..*[Event]
            [Fish]0..* - 1..*[Fish]
            [Fish]1..* - 0..*[Event]'''
        self.assertEqual(mark_answer(question, answer,
                         stu_answer).get('mark'), 8)


    # Mark empty answer
    def test_mark_answer03(self):
        question = 'question'
        answer = \
            [{'answer': '''[Tank|number {PK};name;volume;color]
                    [Fish|id {PK};name;color;weight]
                    [Species|id {PK};name;preferredFood]
                    [Event|date {PPK};note]
                    [Tank]1..1 - 0..*[Fish]
                    [Fish]1..* - 1..1[Species]
                    [Fish]1..1 - 0..*[Event]
                    [Fish]0..* - 1..*[Fish]
                    [Fish]1..* - *[Event]'''}]

        stu_answer = ''
        self.assertEqual(mark_answer(question, answer,
                         stu_answer).get('mark'), 0)



    # check_sp_char(...) translates cardinalities into special characters for grading
    # testing if function correctly assigns special characters if needed

    # Testing all possible combinations
    def test_check_sp_char01(self):
        ans_card = '*'
        stu_card = '0..*'
        self.assertEqual(check_sp_char(stu_card, ans_card), '*')


    def test_check_sp_char02(self):
        stu_card = '1..*'
        ans_card = '*'
        self.assertEqual(check_sp_char(stu_card, ans_card), '*')


    def test_check_sp_char03(self):
        stu_card = '0..1'
        ans_card = '*'
        self.assertEqual(check_sp_char(stu_card, ans_card), '0..1')


    def test_check_sp_char04(self):
        stu_card = '1..1'
        ans_card = '*'
        self.assertEqual(check_sp_char(stu_card, ans_card), '1..1')


    def test_check_sp_char05(self):
        stu_card = '0..*'
        ans_card_2 = '0@1'
        self.assertEqual(check_sp_char(stu_card, ans_card_2), '0..*')


    def test_check_sp_char06(self):
        stu_card = '1..*'
        ans_card_2 = '0@1'
        self.assertEqual(check_sp_char(stu_card, ans_card_2), '1..*')


    def test_check_sp_char07(self):
        stu_card = '0..1'
        ans_card_2 = '0@1'
        self.assertEqual(check_sp_char(stu_card, ans_card_2), '0@1')


    def test_check_sp_char08(self):
        stu_card = '1..1'
        ans_card_2 = '0@1'
        self.assertEqual(check_sp_char(stu_card, ans_card_2), '0@1')



    # mark(...) compares two dictionaries for discrepancies and returns a final mark (called inside mark_answer(...))
    # testing if marking correctly follows criteria with different answers

    # Mark correct answer
    def test_mark01(self):
        correct_answer = {'entities': [{
            'entity_name': 'Tank',
            'primary_key': [],
            'partial_primary_key': [],
            'attributes': ['name', 'number', 'volume'],
            }, {
            'entity_name': 'Fish',
            'primary_key': [],
            'partial_primary_key': [],
            'attributes': ['color', 'id', 'name'],
            }, {
            'entity_name': 'Species',
            'primary_key': [],
            'partial_primary_key': [],
            'attributes': ['id', 'name', 'preferredFood'],
            }, {
            'entity_name': 'Color',
            'primary_key': [],
            'partial_primary_key': [],
            'attributes': [],
            }], 'relationships': [{'entities': ['Color', 'Fish'],
                                  'Color': '', 'Fish': ''},
                                  {'entities': ['Fish', 'Species'],
                                  'Species': '', 'Fish': ''}]}

        student_answer_1 = {'entities': [{
            'entity_name': 'Tank',
            'primary_key': [],
            'partial_primary_key': [],
            'attributes': ['name', 'number', 'volume'],
            }, {
            'entity_name': 'Fish',
            'primary_key': [],
            'partial_primary_key': [],
            'attributes': ['color', 'id', 'name'],
            }, {
            'entity_name': 'Species',
            'primary_key': [],
            'partial_primary_key': [],
            'attributes': ['id', 'name', 'preferredFood'],
            }, {
            'entity_name': 'Color',
            'primary_key': [],
            'partial_primary_key': [],
            'attributes': [],
            }], 'relationships': [{'entities': ['Color', 'Fish'],
                                  'Color': '', 'Fish': ''},
                                  {'entities': ['Fish', 'Species'],
                                  'Species': '', 'Fish': ''}]}

        self.assertEqual(mark(correct_answer,
                         student_answer_1).get('mark'), 10)


    # Mark partially correct answer
    def test_mark02(self):
        correct_answer = {'entities': [{
            'entity_name': 'Tank',
            'primary_key': [],
            'partial_primary_key': [],
            'attributes': ['name', 'number', 'volume'],
            }, {
            'entity_name': 'Fish',
            'primary_key': [],
            'partial_primary_key': [],
            'attributes': ['color', 'id', 'name'],
            }, {
            'entity_name': 'Species',
            'primary_key': [],
            'partial_primary_key': [],
            'attributes': ['id', 'name', 'preferredFood'],
            }, {
            'entity_name': 'Color',
            'primary_key': [],
            'partial_primary_key': [],
            'attributes': [],
            }], 'relationships': [{'entities': ['Color', 'Fish'],
                                  'Color': '', 'Fish': ''},
                                  {'entities': ['Fish', 'Species'],
                                  'Species': '', 'Fish': ''}]}

        student_answer_2 = {'entities': [{
            'entity_name': 'Fish',
            'primary_key': [],
            'partial_primary_key': [],
            'attributes': ['color', 'id', 'name'],
            }, {
            'entity_name': 'Species',
            'primary_key': [],
            'partial_primary_key': [],
            'attributes': ['id', 'name', 'preferredFood'],
            }, {
            'entity_name': 'Color',
            'primary_key': [],
            'partial_primary_key': [],
            'attributes': [],
            }], 'relationships': [{'entities': ['Color', 'Fish'],
                                  'Color': '', 'Fish': ''},
                                  {'entities': ['Fish', 'Species'],
                                  'Species': '', 'Fish': ''}]}

        self.assertEqual(mark(correct_answer,
                         student_answer_2).get('mark'), 8.33)


    # Mark empty answer
    def test_mark03(self):
        correct_answer = {'entities': [{
            'entity_name': 'Tank',
            'primary_key': [],
            'partial_primary_key': [],
            'attributes': ['name', 'number', 'volume'],
            }, {
            'entity_name': 'Fish',
            'primary_key': [],
            'partial_primary_key': [],
            'attributes': ['color', 'id', 'name'],
            }, {
            'entity_name': 'Species',
            'primary_key': [],
            'partial_primary_key': [],
            'attributes': ['id', 'name', 'preferredFood'],
            }, {
            'entity_name': 'Color',
            'primary_key': [],
            'partial_primary_key': [],
            'attributes': [],
            }], 'relationships': [{'entities': ['Color', 'Fish'],
                                  'Color': '', 'Fish': ''},
                                  {'entities': ['Fish', 'Species'],
                                  'Species': '', 'Fish': ''}]}

        student_answer_3 = {'entities': {}, 'relationships': {}}
        self.assertEqual(mark(correct_answer,
                         student_answer_3).get('mark'), 0)



    # grade_question(...) grabs information to put into the `data` element
    # testing if information is correctly stored into this `data` element

    # Test if data is properly stored and retained
    def test_grade_question01(self):
        data_old = {'params': {
            'answer': [{'answer': '''[Tank|number {PK};name;volume;color]
                    [Fish|id {PK};name;color;weight]
                    [Species|id {PK};name;preferredFood]
                    [Event|date {PPK};note]
                    [Tank]1..1 - 0..*[Fish]
                    [Fish]1..* - 1..1[Species]
                    [Fish]1..1 - 0..*[Event]
                    [Fish]0..* - 1..*[Fish]
                    [Fish]1..* - 0..*[Event]'''}],
            'question_data': '''Construct a database design in UML for a fish store where:
                    A fish store maintains a number of [aquaria (tanks)](tank), each with a [number](number), [name](name), [volume](volume) and [color](color).
                    Each [tank](tank) contains a number of [fish](fish), each with an [id](id), [name](name), [color](color), and [weight](weight).
                    Each [fish](fish) is of a particular [species](species), which has a [id](id), [name](name), and [preferred food](preferredFood).
                    Each individual [fish](fish) has a number of [events](event) in its life, involving a [date](date) and a [note](note) relating to the event.
                    ''',
            'oldAnswer': '',
            'score': 0,
            'feedback': '',
            },
                'submitted_answers': {'c': '''[Tank|number {PK};name;volume;color]
                    [Fish|id {PK};name;color;weight]
                    [Species|id {PK};name;preferredFood]
                    [Event|date {PPK};note]
                    [Tank]1..1 - 0..*[Fish]
                    [Fish]1..* - 1..1[Species]
                    [Fish]1..1 - 0..*[Event]
                    [Fish]0..* - 1..*[Fish]
                    [Fish]1..* - 0..*[Event]'''}}

        data_new = {'params': {
            'answer': [{'answer': '''[Tank|number {PK};name;volume;color]
                    [Fish|id {PK};name;color;weight]
                    [Species|id {PK};name;preferredFood]
                    [Event|date {PPK};note]
                    [Tank]1..1 - 0..*[Fish]
                    [Fish]1..* - 1..1[Species]
                    [Fish]1..1 - 0..*[Event]
                    [Fish]0..* - 1..*[Fish]
                    [Fish]1..* - 0..*[Event]'''}],
            'question_data': '''Construct a database design in UML for a fish store where:
                    A fish store maintains a number of [aquaria (tanks)](tank), each with a [number](number), [name](name), [volume](volume) and [color](color).
                    Each [tank](tank) contains a number of [fish](fish), each with an [id](id), [name](name), [color](color), and [weight](weight).
                    Each [fish](fish) is of a particular [species](species), which has a [id](id), [name](name), and [preferred food](preferredFood).
                    Each individual [fish](fish) has a number of [events](event) in its life, involving a [date](date) and a [note](note) relating to the event.
                    ''',
            'score': 1.0,
            'feedback': '''Entity name marks: 0.8/0.8
Entity attribute marks: 0.4/0.4
Entity primary key marks: 0.8/0.8
Weak entity key marks: 0.5/0.5
Extra entities: 0.0
Total entity marks: 2.5/2.5
Relationship entity marks: 2.5/2.5
Relationship cardinalities marks: 2.5/2.5
Extra relationships: 0.0
Total relationship marks: 5.0/5.0
Total marks: 7.5/7.5
Total scaled marks: 10.0/10
''',
            'marker_feedback': '',
            'oldAnswer': '''[Tank|number {PK};name;volume;color]
                    [Fish|id {PK};name;color;weight]
                    [Species|id {PK};name;preferredFood]
                    [Event|date {PPK};note]
                    [Tank]1..1 - 0..*[Fish]
                    [Fish]1..* - 1..1[Species]
                    [Fish]1..1 - 0..*[Event]
                    [Fish]0..* - 1..*[Fish]
                    [Fish]1..* - 0..*[Event]''',
            },
                'submitted_answers': {'c': '''[Tank|number {PK};name;volume;color]
                    [Fish|id {PK};name;color;weight]
                    [Species|id {PK};name;preferredFood]
                    [Event|date {PPK};note]
                    [Tank]1..1 - 0..*[Fish]
                    [Fish]1..* - 1..1[Species]
                    [Fish]1..1 - 0..*[Event]
                    [Fish]0..* - 1..*[Fish]
                    [Fish]1..* - 0..*[Event]'''}}

        self.assertEqual(grade_question(data_old), data_new)

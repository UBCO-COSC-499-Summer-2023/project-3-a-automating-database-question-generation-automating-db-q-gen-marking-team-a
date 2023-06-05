#!/usr/bin/python
# -*- coding: utf-8 -*-
import copy
import re

#   PLEASE CHANGE FOLLOWING ATTRIBUTES FOR ALTERED GRADING SCHEMA

correct_entity_name = 0.2  # Default Weighting = 0.2
correct_attributes = 0.1  # Default Weighting = 0.1
correct_primary_keys = 0.2  # Default Weighting = 0.2
extra_entities = 0.25  # Default Weighting = 0.25
correct_weak_entities = 0.5  # Default Weighting = 0.5
correct_relationship_entities = 0.5  # Default Weighting = 0.5
correct_cardinality = 0.25  # Default Weighting = 0.25
extra_relationship = 0.25  # Default Weighting = 0.25
#  new added
#  correct_cardinality_text = 0.25  # Default Weighting = 0.25
MAXIMUM_GRADE = 10

# DEFAULT QUESTION WEIGHTS

marking_criteria = {
    'correct_entity_name': correct_entity_name,
    'correct_attributes': correct_attributes,
    'correct_primary_keys': correct_primary_keys,
    'extra_entity': extra_entities,
    'correct_weak_entity': correct_weak_entities,
    'correct_relationship_entity': correct_relationship_entities,
    'correct_cardinality': correct_cardinality,
    'extra_relationship': extra_relationship,
#  new added
# "correct_cardinality_text": correct_cardinality_text,
    }


def setMaxGrade(max_grade):
    global MAXIMUM_GRADE

    if isinstance(max_grade, int) or isinstance(max_grade, float):
        if max_grade > 0:
            MAXIMUM_GRADE = max_grade
            return MAXIMUM_GRADE

    return MAXIMUM_GRADE


def setMarkingCriteria(
    entity_name,
    entity_attributes,
    entity_key,
    extra_entity_penalty,
    weak_entity,
    relationship,
    cardinality,
    extra_relationship_penalty,
    # new added
    # cardinality_text,
    ):
    global correct_entity_name
    global correct_attributes
    global correct_primary_keys
    global extra_entities
    global correct_weak_entities
    global correct_relationship_entities
    global correct_cardinality
    global extra_relationship
    # new added
    # global correct_cardinality_text

    correct_entity_name = entity_name
    correct_attributes = entity_attributes
    correct_primary_keys = entity_key
    extra_entities = extra_entity_penalty
    correct_weak_entities = weak_entity
    correct_relationship_entities = relationship
    correct_cardinality = cardinality
    extra_relationship = extra_relationship_penalty
    # new added
    # correct_cardinality_text = cardinality_text

    global marking_criteria
    marking_criteria = {
        'correct_entity_name': correct_entity_name,
        'correct_attributes': correct_attributes,
        'correct_primary_keys': correct_primary_keys,
        'extra_entity': extra_entities,
        'correct_weak_entity': correct_weak_entities,
        'correct_relationship_entity': correct_relationship_entities,
        'correct_cardinality': correct_cardinality,
        'extra_relationship': extra_relationship,
        # new added
        # "correct_cardinality_text": correct_cardinality_text,
        }

    # Dictionary of default values in case of invalid input
    # VALID INPUTS: int/floats between 0 (exclusive) and 1 (exclusive)

    defaults = {
        'correct_entity_name': 0.2,
        'correct_attributes': 0.1,
        'correct_primary_keys': 0.2,
        'extra_entity': 0.25,
        'correct_weak_entity': 0.5,
        'correct_relationship_entity': 0.5,
        'correct_cardinality': 0.25,
        'extra_relationship': 0.25,
        }

    keys = marking_criteria.keys()
    for key in keys:
        value = marking_criteria[key]

        if isinstance(value, int) or isinstance(value, float):
            if value > 0 and value < 1:
                continue

        marking_criteria[key] = defaults[key]

    return marking_criteria


def convert(text):
    er_dict = {'entities': [], 'relationships': []}

    def parse_relationship(r_line):
        entities = re.findall(r'\[(.*?)\]', r_line)
        rel = re.search(r'\](.*?)\[', r_line)
        cardinalities = [x.strip() for x in rel.group(1).split('-')]
        entities_sorted = entities.copy()
        entities_sorted.sort()
        if entities_sorted[0] != entities_sorted[1]:
            relationship = {'entities': entities_sorted,
                            entities[0]: cardinalities[0],
                            entities[1]: cardinalities[1]}
        else:
            relationship = {'entities': entities_sorted,
                            entities[0]: [cardinalities[0],
                            cardinalities[1]]}
        er_dict['relationships'].append(relationship)

    def parse_entity(e_line):
        attributes = []
        primary_key = []
        partial_primary_keys = []
        e_line = re.search(r'\[(.*?)\]', e_line)
        try:
            split_line = e_line.group(1).split('|')
        except AttributeError:
            split_line = e_line.split('|')
        entity_name = split_line[0]
        if len(split_line) > 1:
            attributes = [x.strip() for x in split_line[1].split(';')]
            for (i, att) in enumerate(attributes):
                if '{PK}' in att:
                    attributes[i] = att.strip(' {PK}')
                    primary_key.append(attributes[i])
                if '{PPK}' in att:
                    attributes[i] = att.strip(' {PPK}')
                    partial_primary_keys.append(attributes[i])

            # sorting of the lists here to avoid doing it during marking but could move

            attributes.sort()
            primary_key.sort()
            partial_primary_keys.sort()
        entity = {
            'entity_name': entity_name,
            'primary_key': primary_key,
            'partial_primary_key': partial_primary_keys,
            'attributes': attributes,
            }
        er_dict['entities'].append(entity)

    def parse_line(t_line):
        index = t_line.find('-')
        if index == -1:
            parse_entity(t_line)
        else:
            parse_relationship(t_line)

    for line in text.splitlines():
        if line != '':
            parse_line(line)

    def sort_on_entities(e):
        return e['entities'][0]

    er_dict['relationships'].sort(key=sort_on_entities)
    return er_dict


def mark_answer(question, answers, stu_answer):
    student_answer = convert(stu_answer)
    global maximum_grade, marking_criteria
    maximum_grade = MAXIMUM_GRADE

    # try:
    #    question["other_marking_criteria"] = question["other_marking_criteria"].strip()
    #    if question["other_marking_criteria"][0] != '{' and question["other_marking_criteria"][-1] != '}':
    #        question["other_marking_criteria"] = '{ ' + \
    #            question["other_marking_criteria"] + ' }'
    #    other_marking_criteria = json.loads(question["other_marking_criteria"])
    #    for key in other_marking_criteria:
    #        if key in marking_criteria:
    #            marking_criteria[key] = other_marking_criteria[key]
    # except Exception as inst:
    #    print(inst)

    top_mark = -1
    top_result = dict()
    for nomnoml_answer in answers:
        answer = convert(nomnoml_answer['answer'])
        result = mark(answer, student_answer)
        if top_mark < result['mark']:
            top_mark = result['mark']
            top_result = result
    return top_result


def check_sp_char(stu_card, ans_card):
    if ans_card == '*' and (stu_card == '0..*' or stu_card == '1..*'):
        stu_card = '*'
    elif ans_card == '0@1' and (stu_card == '0..1' or stu_card == '1..1'
                                ):
        stu_card = '0@1'
    return stu_card


def mark(correct_answer, student_answer):
    global maximum_grade
    maximum_grade = MAXIMUM_GRADE

    # TOTAL MARKS VARIABLES

    entity_name_marks = 0
    entity_attribute_marks = 0
    entity_primary_key_marks = 0
    weak_entity_key_marks = 0
    relationship_entity_marks = 0
    relationship_cardinality_marks = 0
    # relationship_cardinality_text_marks = 0

    # STUDENT ANSWER VARIABLES

    student_entity_names_mark = 0
    student_attributes_mark = 0
    student_primary_keys_mark = 0
    student_weak_entities_mark = 0
    student_relationship_entities_mark = 0
    student_relationship_cardinalities_mark = 0
    # student_relationship_cardinalities_text_mark = 0

    student_answer_copy = copy.deepcopy(student_answer)
    correct_answer_copy = copy.deepcopy(correct_answer)

    marker_feedback = ''

    # calculate the total marks for the question

    for answer_entity in correct_answer['entities']:
        entity_name_marks += marking_criteria['correct_entity_name']
        entity_attribute_marks += marking_criteria['correct_attributes']
        entity_primary_key_marks += \
            marking_criteria['correct_primary_keys']
        if not answer_entity['primary_key']:
            weak_entity_key_marks += \
                marking_criteria['correct_weak_entity']
    for relationship in correct_answer['relationships']:
        relationship_entity_marks += \
            marking_criteria['correct_relationship_entity']
        relationship_cardinality_marks += \
            marking_criteria['correct_cardinality'] * 2
        # relationship_cardinality_text_marks += \
        #     marking_criteria["correct_cardinality_text"]
    entity_marks = entity_name_marks + entity_attribute_marks \
        + entity_primary_key_marks + weak_entity_key_marks
    # relationship_marks = relationship_entity_marks \
    #     + relationship_cardinality_marks+ relationship_cardinality_text_marks
    relationship_marks = relationship_entity_marks \
        + relationship_cardinality_marks
    total_marks = entity_marks + relationship_marks

    # marking entities

    for answer_entity in correct_answer['entities']:
        for (i, stu_entity) in enumerate(student_answer_copy['entities'
                ]):
            if stu_entity['entity_name'] == answer_entity['entity_name'
                    ]:
                correct_answer_copy['entities'].remove(answer_entity)
                student_entity_names_mark += \
                    marking_criteria['correct_entity_name']
                if stu_entity['attributes'] \
                    == answer_entity['attributes']:
                    student_attributes_mark += \
                        marking_criteria['correct_attributes']
                else:
                    marker_feedback += 'Incorrect attributes on the ' \
                        + stu_entity['entity_name'] + ' entity\n'
                    marker_feedback += 'Student: ' \
                        + ', '.join(stu_entity['attributes']) + '\n'
                    marker_feedback += 'Correct: ' \
                        + ', '.join(answer_entity['attributes']) \
                        + '''

'''
                if stu_entity['primary_key'] \
                    == answer_entity['primary_key']:
                    student_primary_keys_mark += \
                        marking_criteria['correct_primary_keys']
                else:
                    marker_feedback += 'Incorrect primary key on the ' \
                        + stu_entity['entity_name'] + ' entity\n'
                    marker_feedback += 'Student: ' \
                        + ', '.join(stu_entity['primary_key']) + '\n'
                    marker_feedback += 'Correct: ' \
                        + ', '.join(answer_entity['primary_key']) \
                        + '''

'''
                if not answer_entity['primary_key']:
                    if not stu_entity['primary_key'] \
                        and stu_entity['partial_primary_key'] \
                        == answer_entity['partial_primary_key']:
                        student_weak_entities_mark += \
                            marking_criteria['correct_weak_entity']
                    else:
                        marker_feedback += \
                            'Incorrect partial primary key on the ' \
                            + stu_entity['entity_name'] + ' entity\n'
                        marker_feedback += 'Student: ' \
                            + ', '.join(stu_entity['partial_primary_key'
                                ]) + '\n'
                        marker_feedback += 'Correct: ' \
                            + ', '.join(answer_entity['partial_primary_key'
                                ]) + '''

'''

                # Probably not a good idea

                del student_answer_copy['entities'][i]

    # Dock marks for extra entities

    student_extra_entities_mark = 0 - marking_criteria['extra_entity'] \
        * len(student_answer_copy['entities'])

    if len(student_answer_copy['entities']) > 0:
        s = ', '.join([str(item['entity_name']) for item in
                      student_answer_copy['entities']])
        marker_feedback += 'Extra entities: ' + s + '''

'''
    if len(correct_answer_copy['entities']) > 0:
        s = ', '.join([str(item['entity_name']) for item in
                      correct_answer_copy['entities']])
        marker_feedback += 'Missed entities: ' + s + '''

'''

    student_entities_mark = student_entity_names_mark \
        + student_attributes_mark + student_primary_keys_mark \
        + student_weak_entities_mark + student_extra_entities_mark

    # marking relationships
    # if the entire relationship is correct

    correct_answer_ = copy.deepcopy(correct_answer_copy)
    for answer_rel in correct_answer_['relationships']:
        for (i, stu_rel) in \
            enumerate(student_answer_copy['relationships']):
            if stu_rel['entities'] == answer_rel['entities']:
                # global stu_cardinality_text
                # global ans_cardinality_text
                # stu_cardinality_text= ""
                # ans_cardinality_text = ""
                if answer_rel['entities'][0] == answer_rel['entities'
                        ][1]:
                    ans_cardinality_a = answer_rel[stu_rel['entities'
                            ][0]][0]
                    stu_cardinality_a = \
                        check_sp_char(stu_rel[stu_rel['entities'
                            ][0]][0], ans_cardinality_a)
                    ans_cardinality_b = answer_rel[stu_rel['entities'
                            ][0]][1]
                    stu_cardinality_b = \
                        check_sp_char(stu_rel[stu_rel['entities'
                            ][0]][1], ans_cardinality_b)
                    # if 'cardinality_text_variable' in answer_rel:
                    #     ans_cardinality_text = answer_rel['cardinality_text_variable']
                    # if 'cardinality_text_variable' in stu_rel:
                    #     stu_cardinality_text = stu_rel['cardinality_text_variable']
                else:
                    ans_cardinality_a = answer_rel[stu_rel['entities'
                            ][0]]
                    stu_cardinality_a = \
                        check_sp_char(stu_rel[stu_rel['entities'][0]],
                            ans_cardinality_a)
                    ans_cardinality_b = answer_rel[stu_rel['entities'
                            ][1]]
                    stu_cardinality_b = \
                        check_sp_char(stu_rel[stu_rel['entities'][1]],
                            ans_cardinality_b)
                    # if 'cardinality_text_variable' in answer_rel:
                    #     ans_cardinality_text = answer_rel['cardinality_text_variable']
                    # if 'cardinality_text_variable' in stu_rel:
                    #     stu_cardinality_text = stu_rel['cardinality_text_variable']

                # if ((stu_cardinality_a == ans_cardinality_a and  # exact match
                #      stu_cardinality_b == ans_cardinality_b and
                #     stu_cardinality_text == ans_cardinality_text ) or
                #     (answer_rel['entities'][0] == answer_rel['entities'][1] and  # self relationship
                #      (stu_cardinality_a == ans_cardinality_b and
                #       stu_cardinality_b == ans_cardinality_a and
                #       stu_cardinality_text == ans_cardinality_text))):
                if stu_cardinality_a == ans_cardinality_a \
                    and stu_cardinality_b == ans_cardinality_b \
                    or answer_rel['entities'][0] \
                    == answer_rel['entities'][1] and stu_cardinality_a \
                    == ans_cardinality_b and stu_cardinality_b \
                    == ans_cardinality_a:  # exact match
                                           # self relationship
                    correct_answer_copy['relationships'
                            ].remove(answer_rel)
                    student_relationship_entities_mark += \
                        marking_criteria['correct_relationship_entity']
                    student_relationship_cardinalities_mark += \
                        marking_criteria['correct_cardinality'] * 2
                    # student_relationship_cardinalities_mark += (marking_criteria["correct_cardinality"] * 2)
                    # if stu_cardinality_text != "":
                    #     student_relationship_cardinalities_text_mark += marking_criteria["correct_cardinality_text"]
                    # else:
                    #    student_relationship_cardinalities_text_mark =0

                    # Probably not a good idea

                    del student_answer_copy['relationships'][i]

    # if one cardinality of the relationship is correct

    correct_answer_ = copy.deepcopy(correct_answer_copy)
    for answer_rel in correct_answer_['relationships']:
        for (i, stu_rel) in \
            enumerate(student_answer_copy['relationships']):
            if stu_rel['entities'] == answer_rel['entities']:
                if answer_rel['entities'][0] == answer_rel['entities'
                        ][1]:
                    ans_cardinality_a = answer_rel[stu_rel['entities'
                            ][0]][0]
                    stu_cardinality_a = \
                        check_sp_char(stu_rel[stu_rel['entities'
                            ][0]][0], ans_cardinality_a)
                    ans_cardinality_b = answer_rel[stu_rel['entities'
                            ][0]][1]
                    stu_cardinality_b = \
                        check_sp_char(stu_rel[stu_rel['entities'
                            ][0]][1], ans_cardinality_b)
                    # if 'cardinality_text_variable' in answer_rel:
                    #     ans_cardinality_text = answer_rel['cardinality_text_variable']
                    # if 'cardinality_text_variable' in stu_rel:
                    #     stu_cardinality_text = stu_rel['cardinality_text_variable']
                else:
                    ans_cardinality_a = answer_rel[stu_rel['entities'
                            ][0]]
                    stu_cardinality_a = \
                        check_sp_char(stu_rel[stu_rel['entities'][0]],
                            ans_cardinality_a)
                    ans_cardinality_b = answer_rel[stu_rel['entities'
                            ][1]]
                    stu_cardinality_b = \
                        check_sp_char(stu_rel[stu_rel['entities'][1]],
                            ans_cardinality_b)
                    # if 'cardinality_text_variable' in answer_rel:
                    #     ans_cardinality_text = answer_rel['cardinality_text_variable']
                    # if 'cardinality_text_variable' in stu_rel:
                    #     stu_cardinality_text = stu_rel['cardinality_text_variable']

                # if ((stu_cardinality_a == ans_cardinality_a or
                #      stu_cardinality_b == ans_cardinality_b or
                #     stu_cardinality_text == ans_cardinality_text ) or
                #     (answer_rel['entities'][0] == answer_rel['entities'][1] and  # self relationship
                #      (stu_cardinality_a == ans_cardinality_b or
                #       stu_cardinality_b == ans_cardinality_a or
                #       stu_cardinality_text == ans_cardinality_text))):# one cardinality
                #                                        # self relationship one cardinality

                if stu_cardinality_a == ans_cardinality_a \
                    or stu_cardinality_b == ans_cardinality_b \
                    or answer_rel['entities'][0] \
                    == answer_rel['entities'][1] and (stu_cardinality_a
                        == ans_cardinality_b or stu_cardinality_b
                        == ans_cardinality_a):  # one cardinality
                                                # self relationship one cardinality
                    correct_answer_copy['relationships'
                            ].remove(answer_rel)
                    student_relationship_entities_mark += \
                        marking_criteria['correct_relationship_entity']
                    student_relationship_cardinalities_mark += \
                        marking_criteria['correct_cardinality']
                    # if stu_cardinality_text != "":
                    #     student_relationship_cardinalities_text_mark += marking_criteria["correct_cardinality_text"]
                    # else:
                    #     student_relationship_cardinalities_text_mark=0
                    marker_feedback += 'Incorrect cardinality on the ' \
                        + str(stu_rel['entities']) + ' relationship\n'
                    # marker_feedback += 'Student: [' \
                    #     + str(stu_rel['entities'][0]) + '] ' \
                    #     + stu_cardinality_a + ' - ' + stu_cardinality_b \
                    #     + ' [' + str(stu_rel['entities'][1]) + ']'\
                    #     + ' : ' +  stu_cardinality_text +'\n'
                    # marker_feedback += 'Correct: [' \
                    #     + str(answer_rel['entities'][0]) + '] ' \
                    #     + ans_cardinality_a + ' - ' + ans_cardinality_b \
                    #     + ' [' + str(answer_rel['entities'][1]) \
                    #     + ''']''' +' : ' +  ans_cardinality_text
                    marker_feedback += 'Student: [' \
                        + str(stu_rel['entities'][0]) + '] ' \
                        + stu_cardinality_a + ' - ' + stu_cardinality_b \
                        + ' [' + str(stu_rel['entities'][1]) + ']\n'
                    marker_feedback += 'Correct: [' \
                        + str(answer_rel['entities'][0]) + '] ' \
                        + ans_cardinality_a + ' - ' + ans_cardinality_b \
                        + ' [' + str(answer_rel['entities'][1]) \
                        + ''']

'''

                    # Probably not a good idea

                    del student_answer_copy['relationships'][i]

    # if just the entities of the relationship is correct

    correct_answer_ = copy.deepcopy(correct_answer_copy)
    for answer_rel in correct_answer_['relationships']:
        for (i, stu_rel) in \
            enumerate(student_answer_copy['relationships']):
            if stu_rel['entities'] == answer_rel['entities']:
                if answer_rel['entities'][0] == answer_rel['entities'
                        ][1]:
                    ans_cardinality_a = answer_rel[stu_rel['entities'
                            ][0]][0]
                    stu_cardinality_a = \
                        check_sp_char(stu_rel[stu_rel['entities'
                            ][0]][0], ans_cardinality_a)
                    ans_cardinality_b = answer_rel[stu_rel['entities'
                            ][0]][1]
                    stu_cardinality_b = \
                        check_sp_char(stu_rel[stu_rel['entities'
                            ][0]][1], ans_cardinality_b)
                    # if 'cardinality_text_variable' in answer_rel:
                    #     ans_cardinality_text = answer_rel['cardinality_text_variable']
                    # if 'cardinality_text_variable' in stu_rel:
                    #     stu_cardinality_text = stu_rel['cardinality_text_variable']
                else:
                    ans_cardinality_a = answer_rel[stu_rel['entities'
                            ][0]]
                    stu_cardinality_a = \
                        check_sp_char(stu_rel[stu_rel['entities'][0]],
                            ans_cardinality_a)
                    ans_cardinality_b = answer_rel[stu_rel['entities'
                            ][1]]
                    stu_cardinality_b = \
                        check_sp_char(stu_rel[stu_rel['entities'][1]],
                            ans_cardinality_b)
                    # if 'cardinality_text_variable' in answer_rel:
                    #     ans_cardinality_text = answer_rel['cardinality_text_variable']
                    # if 'cardinality_text_variable' in stu_rel:
                    #     stu_cardinality_text = stu_rel['cardinality_text_variable']
                correct_answer_copy['relationships'].remove(answer_rel)
                student_relationship_entities_mark += \
                    marking_criteria['correct_relationship_entity']
                marker_feedback += 'Incorrect cardinalities on the ' \
                    + str(stu_rel['entities']) + ' relationship\n'
                # marker_feedback += 'Student: [' + str(stu_rel['entities'
                #         ][0]) + '] ' + stu_cardinality_a + ' - ' \
                #     + stu_cardinality_b + ' [' + str(stu_rel['entities'
                #         ][1]) + ']' +' : ' + stu_cardinality_text +'\n'
                # marker_feedback += 'Correct: [' \
                #     + str(answer_rel['entities'][0]) + '] ' \
                #     + ans_cardinality_a + ' - ' + ans_cardinality_b \
                #     + ' [' + str(answer_rel['entities'][1]) \
                #     + ''']''' + ' : ' + ans_cardinality_text
                marker_feedback += 'Student: [' + str(stu_rel['entities'
                        ][0]) + '] ' + stu_cardinality_a + ' - ' \
                    + stu_cardinality_b + ' [' + str(stu_rel['entities'
                        ][1]) + ']\n'
                marker_feedback += 'Correct: [' \
                    + str(answer_rel['entities'][0]) + '] ' \
                    + ans_cardinality_a + ' - ' + ans_cardinality_b \
                    + ' [' + str(answer_rel['entities'][1]) \
                    + ''']

'''

                # Probably not a good idea

                del student_answer_copy['relationships'][i]

    # Dock marks for extra relationships

    student_extra_relationships_mark = 0 \
        - marking_criteria['extra_relationship'] \
        * len(student_answer_copy['relationships'])

    if len(student_answer_copy['relationships']) > 0:
        s = ', '.join([str(item['entities']) for item in
                      student_answer_copy['relationships']])
        marker_feedback += 'Extra relationships: ' + s + '''

'''
    if len(correct_answer_copy['relationships']) > 0:
        s = ', '.join([str(item['entities']) for item in
                      correct_answer_copy['relationships']])
        marker_feedback += 'Missed relationships: ' + s + '''

'''

    student_relationships_mark = student_relationship_entities_mark \
        + student_relationship_cardinalities_mark \
        + student_extra_relationships_mark

    student_total_marks = student_entities_mark \
        + student_relationships_mark

    if student_total_marks < 0:
        student_total_marks = 0

    # scale marks with question maximum grade

    scaled_student_total_marks = student_total_marks / total_marks \
        * maximum_grade

    feedback = 'Entity name marks: ' \
        + str(round(student_entity_names_mark, 2)) + '/' \
        + str(round(entity_name_marks, 2)) + '\n' \
        + 'Entity attribute marks: ' \
        + str(round(student_attributes_mark, 2)) + '/' \
        + str(round(entity_attribute_marks, 2)) + '\n' \
        + 'Entity primary key marks: ' \
        + str(round(student_primary_keys_mark, 2)) + '/' \
        + str(round(entity_primary_key_marks, 2)) + '\n' \
        + 'Weak entity key marks: ' \
        + str(round(student_weak_entities_mark, 2)) + '/' \
        + str(round(weak_entity_key_marks, 2)) + '\n' \
        + 'Extra entities: ' + str(round(student_extra_entities_mark,
                                   2)) + '\n' + 'Total entity marks: ' \
        + str(round(student_entities_mark, 2)) + '/' \
        + str(round(entity_marks, 2)) + '\n' \
        + 'Relationship entity marks: ' \
        + str(round(student_relationship_entities_mark, 2)) + '/' \
        + str(round(relationship_entity_marks, 2)) + '\n' \
        + 'Relationship cardinalities marks: ' \
        + str(round(student_relationship_cardinalities_mark, 2)) + '/' \
        + str(round(relationship_cardinality_marks, 2)) + '\n' \
        + 'Extra relationships: ' \
        + str(student_extra_relationships_mark) + '\n' \
        + 'Total relationship marks: ' \
        + str(round(student_relationships_mark, 2)) + '/' \
        + str(round(relationship_marks, 2)) + '\n' + 'Total marks: ' \
        + str(round(student_total_marks, 2)) + '/' \
        + str(round(total_marks, 2)) + '\n' + 'Total scaled marks: ' \
        + str(round(scaled_student_total_marks, 2)) + '/' \
        + str(round(maximum_grade, 2)) + '\n'

    result = {
        'mark': round(scaled_student_total_marks, 2),
        'total': maximum_grade,
        'feedback': feedback,
        'marker_feedback': marker_feedback,
        }
    return result
#  place it below 656
# + 'Relationship cardinalities text marks: ' \
        # + str(round(student_relationship_cardinalities_text_mark, 2)) + '/'\
        # + str(round(relationship_cardinality_text_marks, 2)) + '\n'\


a2 = '''[Fish]
[Species]
[Tank]
[Fish] - [Species]'''
a1 = \
    '''[Tank|number;name;volume]
[Fish|id;name;color]
[Species|id;name;preferredFood]
[Color]
[Color] - [Fish]
[Species] - [Fish]'''
a3 = '''[Tank]
[Fish]
[Species]
[Event]
[Tank]0..1 - 0..*[Fish]'''
a4 = \
    '''[Tank]
[Fish]
[Tank]0..1 - 0..*[Fish]
[Fish]0..* - 1..*[Fish]'''
a5 = \
    '''[Tank|number {PK};name;volume;color]
[Fish|id {PK};name;color;weight]
[Species|id {PK};name;preferredFood]
[Event|date {PPK};note]
[Tank]1..1 - 0..*[Fish]
[Fish]1..* - 1..1[Species]
[Fish]1..1 - 0..*[Event]
[Fish]0..* - 1..*[Fish]
[Fish]1..* - 0..*[Event]'''

question_template = {
    'id': 6,
    'title': 'fishstore',
    'created_by': 1,
    'question_template': 1,
    'maximum_grade': MAXIMUM_GRADE,
    'other_marking_criteria': {
        'correct_entity_name': correct_entity_name,
        'correct_attributes': correct_attributes,
        'correct_primary_keys': correct_primary_keys,
        'extra_entity': extra_entities,
        'correct_weak_entity': correct_weak_entities,
        'correct_relationship_entity': correct_relationship_entities,
        'correct_cardinality': correct_cardinality,
        'extra_relationship': extra_relationship,
        # "correct_cardinality_text": correct_cardinality_text,
        },
    'custom_css': '',
    'question': '''Construct a database design in UML for a fish store where:

A fish store maintains a number of [aquaria (tanks)](tank), each with a [number](number), [name](name), [volume](volume) and [color](color).
Each [tank](tank) contains a number of [fish](fish), each with an [id](id), [name](name), [color](color), and [weight](weight).
Each [fish](fish) is of a particular [species](species), which has a [id](id), [name](name), and [preferred food](preferredFood).
Each individual [fish](fish) has a number of [events](event) in its life, involving a [date](date) and a [note](note) relating to the event.
''',
    'answers': [],
    }


def grade_question(data):
    """This function's purpose is that when prairieLearn calls the grade function for a question, certain parameters in
    the data object will get modified. Parameters are stored in data['params'] so first the correct answer that was
    stored data['params']['answer'] will be used to compare the users answer for grading. Once grading function is
    complete grading information such as grade will be stored in data['params']['score'], question feedback will be
    stored in data['params']['feedback'], and detailed marker feedback will be stored in
    data['params']['marker_feedback']. All of this information will be used by PrarieLearn for grading and giving the
    feedback to the user.



    :param data: prairieLearn data Object
    :type data: Object
    :return: return the modified prairieLearn data Object
    """
    # set template question and answers

    question_template['answers'] = data['params']['answer']
    question_template['question'] = data['params']['question_data']

    # grab required attributes of question

    question = question_template
    potential_answers = question['answers']

    # save student response and grade

    student_answer = data['submitted_answers'].get('c', '')
    data['params']['oldAnswer'] = student_answer
    results = mark_answer(question, potential_answers, student_answer)
    data['params']['score'] = results['mark'] / results['total']
    data['params']['feedback'] = results['feedback']
    data['params']['marker_feedback'] = results['marker_feedback']

    return data

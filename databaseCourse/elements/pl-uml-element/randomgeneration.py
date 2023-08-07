import random
import sys

from gibberish import Gibberish

# ENTITY PROPERTIES
MIN_STRONG_ENTITY = 3
MAX_STRONG_ENTITY = 4

MIN_WEAK_ENTITY = 1
MAX_WEAK_ENTITY = 1

MIN_11_RELATIONSHIP = 1
MAX_11_RELATIONSHIP = 2

MIN_1N_RELATIONSHIP = 2
MAX_1N_RELATIONSHIP = 4

MIN_MN_RELATIONSHIP = 1
MAX_MN_RELATIONSHIP = 1


def generate_random(data):
    def generate_seed():
        return random.randrange(sys.maxsize)

    gib = Gibberish()

    def generate_question(seed_value):

        # Setup random seed
        random.seed(seed_value)

        # Create a random entity
        def buildEntity(name, identifyingEntity):
            key = []
            ppk = []
            attr = []
            minattr = 1
            maxattr = 3

            if identifyingEntity == None:
                # Generate key fields
                val = random.random()
                if val <= 0.8:
                    numkey = 1
                else:
                    numkey = 2

                for j in range(0, numkey):
                    # key.append(entityChar+str(j+1))
                    attrName = gib.generate_word()
                    key.append(attrName)
            else:
                # Weak entity
                maxattr = 2
                if identifyingEntity != None:
                    numkey = 1
                else:
                    val = random.random()
                    if val <= 0.5:
                        numkey = 0
                        minattr = 0
                    elif val <= 0.9:
                        numkey = 1
                    else:
                        numkey = 2

                for j in range(0, numkey):
                    # ppk.append(entityChar+str(j+1))
                    attrName = gib.generate_word()
                    ppk.append(attrName)

            numattr = random.randint(minattr, maxattr)
            for j in range(0, numattr):
                # attr.append(entityChar+str(numkey+j+1))
                attrName = gib.generate_word()
                attr.append(attrName)

            return [name, key, ppk, attr, identifyingEntity]

        def listToStr(lst, separator, appendText=''):
            st = ""
            if len(lst) == 0:
                return st

            st += str(lst[0]) + appendText
            for i in range(1, len(lst)):
                st += separator + str(lst[i]) + appendText
            return st

        def entityToText(entity):
            entityName = entity[0]
            key = entity[1]
            ppk = entity[2]
            attr = entity[3]
            identifyingEntity = entity[4]

            st = ""
            st += "[" + entityName + "](" + entityName + ")"
            if len(key) > 0:
                st += random.choice([" is identified by ", " has key "])
                markupKey = ['[{0}]({0})'.format(x) for x in key]
                st += listToStr(markupKey, ", ")
                st += random.choice([" and has attribute", " has field"])
            elif len(ppk) > 0:
                if type(identifyingEntity) is list:
                    identifyingEntity = identifyingEntity[0]
                st += random.choice([" is identified by its association with ", " exists dependent on "])
                st += "[" + identifyingEntity + "](" + identifyingEntity + ") and has identifying attribute "
                markupPPK = ['[{0}]({0})'.format(x) for x in ppk]
                st += listToStr(markupPPK, ", ")
                st += ". [" + entityName + "](" + entityName + ")"
                st += random.choice([" also has attribute", " has field"])

            if len(attr) > 1:
                st += "s "
            else:
                st += " "
            markupAttr = ['[{0}]({0})'.format(x) for x in attr]
            st += listToStr(markupAttr, ", ")
            st += "."

            return st

        def weakEntityToText(entity, card1, card2):
            entityName = entity[0]
            key = entity[1]
            ppk = entity[2]
            attr = entity[3]
            identifyingEntity = entity[4]

            if type(identifyingEntity) is list and len(identifyingEntity) >= 2:
                e1 = identifyingEntity[0]
                e2 = identifyingEntity[1]

            st = "There is a many-to-many relationship [" + entityName + "] between "
            st += "[" + e1 + "](" + e1 + ") and [" + e2 + "](" + e2 + ")"
            if len(attr) > 0:
                st += random.choice([" that has attributes ", " with properties "])
                markupAttr = ['[{0}]({0})'.format(x) for x in attr]
                st += listToStr(markupAttr, ", ") + "."
            else:
                st += "."

            if len(ppk) > 0:
                st += random.choice([" Instances are differentiated by ", " Identifying field are "])
                markupPPK = ['[{0}]({0})'.format(x) for x in ppk]
                st += listToStr(markupPPK, ", ")
                st += ". "

            return st

        def entityToAnswer(entity):
            entityName = entity[0]
            key = entity[1]
            ppk = entity[2]
            attr = entity[3]

            st = "["
            st += entityName
            st += "|"
            st += listToStr(key, ";", " {PK}")
            if len(key) > 0:
                st += ";"
            st += listToStr(ppk, ";", " {PPK}")
            if len(ppk) > 0:
                st += ";"
            st += listToStr(attr, ";")

            st += "]"
            return st

        def cardinalityToText(card):
            if card == "0..1" or card == "0@1":
                return random.choice([" may be related to at most one ", " has at most one connection with "])
            elif card == "1..1":
                return random.choice([" must be related to exactly one ", " is connected with one "])
            elif card == "0..*" or card == "*":
                return random.choice([" may be related to many ", " has multiple relationships with ",
                                      " has zero or more connections with "])
            elif card == "1..*":
                return random.choice(
                    [" must be related to at least one but possibly many ", "is associated with one or more "])

        def relationshipToText(r):
            e1 = r[0]
            e2 = r[1]
            card1 = r[2]
            card2 = r[3]
            attr = r[4]
            st = ""

            if e1 == e2:
                # Special case for recursive relationship
                st = "[" + e1 + "](" + e1 + ")" + random.choice(
                    [" has a recursive relationship with itself. ", " has a self-relationship. "])
                st += "[" + e1 + "](" + e1 + ")" + cardinalityToText(card2) + "[" + e2 + "](" + e2 + ")" + ", and "
                st += "[" + e2 + "](" + e2 + ")" + cardinalityToText(card1) + "[" + e1 + "](" + e1 + ")" + "."
            else:
                st = "[" + e1 + "](" + e1 + ")" + cardinalityToText(card2) + "[" + e2 + "](" + e2 + ")" + ", and "
                st += "[" + e2 + "](" + e2 + ")" + cardinalityToText(card1) + "[" + e1 + "](" + e1 + ")" + "."

            return st

        def relationshipToAnswer(r):
            e1 = r[0]
            e2 = r[1]
            card1 = r[2]
            card2 = r[3]
            attr = r[4]
            return "[" + e1 + "]" + card1 + " - " + card2 + "[" + e2 + "]"

        questionText = []
        questionAnswer = []

        # Create strong entities
        numEntity = random.randint(MIN_STRONG_ENTITY, MAX_STRONG_ENTITY)
        # print("Entities:",numEntity)
        entities = []
        entityNames = gib.generate_words(numEntity)

        for i in range(0, numEntity):
            # entityChar = chr(ord('a')+i)
            # entityName = entityChar.upper()
            entityName = entityNames[i].capitalize()
            entity = buildEntity(entityName, None)
            entities.append(entity)

            questionText.append(entityToText(entity))
            questionAnswer.append(entityToAnswer(entity))

        # Create weak entities (supports one identifying entity)
        numWeak = random.randint(MIN_WEAK_ENTITY, MAX_WEAK_ENTITY)
        # print("Weak entities:",numWeak)
        entityNames = gib.generate_words(numWeak)
        for i in range(0, numWeak):
            # entityChar = chr(ord('a')+i+numEntity)
            # entityName = entityChar.upper()
            entityName = entityNames[i].capitalize()
            entity = buildEntity(entityName, entities[random.randint(0, numEntity - 1)][0])
            entities.append(entity)

            questionText.append(entityToText(entity))
            questionAnswer.append(entityToAnswer(entity))

        # Create relationships
        relationships = {}
        relTypeMin = [MIN_11_RELATIONSHIP, MIN_1N_RELATIONSHIP, MIN_MN_RELATIONSHIP]  # 1-1, 1-N, M-N
        relTypeMax = [MAX_11_RELATIONSHIP, MAX_1N_RELATIONSHIP, MAX_MN_RELATIONSHIP]

        for j in range(0, 3):
            numrel = random.randint(relTypeMin[j], relTypeMax[j])

            attr = []
            # Generate a relationship
            val = random.random()
            if j == 0:
                # print("Num 1:1:",numrel)
                if val <= 0.4:
                    card1 = "0@1"
                    card2 = "0@1"
                elif val <= 0.6:
                    card1 = "1..1"
                    card2 = "0..1"
                elif val <= 0.8:
                    card1 = "0..1"
                    card2 = "1..1"
                elif val <= 0.9:
                    card1 = "1..1"
                    card2 = "0..1"
                else:
                    card1 = "1..1"
                    card2 = "1..1"
            elif j == 1:
                # print("Num 1:*:",numrel)
                if val <= 0.4:
                    card1 = "0@1"
                    card2 = "*"
                elif val <= 0.6:
                    card1 = "0..1"
                    card2 = "*"
                elif val <= 0.8:
                    card1 = "1..1"
                    card2 = "*"
                elif val <= 0.9:
                    card1 = "1..1"
                    card2 = "0..*"
                else:
                    card1 = "0..1"
                    card2 = "0..*"
            else:
                pass
                # print("Num *:*:",numrel)

            k = 0
            while k < numrel:
                e1 = entities[random.randint(0, len(entities) - 1)][0]
                e2 = entities[random.randint(0, len(entities) - 1)][0]

                # Check if relationship is present or not
                if e1 + "-" + e2 in relationships:
                    continue

                # Make recursive relationships possible but quite rare
                if e1 == e2 and random.random() <= 0.8:
                    continue
                k += 1

                if j == 2:
                    # Generate M-N relationship as a weak entity
                    # entityChar = chr(ord('a')+len(entities)+1)
                    # entityName = entityChar.upper()
                    entityName = gib.generate_word().capitalize()
                    entity = buildEntity(entityName, [e1, e2])

                    if len(entity[3]) == 0 and len(entity[2]) == 0:
                        # No attributes for M-N relationship. Do not need weak entity (but also correct)
                        questionText.append(weakEntityToText(entity, card1, card2))
                        relationships[e1 + "-" + e2] = [e1, e2, "0..*", "0..*", []]
                        rtext = relationshipToAnswer(relationships[e1 + "-" + e2])
                        questionAnswer.append(rtext)
                    else:
                        entities.append(entity)

                        questionAnswer.append(entityToAnswer(entity))

                        # Generate two identifying relationships with new entity
                        card1 = "1..1"
                        card2 = "0..*"
                        relationships[e1 + "-" + entityName] = [e1, entityName, card1, card2, attr]
                        rtext = relationshipToAnswer(relationships[e1 + "-" + entityName])
                        questionAnswer.append(rtext)

                        relationships[e2 + "-" + entityName] = [e2, entityName, card1, card2, attr]
                        rtext = relationshipToAnswer(relationships[e2 + "-" + entityName])
                        questionAnswer.append(rtext)

                        questionText.append(weakEntityToText(entity, card1, card2))
                else:
                    relationships[e1 + "-" + e2] = [e1, e2, card1, card2, attr]
                    rtext = relationshipToAnswer(relationships[e1 + "-" + e2])

                    questionAnswer.append(rtext)
                    questionText.append(relationshipToText(relationships[e1 + "-" + e2]))

        # print("\nQuestionText:\n"+ listToStr(questionText, "\n", ""))
        # print("\nQuestionAnswer:\n"+ listToStr(questionAnswer, "\n", ""))

        # Question text with more variation of statements and intermix relationships and entities
        # Idea: Add some relationships right where the entity is defined. Combine some sentences.
        altQuestionText = []
        todoRelationships = dict(relationships)

        for i1 in range(0, len(entities)):
            entity1 = entities[i1]
            etext = entityToText(entity1)
            e1 = entity1[0]
            # See if have a relationship with entity
            for i2 in range(0, i1 + 1):
                entity2 = entities[i2]
                e2 = entity2[0]
                if e1 + "-" + e2 in relationships:
                    # Add relationship text
                    rtext = relationshipToText(relationships[e1 + "-" + e2])
                    etext = etext + " " + rtext
                    del todoRelationships[e1 + "-" + e2]

            altQuestionText.append(etext)

        # Add remaining relationships
        for r in todoRelationships:
            altQuestionText.append(relationshipToText(todoRelationships[r]))

        # print("\nAltQuestionText:\n"+ listToStr(altQuestionText, "\n", ""))

        # Penalty type

        # 0 - restricting number of attempts
        # 1 - regression
        # 2 - prompt penalty type selection
        # 3 - assign penalty type randomly
        result = {
            "question": listToStr(altQuestionText, "\n", ""),
            "answer": listToStr(questionAnswer, "\n", ""),
            "maximum_attempts": 7,
            "penalty_type": 0
        }

        return result

    question_data = generate_question(generate_seed())
    # Put these two integers into data['params']
    # data['params']['result'] = question_data
    # data['params']['question_data'] = question_data['question']
    # data['params']['answer'] = question_data['answer']

    return question_data

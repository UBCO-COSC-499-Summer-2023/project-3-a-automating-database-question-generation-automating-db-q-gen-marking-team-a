import random
import sys


from gibberish import Gibberish
gib = Gibberish()  # initialize the "Gibberish" for the generation of words

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

default_value = {
    "MIN_STRONG_ENTITY": MIN_STRONG_ENTITY,
    "MAX_STRONG_ENTITY": MAX_STRONG_ENTITY,
    "MIN_WEAK_ENTITY": MIN_WEAK_ENTITY,
    "MAX_WEAK_ENTITY": MAX_WEAK_ENTITY,
    "MIN_11_RELATIONSHIP": MIN_11_RELATIONSHIP,
    "MAX_11_RELATIONSHIP": MAX_11_RELATIONSHIP,
    "MIN_1N_RELATIONSHIP": MIN_1N_RELATIONSHIP,
    "MAX_1N_RELATIONSHIP": MAX_1N_RELATIONSHIP,
    "MIN_MN_RELATIONSHIP": MIN_MN_RELATIONSHIP,
    "MAX_MN_RELATIONSHIP": MAX_MN_RELATIONSHIP,
}
# Setting Default Value

def setDefault_Value(min_strong_entity, max_strong_entity, min_weak_entity, max_weak_entity, min_11_relationship, max_11_relationship, min_1n_relationship, max_1n_relationship, min_mn_relationship, max_mn_relationship):
    """
    This function sets the default values of the entities and the relationships as global values.
    :return: the default values for relationships and entities
    :rtype: dictionary
    """
    global MIN_STRONG_ENTITY
    global MAX_STRONG_ENTITY
    global MIN_WEAK_ENTITY
    global MAX_WEAK_ENTITY
    global MIN_11_RELATIONSHIP
    global MAX_11_RELATIONSHIP
    global MIN_1N_RELATIONSHIP
    global MAX_1N_RELATIONSHIP
    global MIN_MN_RELATIONSHIP
    global MAX_MN_RELATIONSHIP

    MIN_STRONG_ENTITY = min_strong_entity
    MAX_STRONG_ENTITY = max_strong_entity
    MIN_WEAK_ENTITY = min_weak_entity
    MAX_WEAK_ENTITY = max_weak_entity
    MIN_11_RELATIONSHIP = min_11_relationship
    MAX_11_RELATIONSHIP = max_11_relationship
    MIN_1N_RELATIONSHIP = min_1n_relationship
    MAX_1N_RELATIONSHIP = max_1n_relationship
    MIN_MN_RELATIONSHIP = min_mn_relationship
    MAX_MN_RELATIONSHIP = max_mn_relationship


    global default_value
    default_value = {
    "MIN_STRONG_ENTITY": MIN_STRONG_ENTITY,
    "MAX_STRONG_ENTITY": MAX_STRONG_ENTITY,
    "MIN_WEAK_ENTITY": MIN_WEAK_ENTITY,
    "MAX_WEAK_ENTITY": MAX_WEAK_ENTITY,
    "MIN_11_RELATIONSHIP": MIN_11_RELATIONSHIP,
    "MAX_11_RELATIONSHIP": MAX_11_RELATIONSHIP,
    "MIN_1N_RELATIONSHIP": MIN_1N_RELATIONSHIP,
    "MAX_1N_RELATIONSHIP": MAX_1N_RELATIONSHIP,
    "MIN_MN_RELATIONSHIP": MIN_MN_RELATIONSHIP,
    "MAX_MN_RELATIONSHIP": MAX_MN_RELATIONSHIP,
    }

    return default_value

# for randomness
def generate_seed():
    """
    This method generates the seed that will be called by generate_question method
    :return: returns a random number within the maxsize.
    :rtype: integer
    """
    return random.randrange(sys.maxsize)


# generate entities
# identifyingEntity==None -> strong entities
# identifyingEntity!=None -> weak entities
def buildEntity(name, identifyingEntity, minattr=1, maxattr=3):
    """
    This method creates entities and its name, entity and attributes.
    :param name: name of entities
    :type name: string
    :param identifyingEntity: list for identified entities
    :type identifyingEntity: list
    :param minattr:the min number of how many attributes to be generated
    :type minattr: int
    :param maxattr:the max number of how many attributes to be generated
    :type maxattr: int
    :return: return the name of the entities, keys and ppks of the entity, attributes of the entity, entities being identified
    :rtype: list
    """
    key = []  # primary key (for strong entities)
    ppk = []  # partial primary key (for weak entites)
    attr = []  # attributes for entities
    # minattr = 1 # the min number of how many attributes to be generated
    # maxattr = 3 # the max number of how many attributes to be generated

    if identifyingEntity == None:
        # strong entites
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


# generate cardinality
# j = 0 -> 1-1, j = 1 -> 1-N, j = 2 -> M-N
def buildCardinality(j):
    """
    This method creates random cardinalities for the question.
    :param j: type of relation
    :type j: int
    :return: cardinality 1 and cardinality 2
    :rtype: string
    """
    val = random.random()
    # get card1, card2
    if j == 0:  # 1-1
        # print("Num 1:1:",numrel)
        card1 = "1..1"
        card2 = "1..1"
    elif j == 1:  # 1-N
        if val <= 0.5:
            # print("Num 1:*:",numrel)
            card1 = "1..1"
            card2 = "1..*"
        else:
            # print("Num *:1:",numrel)
            card1 = "1..*"
            card2 = "1..1"
    else:  # N-M
        # print("Num *:*:",numrel)
        card1 = "1..*"
        card2 = "1..*"
    #
    return card1, card2


# generate relationship
# e1, e2: entities
# card1, card2: cardinalities
def buildRelationship(e1, e2, j):
    """
    This method builds relationships between given two entities
    :param e1: entity 1
    :type e1: list
    :param e2: entity 2
    :type e2: list
    :param j: type of relation
    :type j: int
    :return: the attributes in a list
    :rtype: list
    """
    card1, card2 = buildCardinality(j)
    attr = []
    return [e1, e2, card1, card2, attr]


# list -> string
def listToStr(lst, separator, appendText=''):
    """
    This method transforms the lists to strings using for loop.
    :param lst: a list to be turned into a string
    :type lst: list
    :param separator: a separator for the list to be separated when turning into a string
    :type separator: string
    :param appendText: appended text
    :type appendText: string
    :return: the string turned from the list
    :rtype: string
    """
    st = ""
    if len(lst) == 0:
        return st

    st += str(lst[0]) + appendText
    for i in range(1, len(lst)):
        st += separator + str(lst[i]) + appendText
    return st


# entity -> detailed string
def entityToText(entity):
    """
    Transforms entities and its properties to string type.
    :param entity: the entity to be turned into a string
    :type entity: list
    :return: string turned from the entity
    :rtype: string
    """
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
        # if type(identifyingEntity) is list:
        #	identifyingEntity = identifyingEntity[0]
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


# entity -> concise string
def entityToAnswer(entity):
    """
    Using listToStr to change entities and their properties into answers in strings.
    :param entity: the entity that is to turn into a string answer
    :type entity: list
    :return: string answer
    :rtype: string
    """
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


# cardinality -> detailed string
# the relationship between 2 entities can be broken down to: E1 cardinality E2, E2 cardinality E1
# 1-1, 1-N, M-N
def cardinalityToText(card):
    """
    This method changes the type for cardinalities to strings by calling the random.choice function.
    :param card: cardinality
    :type card: string
    :return: the relationship
    :rtype: string
    """
    if card == "1..1":
        return random.choice([" is connected with one "])
    elif card == "1..*" or card == "*":
        return random.choice([" has multiple relationships with "])


# relationship -> detailed string
def relationshipToText(r):
    """
    This method changes relationships and its properties into string texts.
    :param r: relationship
    :type r: list
    :return:the relationship in text
    :rtype: string
    """
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


# relationship -> concise string
def relationshipToAnswer(r):
    """
    This method changes relationships and its properties into answers in strings.
    :param r:relationship
    :type r: list
    :return: a string of answer for relationship
    :rtype: string
    """
    e1 = r[0]
    e2 = r[1]
    card1 = r[2]
    card2 = r[3]
    attr = r[4]  # no use
    return "[" + e1 + "]" + card1 + " - " + card2 + "[" + e2 + "]"


# process to generate entities and relationships
def generate_question(seed_value, data):
    """
    This method generates questions and its properties.
    Properties includes the number of entities and relationships
    to be generated, setting up the random seed, creating
    lists for relating information, creating entities and relations.
    :type data: object
    :param seed_value: the value of the seed generated
    :type seed_value: int
    :param data: data
    :type data: object
    :return:
    :rtype:
    """
    # how many entities & relatioships to be generated
    data_default = default_value

    # Setup random seed
    random.seed(seed_value)
    # Create lists to store related info
    questionText = []
    questionAnswer = []

    # Create strong entities
    numEntity = random.randint(data_default["MIN_STRONG_ENTITY"], data_default["MAX_STRONG_ENTITY"])
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
    numWeak = random.randint(data_default["MIN_WEAK_ENTITY"], data_default["MAX_WEAK_ENTITY"])
    # print("Weak entities:",numWeak)
    entityNames = gib.generate_words(numWeak)
    for i in range(0, numWeak):
        # entityChar = chr(ord('a')+i+numEntity)
        # entityName = entityChar.upper()
        entityName = entityNames[i].capitalize()
        entity = buildEntity(entityName,
                             entities[random.randint(0, numEntity - 1)][0])  # choose one strong entity and use its name
        entities.append(entity)

        questionText.append(entityToText(entity))
        questionAnswer.append(entityToAnswer(entity))

    # Create relationships
    relationships = {}
    relTypeMin = [data_default["MIN_11_RELATIONSHIP"], data_default["MIN_1N_RELATIONSHIP"], data_default["MIN_MN_RELATIONSHIP"]]  # min: 1-1, 1-N, M-N
    relTypeMax = [data_default["MAX_11_RELATIONSHIP"], data_default["MAX_1N_RELATIONSHIP"], data_default["MAX_MN_RELATIONSHIP"]]  # max: 1-1, 1-N, M-N

    for j in range(0, 3):  # 3 is the length of relTypeMin & relTypeMax
        # determine how many relationships to be generated
        numrel = random.randint(relTypeMin[j], relTypeMax[j])

        # Generate a relationship
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

            relationships[e1 + "-" + e2] = buildRelationship(e1, e2, j)
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


# function package by calling above functions
def generate_random(data):
    """
    This method is to generate the random question when called.
    :param data: data
    :type data: Object
    :return: data of question
    :rtype: dict
    """
    data['params'] = {}
    data['params'] = default_value
    return generate_question(generate_seed(),data)

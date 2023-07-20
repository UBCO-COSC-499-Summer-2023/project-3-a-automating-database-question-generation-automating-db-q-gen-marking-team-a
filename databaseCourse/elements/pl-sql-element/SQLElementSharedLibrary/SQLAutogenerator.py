import random

# This allows DroneCI to see the RASQLib module
import sys
sys.path.append('/drone/src/databaseCourse/serverFilesCourse/')

from RASQLib import textDatabaseHandler as db
from RASQLib import noisyData as nd



# Automatically generates an SQL question based on the question's parameters
def autogenerate(data):
    
    # Gets question parameters
    # random = data['params']['html_params']['random']
    # maxGrade = data['params']['html_params']['maxGrade']
    # markerFeedback = data['params']['html_params']['markerFeedback']
    questionType = data['params']['html_params']['questionType']
    difficulty = data['params']['html_params']['difficulty']


    # Checks if the difficulty are valid
    if difficulty not in ['easy', 'medium', 'hard', None]:
        return None

    # Generates the appropriate question
    match questionType:
        case 'create':  generateCreate(data, difficulty)
        case 'insert': generateInsert(data, difficulty)
        case 'update': generateUpdate(data, difficulty)
        case 'delete': generateDelete(data, difficulty)
        case 'query': generateQuery(data, difficulty)

'''
    Begin create-style question
'''

# Generates a 'create' style SQL question
def generateCreate(data, difficulty):

    # Obtains question specific parameters
    columns, joins, tableClauses, queryClauses = getQuestionParameters(data)

    # Creates an appropriate table
    database = None
    match difficulty:
        case 'easy': database = db.Database(file=random.choice(['airport', 'airplane', 'product', 'customer']), random=False)
        case 'medium': database = db.Database(file=random.choice(['passenger', 'shipment']), random=False)
        case 'hard': database = db.Database(file=random.choice(['flight', 'shippedproduct']), random=False)
        case _: database = db.Database(columns=columns, joins=joins, clauses=tableClauses)

    # Grabs the primary table for easy referencing
    table = database.primaryTable



    # Creates a string to tell the student what they need
    # to do for the qestion
    questionString = f"Create a table named <b>{table.name}</b> with columns"

    # Adds a list of columns and units to the question string
    columnList = list(table.columns.keys())
    columnValues = list(table.columns.values())
    for i in range(len(columnList)):

        # Adds an 'and' at the start of the last iteration
        if i == len(columnList) - 1:
            questionString += ' and'
        
        # Adds the column name
        questionString += f" <b>{columnValues[i]['name']}</b>"



        # Handles the text for units
        match columnValues[i]['unit']:
            case 'INTEGER': questionString += ' (an integer)'
            case 'DECIMAL': questionString += f" (a decimal value with a total of {columnValues[i]['unitOther'].split(',')[0]} digits, {columnValues[i]['unitOther'].split(',')[1]} of which are after the decimal point)"
            case 'CHAR': questionString += f" (a string of exactly {columnValues[i]['unitOther']} characters)"
            case 'VARCHAR': questionString += f" (a string up to {columnValues[i]['unitOther']} characters)"
            case 'DATE': questionString += ' (DATE)'
            case 'DATETIME': questionString += ' (DATETIME)'
            case other: questionString += f" ({columnValues[i]['unit']})"
            
        # Mentions primary key, if necessary
        if columnValues[i]['isPrimary']:
            questionString += ' <em>that is a primary key</em>'

        # Mentions foreign key and its clauses, if necessary
        if columnValues[i]['references']:
            questionString += f" that references <b>{columnValues[i]['references']}</b>\'s <b>{columnValues[i]['foreignKey']}</b>"

            # Handles cascade
            if columnValues[i]['isOnUpdateCascade']:
                questionString += ' <em>that cascades on an update</em>'
            
            # Handles delete set null
            if columnValues[i]['isOnDeleteSetNull']:
                questionString += ' <em>that is set to null when deleted</em>'

        # Mentions other clauses, if necessary
        if columnValues[i]['isNotNull']:
            questionString += ' <em>that cannot be null</em>'
        
        if columnValues[i]['isUnique']:
            questionString += ' <em>where all values are unqiue</em>'

        # Adds a comma at the end of each iteration
        questionString += ', '


    # Remove the last comma and replace it with a period
    questionString = questionString[:-2] + '.'



    # Loads any tables this one references into the schema.
    # This DOES NOT load the primary table into data,
    # since that would give students the answer
    if database.referencedTables:
        for referencedTable in database.referencedTables:
            data['params']['db_initialize'] += f"{database.referencedTables[referencedTable].getSchema()}\n"

    # Places the question string into data
    data['params']['questionString'] = questionString

    # Places the solution into data
    data['correct_answers']['SQLEditor'] = createStatement(table)

# Returns the schema for the current table.
def createStatement(table):
    return table.getSchema()

'''
    End create-style question
'''



'''
    Begin insert-style question
'''

# Generates a 'insert' style SQL question
def generateInsert(data, difficulty):

    # Obtains question specific parameters
    columns, joins, tableClauses, queryClauses = getQuestionParameters(data)

    # Based on the difficulty, choose a random amount of columns
    # If no difficulty is specified, uses question parameters instead
    database = None
    match difficulty:
        case 'easy': database = db.Database(file=loadTrimmedTable(random.randint(3, 4), 0), columns=0)
        case 'medium': database = db.Database(file=loadTrimmedTable(random.randint(4, 6), 0), columns=0)
        case 'hard': database = db.Database(file=loadTrimmedTable(random.randint(5, 8), 0), columns=0)
        case _: database = db.Database(columns=columns, joins=joins, clauses=tableClauses)

    # Grabs the primary table for easy referencing
    table = database.primaryTable

    # Generates some data
    database.generateRows(random.randint(3, 7))



    # Obtains the row to be inserted by removed it
    # from the primary table's rows    
    row = [table.rows[key].pop() for key in table.columns.keys()]
    


    # Creates the question string
    questionString = f"Insert the following values into the <b>{table.name}</b> table:\n({str(row)[1:-1]})"

    # Loads the database
    database.loadDatabase(data)

    # Adds the question string
    data['params']['questionString'] = questionString

    # Creates the answer string
    data['correct_answers']['SQLEditor'] = insertStatement(table, row)

# Generates an insert statement based on the data
def insertStatement(table, row):
    return f"INSERT INTO {table.name} VALUES ({str(row)[1:-1]});\n"

'''
    End insert-style question
'''



'''
    Begin update-stype question
'''

def generateUpdate(data, difficulty):
    
    # Obtains question specific parameters
    columns, joins, tableClauses, queryClauses = getQuestionParameters(data)

    # Chooses a table to load based on quesiton difficulty
    database = None
    match difficulty:
        case 'easy': 
            database = db.Database(file=loadTrimmedTable(random.randint(3, 4)), columns=0, random=False)
            queryClauses['useConditional'] = False
            queryClauses['useSubquery'] = False

        case 'medium': 
            database = db.Database(file=loadTrimmedTable(random.randint(4, 6)), columns=0, random=False)
            queryClauses['useConditional'] = True
            queryClauses['useSubquery'] = False

        case 'hard': 
            database = db.Database(file=loadTrimmedTable(random.randint(5, 8)), columns=0, random=False)
            queryClauses['useConditional'] = False
            queryClauses['useSubquery'] = True
            return None # Not yet implemented; first requires quesryStatement() to be completed
        
        case _:
            database = db.Database(columns=columns, joins=joins, clauses=tableClauses)

    # Gets the primary table for easy referencing
    table = database.primaryTable



    # Checks if the parameters are valid
    nonCascadingForeignKeys = len([key for key in table.columns.keys() if table.columns[key]['references'] and not table.columns[key]['isOnUpdateCascade']])
    if columns - nonCascadingForeignKeys < queryClauses['useConditional']:
        print(f"UPDATE question cannot have more conditional clauses than foreign keys that do not cascade on update (was supplied with {queryClauses['useConditional']} conditionals and {nonCascadingForeignKeys} non-cascading foreign keys)")

    # Generates a bunch of rows
    database.generateRows(random.randint(6, 10))

    # Selects a random column to affect
    updateColumn = random.choice(list(table.columns.keys()))

    # Generates the updated valued
    updateValue = nd.generateNoisyData(table, updateColumn)[0]



    # If the quesiton should use a condition, set parameters
    conditionalValues = {}
    columnList = list(table.columns.keys())
    indexList = [i for i in range(len(list(table.rows.values())[0]))]
    for i in range(queryClauses['useConditional']):

        # Selects a random column to affect.
        # Cannot select a column that is both foreign and does not
        # update on cascade
        conditionalColumn = None
        while not conditionalColumn or table.columns[conditionalColumn]['references'] and not table.columns[conditionalColumn]['isOnUpdateCascade']:
            conditionalColumn = nd.popRandom(columnList)

        # Chooses a random value from the generated data to be updated
        randomValueIndex = nd.popRandom(indexList)

        # Grabs the randomly selected values
        conditionalValues[conditionalColumn] = table.rows[conditionalColumn][randomValueIndex]


    # Generates the question string
    questionString = f"From the table <b>{table.name}</b> and in the column <b>{updateColumn}</b>, change all values to be <b>{updateValue}</b>"

    # Adds the 'where' if necessary
    if queryClauses['useConditional'] or queryClauses['useSubquery']:
        questionString += ' where'

    # Adds conditionals to question string
    if queryClauses['useConditional']:

        for key in conditionalValues.keys():
            questionString += f" <b>{key}</b> equals <b>{conditionalValues[key]}</b>"
        
            # And the logical operator
            if queryClauses['useAndInsteadOfOr']:
                questionString += ' and'
            else:
                questionString += ' or'

    # Adds subquery to question string
    # TODO: this
    if queryClauses['useSubquery']:
        questionString += f""

    # Removes trailing 'or' if necessary
    if queryClauses['useConditional'] or queryClauses['useSubquery']:
        if queryClauses['useAndInsteadOfOr']:
            questionString = questionString[:-4]
        else:
            questionString = questionString[:-3]
    
    # Finishes the sentence
    questionString += "."

    # Loads data
    database.loadDatabase(data)

    # Sets the question string
    data['params']['questionString'] = questionString

    # Loads the correct answer
    data['correct_answers']['SQLEditor'] = updateStatement(table, updateColumn, updateValue, conditionalValues, queryClauses['useAndInsteadOfOr'])

# Creates an update statement
def updateStatement(table, updateColumn, updateValue, conditionalValues = None, useAnd = False, subquery = None):

    # Sets up the statement
    statement = f"UPDATE {table.name} SET {updateColumn} = '{updateValue}'"

    # Adds where if necessary
    if conditionalValues or subquery:
        statement += ' WHERE'

    # Includes the conditional if they exist
    if conditionalValues:
        for key in conditionalValues:
            statement += f" {key} = '{conditionalValues[key]}'"
        
            # And the logical operator
            if useAnd:
                statement += ' AND'
            else:
                statement += ' OR'

    # Removes trailing 'OR' if necessary
    if conditionalValues or subquery:
        if useAnd:
            statement = statement[:-4]
        else:
            statement = statement[:-3]
    
    # Add finishing touches and returns
    statement += ';\n'
    return statement

'''
    End update-style question
'''


'''
    Begin delete-style question
'''

def generateDelete(data, difficulty):
    
    # Obtains question specific parameters
    columns, joins, tableClauses, queryClauses = getQuestionParameters(data)

    # Chooses a table to load based on quesiton difficulty
    database = None
    match difficulty:
        case 'easy': 
            database = db.Database(file=loadTrimmedTable(random.randint(3, 4)), columns=0, random=False)
            queryClauses['useConditional'] = False
            queryClauses['useSubquery'] = False

        case 'medium': 
            database = db.Database(file=loadTrimmedTable(random.randint(4, 6)), columns=0, random=False)
            queryClauses['useConditional'] = True
            queryClauses['useSubquery'] = False

        case 'hard': 
            database = db.Database(file=loadTrimmedTable(random.randint(5, 8)), columns=0, random=False)
            queryClauses['useConditional'] = False
            queryClauses['useSubquery'] = True
            return None # Not yet implemented; first requires quesryStatement() to be completed
        
        case _:
            database = db.Database(columns=columns, joins=joins, clauses=tableClauses)

    # Gets the primary table for easy referencing
    table = database.primaryTable

    # Generates a bunch of bogus rows
    database.generateRows(random.randint(3, 7))


    
    # If the quesiton should use a condition, set parameters
    conditionalValues = {}
    columnList = list(table.columns.keys())
    indexList = [i for i in range(len(list(table.rows.values())[0]))]
    for i in range(queryClauses['useConditional']):

        # Selects a random column to affect.
        # Cannot select a column that is both foreign and is
        # not set to null on delete
        conditionalColumn = None
        while not conditionalColumn or table.columns[conditionalColumn]['references'] and not table.columns[conditionalColumn]['isOnDeleteSetNull']:
            conditionalColumn = nd.popRandom(columnList)

        # Chooses a random value from the generated data to be updated
        randomValueIndex = nd.popRandom(indexList)

        # Grabs the randomly selected values
        conditionalValues[conditionalColumn] = table.rows[conditionalColumn][randomValueIndex]



    # Generates the question string
    questionString = f"From the table <b>{table.name}</b>, delete all values"

    # Adds the 'where' if necessary
    if queryClauses['useConditional'] or queryClauses['useSubquery']:
        questionString += ' where'

    # Adds conditionals to question string
    if queryClauses['useConditional']:

        for key in conditionalValues.keys():
            questionString += f" <b>{key}</b> equals <b>{conditionalValues[key]}</b>"
        
            # And the logical operator
            if queryClauses['useAndInsteadOfOr']:
                questionString += ' and'
            else:
                questionString += ' or'

    # Adds subquery to question string
    # TODO: this
    if queryClauses['useSubquery']:
        questionString += f""

    # Removes trailing 'or' if necessary
    if queryClauses['useConditional'] or queryClauses['useSubquery']:
        if queryClauses['useAndInsteadOfOr']:
            questionString = questionString[:-4]
        else:
            questionString = questionString[:-3]
    
    # Finishes the sentence
    questionString += "."



    # Loads the database
    database.loadDatabase(data)

    # Sets the question string
    data['params']['questionString'] = questionString

    # Sets the correct answer
    data['correct_answers']['SQLEditor'] = deleteStatement(table, conditionalValues, queryClauses['useAndInsteadOfOr'], queryClauses['useSubquery'])

# Creates a delete statement
def deleteStatement(table, conditionalValues = None, useAnd = False, subquery = None):

    # Sets up the statement
    statement = f"DELETE FROM {table.name}"

    # Adds where if necessary
    if conditionalValues or subquery:
        statement += ' WHERE'

    # Includes the conditional if they exist
    if conditionalValues:
        for key in conditionalValues:
            statement += f" {key} = '{conditionalValues[key]}'"
        
            # And the logical operator
            if useAnd:
                statement += ' AND'
            else:
                statement += ' OR'

    # Removes trailing 'OR' if necessary
    if conditionalValues or subquery:
        if useAnd:
            statement = statement[:-4]
        else:
            statement = statement[:-3]
    
    # Add finishing touches and returns
    statement += ';\n'
    return statement

'''
    End delete-style question
'''


'''
    Begin query-style question
'''

# TODO
# Generate clauses
# Have proper conditionals
def generateQuery(data, difficulty):
    
    # Obtains question specific parameters
    columns, joins, tableClauses, queryClauses = getQuestionParameters(data)

    # Chooses a table to load based on quesiton difficulty
    database = None
    match difficulty:
        case 'easy': 
            database = db.Database(file=loadTrimmedTable(random.randint(3, 4)), columns=0, joins=0, random=False)
            clauses = {}

        case 'medium': 
            database = db.Database(file=loadTrimmedTable(random.randint(4, 6)), columns=0, joins=random.randint(1, 2), random=False)
            clauses = {}

        case 'hard': 
            database = db.Database(file=loadTrimmedTable(random.randint(5, 8)), columns=0, joins=random.randint(1, 2), random=False)
            clauses = {}
            clauses = random.randint(1, 3)
            return None # Not yet implemented; first requires queryStatement() to be completed
        
        case _:
            database = db.Database(columns=columns, joins=joins, clauses=tableClauses)

    # Gets the primary table for easy referencing
    table = database.primaryTable

    # Gets the referenced tables for easy referencing
    referenced = database.referencedTables

    # Generates a bunch of bogus rows
    database.generateRows(random.randint(3, 7))



    # keyMap maps the primary table's FKs to the other tables
    # keyMap = {
    #   $foreignKey: {
    #       'references': $foreignTableName
    #       'foreignKey': $columnReferenced
    #   }
    # }
    keyMap = table.getKeyMap()

    # Maps the foreign keys to tables
    # foreignKeyMap = {
    #   $columnName: table
    # }
    foreignKeyMap = {table.name: table}

    # Randomly chooses which tables are joined together
    for join in range(joins):

        # Chooses the foreign key randomly from the list
        foreignKey = random.choice(list(keyMap.keys()))

        # Pops the key out (ensures no repeated joins) and
        # adds it to the mapping
        foreignKeyMap[foreignKey] = referenced[keyMap.pop(foreignKey)['references']]



    # The columns that will be selected by the query
    # selectedColumns {
    #   $foreignKey: $column
    # }
    selectedColumns = {}

    # Chooses one column randomly from each joined table.
    # Ensures that at least one column per table joined is
    # in the query
    for key in foreignKeyMap:
        selectedColumns[key] = [random.choice(list(foreignKeyMap[key].columns.keys()))]

    # Adds more columns until there are the amount as
    # specified by the difficulty
    for i in range(len(list(table.columns)) - joins - 1):

        # Chooses a foreign key, aka chooses a table
        foreignKey = random.choice(list(foreignKeyMap.keys()))

        # Chooses unique column
        uniqueKey = None
        while not uniqueKey or uniqueKey in selectedColumns[foreignKey]:
            uniqueKey = random.choice(list(foreignKeyMap[foreignKey].columns.keys()))

        # Adds the column to the appropriate table's selected column
        selectedColumns[foreignKey].append(uniqueKey)



    # Generate a new keyMap since the last one was modified
    # through pop()
    keyMap = table.getKeyMap()

    # Adds the current table to the keyMap (for ease)
    keyMap[table.name] = {'references': table.name, 'foreignKey': None}



    # Creates the question string
    questionString = 'From the tables'

    # De-pluralizes the string if there are no joins
    if joins == 0:
        questionString = questionString[:-1]

    # Adds the tables to the string
    keyIndex = 0
    for key in foreignKeyMap:

        # Used to track when the 'and' needs to be added
        keyIndex += 1

        # Adds an 'and' if it's the last item and
        # there are more than one item
        if keyIndex == len(list(foreignKeyMap)) and joins > 0:
            questionString += ' and'

        questionString += f" <b>{keyMap[key]['references']}</b>,"
    
    # Removes the trailing comma and add the next bit of text
    questionString = questionString[:-1] + ' select the columns'

    # De-pluralizes the string if there is only one column
    if len(list(table.columns)) == 1:
        questionString = questionString[:-1]

    # Adds the columns to be selected
    keyIndex = 0
    for key in selectedColumns:

        # Used to keep track of the and
        columnIndex = 0
        keyIndex += 1

        # Specifies which table the column belongs to.
        # Also specifies the 'as' clause
        questionString += f" ({keyMap[key]['references']} as {keyMap[key]['references'][0:1].upper()})"

        # Adds the column to the string
        for column in selectedColumns[key]:
            columnIndex += 1

            # Adds an 'and' if it's the last item and
            # there are more than one item
            if columnIndex == len(list(selectedColumns[key])) and keyIndex == len(list(selectedColumns)) and len(list(table.columns)) > 1:
                questionString += ' and'
            
            questionString += f" <b>{column}</b>,"

    # Removes the trailing comma
    questionString = questionString[:-1] + '.'


    # Loads some rows
    database.generateRows(random.randint(3, 7))

    # Loads the database
    database.loadDatabase(data)

    # Adds the question string to data
    data['params']['questionString'] = questionString

    # Sets the correct answers
    # TODO: clauses (the '[]') is blank; make it not blank
    data['correct_answers']['SQLEditor'] = queryStatement(table, keyMap, foreignKeyMap, selectedColumns, [])

# Creates a delete statement
# TODO
#   Conditionals
#   Clauses
def queryStatement(table, keyMap, foreignKeyMap, selectedColumns, clauses):
    
    # Begins the query string
    queryString = 'SELECT'

    # Adds the columns to the query string
    # All columns use a '$table.' to specify
    for key in selectedColumns:
        for column in selectedColumns[key]:
            queryString += f" {keyMap[key]['references'][0:1].upper()}.{column},"
    
    # Removes trailing comma
    queryString = queryString[:-1] + ' FROM'

    # Adds the tables to be selected from
    for key in foreignKeyMap:
        queryString += f" {keyMap[key]['references']} AS {keyMap[key]['references'][0:1].upper()},"

    # Removes trailing comma
    queryString = queryString[:-1] + ' WHERE'



    # Specifies how the tables are joined together

    # Removes the primary table, since it is the holder of all
    # the foreign keys so we don't want to say "join table to self"
    foreignKeyMap.pop(table.name)

    if foreignKeyMap:
        for key in foreignKeyMap:
            queryString += f" {table.name[0:1].upper()}.{key} = {keyMap[key]['references'][0:1].upper()}.{keyMap[key]['foreignKey']} AND"

        # Removes the final 'AND'
        queryString = queryString[:-4]
    
    # Removes the WHERE clause if necessary
    if not clauses and not foreignKeyMap:
        queryString = queryString[:-6]



    # Returns, appending the finishing touches
    return queryString + ";\n"

'''
    End query-style question
'''



'''
    Begin helper functions
'''

# Returns a string for an SQL conditional
def conditionalStatement(column, condition):
    return f"WHERE {column} = '{condition}'"



# Grabs the question's required parameters
def getQuestionParameters(data):

    numberOfColumns = None
    numberOfJoins = None
    try:
        numberOfColumns = data['params']['html_params']['columns']
        numberOfJoins = data['params']['html_params']['joins']
    except:
        numberOfColumns = 5
        numberOfJoins = 1

    # Constructs table clauses.
    # Parameters:
    #   - primaryKeys
    #   - isNotNull
    #   - isUnique
    #   - isOnUpdateCascade
    #   - isOnDeleteSetNull
    tableClauses = {}
    try:
        for clause in data['params']['html_table_clauses']:
            if data['params']['html_table_clauses'][clause]:
                tableClauses[clause] = data['params']['html_table_clauses'][clause]
    except:
        pass

    # Constructs query clauses.
    # Parameters:
    #   - useConditional
    #   - useSubquery
    queryClauses = {}
    try:
        for clause in data['params']['html_query_clauses']:
            queryClauses[clause] = data['params']['html_query_clauses'][clause]
    except:
        queryClauses = {
            'useConditional': 1,
            'useSubquery': False,
            'useAndInsteadOfOr': False
        }
    
    return numberOfColumns, numberOfJoins, tableClauses, queryClauses



# Returns a table with a specified number of columns
def loadTrimmedTable(columnCount, joinCount=0):

    # Checks to see if the column count is valid
    if(columnCount <= 0 or joinCount < 0):
        return None

    # Gets all random tables so a random one may be chosen
    possibleTables = db.getAllTableFiles()

    # Keeps trying random tables until it finds one with enough columns
    # and a enough foreign keys
    table = None
    while not table or len(table.columns) < columnCount or len(table.getKeyMap()) < joinCount:

        # Checks to see if there are no possible tables left.
        # This will only occur if there are no tables with enough
        # columns to satisfy the requirements.
        if len(possibleTables) == 0:
            return None

        # Pops the current table so there's no repeats
        possibleTable = possibleTables.pop(random.choice(range(len(possibleTables))))
        table = db.Table(possibleTable, random=False)

    # Removes columns until there is an appropriate amount left
    doomCounter = 10
    while len(table.columns) > columnCount:

        # If the doom counter reaches 0, it means that we are unable to remove
        # enough columns because they are PKs or necessary FKs. In that case,
        # just return the table, even if it has too many columns
        if doomCounter == 0:
            return table

        # We have to convert keys to a list because of subscriptables
        tryPop = random.choice(list(table.columns.keys()))

        # Don't remove...
        # primary keys, or
        # foreign keys if it would cause there to be not enough joins
        if not table.columns[tryPop]['isPrimary'] and (not table.columns[tryPop]['references'] or len(table.getKeyMap()) > joinCount):
            table.columns.pop(tryPop)
        else:
            doomCounter -= 1
    
    return table

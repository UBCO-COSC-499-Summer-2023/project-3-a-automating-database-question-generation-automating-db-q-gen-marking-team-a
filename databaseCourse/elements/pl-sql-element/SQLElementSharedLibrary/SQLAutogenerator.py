import SQLElementSharedLibrary.textDatabaseHandler as db
import random
import SQLElementSharedLibrary.SQLNoisyData as nd



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
    table = None
    match difficulty:
        case 'easy': table = db.Table(random.choice(['airport', 'airplane', 'product', 'customer']), random=False)
        case 'medium': table = db.Table(random.choice(['passenger', 'shipment']), random=False)
        case 'hard': table = db.Table(random.choice(['flight', 'shippedproduct']), random=False)
        case _: table = db.Table(columns=columns, joins=joins, clauses=tableClauses)


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



    # Loads any tables this one references into the schema
    loadSchemas(data, None, getReferencedTables(table, unique=True))

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
    table = None
    match difficulty:
        case 'easy': table = loadTrimmedTable(random.randint(3, 4), 0)
        case 'medium': table = loadTrimmedTable(random.randint(4, 6), 0)
        case 'hard': table = loadTrimmedTable(random.randint(5, 8), 0)
        case _: table = db.Table(columns=columns, joins=joins, clauses=tableClauses)



    # Creates the values ands add them to the question string

    # Generates the data to be inserted.
    # Converts the dictionary row to a list and removes arrays
    columnData = nd.generateColumns(table, random.randint(3, 7))
    columnDatum = [value[0] for value in list(columnData.values())]
    


    # Adds the data to the question string, replacing the '[]'
    # with '()'
    valuesString = f"({str(columnDatum)[1:-1]})"

    # Creates and adds the question string
    data['params']['questionString'] = f"Insert the following values into the <b>{table.name}</b> table:\n{valuesString}"



    # Gets referenced tables
    referencedTables = getReferencedTables(table)

    # Adds the table to the schema as well as
    # the schemas of referenced tables
    loadAllSchema(data, table, referencedTables)



    # Loads noisy data
    # Doesn't call loadAllNoisyData() since we want
    # to load the referenced row into the foreign
    # table, but we don't want to load the row the
    # student is supposed to insert themselves

    # Gets a key map for easy reference later
    keyMap = table.getKeyMap()

    # Generates the noisy data. At this point, there
    # is NOT consistency across foreign keys.
    generatedData = {key: nd.generateColumns(referencedTables[keyMap[key]['references']], len(list(columnData.values())[0])) for key in keyMap}

    # Overrides the generated data to be the same as
    # the primary table's data. This IS now consistent
    # across foreign keys.
    for key in keyMap:
        generatedData[key][keyMap[key]['foreignKey']] = columnData[key]
    
    # Loads the data into the actual table
    for key in keyMap:
        loadNoisyData(data, referencedTables[keyMap[key]['references']], generatedData[key])

    # Loads the primary table's data, aside from
    # the row that needs to be inserted
    columnData = {key: columnData[key][1:] for key in columnData}
    loadNoisyData(data, table, columnData)



    # Creates the answer string
    data['correct_answers']['SQLEditor'] = insertStatement(table, columnDatum)

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
    # Randomly selects from the list at the given difficulty
    table = None
    match difficulty:
        case 'easy': 
            table = loadTrimmedTable(random.randint(3, 4))
            queryClauses['useConditional'] = False
            queryClauses['useSubquery'] = False

        case 'medium': 
            table = loadTrimmedTable(random.randint(4, 6))
            queryClauses['useConditional'] = True
            queryClauses['useSubquery'] = False

        case 'hard': 
            table = loadTrimmedTable(random.randint(5, 8))
            queryClauses['useConditional'] = False
            queryClauses['useSubquery'] = True
            return None # Not yet implemented; first requires quesryStatement() to be completed
        
        case _:
            table = db.Table(columns=columns, joins=joins, clauses=tableClauses)

    # Checks if the parameters are valid
    nonCascadingForeignKeys = len([key for key in table.columns.keys() if table.columns[key]['references'] and not table.columns[key]['isOnUpdateCascade']])
    if columns - nonCascadingForeignKeys < queryClauses['useConditional']:
        print(f"UPDATE question cannot have more conditional clauses than foreign keys that do not cascade on update (was supplied with {queryClauses['useConditional']} conditionals and {nonCascadingForeignKeys} non-cascading foreign keys)")

    # Generates a bunch of bogus rows
    columnData = nd.generateColumns(table, random.randint(6, 10))

    # Selects a random column to affect
    updateColumn = random.choice(list(table.columns.keys()))

    # Generates the updated valued
    updateValue = nd.generateNoisyData(table, updateColumn)[0]



    # If the quesiton should use a condition, set parameters
    conditionalValues = {}
    columnList = list(table.columns.keys())
    indexList = [i for i in range(len(list(columnData.values())[0]))]
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
        conditionalValues[conditionalColumn] = columnData[conditionalColumn][randomValueIndex]


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

    # Loads referenced tables
    referenced = getReferencedTables(table)

    # Loads the schema of all referenced tables
    loadAllSchema(data, table, referenced)

    # Loads the noisy data into the primary table as
    # well as generating noisy data for referenced tables
    loadAllNoisyData(data, table, columnData, referenced)

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
    # Randomly selects from the list at the given difficulty
    table = None
    match difficulty:
        case 'easy': 
            table = loadTrimmedTable(random.randint(3, 4))
            queryClauses['useConditional'] = False
            queryClauses['useSubquery'] = False

        case 'medium': 
            table = loadTrimmedTable(random.randint(4, 6))
            queryClauses['useConditional'] = True
            queryClauses['useSubquery'] = False

        case 'hard': 
            table = loadTrimmedTable(random.randint(5, 8))
            queryClauses['useConditional'] = False
            queryClauses['useSubquery'] = True
            return None # Not yet implemented; first requires quesryStatement() to be completed
        
        case _:
            table = db.Table(columns=columns, joins=joins, clauses=tableClauses)

    # Generates a bunch of bogus rows
    columnData = nd.generateColumns(table, columns * 3 + random.randint(-3, 3))


    
    # If the quesiton should use a condition, set parameters
    conditionalValues = {}
    columnList = list(table.columns.keys())
    indexList = [i for i in range(len(list(columnData.values())[0]))]
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
        conditionalValues[conditionalColumn] = columnData[conditionalColumn][randomValueIndex]



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



    # Gets referenced tables
    referenced = getReferencedTables(table)

    # Loads the schema of all referenced tables
    loadAllSchema(data, table, referenced)

    # Loads the noisy data into the primary table as
    # well as generating noisy data for referenced tables
    loadAllNoisyData(data, table, columnData, referenced)

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
    
    # Sets the difficulty
    columnCount = None
    joins = None
    clauses = None
    match difficulty:

        # Easy:   conditional, no join, no clauses
        case 'easy': 
            columnCount = random.randint(1, 3)
            joins = 0
            clauses = 0

        # Medium: conditional, join, no clauses
        case 'medium': 
            columnCount = random.randint(3, 4)
            joins = random.randint(1, 2)
            clauses = 0

        # Hard:   conditional, join, clauses
        case 'hard': 
            columnCount = random.randint(4, 5)
            joins = random.randint(1, 2)
            clauses = random.randint(1, 3)



    # Selects a table based on the difficulty

    # Keeps trying random tables until it finds one that
    # fulfills the conditions set by the difficulty
    table = loadTrimmedTable(columnCount, joins)

    # Gets the referenced tables
    referenced = getReferencedTables(table)



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
    for i in range(columnCount - joins - 1):

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
    if columnCount == 1:
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
            if columnIndex == len(list(selectedColumns[key])) and keyIndex == len(list(selectedColumns)) and columnCount > 1:
                questionString += ' and'
            
            questionString += f" <b>{column}</b>,"

    # Removes the trailing comma
    questionString = questionString[:-1] + '.'

    # Adds the question string to data
    data['params']['questionString'] = questionString



    # Loads the schema of all referenced tables
    loadAllSchema(data, table, referencedTables=referenced)

    # Generates random data to populate the table
    rows = nd.generateColumns(table, len(list(table.columns.keys())) * 3 + random.randint(-3, 3))

    # Loads the noisy data into the primary table as
    # well as generating noisy data for referenced tables
    loadAllNoisyData(data, table, rows, referencedTables=referenced)

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



# Returns a dictionary that maps the foreign key of the supplied
# table to the referenced tables. If the unique parameter is true,
# this dictionary contains a set of tables: no duplicated. Otherwise,
# there may be duplicate tables with unique foreign keys.
def getReferencedTables(table, unique=True, static=False):
    
    # Uses a dictionary to store the tables and a set to keep track
    # of unique table names
    tables = {}
    tableSet = set()

    # Iterates over the table's foreign keys
    for key in table.getKeyMap().keys():

        # Checks to see if the table name is already in the set.
        # Only matters if unique is True.
        if table.columns[key]['references'] not in tableSet:

            columns = random.randint(3, 6)

            # Ensures foreign key consistency across generated tables
            #   name of the column in the foreign table: {
            #       'unit': the data type of the column
            #       'unitOther': the other information related to the data type
            #   }
            constraints = {
                table.columns[key]['foreignKey']: {
                    'name': table.columns[key]['foreignKey'],
                    'unit': table.columns[key]['unit'],
                    'unitOther': table.columns[key]['unitOther']
                }
            }

            # Loads an approrpiate table into the dictionary
            tables[table.columns[key]['references']] = db.Table(file=table.columns[key]['references'], columns=columns, constraints=constraints, random=not static)

            # Adds the table name to the set if unique is True
            if unique:
                tableSet.add(table.columns[key]['references'])

    # Returns a dictionary of all referenced tables
    #   table name: respective Table object
    return tables



# Adds the schema tables to data
def loadSchemas(data, table, referencedTables):

    # Iterate over tables, if there are any
    # Add their schema to the initialize string
    if referencedTables:
        for key in referencedTables:
            data['params']['db_initialize'] += f"{referencedTables[key].getSchema()}\n"
    
    # Adds the primary table afterwards.
    # Since the primary table may reference the foreign
    # tables but NOT vice versa, it is required that the
    # primary table is loaded after such that foreign
    # key constrains are satisfied.
    if table:
        data['params']['db_initialize'] += f"{table.getSchema()}\n"

# Loads the schema of the current table as well
# as all referenced tables.
def loadAllSchema(data, table, referencedTables={}):

    # Gets all referenced tables
    if not referencedTables:
        referencedTables = getReferencedTables(table, unique=True)

    # Loads all their schema
    loadSchemas(data, table, referencedTables)



# Loads noisy data into the editors
def loadNoisyData(data, table, rows):

    # For each column, select the i-th item and create
    # a create an INSERT statemetn. Do so for all i items
    data['params']['db_initialize'] += ''.join(insertStatement(table, [rows[key][i] for key in rows]) for i in range(len(list(rows.values())[0])))

# Loads the noisy data supplied as well as generating and
# loading noisy data for the referenced tables.
#
# Note: This function respects references so a foreign key
# reference between two tables will holds the same value.
#
# Note: this CAN throw a "UNIQUE constraint failed" IF the
# primary table has two references to the same table (such
# as the static `flight` table) AND there exists a duplicate
# value between the different tables. THIS CAN NEVER HAPPEN
# ON RANDOM TABLES since a random primary table will never
# hold more than one reference to a given secondary random
# table. In other words, no worries.
def loadAllNoisyData(data, table, rows, referencedTables={}):

    # Gets a dicitonary of referenced tables.
    # The keys are the name of the table
    if not referencedTables:
        referencedTables = getReferencedTables(table, unique=False)

    # Gets a dictionary that maps the column to both
    # the referenced table name and foreign key
    keyMap = table.getKeyMap()



    # Generates the noisy data. At this point, there
    # is NOT consistency across foreign keys.
    generatedData = {key: nd.generateColumns(referencedTables[keyMap[key]['references']], len(list(rows.values())[0])) for key in keyMap}

    # Overrides the generated data to be the same as
    # the primary table's data. This IS now consistent
    # across foreign keys.
    for key in keyMap:
        generatedData[key][keyMap[key]['foreignKey']] = rows[key]
    


    # Loads the data into the actual table
    for key in keyMap:
        loadNoisyData(data, referencedTables[keyMap[key]['references']], generatedData[key])
    
    # Finally loads the primary table's data.
    # Since the primary table may reference the foreign
    # tables but NOT vice versa, it is required that the
    # primary table is loaded after such that foreign
    # key constrains are satisfied.
    loadNoisyData(data, table, rows)



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

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
    numberOfColumns = data['params']['html_params']['columns']
    numberOfJoins = data['params']['html_params']['joins']

    # Constructs table clauses
    clauses = {}
    for clause in data['params']['html_table_clauses']:
        if data['params']['html_table_clauses'][clause]:
            clauses[clause] = data['params']['html_table_clauses'][clause]


    # Creates an appropriate table
    table = None
    match difficulty:
        case 'easy': table = db.Table(random.choice(['airport', 'airplane', 'product', 'customer']), random=False)
        case 'medium': table = db.Table(random.choice(['passenger', 'shipment']), random=False)
        case 'hard': table = db.Table(random.choice(['flight', 'shippedproduct']), random=False)
        case _: table = db.Table(columns=numberOfColumns, joins=numberOfJoins, clauses=clauses)


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

    # Based on the difficulty, choose a random amount of columns
    columnCount = None
    match difficulty:
        case 'easy': columnCount = random.randint(3, 4)
        case 'medium': columnCount = random.randint(4, 6)
        case 'hard': columnCount = random.randint(5, 8)

    # Gets a table with the specified number of columns
    table = loadTrimmedTable(columnCount, 0)



    # Creates the values ands add them to the question string

    # Generates the data to be inserted.
    # Converts the dictionary row to a list and removes arrays
    row = [value[0] for value in list(nd.generateColumns(table).values())]
    
    # Adds the data to the question string, replacing the '[]'
    # with '()'
    valuesString = f"({str(row)[1:-1]})"



    # Creates and adds the question string
    data['params']['questionString'] = f"Insert the following values into the <b>{table.name}</b> table:\n{valuesString}"


    # Gets referenced tables
    referenced = getReferencedTables(table)

    # Adds the table to the schema as well as
    # the schemas of referenced tables
    loadAllSchema(data, table, referenced)

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
    
    # Chooses a table to load based on quesiton difficulty
    # Randomly selects from the list at the given difficulty
    columnCount = None
    useConditional = None
    match difficulty:
        case 'easy': 
            columnCount = random.randint(3, 4)
            useConditional = False

        case 'medium': 
            columnCount = random.randint(4, 6)
            useConditional = True

        case 'hard': 
            return None # Not yet implemented; first requires quesryStatement() to be completed

    # Gets a table with the specified number of columns
    table = loadTrimmedTable(columnCount, 0)



    # Generates a bunch of bogus rows
    rows = nd.generateColumns(table, columnCount * 3 + random.randint(-3, 3))

    # Selects a random column to affect
    updateColumn = random.choice(list(table.columns.keys()))

    # Generates the updated valued
    updateValue = nd.generateNoisyData(table, updateColumn)[0]


    # If the quesiton should use a condition, set parameters
    conditionalColumn = None
    conditionalValue = None
    if useConditional:

        # Selects a random column to affect
        conditionalColumn = random.choice(list(table.columns.keys()))

        # Chooses a random value from the generated data to be updated
        randomValueIndex = random.choice(range(len(rows)))

        # Grabs the randomly selected values
        conditionalValue = rows[conditionalColumn][randomValueIndex]



    # Generates the question string
    # Changes depending on whether it uses a conditional or not
    if useConditional:
        data['params']['questionString'] = f"From the table <b>{table.name}</b> and in the column <b>{updateColumn}</b>, change all values to be <b>{updateValue}</b> where <b>{conditionalColumn}</b> is equal to <b>{conditionalValue}</b>."
    else:
        data['params']['questionString'] = f"From the table <b>{table.name}</b> and in the column <b>{updateColumn}</b>, change all values to be <b>{updateValue}</b>."


    # Loads referenced tables
    referenced = getReferencedTables(table)

    # Loads the schema of all referenced tables
    loadAllSchema(data, table, referenced)

    # Loads the noisy data into the primary table as
    # well as generating noisy data for referenced tables
    loadAllNoisyData(data, table, rows, referenced)

    # Loads the correct answer
    data['correct_answers']['SQLEditor'] = updateStatement(table, updateColumn, updateValue, conditionalColumn, conditionalValue)

# Creates an update statement
def updateStatement(table, updateColumn, updateValue, conditionalColumn = None, conditionalValue = None):

    # Includes the conditional if they exist
    if conditionalColumn and conditionalValue:
        return f"UPDATE {table.name} SET {updateColumn} = '{updateValue}' {conditionalStatement(conditionalColumn, conditionalValue)};\n"

    # This else isn't required but is included for clarity
    else:
        return f"UPDATE {table.name} SET {updateColumn} = '{updateValue}';\n"

'''
    End update-style question
'''


'''
    Begin delete-style question
'''

def generateDelete(data, difficulty):
        
    # Chooses a table to load based on quesiton difficulty
    # Randomly selects from the list at the given difficulty
    columnCount = None
    match difficulty:
        case 'easy': columnCount = random.randint(3, 4)
        case 'medium': columnCount = random.randint(4, 6)
        case 'hard': return None # Not yet implemented; first requires quesryStatement() to be completed

    # Gets a table with the specified number of columns
    table = loadTrimmedTable(columnCount, 0)

    # Generates a bunch of bogus rows
    rows = nd.generateColumns(table, columnCount * 3 + random.randint(-3, 3))

    # Selects a random column to affect
    # Won't select a foreign key if the difficulty is easy
    randomKey = None
    while not randomKey or (table.columns[randomKey]['references'] and difficulty == 'easy'):
        randomKey = random.choice(list(table.columns.keys()))

    # Chooses a random value from the generated data to be deleted
    randomValueIndex = random.choice(range(len(rows)))

    # Grabs the randomly selected values
    deleteValue = rows[randomKey][randomValueIndex]



    # Creates the question string
    data['params']['questionString'] = f"From the table <b>{table.name}</b>, delete the entry where <b>{randomKey}</b> equals <b>'{deleteValue}'</b>."


    # Gets referenced tables
    referenced = getReferencedTables(table)

    # Loads the schema of all referenced tables
    loadAllSchema(data, table, referenced)

    # Loads the noisy data into the primary table as
    # well as generating noisy data for referenced tables
    loadAllNoisyData(data, table, rows, referenced)

    # Sets the correct answer
    data['correct_answers']['SQLEditor'] = deleteStatement(table, randomKey, deleteValue)


# Creates a delete statement
def deleteStatement(table, column = None, condition = None):
    ans = f"DELETE FROM {table.name}"
    if(column and condition):
        ans += f" {conditionalStatement(column, condition)};\n"
    return ans

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
                table.columns[key]['foreignKey'] : {
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
def loadTrimmedTable(columnCount, joinCount):

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

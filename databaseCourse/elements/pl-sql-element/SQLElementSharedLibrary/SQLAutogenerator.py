import SQLElementSharedLibrary.textDatabaseHandler as db
import random
from string import ascii_uppercase

# Automatically generates an SQL question based on the question's parameters
def autogenerate(data):
    
    # Gets question parameters
    # random = data['params']['html_params']['random']
    # maxGrade = data['params']['html_params']['maxGrade']
    # markerFeedback = data['params']['html_params']['markerFeedback']
    questionType = data['params']['html_params']['questionType']
    difficulty = data['params']['html_params']['difficulty']


    # Checks if the difficulty are valid
    if difficulty not in ['easy', 'medium', 'hard']:
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

    # Chooses a table to load based on quesiton difficulty
    # Randomly selects from the list at the given difficulty
    tableFile = ''
    match difficulty:
        case 'easy': tableFile = random.choice(['airport', 'airplane', 'product', 'customer'])
        case 'medium': tableFile = random.choice(['passenger', 'shipment'])
        case 'hard': tableFile = random.choice(['flight', 'shippedproduct'])
    
    # Loads the selected table
    table = db.load(relativeFilePath(tableFile))


    # Creates a string to tell the student what they need
    # to do for the qestion
    questionString = f"Create a table named {table.name} with columns"

    # Adds a list of columns and units to the question string
    columnList = list(table.columns.keys())
    columnValues = list(table.columns.values())
    for i in range(len(columnList)):

        # Adds an 'and' at the start of the last iteration
        if i == len(columnList) - 1:
            questionString += ' and'
        
        # Adds the column name
        questionString += f" {columnValues[i]['name']}"

        # Mentions primary key, if necessary
        if columnValues[i]['isPrimary']:
            questionString += ' that is a primary key'

        # Handles the text for units
        match columnValues[i]['unit']:
            case 'INTEGER': questionString += ' (an integer)'
            case 'DECIMAL': questionString += f" (a decimal value with a total of {columnValues[i]['unitOther'].split(',')[0]} digits, {columnValues[i]['unitOther'].split(',')[1]} of which are after the decimal point)"
            case 'CHAR': questionString += f" (a string of exaclty {columnValues[i]['unitOther']} characters)"
            case 'VARCHAR': questionString += f" (a string up to {columnValues[i]['unitOther']} characters)"
            case 'DATE': questionString += ' (DATE)'
            case 'DATETIME': questionString += ' (DATETIME)'
            case other: questionString += f" ({columnValues[i]['unit']})"

        # Mentions foreign key and its clauses, if necessary
        if columnValues[i]['references']:
            questionString += f" that references {columnValues[i]['references']}\'s {columnValues[i]['foreignKey']}"

            # Handles cascade
            if columnValues[i]['isOnUpdateCascade']:
                questionString += ' that cascades on an update'
            
            # Handles delete set null
            if columnValues[i]['isOnDeleteSetNull']:
                questionString += ' that is set to null when deleted'

        # Mentions other clauses, if necessary
        if columnValues[i]['isNotNull']:
            questionString += ' and cannot be null'

        # Adds a comma at the end of each iteration
        questionString += ', '


    # Remove the last comma and replace it with a period
    questionString = questionString[:-2] + '.'



    # Loads any tables this one references into the schema
    # First gets a set of all referenced tables
    loadSchemas(data, getReferencedTablesSet(table))

    # Places the question string into data
    data['params']['questionString'] = questionString

    # Places the solution into data
    #
    # TODO
    # Replaced the called method with createStatement() when
    # that method is completed; i.e. it includes clauses,
    # primary keys, and foreign keys
    data['correct_answers']['SQLEditor'] = db.getDDL(relativeFilePath(tableFile))

# Returns the schema for the current table.
# Currently DOES NOT include clauses (such as NOT NULL),
# foreign keys, or primary keys.
def createStatement(table):
    # Starts the string with the create table and name
    schemaString = f"CREATE TABLE {table.name} ("

    # Iterates over columns
    for key in table.columns:

        # Adds the columns name and data type
        schemaString += f"\n\t{table.columns[key]['name']} {table.columns[key]['unit']}"

        # If the data type has another component, add it
        if table.columns[key]['unitOther']:
            schemaString += f"({table.columns[key]['unitOther']})"
        
        # Adds the trailing comma
        schemaString += ','

    # Removes the trailing comma from the final line and
    # on a new line add the ');'
    return f"{schemaString[:-1]}\n\t);"

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
    # Converts the dictionary row to a list
    row = list(generateRow(table).values())
    
    # Adds the data to the question string, replacing the '[]'
    # with '()'
    valuesString = f"({str(row)[1:-1]})"



    # Creates and adds the question string
    data['params']['questionString'] = f"Insert the following values into the {table.name} table:\n{valuesString}"

    # Adds the table to the schema as well as
    # the schemas of referenced tables
    loadAllSchema(data, table)

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
    rows = generateRows(table, columnCount * 3 + random.randint(-3, 3))

    # Selects a random column to affect
    updateColumn = random.choice(list(table.columns.keys()))

    # Generates the updated valued
    updateValue = generateNoisyData(table, updateColumn)


    # If the quesiton should use a condition, set parameters
    conditionalColumn = None
    conditionalValue = None
    if useConditional:

        # Selects a random column to affect
        conditionalColumn = random.choice(list(table.columns.keys()))

        # Chooses a random value from the generated data to be updated
        randomValueIndex = random.choice(range(len(rows)))

        # Grabs the randomly selected values
        conditionalValue = rows[randomValueIndex][conditionalColumn]



    # Generates the question string
    # Changes depending on whether it uses a conditional or not
    if useConditional:
        data['params']['questionString'] = f"From the table {table.name} and in the column {updateColumn}, change all values to be {updateValue} where {conditionalColumn} is equal to {conditionalValue}."
    else:
        data['params']['questionString'] = f"From the table {table.name} and in the column {updateColumn}, change all values to be {updateValue}."

    # Loads the schema of all referenced tables
    loadAllSchema(data, table)

    # Loads the noisy data into the primary table as
    # well as generating noisy data for referenced tables
    loadAllNoisyData(data, table, rows)

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
    End updatestyle question
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
    rows = generateRows(table, columnCount * 3 + random.randint(-3, 3))

    # Selects a random column to affect
    # Won't select a foreign key if the difficulty is easy
    randomKey = None
    while not randomKey or (table.columns[randomKey]['references'] and difficulty == 'easy'):
        randomKey = random.choice(list(table.columns.keys()))

    # Chooses a random value from the generated data to be deleted
    randomValueIndex = random.choice(range(len(rows)))

    # Grabs the randomly selected values
    deleteValue = rows[randomValueIndex][randomKey]



    # Creates the question string
    data['params']['questionString'] = f"From the table {table.name}, delete the entry where {randomKey} equals '{deleteValue}'."

    # Loads the schema of all referenced tables
    loadAllSchema(data, table)

    # Loads the noisy data into the primary table as
    # well as generating noisy data for referenced tables
    loadAllNoisyData(data, table, rows)

    # Sets the correct answer
    data['correct_answers']['SQLEditor'] = deleteStatement(table, randomKey, deleteValue)


# Creates a delete statement
def deleteStatement(table, column = None, condition = None):
    ans = f"DELETE FROM {table.name}"
    if(column and condition):
        ans += f"{conditionalStatement(column, condition)};\n"
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
    referenced = getReferencedTableDictionary(table)



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

        questionString += f" {keyMap[key]['references']},"
    
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
            
            questionString += f" {column},"

    # Removes the trailing comma
    questionString = questionString[:-1] + '.'

    # Adds the question string to data
    data['params']['questionString'] = questionString



    # Loads the schema of all referenced tables
    loadAllSchema(data, table)

    rows = generateRows(table, len(list(table.columns.keys())) * 3 + random.randint(-3, 3))

    # Loads the noisy data into the primary table as
    # well as generating noisy data for referenced tables
    loadAllNoisyData(data, table, rows)

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

# Returns the file path to the table file
def relativeFilePath(filePath):
    return f"./SQLElementSharedLibrary/randomTables/{filePath}.txt"

# Gets the filepaths to all tables referenced by this one
# Returns a set to ensure no duplicate tables
def getReferencedTablesSet(table):

    # Uses a set in case a table is referenced more than once
    # Tracks name, since it is easily hashable
    tables = set()

    # Checks each column for its reference
    # Adds the referenced item, if it exists
    for key in table.columns:
        if table.columns[key]['references']:
            tables.add(table.columns[key]['references'])

    # Doesn't return the table names, returns the table objects
    return set(db.load(relativeFilePath(referenced)) for referenced in tables)

# Returns a dictionary that maps the foreign key of the supplied
# table to the referenced tables.
# May contain multiple of the same table, referenced by
# different foreign keys
def getReferencedTableDictionary(table):
    
    # Uses a dictionary to store the tables
    tables = {}

    # Checks each column for its reference
    # Adds the referenced item, if it exists
    for key in table.columns.keys():
        if table.columns[key]['references']:
            tables[table.columns[key]['references']] = db.load(relativeFilePath(table.columns[key]['references']))

    return tables

# Adds the schema tables to data
def loadSchemas(data, tables):

    # Iterate over tables, if there are any
    # Add their schema to the initialize string
    if tables:
        for table in tables:
            data['params']['db_initialize'] += f"{createStatement(table)}\n"

# Loads the schema of the current table as well
# as all referenced tables.
def loadAllSchema(data, table):

    # Gets all referenced tables
    tables = getReferencedTablesSet(table)

    # Adds this table to the set
    tables.add(table)

    # Loads all their schema
    loadSchemas(data, tables)

# Loads noisy data into the editors
def loadNoisyData(data, table, rows):
    data['params']['db_initialize'] += ''.join(insertStatement(table, list(row.values())) for row in rows)


# Loads the noisy data supplied as well as generating and
# loading noisy data for the referenced tables.
#
# Note: This function respects references so a foreign key
# reference between two tables will holds the same value.
def loadAllNoisyData(data, table, rows):
    
    # First loads the rows into the actual table
    loadNoisyData(data, table, rows)

    # Gets a dicitonary of referenced tables.
    # The keys are the name of the table
    referencedTables = getReferencedTableDictionary(table)


    # Gets a dictionary that maps the column to both
    # the referenced table name and foreign key
    keyMap = table.getKeyMap()

    # All table of data
    generatedData = {}

    # Iterates over foreign keys
    for key in keyMap.keys():

        # Grabs the referenced table
        referenced = referencedTables[keyMap[key]['references']]

        # A table of data
        generatedData[key] = []

        # Iterates over the provided data
        for row in rows:

            # A row of data
            noisyRow = {}

            # Iterates over the referenced table's columns
            for column in referenced.columns:
                
                # If this column is referenced by the original
                # table, map the data over
                if column == keyMap[key]['foreignKey']:
                    noisyRow[column] = row[key]

                # Otherwise generate new data
                else:
                    noisyRow[column] = generateNoisyData(referenced, column)
                
            # Adds the row of data to the appropriate table
            generatedData[key].append(noisyRow)

    # Loads the data into the actual table
    for key in generatedData:
        loadNoisyData(data, referencedTables[keyMap[key]['references']], generatedData[key])



# Returns a table with a specified number of columns
def loadTrimmedTable(columnCount, joinCount):

    # Checks to see if the column count is valid
    if(columnCount <= 0 or joinCount < 0):
        return None

    # Gets all random tables so a random one may be chosen
    possibleTables = db.getAllTableFiles('./SQLElementSharedLibrary/randomTables/')

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
        table = db.load(relativeFilePath(possibleTable))

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



# Generates one row's worth of noisy data
def generateRow(table):
    return {key: generateNoisyData(table, key) for key in table.columns}

# Generates qty's worth of rows of noisy data
def generateRows(table, qty):
    return [generateRow(table) for i in range(qty)]



# Generates random data based on the unit type
def generateNoisyData(table, key):
    
    # Grabs the important information
    unit = table.columns[key]['unit']
    unitOther = table.columns[key]['unitOther']

    # Matches on the unit type
    match unit:
        # Integers
        case 'INTEGER': return generateNoisyInteger()

        # CHARs require the number of characters
        case 'CHAR': return generateNoisyChar(int(unitOther))

        # VARCHARs are capped at a length of 8 to prevent
        # a string of 50 random characters
        case 'VARCHAR': return generateNoisyVarchar(min(int(unitOther), 8))

        # DATE and DATETIME
        case 'DATE': return generateRandomDate()
        case 'DATETIME': return generateRandomDateTime()

        # Crash if the datatype is not correct
        case other: return None

# Generates a random integer in the range 0 to 1000
def generateNoisyInteger():
    return random.randint(1, 1000)

# Generates a random string of length unitOther
def generateNoisyChar(unitOther):

    # Chooses unitOther amount of random uppcercase and
    # letter characters
    return ''.join(random.choice(ascii_uppercase + '1234567890') for i in range(unitOther))

# Generates a random string up to length unitOther
def generateNoisyVarchar(unitOther):

    return generateNoisyChar(random.randint(1, unitOther))

# Generates a random date between 1955 and 2023
def generateRandomDate():

    # Generates a random month
    month = random.randint(1, 12)
    
    # Ensures the day is valid.
    # And no, I'm not doing the legwork to check
    # whether or not it's a leapyear and thus
    # allow a 29th day in February
    day = -1
    if month % 2 == 1:
        day = random.randint(1, 31)
    elif month == 2:
        day = random.randint(1, 28)
    else:
        day = random.randint(1, 30)

    # the ':02' formatting ensures that the length of the
    # string is a minimum of 2, padded left with zeroes
    return f"{random.randint(1955, 2023)}-{month:02}-{day:02}"

# Generates a random date time between 1955 and now
def generateRandomDateTime():

    # The minutes portion can be any increment of 5 minutes.
    # the ':02' formatting ensures that the length of the
    # string is a minimum of 2, padded left with zeroes
    return f"{generateRandomDate()} {random.randint(0, 23):02}:{random.randint(0, 11) * 5:02}:00"
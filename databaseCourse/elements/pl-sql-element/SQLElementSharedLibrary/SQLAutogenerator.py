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

    # Chooses a database to load based on quesiton difficulty
    # Randomly selects from the list at the given difficulty
    databaseFile = ''
    match difficulty:
        case 'easy': databaseFile = random.choice(['airport', 'airplane'])
        case 'medium': databaseFile = random.choice(['passenger'])
        case 'hard': databaseFile = random.choice(['flight'])
    
    # Loads the selected database
    database = db.load(relativeFilePath(databaseFile))


    # Creates a string to tell the student what they need
    # to do for the qestion
    questionString = f"Create a table named {database.name} with columns"

    # Adds a list of columns and units to the question string
    columnList = list(database.columns.keys())
    columnValues = list(database.columns.values())
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
    # First gets a set of all referenced databases
    loadSchemas(data, getReferencedDatabasesSet(database))

    # Places the question string into data
    data['params']['questionString'] = questionString

    # Places the solution into data
    #
    # TODO
    # Replaced the called method with createStatement() when
    # that method is completed; i.e. it includes clauses,
    # primary keys, and foreign keys
    data['correct_answers']['SQLEditor'] = db.getDDL(relativeFilePath(databaseFile))

# Returns the schema for the current database.
# Currently DOES NOT include clauses (such as NOT NULL),
# foreign keys, or primary keys.
def createStatement(database):
    # Starts the string with the create table and name
    schemaString = f"CREATE TABLE {database.name} ("

    # Iterates over columns
    for key in database.columns:

        # Adds the columns name and data type
        schemaString += f"\n\t{database.columns[key]['name']} {database.columns[key]['unit']}"

        # If the data type has another component, add it
        if database.columns[key]['unitOther']:
            schemaString += f"({database.columns[key]['unitOther']})"
        
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

    # Gets a database with the specified number of columns
    database = loadTrimmedDatabase(columnCount)



    # Creates the values ands add them to the question string

    # Generates the data to be inserted.
    # Converts the dictionary row to a list
    row = list(generateRow(database).values())
    
    # Adds the data to the question string, replacing the '[]'
    # with '()'
    valuesString = f"({str(row)[1:-1]})"



    # Creates and adds the question string
    data['params']['questionString'] = f"Insert the following values into the {database.name} table:\n{valuesString}"

    # Adds the database to the schema as well as
    # the schemas of referenced databases
    loadAllSchema(data, database)

    # Creates the answer string
    data['correct_answers']['SQLEditor'] = insertStatement(database, row)

# Generates an insert statement based on the data
def insertStatement(database, row):
    return f"INSERT INTO {database.name} VALUES ({str(row)[1:-1]});\n"

'''
    End insert-style question
'''



'''
    Begin update-stype question
'''

def generateUpdate(data, difficulty):
    
    # Chooses a database to load based on quesiton difficulty
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

    # Gets a database with the specified number of columns
    database = loadTrimmedDatabase(columnCount)



    # Generates a bunch of bogus rows
    rows = generateRows(database, columnCount * 3 + random.randint(-3, 3))

    # Selects a random column to affect
    updateColumn = random.choice(list(database.columns.keys()))

    # Generates the updated valued
    updateValue = generateNoisyData(database, updateColumn)


    # If the quesiton should use a condition, set parameters
    conditionalColumn = None
    conditionalValue = None
    if useConditional:

        # Selects a random column to affect
        conditionalColumn = random.choice(list(database.columns.keys()))

        # Chooses a random value from the generated data to be updated
        randomValueIndex = random.choice(range(len(rows)))

        # Grabs the randomly selected values
        conditionalValue = rows[randomValueIndex][conditionalColumn]



    # Generates the question string
    # Changes depending on whether it uses a conditional or not
    if useConditional:
        data['params']['questionString'] = f"From the table {database.name} and in the column {updateColumn}, change all values to be {updateValue} where {conditionalColumn} is equal to {conditionalValue}."
    else:
        data['params']['questionString'] = f"From the table {database.name} and in the column {updateColumn}, change all values to be {updateValue}."

    # Loads the schema of all referenced databases
    loadAllSchema(data, database)

    # Loads the noisy data into the primary database as
    # well as generating noisy data for referenced databases
    loadAllNoisyData(data, database, rows)

    # Loads the correct answer
    data['correct_answers']['SQLEditor'] = updateStatement(database, updateColumn, updateValue, conditionalColumn, conditionalValue)

# Creates an update statement
def updateStatement(database, updateColumn, updateValue, conditionalColumn = None, conditionalValue = None):

    # Includes the conditional if they exist
    if conditionalColumn and conditionalValue:
        return f"UPDATE {database.name} SET {updateColumn} = '{updateValue}' {conditionalStatement(conditionalColumn, conditionalValue)};\n"

    # This else isn't required but is included for clarity
    else:
        return f"UPDATE {database.name} SET {updateColumn} = '{updateValue}';\n"

'''
    End updatestyle question
'''


'''
    Begin delete-style question
'''

def generateDelete(data, difficulty):
        
    # Chooses a database to load based on quesiton difficulty
    # Randomly selects from the list at the given difficulty
    columnCount = None
    match difficulty:
        case 'easy': columnCount = random.randint(3, 4)
        case 'medium': columnCount = random.randint(4, 6)
        case 'hard': return None # Not yet implemented; first requires quesryStatement() to be completed

    # Gets a database with the specified number of columns
    database = loadTrimmedDatabase(columnCount)

    # Generates a bunch of bogus rows
    rows = generateRows(database, columnCount * 3 + random.randint(-3, 3))

    # Selects a random column to affect
    # Won't select a foreign key if the difficulty is easy
    randomKey = None
    while not randomKey or (database.columns[randomKey]['references'] and difficulty == 'easy'):
        randomKey = random.choice(list(database.columns.keys()))

    # Chooses a random value from the generated data to be deleted
    randomValueIndex = random.choice(range(len(rows)))

    # Grabs the randomly selected values
    deleteValue = rows[randomValueIndex][randomKey]



    # Creates the question string
    data['params']['questionString'] = f"From the table {database.name}, delete the entry where {randomKey} equals '{deleteValue}'."

    # Loads the schema of all referenced databases
    loadAllSchema(data, database)

    # Loads the noisy data into the primary database as
    # well as generating noisy data for referenced databases
    loadAllNoisyData(data, database, rows)

    # Sets the correct answer
    data['correct_answers']['SQLEditor'] = deleteStatement(database, randomKey, deleteValue)


# Creates a delete statement
def deleteStatement(database, column = None, condition = None):
    ans = f"DELETE FROM {database.name}"
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



    # Selects a database based on the difficulty

    # Gets all random databases so a random one may be chosen
    possibleDatabases = db.getAllDatabaseFiles('./SQLElementSharedLibrary/randomDatabases/')

    # Keeps trying random databases until it finds one that
    # fulfills the conditions set by the difficulty
    #
    # The len(db.getKeyMap()) ensures that there are enough foreign
    # keys to fulfill the joins requirement
    #
    # The (joins + 1) allows for the main database to have insufficient 
    # columns since it will be able to use the columns in the joined
    # databases
    database = None
    while not database or len(database.getKeyMap()) < joins or len(database.columns) < columnCount / (joins + 1):
        database = db.load(relativeFilePath(random.choice(possibleDatabases)))

    # Gets the referenced databases
    referenced = getReferencedDatabaseDictionary(database)



    # keyMap maps the primary database's FKs to the other tables
    # keyMap = {
    #   $foreignKey: {
    #       'references': $foreignDatabaseName
    #       'foreignKey': $columnReferenced
    #   }
    # }
    keyMap = database.getKeyMap()

    # Maps the foreign keys to databases
    # foreignKeyMap = {
    #   $columnName: database
    # }
    foreignKeyMap = {database.name: database}

    # Randomly chooses which databases are joined together
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

    # Chooses one column randomly from each joined database.
    # Ensures that at least one column per database joined is
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
    keyMap = database.getKeyMap()

    # Adds the current database to the keyMap (for ease)
    keyMap[database.name] = {'references': database.name, 'foreignKey': None}



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



    # Loads the schema of all referenced databases
    loadAllSchema(data, database)

    rows = generateRows(database, len(list(database.columns.keys())) * 3 + random.randint(-3, 3))

    # Loads the noisy data into the primary database as
    # well as generating noisy data for referenced databases
    loadAllNoisyData(data, database, rows)

    # Sets the correct answers
    # TODO: clauses (the '[]') is blank; make it not blank
    data['correct_answers']['SQLEditor'] = queryStatement(database, keyMap, foreignKeyMap, selectedColumns, [])

# Creates a delete statement
# TODO
#   Conditionals
#   Clauses
def queryStatement(database, keyMap, foreignKeyMap, selectedColumns, clauses):
    
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

    # Removes the primary database, since it is the holder of all
    # the foreign keys so we don't want to say "join table to self"
    foreignKeyMap.pop(database.name)

    if foreignKeyMap:
        for key in foreignKeyMap:
            queryString += f" {database.name[0:1].upper()}.{key} = {keyMap[key]['references'][0:1].upper()}.{keyMap[key]['foreignKey']} AND"

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

# Returns the file path to the database file
def relativeFilePath(filePath):
    return f"./SQLElementSharedLibrary/randomDatabases/{filePath}.txt"

# Gets the filepaths to all databases referenced by this one
# Returns a set to ensure no duplicate databases
def getReferencedDatabasesSet(database):

    # Uses a set in case a database is referenced more than once
    # Tracks name, since it is easily hashable
    databases = set()

    # Checks each column for its reference
    # Adds the referenced item, if it exists
    for key in database.columns:
        if database.columns[key]['references']:
            databases.add(database.columns[key]['references'])

    # Doesn't return the database names, returns the database objects
    return set(db.load(relativeFilePath(referenced)) for referenced in databases)

# Returns a dictionary that maps the foreign key of the supplied
# database to the referenced databases.
# May contain multiple of the same database, referenced by
# different foreign keys
def getReferencedDatabaseDictionary(database):
    
    # Uses a dictionary to store the databases
    databases = {}

    # Checks each column for its reference
    # Adds the referenced item, if it exists
    for key in database.columns.keys():
        if database.columns[key]['references']:
            databases[database.columns[key]['references']] = db.load(relativeFilePath(database.columns[key]['references']))

    return databases

# Adds the schema databases to data
def loadSchemas(data, databases):

    # Iterate over databases, if there are any
    # Add their schema to the initialize string
    if databases:
        for database in databases:
            data['params']['db_initialize'] += f"{createStatement(database)}\n"

# Loads the schema of the current database as well
# as all referenced databases.
def loadAllSchema(data, database):

    # Gets all referenced databases
    databases = getReferencedDatabasesSet(database)

    # Adds this database to the set
    databases.add(database)

    # Loads all their schema
    loadSchemas(data, databases)

# Loads noisy data into the editors
def loadNoisyData(data, database, rows):
    data['params']['db_initialize'] += ''.join(insertStatement(database, list(row.values())) for row in rows)


# Loads the noisy data supplied as well as generating and
# loading noisy data for the referenced databases.
#
# Note: This function respects references so a foreign key
# reference between two tables will holds the same value.
def loadAllNoisyData(data, database, rows):
    
    # First loads the rows into the actual database
    loadNoisyData(data, database, rows)

    # Gets a dicitonary of referenced databases.
    # The keys are the name of the database
    referencedDatabases = getReferencedDatabaseDictionary(database)


    # Gets a dictionary that maps the column to both
    # the referenced database name and foreign key
    keyMap = database.getKeyMap()

    # All table of data
    generatedData = {}

    # Iterates over foreign keys
    for key in keyMap.keys():

        # Grabs the referenced database
        referenced = referencedDatabases[keyMap[key]['references']]

        # A table of data
        generatedData[key] = []

        # Iterates over the provided data
        for row in rows:

            # A row of data
            noisyRow = {}

            # Iterates over the referenced database's columns
            for column in referenced.columns:
                
                # If this column is referenced by the original
                # database, map the data over
                if column == keyMap[key]['foreignKey']:
                    noisyRow[column] = row[key]

                # Otherwise generate new data
                else:
                    noisyRow[column] = generateNoisyData(referenced, column)
                
            # Adds the row of data to the appropriate table
            generatedData[key].append(noisyRow)

    # Loads the data into the actual database
    for key in generatedData:
        loadNoisyData(data, referencedDatabases[keyMap[key]['references']], generatedData[key])



# Returns a database with a specified number of columns
def loadTrimmedDatabase(columnCount):
    
    # Gets all random databases so a random one may be chosen
    possibleDatabases = db.getAllDatabaseFiles('./SQLElementSharedLibrary/randomDatabases/')

    # Keeps trying random databases until it finds one with enough columns
    database = None
    while not database or len(database.columns) < columnCount:
        database = db.load(relativeFilePath(random.choice(possibleDatabases)))

    # Removes columns until there is an appropriate amount left
    while len(database.columns) > columnCount:

        # We have to convert keys to a list because of subscriptables
        tryPop = random.choice(list(database.columns.keys()))

        # Don't remove primary keys
        if not database.columns[tryPop]['isPrimary']:
            database.columns.pop(tryPop)
    
    return database



# Generates one row's worth of noisy data
def generateRow(database):
    return {key: generateNoisyData(database, key) for key in database.columns}

# Generates qty's worth of rows of noisy data
def generateRows(database, qty):
    return [generateRow(database) for i in range(qty)]



# Generates random data based on the unit type
def generateNoisyData(database, key):
    
    # Grabs the important information
    unit = database.columns[key]['unit']
    unitOther = database.columns[key]['unitOther']

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
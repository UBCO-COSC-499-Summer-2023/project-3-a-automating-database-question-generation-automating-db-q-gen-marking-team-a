import SQLElementSharedLibrary.textDatabaseHandler as db
import random
from string import ascii_uppercase

# Automatically generates an SQL question based on the question's parameters
def autogenerate(data):
    
    # Gets question parameters
    random = data['params']['html_params']['random']
    questionType = data['params']['html_params']['questionType']
    difficulty = data['params']['html_params']['difficulty']
    maxGrade = data['params']['html_params']['maxGrade']
    markerFeedback = data['params']['html_params']['markerFeedback']

    # Generates the appropriate question
    match questionType:
        case 'create': generateCreate(data, difficulty)
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
        case other: print(f"{difficulty} is not a valid difficulty.\nValid difficulties are: 'easy', 'medium', and 'hard'.")
    
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
    loadSchemas(data, getReferencedDatabases(database))

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
    columns = -1
    match difficulty:
        case 'easy': columns = random.randint(3, 4)
        case 'medium': columns = random.randint(4, 6)
        case 'hard': columns = random.randint(5, 8)
        case other: print(f"{difficulty} is not a valid difficulty.\nValid difficulties are: 'easy', 'medium', and 'hard'.")

    # Gets all random databases so a random one may be chosen
    possibleDatabases = db.getAllDatabaseFiles('./SQLElementSharedLibrary/randomDatabases/')

    # Keeps trying random databases until it finds one with enough columns
    database = None
    while not database or len(database.columns) < columns:
        database = db.load(relativeFilePath(random.choice(possibleDatabases)))

    # Removes columns until there is an appropriate amount left
    while len(database.columns) > columns:

        # We have to convert keys to a list because of subscriptables
        tryPop = random.choice(list(database.columns.keys()))

        # Don't remove primary keys
        if not database.columns[tryPop]['isPrimary']:
            database.columns.pop(tryPop)



    # Creates the values ands add them to the question string

    # Generates the data to be inserted
    row = generateRow(database.columns)
    
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
    pass

def updateStatement():
    pass

'''
    End updatestyle question
'''


'''
    Begin delete-style question
'''

'''
    Current approach:
    Easy and medium will work like INSERT where they'll select a
    database of a certain size. In addition, they'll select the
    number of affected rows. Hard will be about the same as medium,
    except it will require a subquery, but I first need to first
    complete the queryStatement() function
'''

def generateDelete(data, difficulty):
        
    # Chooses a database to load based on quesiton difficulty
    # Randomly selects from the list at the given difficulty
    #databaseFile = ''
    match difficulty:
        case 'easy': pass
        case 'medium': pass
        case 'hard': pass # Not yet implemented; first requires quesryStatement() to be completed
        case other: print(f"{difficulty} is not a valid difficulty.\nValid difficulties are: 'easy', 'medium', and 'hard'.")

def deleteStatement():
    pass

'''
    End delete-style question
'''


'''
    Begin query-style question
'''

def generateQuery(data, difficulty):
    pass

def queryStatement():
    pass

'''
    End query-style question
'''



'''
    Begin helper functions
'''

# Returns the file path to the database file
def relativeFilePath(filePath):
    return f"./SQLElementSharedLibrary/randomDatabases/{filePath}.txt"

# Gets the filepaths to all databases referenced by this one
def getReferencedDatabases(database):

    # Uses a set in case a database is refereenced more than once
    databases = set()

    # Checks each column for its reference
    # Adds the referenced item, if it exists
    for key in database.columns:
        if database.columns[key]['references']:
            databases.add(db.load(relativeFilePath(database.columns[key]['references'])))

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
    databases = getReferencedDatabases(database)

    # Adds this database to the set
    databases.add(database)

    # Loads all their schema
    loadSchemas(data, databases)



# Generates one row's worth of noisy data
def generateRow(columns):
    return [generateNoisyData(columns[key]['unit'], columns[key]['unitOther']) for key in columns]

# Generates qty's worth of rows of noisy data
def generateRows(columns, qty):
    return [generateRow(columns) for i in range(qty)]



# Generates random data based on the unit type
def generateNoisyData(unit, unitOther):
    
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
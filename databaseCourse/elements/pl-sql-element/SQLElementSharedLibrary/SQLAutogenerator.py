import SQLElementSharedLibrary.textDatabaseHandler as db
import random

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
    schemas = getReferencedDatabases(database)

    # Adds the database filepath to data
    if schemas:
        for schema in schemas:
            data['params']['db_initialize'] += db.getDDL(schema)

    # Places the question string into data
    data['params']['questionString'] = questionString

    # Places the solution into data
    data['correct_answers']['SQLEditor'] = db.getDDL(relativeFilePath(databaseFile))


# Generates a 'insert' style SQL question
#
# Another way of doing this is to have a list of possible columns
# then to select $x amount of them depending on the difficulty.
# We could also include or exclude unit types based on their difficulty,
# i.e. easy questions never get a DATETIME.
def generateInsert(data, difficulty):

    # Based on the difficulty, choose a random amount of columns
    columns = -1
    match difficulty:
        case 'easy': columns = random.randint(3, 4)
        case 'medium': columns = random.randint(4, 6)
        case 'hard': columns = random.randint(5, 10)
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

    # TODO
    # Expands upon the database handler so it can 'store' data.
    # Another textfile that maps variable type to data,
    # so we have a list of: names E VARCHAR (20) for example.
    #
    # Alternatively a random generator for each data type.
    # So date returns f"{random(1955, 2023)}-..."
    

def generateUpdate(data, difficulty):
    pass

def generateDelete(data, difficulty):
    pass

def generateQuery(data, difficulty):
    pass

def relativeFilePath(filePath):
    return f"./SQLElementSharedLibrary/randomDatabases/{filePath}.txt"

# Gets the filepaths to all databases referenced by this one
def getReferencedDatabases(database):

    # Uses a set in case a database is refereenced more than once
    schemas = set()

    # Checks each column for its reference
    # Adds the referenced item, if it exists
    for key in database.columns:
        if database.columns[key]['references']:
            schemas.add(relativeFilePath(database.columns[key]['references']))

    return schemas
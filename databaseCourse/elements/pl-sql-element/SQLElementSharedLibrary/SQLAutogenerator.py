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
        case other: print(f"{difficulty} is not a valid difficulty.")
    
    # Loads the selected database
    database = db.load(relativeFilePath(databaseFile))


    # Creates a string to tell the student what they need
    # to do for the qestion
    questionString = f"Create a table named {database.name} with columns"

    # Adds a list of columns and units to the question string
    for key in list(database.columns.keys())[:-1]:
        questionString += f" {key} ({database.columns[key]['unit']}),"

    # The last item won't have a comma, so it's serpated
    # Also adds the finishing touches
    questionString += f" and {list(database.columns.keys())[-1]} ({list(database.columns.values())[-1]['unit']})."


    # Loads any tables this one references into the schema
    schemas = set()
    for key in database.columns:
        if database.columns[key]['references']:
            schemas.add(database.columns[key]['references'])

    for schema in schemas:
        print(schema)

    if schemas:
        for schema in schemas:
            data['params']['db_initialize'] += db.getDDL(relativeFilePath(schema))

    # Places the question string into data
    data['params']['questionString'] = questionString

    # Places the solution into data
    data['correct_answers']['SQLEditor'] = db.getDDL(relativeFilePath(databaseFile))



def generateInsert(data, difficulty):
    pass

def generateUpdate(data, difficulty):
    pass

def generateDelete(data, difficulty):
    pass

def generateQuery(data, difficulty):
    pass

def relativeFilePath(filePath):
    return f"./SQLElementSharedLibrary/randomDatabases/{filePath}.txt"
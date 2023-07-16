# import SQLElementSharedLibrary.textDatabaseHandler as db
import random as rand
import numpy as np

# Returns the filepath to a specific noisy data file
def relativeFilePath(filePath):
    return f"./RelaXElementSharedLibrary/noisyData/{filePath}.txt"

# Selects a random line from the specified text file
def randomLine(filePath):
    with open(relativeFilePath(filePath), 'r') as file:
        return rand.choice(file.readlines()).strip()
# import SQLElementSharedLibrary.SQLNoisyData as nd
# Returns a list of names for random tables
def getRandomTableNames(path='./RelaXElementSharedLibrary/randomTableNames.txt'):
    try:
        with open(path) as file:
            # Strips out whitespace and only considers lines
            # that aren't exclusively whitespace
            return [line.strip() for line in file.readlines() if not line.isspace()]
    except:
       return []

def generateRandom(unit, stringType=None):
    match unit:
        case 'NUMBER': return rand.randint(0,100)
        case 'DATE': return f"{rand.randint(1970,2023)}-{str(rand.randint(1,12)).zfill(2)}-{str(rand.randint(1,28)).zfill(2)}"
        case 'STRING': 
            match stringType:
                case 'state': return f"'{randomLine('states')}'"
                case 'city': return f"'{randomLine('cities')}'"
                case 'cname': return f"'{randomLine('firstNames')} {randomLine('lastNames')}'"
                case 'address': return f"'{randomLine('addresses')}'"
                case 'province': return f"'{randomLine('provinces')}'"
                case 'aname': return f"'{randomLine('airports')}'"
                case 'departAirport': return f"'{randomLine('airports')}'"
                case 'arriveAirport': return f"'{randomLine('airports')}'"
                case 'firstName': return f"'{randomLine('firstNames')}'"
                case 'lastName': return f"'{randomLine('lastNames')}'"
                case 'street': return f"'{randomLine('addresses')}'"
                case 'country': return f"'{randomLine('countries')}'"

#? Plan is to use this function to return a string similar to reading 'shipmentDatabase.txt'
def autoGenTableSet():
    #* 1. create rand num of tables
        #* a. rand num gen for amount of tables
        #* b. rand num for rows and columns of each table
        #* c. place each table into an array.
    #* 2. Fill each table with dummy data
        #* a. check dependent columns (cid/pid)
        #* b. save dependents data 
    #* 3. to string each table
    #* contat each table as in 'shipmentDatabase.txt'
    pass

possibleTableNames = getRandomTableNames()
#print(possibleTableNames)
class Table:
    #* Table Attributes
    # tableName
    # tableColumnCount
    # tableColumns = {}
        #* Column Attributes
        # columnName
        # columnUnit
        # TableReferenced
        # columnOfTableReferenced

    def __init__(self, columns=5, joins=0, clauses=[], constraints={}, random=True):
        self.name = possibleTableNames.pop(rand.choice(range(len(possibleTableNames))))
        self.columns= {}
        self.rowLength = rand.randint(4,7)
        self.generateSchema(columns, joins, clauses, constraints)
        self.generateTable()

    def generateSchema(self, columns, joins, clauses, constraints):
        possibleColumns = parseColumnsFromFile('randomColumns')
        for i in range(columns):
            name, unit = possibleColumns.pop(rand.choice(range(len(possibleColumns))))
            self.columns[name] = {
                'name' : name,
                'unit' : unit,
                'references' : None,
                "foreignKey" : None,
                'columnData' : {}
            }
            #print(self.columns[name]['unit'])

    def generateTable(self):
        # generate schema
        
        # generate row data 
        for i in range(self.rowLength):
            for column, column_data in self.columns.items():
                self.columns[column]['columnData'][i] = generateRandom(column_data['unit'], column)

    #* Desired output
    def toString(self):
        output = ''
        for i, column in enumerate(self.columns):
            if i == len(self.columns) - 1:
                output += f"{self.name}.{column}:{self.columns[column]['unit']} \n"
            else:
                output += f"{self.name}.{column}:{self.columns[column]['unit']}, "

        for j in range(self.rowLength):
            for i, column in enumerate(self.columns):
                if i == len(self.columns) - 1:
                    output += f"{self.columns[column]['columnData'][j]} \n"
                else:
                    output += f"{self.columns[column]['columnData'][j]}, "

        return "{\n "+output+" }"















def generateDataset():
    tableString = ''

    return tableString

def parseColumnsFromFile(file):

    # Holds all the columns that can be selected
    possibleColumns = []

    # Reads the text file
    with open(f"./RelaXElementSharedLibrary/{file}.txt") as columnsFile:

        # Iterates over each line
        for line in columnsFile:

            # Only cares about non-whitespace lines
            if line and not line.isspace():

                # Formats the line correctly.
                # Removes leading and trailing whitespace from
                # each word, as deliminated by ',' in the line
                words = [word.strip() for word in line.split(',')]

                # Grabs the parameters
                name = words[0]
                unit = words[1]
                unitOther = None

                possibleColumns.append([name, unit])
            
    # Returns the populated array
    return possibleColumns

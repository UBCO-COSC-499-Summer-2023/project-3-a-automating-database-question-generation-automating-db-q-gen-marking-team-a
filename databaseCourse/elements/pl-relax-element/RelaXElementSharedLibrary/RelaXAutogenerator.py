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
        case 'NUMBER':
            match stringType:
                case 'id': return rand.randint(0,100)
                case 'price': return round(rand.random()*100, 2)
                case 'inventory': return rand.randint(0,50)
                case 'quantity': return rand.randint(0,50)
        case 'DATE': return f"{rand.randint(1955,2023)}-{str(rand.randint(1,12)).zfill(2)}-{str(rand.randint(1,28)).zfill(2)}"
        case 'STRING': 
            match stringType:
                case 'state': return f'"{randomLine("states")}"'
                case 'name': return f"'{randomLine('firstNames')}'"
                case 'city': return f'"{randomLine("cities")}"'
                case 'cname': return f"'{randomLine('firstNames')} {randomLine('lastNames')}'"
                case 'address': return f"'{randomLine('addresses')}'"
                case 'province': return f"'{randomLine('provinces')}'"
                case 'aname': return f'"{randomLine("airports")}"'
                case 'departAirport': return f'"{randomLine("airports")}"'
                case 'arriveAirport': return f'"{randomLine("airports")}"'
                case 'firstName': return f"'{randomLine('firstNames')}'"
                case 'lastName': return f"'{randomLine('lastNames')}'"
                case 'street': return f"'{randomLine('addresses')}'"
                case 'country': return f"'{randomLine('countries')}'"


#? Plan is to use this function to return a string similar to reading 'shipmentDatabase.txt'
possibleTableNames = getRandomTableNames()

def generateDataset(numTables=5) -> dict:
    possibleColumns = parseColumnsFromFile('randomColumns')
    dataset = {}
    # tableNameSet = {}
    depth = rand.randint(1,numTables-2)
    for i in range(numTables):
        if i == 0:
            dataset[i] = Table(columns=rand.randint(3,5), possibleColumns=possibleColumns, joins=2)
        else:    
            dataset[i] = Table(columns=rand.randint(2,4), possibleColumns=possibleColumns, joins=2)
        # tableNameSet[i] = dataset[i].name

    for i in range(depth-1):
        dataset[i].link(dataset[i+1])

    for i in range(depth, numTables):
        dataset[rand.randint(0,depth-1)].link(dataset[i])

    return dataset




class Table:
    #* Table Attributes
    # tableName
    # tableColumnCount
    # tableColumns = {}
        #* Column Attributes
        # columnName
        # column
        # TableReferenced
        # columnOfTableReferenced

    def __init__(self, name=None, columns=5, joins=0, possibleColumns=None, clauses=[], constraints={}, random=True):
        if name is None:
            self.name = possibleTableNames.pop(rand.choice(range(len(possibleTableNames))))
        self.columns= {}
        self.rowLength = rand.randint(4,7)
        self.generateSchema(columns, joins, possibleColumns, clauses, constraints)
        self.generateTable()

    def generateSchema(self, columns, joins, possibleColumns, clauses, constraints):
        for i in range(columns):
            if len(possibleColumns) < 1:
                return
            name, unit = possibleColumns.pop(rand.choice(range(len(possibleColumns))))
            self.columns[name] = {
                'name' : name,
                'unit' : unit,
                'references' : None,
                "foreignKey" : name,
                'columnData' : {}
            }

    def generateTable(self):
        # generate row data 
        for i in range(self.rowLength):
            for column, columnData in self.columns.items():
                self.columns[column]['columnData'][i] = generateRandom(columnData['unit'], column)

    def addColumn(self, name, unit):
        self.columns[name] = {
            'name': name,
            'unit': unit,
            'references': None,
            "foreignKey": name,
            'columnData': {}
        }

    def fillColumn(self, name, columnData):
        for i in range(self.rowLength):
            self.columns[name]['columnData'][i] = rand.choice(columnData)

    def link(self, table):     
        column = (rand.choice(list(self.columns.keys())))
        table.addColumn(name=column, unit=self.columns[column]['unit'])
        table.fillColumn(name=column, columnData=self.columns[column]['columnData'])


        
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

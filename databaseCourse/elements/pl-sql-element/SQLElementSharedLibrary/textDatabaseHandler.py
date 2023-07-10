from os import listdir
from random import choice

# Used for modelling a tables during question generation
# and loading table data from text files

# Returns the file path to the table file
def relativeFilePath(file):
    return f"./SQLElementSharedLibrary/randomTables/{file}.txt"

# Returns the create table statement from the
# text file
def getStaticSchema(file):
    try:
        with open(relativeFilePath(file)) as file:
            return file.read()
    except:
        return None

# Lists all table files in the specified path
def getAllTableFiles(path):
    try:
        # Removes the file extension of all files, if they exist
        return [file[:file.find('.')] for file in listdir(path)]
    except:
        return []


# Models a table for easy question generation
class Table:

    # A table has a name and some columns
    # File name and table name are equivalent
    def __init__(self, file, columns=1, joins=0, clauses=[]):
        self.name = file
        self.columns = {}

        self.load(file, columns, joins, clauses)



    # Loads a table object based on the file.
    # All parameters other than file only matter to
    # random tables, not static tables; for random tables,
    # f"{file}" will become the table name"
    def load(self, file, columns, joins, clauses):
        tableFiles = getAllTableFiles('./SQLElementSharedLibrary/randomTables/')

        if file in tableFiles:
            self.loadFromText(relativeFilePath(file))
        else:
            self.loadRandom(file, columns, joins, clauses)

    # Given the path to a text file, loads its data
    def loadFromText(self, filePath):

        # Contains all the lines of the file
        lines = []

        # Opens the file and iterate over lines
        with open(filePath, 'r') as tableFile:
            for line in tableFile:

                # Does not add the lines if it is whitespace
                if not str.isspace(line):
                    lines.append(line.strip())
        

        # Creates the column and adds it
        # The first line contains the table name so ignore it
        # The last line contains '};' so ignore it
        for line in lines[1:-1]:

            # Gets the words from the line
            words = line.split(' ')

            # Handles the case where the line describes a foreign key
            if 'FOREIGN KEY' in line.upper():

                # Gets the foreign key
                # Removes the parenthesis
                column = words[2][1:-1]

                # Get the table it references
                references = words[4]

                # Gets the column it references
                # Removes parentheses
                foreignKey = words[5][words[5].find('(') + 1 : words[5].find(')')]

                # Checks additional clauses
                isOnUpdateCascade = 'ON UPDATE CASCADE' in line.upper()
                isOnDeleteSetNull = 'ON DELETE SET NULL' in line.upper()

                # Updates the column
                self.columns[column]['references'] = references
                self.columns[column]['foreignKey'] = foreignKey
                self.columns[column]['isOnUpdateCascade'] = isOnUpdateCascade
                self.columns[column]['isOnDeleteSetNull'] = isOnDeleteSetNull

            # Handles the case where the line describes a primary key
            elif 'PRIMARY KEY' in line.upper():
                
                # Gets the primary key
                # Removes the parentheses
                primaryKey = words[2][words[2].find('(') + 1 : words[2].find(')')]

                # Sets the column as a primary key
                self.columns[primaryKey]['isPrimary'] = True

            # Otherwise add the column
            else:

                # The first word is always the name of the column
                name = words[0]

                # The second word is the unit
                # Removes the comma if it is present
                unit = words[1].upper() if ',' not in words[1] else words[1][:-1].upper()

                # If there is some additional clause for the unit, such
                # as the length of a CHAR, grab it and remove parenthesis
                unitOther = None
                if words[1].find('(') != -1:
                    unitOther = unit[unit.find('(') + 1 : unit.find(')')]
                    unit = unit[: unit.find('(')]


                # Checks if the line has a NOT NULL clause
                isNotNull = 'NOT NULL' in line.upper()

                # Adds the column
                self.columns[name] = {
                    'name': name,
                    'unit': unit,
                    'unitOther': unitOther,
                    'isPrimary': False,
                    'isNotNull': isNotNull,
                    'references': None,
                    'foreignKey': None,
                    'isOnUpdateCascade': False,
                    'isOnDeleteSetNull': False

                }



    # Creates a random table
    # TODO
    #   - intentional joins
    #   - clauses
    #   - improve selection source for column names
    def loadRandom(self, name, columns, joins, clauses):

        # Current approach for loading a random table is
        # to create one very large table with all columns
        # from every table and pop them out randomly until
        # we have enough tables
        # 
        # Some issues with this approach is that columns with
        # duplicate names over different tables will override
        # each other. Additionally, it is difficult to specify
        # how many joins you want, and very difficuly to set
        # clauses. Finally, it is barely better than the
        # previous 'random' table generation, where it selects
        # a random table from a list; the only improvement this
        # offers it the columns are swapped around a bit.

        # Creates the mega-table
        selectionTable = Table('airport')

        # Gets all possible tables
        tableFiles = getAllTableFiles('./SQLElementSharedLibrary/randomTables/')

        # Adds ALL columns to the selection table
        for tableFile in tableFiles:
            selectionTable.loadFromText(relativeFilePath(tableFile))

        # Adds columns
        while len(self.columns) < columns:
            pop = selectionTable.columns.pop(choice(list(selectionTable.columns.keys())))
            self.columns[pop['name']] = pop



    # Returns a dictionary with the following mapping:
    #   column: (if the column is a foreign key)
    #       'references': the table referenced
    #       'foreignKey': the column in the referenced table
    def getKeyMap(self):
        return {key: {'references': self.columns[key]['references'], 'foreignKey': self.columns[key]['foreignKey']} for key in self.columns.keys() if self.columns[key]['references']}



    # Returns the table's DDL schema
    def getSchema(self):

        # Creates the first line
        schema = f"CREATE TABLE {self.name}" + " (\n"

        # Adds each column
        for column in self.columns:
            schema += f"\t{self.columns[column]['name']} {self.columns[column]['unit']}"

            # Includes the unit other in parentheses
            if self.columns[column]['unitOther']:
                schema += f"({self.columns[column]['unitOther']})"
            
            # Includes the not null clause if necessary
            if self.columns[column]['isNotNull']:
                schema += ' NOT NULL'

            # Adds a comma at the end
            schema += ',\n'
        


        # Adds the primary keys
        for column in self.columns:

            # Adds a primary key
            if self.columns[column]['isPrimary']:

                # For the first primary key
                if "PRIMARY KEY" not in schema:
                    schema += f"\tPRIMARY KEY ({self.columns[column]['name']}"
                # For all subsequent primary keys
                else:
                    schema += f", {self.columns[column]['name']}"
        
        # Finishes the line, if necessary
        if "PRIMARY KEY" in schema:
            schema += "),\n"



        # Adds the foreign keys
        for column in self.columns:
            if self.columns[column]['references']:
                schema += f"\tFOREIGN KEY ({self.columns[column]['name']}) REFERENCES {self.columns[column]['references']} ({self.columns[column]['foreignKey']})"

                # Set null clause
                if self.columns[column]['isOnDeleteSetNull']:
                    schema += ' ON DELETE SET NULL'

                # Cascade clause
                if self.columns[column]['isOnUpdateCascade']:
                    schema += ' ON UPDATE CASCADE'

                # Comma and newline
                schema += ",\n"
        
        # Removes the comma at the end; closes schema
        schema = schema[0:-2] + "\n);"

        return schema



    def __str__(self):
        # The Column __str__() function didn't want to work so
        # instead here's some gross list comprehension
        return f"{self.name}: " + str([f"{column['name']}: {column['unit']}" for column in self.columns.values()])

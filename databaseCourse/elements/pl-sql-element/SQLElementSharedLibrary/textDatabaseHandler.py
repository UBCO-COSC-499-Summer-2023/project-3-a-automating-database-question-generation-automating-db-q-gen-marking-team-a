from os import listdir

# Used for modelling a database during question generation
# and loading database data from text files

# Returns the create table statement for a database,
# which is just the text in the database file
def getDDL(filePath):
    with open(filePath) as file:
        return file.read()

# Loads a database object based on the file
def load(filePath):
    return Database(filePath)

# Lists all database files in the specified path
def getAllDatabaseFiles(path):
    # Removes the file extension of all files, if they exist
    return [file[:file.find('.')] for file in listdir(path)]


# Models a database for easy question generation
class Database:

    # A database has a name and some columns
    def __init__(self, filePath):
        self.name = ''
        self.columns = {}

        # Loads the name and columns
        self.loadDatabase(filePath)

    # Given the path to a text file, loads its data
    def loadDatabase(self, filePath):

        # Contains all the lines of the file
        lines = []

        # Opens the file and iterate over lines
        with open(filePath, 'r') as databaseFile:
            for line in databaseFile:

                # Does not add the lines if it is whitespace
                if not str.isspace(line):
                    lines.append(line.strip())
        
        # Gets the database name
        self.name = lines[0].split(' ')[2]

        # Creates the column and adds it
        # The first line contains the database name so ignore it
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

    # Returns a dictionary with the following mapping:
    #   column: (if the column is a foreign key)
    #       'references': the database referenced
    #       'foreignKey': the column in the referenced database
    def getKeyMap(self):
        return {key: {'references': self.columns[key]['references'], 'foreignKey': self.columns[key]['foreignKey']} for key in self.columns.keys() if self.columns[key]['references']}

    def __str__(self):
        # The Column __str__() function didn't want to work so
        # instead here's some gross list comprehension
        return f"{self.name}: " + str([f"{column['name']}: {column['unit']}" for column in self.columns.values()])

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

        # Sets the name
        self.name = name

        # Gets the columns used to build a table
        possibleColumns = self.parseColumnsFromFile('randomColumns')
        


        # Keeps adding columns until there are enough
        while len(self.columns) < columns:

            # Chooses a random column to add
            # Pops the column to ensure no duplicates
            addColumn = possibleColumns.pop(choice(range(len(possibleColumns))))
            
            # Grabs parameters
            columnName = addColumn[0]
            columnUnit = addColumn[1]

            # Grabs the unit specification as necessary
            columnUnitOther = None
            match columnUnit:
                case 'DECIMAL': columnUnitOther = f"{choice(addColumn[2])},{choice(addColumn[3])}"
                case 'CHAR': columnUnitOther = f"{choice(addColumn[2])}"
                case 'VARCHAR': columnUnitOther = f"{choice(addColumn[2])}"
            

            # Adds the column
            self.columns[columnName] = {
                    'name': columnName,
                    'unit': columnUnit,
                    'unitOther': columnUnitOther,
                    'isPrimary': False,
                    'isNotNull': False,
                    'references': None,
                    'foreignKey': None,
                    'isOnUpdateCascade': False,
                    'isOnDeleteSetNull': False
                }

    # Given a marked-up textfile, return an array
    # of possible columns for random table generation.
    # A helper function for loadRandom
    def parseColumnsFromFile(self, file):

        # Holds all the columns that can be selected
        possibleColumns = []

        # Reads the text file
        with open(f"./SQLElementSharedLibrary/{file}.txt") as columnsFile:

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



                    # % is used as a placeholder and is replaced
                    # with the first letter of the respective table's
                    # name
                    if '%' in name:
                        name = name.replace('%', self.name[0:1].lower())

                    # Handles the cases where the unitOther is not none
                    if 'DECIMAL' == unit or 'CHAR' == unit or 'VARCHAR' == unit:
                        unitOther = self.parseRange(words[2])
                        
                        # Decimal needs two bits of data to
                        # describe its unitOther; hence length of 4
                        if unit == 'DECIMAL':
                            possibleColumns.append([name, unit, unitOther, self.parseRange(words[3])])
                        # The other columns with uniOther only require 3
                        else:
                            possibleColumns.append([name, unit, unitOther])
                    
                    # Adds columns without unitOther
                    else:
                        possibleColumns.append([name, unit])
            
        # Returns the populated array
        return possibleColumns

    # Given a range in the form of `xx-yy-zz` or
    # `xx-yy`, returns a range. If there is no `-`,
    # then return it unchanged as a string.
    # A helper funciton of parseColumnsFromFile()
    def parseRange(self, string):

        # Checks if it is a range
        if '-' in string:

            # Split over '-'
            split = string.split('-')

            # The format is:
            #   First item is the start
            #   Second item is the stop (inclusive!)
            #   Third item is the step (optional)
            start = int(split[0])
            stop = int(split[1]) + 1

            # Obtains the step, if it is included.
            # otherwise it defualts to 1
            step = 1
            if len(split) > 2:
                step = int(split[2])
            
            # Returns the range
            return range(start, stop, step)
        
        # If it is not a range, return as a string
        else:
            return f"{string}"


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

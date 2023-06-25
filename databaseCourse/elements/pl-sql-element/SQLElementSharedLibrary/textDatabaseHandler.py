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
            if 'FOREIGN KEY' in line:

                # Gets the foreign key
                # Removes the parenthesis
                foreignKey = words[2][1:-1]

                # Get the table it references
                references = words[4]

                # Checks additional clauses
                isOnUpdateCascade = 'ON UPDATE CASCADE' in line
                isOnDeleteSetNull = 'ON DELETE SET NULL' in line

                # Updates the column
                self.columns[foreignKey]['references'] = references
                self.columns[foreignKey]['isOnUpdateCascade'] = isOnUpdateCascade
                self.columns[foreignKey]['isOnDeleteSetNull'] = isOnDeleteSetNull

            # Handles the case where the line describes a primary key
            elif 'PRIMARY KEY' in line:
                
                # Gets the primary key
                # Removes the parenthesis
                primaryKey = words[2][1:-1]

                # Sets the column as a primary key
                self.columns[primaryKey]['isPrimary'] = True

            # Otherwise add the column
            else:

                # The first word is always the name of the column
                name = words[0]

                # The second word is the unit
                # Removes the comma if it is present
                unit = words[1] if ',' not in words[1] else words[1][:-1]

                # Checks if the line has a NOT NULL clause
                isNotNull = 'NOT NULL' in line

                # Adds the column
                self.columns[name] = {
                    'name': name,
                    'unit': unit,
                    'isPrimary': False,
                    'isNotNull': isNotNull,
                    'references': None,
                    'isOnUpdateCascade': False,
                    'isOnDeleteSetNull': False

                }


    def __str__(self):
        # The Column __str__() function didn't want to work so
        # instead here's some gross list comprehension
        return f"{self.name}: " + str([f"{column.name}: {column.unit}" for column in self.columns])


# Models a column of a database
class Column:

    # A column has a name and a unit
    def __init__(self, databaseLine):
        # Gets the words from the lines
        words = databaseLine.split(' ')

        # Sets the column name
        self.name = words[0]

        # Sets the column unit
        # Removes the trailing comma, if there is one
        self.unit = words[1] if ',' not in words[1] else words[1][:-1]

        self.isPrimary = False

        self.isNotNull = False

        self.references = None
        self.isOnUpdateCascade = False
        self.isOnDeleteSetNull = False
        
        


        
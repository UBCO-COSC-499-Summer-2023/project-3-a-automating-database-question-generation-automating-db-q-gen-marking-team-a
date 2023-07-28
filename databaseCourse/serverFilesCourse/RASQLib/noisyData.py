# This file generates data to populate dummy tables
# for randomly generated questions.

import random
from string import ascii_uppercase
import os

# Generates random data based on the unit type
def generateNoisyData(table, key, qty=1):

    # Checks whether this colomn is unique
    unique = isUnique(table, key)
    
    # Chooses the random selection procedure
    choose = None

    # Pops items from a list, ensuring no
    # duplicated since the files contain
    # no duplicates
    if unique:
        choose = popRandom
    
    # Selects items from a list, so there
    # may be duplicates even if the file
    # contains no duplicates
    else:
        choose = selectRandom

    # If the column passed has a clean data
    # file, then choose items from said file.
    if key in getColumnToFileMap().keys():
        return generateFromFile(qty, readLines(getColumnToFileMap()[key]), choose)

    # Also checks but removing the first letter
    # due to table aliasing
    if  key[1:] in getColumnToFileMap().keys():
        return generateFromFile(qty, readLines(getColumnToFileMap()[key[1:]]), choose)
    

    # If the column does not correspond to a file,
    # then generete the data randomly
    return generateNoisyDataNoFile(table, key, qty, unique)

# Returns data if there is no corresponding file
def generateNoisyDataNoFile(table, key, qty=1, unique=False):
    if table.isSQL:
        return generateNoisyDataNoFileSQL(table, key, qty, unique)
    else:
        return generateNoisyDataNoFileRelaX(table, key, qty, unique)

def generateNoisyDataNoFileSQL(table, key, qty=1, unique=False):
    
    # Grabs the important information
    unit = table.columns[key]['unit']
    unitOther = table.columns[key]['unitOther']
    
    # Match on the unit type if the key is not
    # found in the file map
    match unit:
        # Integers
        case 'INTEGER': return generateNoisyInteger(unique, qty)

        # Decimals require total digits plus decimal precision
        case 'DECIMAL': return generateRandomDecimal(unique, qty, unitOther)

        # CHARs require the number of characters
        case 'CHAR': return generateNoisyChar(unique, qty, int(unitOther))

        # VARCHARs are capped at a length of 8 to prevent
        # a string of 50 random characters
        case 'VARCHAR': return generateNoisyVarchar(unique, qty, min(int(unitOther), 8))

        # DATE and DATETIME
        case 'DATE': return generateRandomDate(unique, qty)
        case 'DATETIME': return generateRandomDateTime(unique, qty)

        # Crash if the datatype is not correct
        case _: return None
        
def generateNoisyDataNoFileRelaX(table, key, qty=1, unique=False):

    # Grabs the important information
    unit = table.columns[key]['unit']

    # Match on the unit type if the key is not
    # found in the file map
    match unit:
        case 'NUMBER':
            
            # We don't have decimals in RelaX so check on the
            # key name instead
            if key == 'price':
                return generateRandomDecimal(unique, qty, '6,2')
            
            else:
                return generateNoisyInteger(unique, qty)

        case 'DATE': return generateRandomDate(unique, qty)
        case 'STRING': return generateNoisyVarchar(unique, qty, 6)



# Generates a random integer in the range 0 to 1000
def generateNoisyInteger(unique, qty):

    # Holds the values to be returned
    values = []
    
    # Adds values until there are enough
    while len(values) < qty:

        # A range of 1 to 1000 is good for most integers
        tryValue = random.randint(1, 1000)
        
        # Ensures no duplicated, if necessary
        if not (unique and tryValue in values):
            values.append(tryValue)
    
    return values


# Generates a random decimal, as specified by the unit
def generateRandomDecimal(unique, qty, unitOther):

    # Grabs the whole and decimal portions of the string
    whole, decimal = unitOther.split(',')

    # Converts the strings into integers
    whole = int(whole)
    decimal = int(decimal)

    # Creates a random decimal values
    # Ensures the final digit is either a 0 or a 5,
    # since it looks better than a purely random number.
    # Plus, decimals are mostly used for currency.
    randomDecimal = str(random.randint(0, 10 ** (decimal - 1) - 1)) + random.choice(['0', '5'])
    

    
    # Gives an exponentially greater likelihood that
    # smaller numbers are returned. Otherwise, it
    # would be linearly more likely that large
    # numbers appear. In other words, increases the
    # odds the random number looks good.
    choices = []
    weights = []
    for i in range(whole - decimal):
        choices.append(i + 1)
        weights.append(2 ** (whole - i))



    # Holds the values
    values = []

    # Keeps populating values
    while len(values) < qty:

        # Chooses a max order of magnitude for the size
        # of the whole number, where small orders of
        # magnitude are preferred
        randomPower = random.choices(choices, weights)

        # Creates the whole number
        randomWhole = random.randint(5, 10 ** randomPower[0])

        # Ensures no duplicated, if necessary
        tryValue = float(f"{randomWhole}.{randomDecimal}")
        if not (unique and tryValue in values):
            values.append(tryValue)

    return values


# Generates a random string of length unitOther
def generateNoisyChar(unique, qty, unitOther):

    # Holds the values to be returned
    values = []
    
    # Adds values until there are enough
    while len(values) < qty:

        # Creates a random string of specified length
        tryValue = ''.join(random.choice(ascii_uppercase + '1234567890') for i in range(unitOther))
        
        # Ensures no duplicated, if necessary
        if not (unique and tryValue in values):
            values.append(tryValue)
    
    return values

# Generates a random string up to length unitOther
def generateNoisyVarchar(unique, qty, unitOther):

    # Holds the values to be returned
    values = []
    
    # Adds values until there are enough
    while len(values) < qty:

        # Creates a random string of somewhat-specified length.
        # The array indexing removes the value from the array
        tryValue = generateNoisyChar(unique, 1, random.randint(1, unitOther))[0]
        
        # Ensures no duplicated, if necessary
        if not (unique and tryValue in values):
            values.append(tryValue)
    
    return values

        

# Generates a random date between 1955 and 2023
def generateRandomDate(unique, qty):

    # Holds the values to be returned
    values = []
    
    # Adds values until there are enough
    while len(values) < qty:

        # Generates a random month
        month = random.randint(1, 12)
        
        # Ensures the day is valid.
        # And no, I'm not doing the legwork to check
        # whether or not it's a leapyear and thus
        # allow a 29th day in February
        day = -1
        if month < 8:
            if month % 2 == 1:
                day = random.randint(1, 31)
            elif month == 2:
                day = random.randint(1, 28)
            else:
                day = random.randint(1, 30)
        else:
            if month % 2 == 1:
                day = random.randint(1, 30)
            else:
                day = random.randint(1, 31)

        # the ':02' formatting ensures that the length of the
        # string is a minimum of 2, padded left with zeroes
        tryValue = f"{random.randint(1955, 2023)}-{month:02}-{day:02}"

        # Ensures no duplicated, if necessary
        if not (unique and tryValue in values):
            values.append(f"{random.randint(1955, 2023)}-{month:02}-{day:02}")

    return values

# Generates a random date time between 1955 and now
def generateRandomDateTime(unique, qty):

    # Holds the values to be returned
    values = []
    
    # Adds values until there are enough
    while len(values) < qty:

        # The minutes portion can be any increment of 5 minutes.
        # the ':02' formatting ensures that the length of the
        # string is a minimum of 2, padded left with zeroes.
        # The array indexing removes the value from the array
        tryValue = f"{generateRandomDate(unique, 1)[0]} {random.randint(0, 23):02}:{random.randint(0, 11) * 5:02}:00"

        # Ensures no duplicated, if necessary
        if not (unique and tryValue in values):
            values.append(tryValue)

    return values

# Given an array of choices and a method of selection choose,
# returns an array of data of size quantity
def generateFromFile(qty, choices, choose):
    return [choose(choices) for i in range(qty)]



# Generates one row's worth of noisy data
def generateColumns(table, qty=1):
    return {key: generateNoisyData(table, key, qty) for key in table.columns.keys()}



# Returns the filepath to a specific noisy data file
def relativeFilePath(file):
    return f"{absoluteDirectoryPath()}/noisyData/{file}.txt"

# Returns the absolute directory of RASQLib
def absoluteDirectoryPath():
    currentDirectory = os.path.abspath(os.curdir)

    if 'RASQLib' in currentDirectory:
        return currentDirectory
    else:
        courseFile = currentDirectory[:currentDirectory.find('/elements')]
        return f"{courseFile}/serverFilesCourse/RASQLib"
    
# Reads all lines from a specified file
def readLines(fileName):
    try:
        with open(relativeFilePath(fileName)) as file:
            return [line.strip() for line in file.readlines() if not line.isspace()]
    except:
        return None



# Returns the mapping between column name and
# the file which contains its clean data
def getColumnToFileMap(path=f"{absoluteDirectoryPath()}/randomTableData/columnToFile.txt"):
    try:
        # Reads the file
        with open(path) as file:
            lines = [line.strip() for line in file.readlines() if not line.isspace()]

        # Splits over the colon, such that 
        # the dictionary has the form...
        #   column name: file name
        return {line[0: line.find(':')]: line[line.find(':') + 1:] for line in lines}
    except:
        return None



# Checks if this column disallows duplicate values.
# SQLite requires that PKs and FKs are unique
def isUnique(table, key):
    return table.columns[key]['isPrimary'] or table.columns[key]['references'] or table.columns[key]['isUnique']



# Given a list, pops and returns a random item
# Repeated calls on the same unique list will not return duplicate values
def popRandom(values, weights=[]):
    
    # If weigths are not supplied, pop a random item and return it
    if not weights:
        return values.pop(random.choice(range(len(list(values)))))
    
    # Chooses a random index
    randomIndex = random.choice(range(len(list(values))))

    # Remove that item from the weights list, in case this method is called
    # again with the same weights list
    weights.pop(randomIndex)

    # Return the corresponding value
    return values.pop()

# Given a list, returns a random values.
# Repeated calls on the same unique list may return duplicate values
def selectRandom(values, weights=[]):
    if not weights:
        return random.choice(list(values))
    
    return random.choices(list(values), weights)[0]
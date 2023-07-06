# This file generates data to populate dummy tables
# for randomly generated questions.

import random
from math import log10
from string import ascii_uppercase

# Generates random data based on the unit type
def generateNoisyData(database, key):
    
    # Grabs the important information
    unit = database.columns[key]['unit']
    unitOther = database.columns[key]['unitOther']

    # Matches on the unit type
    match unit:
        # Integers
        case 'INTEGER': return generateNoisyInteger()

        # Decimals require total digits plus decimal precision
        case 'DECIMAL': return generateRandomDecimal(unitOther)

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

# Generates a random decimal, as specified by the unit
def generateRandomDecimal(unitOther):

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
    


    # Generates a random whole number
    
    # Gives an exponentially greater likelihood that
    # smaller numbers are returned. Otherwise, it
    # would be linearly more likely that large
    # numbers appear
    choices = []
    weights = []
    for i in range(whole - decimal):
        choices.append(i + 1)
        weights.append(2 ** (whole - i))

    # Chooses a max order of magnitude for the size
    # of the whole number, where small orders of
    # magnitude are preferred
    randomPower = random.choices(choices, weights)

    # Creates the whole number
    randomWhole = random.randint(5, 10 ** randomPower[0])

    # Formats and returns
    return float(f"{randomWhole}.{randomDecimal}")


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
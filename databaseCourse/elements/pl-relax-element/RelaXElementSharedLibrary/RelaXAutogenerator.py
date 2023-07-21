import random as rand

# This allows DroneCI to see the RASQLib module
import sys
sys.path.append('/drone/src/databaseCourse/serverFilesCourse/')

from RASQLib import textDatabaseHandler as db
from RASQLib import noisyData as nd


# A very basic autogenerate function.
# At the moment, all it does is create a database
# and load it into the data variable.
#
# The functionality that was previously in
# this file has been moved to the database
# and table objects file
def autogenerate(data):
    
    # Generates a random database
    columns = rand.randint(4, 7)
    joins = rand.randint(2, 5)
    rows = rand.randint(5, 15)
    database = db.Database(isSQL=False, columns=columns, joins=joins, rows=rows)

    # Loads the database into the data variable
    database.loadDatabase(data)

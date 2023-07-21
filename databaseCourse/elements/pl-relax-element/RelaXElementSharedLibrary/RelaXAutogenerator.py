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

class Question:
    Query = "π "

    selectStatement = "σ"
    ClauseArray = { "∧", "∨", "¬", "=", "≠", "≥", "≤", ">", "<"}

    orderByStatement = "τ"
    groupByStatement = " γ"

    crossJoin = "⨯"
    naturalJoin = "⨝"
    outerRightJoins="⟖"
    outerLeftJoins="⟕"
    outerFullJoins="⟗"
    semiRightJoins="⋉"
    semiLeftJoins="⋊"
    antiJoins="▷"

    def  __init__(self, dataset, attribDict,
                    numClauses=0,
                    orderBy=False,
                    groupBy=False,
                    numCrossJoins=0,
                    numNaturalJoins=0,
                    numOuterRightJoins=0,
                    numOuterLeftJoins=0,
                    numOuterFullJoins=0,
                    numSemiRightJoins=0,
                    numSemiLeftJoins=0,
                    numAntiJoins=0) -> None:
        
        attribDict



        self.numClauses=numClauses
        self.orderBy=orderBy
        self.groupBy=groupBy
        self.numCrossJoins=numCrossJoins
        self.numNaturalJoins=numNaturalJoins
        self.numOuterRightJoins=numOuterRightJoins
        self.numOuterLeftJoins=numOuterLeftJoins
        self.numOuterFullJoins=numOuterFullJoins
        self.numSemiRightJoins=numSemiRightJoins
        self.numSemiLeftJoins=numSemiLeftJoins
        self.numAntiJoins=numAntiJoins
        
        return self

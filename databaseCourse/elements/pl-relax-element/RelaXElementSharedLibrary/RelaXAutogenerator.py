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
    joins = rand.randint(2, 5) #! Change to joins/rand -> whichever is bigger
    rows = rand.randint(5, 15)
    database = db.Database(isSQL=False, columns=columns, joins=joins, rows=rows)

    question = Question(dataset=database, attribDict=data['params']['attrib_dict'])
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

    def  __init__(self, dataset, attribDict) -> None:
        

        # Join first -- may need recursive function

        
        table = rand.choice(list(dataset.tableSet.keys()))
        table = dataset.tableSet[table]
        joinDict = {}
        print(dataset)
        for i in range(attribDict['numJoins']):
            for column in table.columns:
                if table.columns[column]['references']:
                    referencedName = table.columns[column]['references']
            joinDict[table.name] = referencedName

            table = dataset.tableSet[referencedName]
        
        print(joinDict)
    
        # Project Second

        # Select third

        # order by / Group by last


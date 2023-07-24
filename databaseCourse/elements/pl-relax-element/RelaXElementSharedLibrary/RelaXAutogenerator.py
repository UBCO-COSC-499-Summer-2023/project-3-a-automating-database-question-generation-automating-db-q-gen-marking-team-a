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
def returnGreater(num1, num2):
    return num1 if num1 > num2 else num2

def autogenerate(data):
    
    # Generates a random database
    columns = rand.randint(4, 7)
    joins = rand.randint(2, 5) #! Change to joins/rand -> whichever is bigger
    rows = rand.randint(5, 15)
    

    database = db.Database(isSQL=False, columns=columns, joins=returnGreater(joins, data['params']['attrib_dict']['numJoins']), rows=rows)

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
        tableDict = {}
        for table in dataset.tableSet:
            for column in dataset.tableSet[table].columns:
                if dataset.tableSet[table].columns[column]['references']:
                    if column not in tableDict or column not in tableDict.keys():
                        #print(table)
                        tableDict[dataset.tableSet[table].columns[column]['references']] = []
                        tableDict[dataset.tableSet[table].columns[column]['references']].append(table)
        print(tableDict)

        keys_list = list(tableDict.keys())
        selected_key = rand.choice(keys_list)
        output = tableDict.pop(selected_key)
        # Project Second

        # Select third 

        # order by / Group by last


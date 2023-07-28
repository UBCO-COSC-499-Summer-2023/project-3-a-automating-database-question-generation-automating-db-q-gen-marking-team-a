import random as rand

# This allows DroneCI to see the RASQLib module
import sys
sys.path.append('databaseCourse/serverFilesCourse/')
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
    joins = returnGreater(rand.randint(2,5), (data['params']['attrib_dict']['numJoins'])) #! Change to joins/rand -> whichever is bigger
    rows = rand.randint(5, 15)
    
    database = db.Database(isSQL=False, columns=columns, joins=joins, rows=rows)

    question = Question(dataset=database, attribDict=data['params']['attrib_dict'])
    # Loads the database into the data variable
    # print(question.getText())
    print(question.getQuery())
    database.loadDatabase(data)

class Question:
    Query = "π "

    joinSection = ""

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
        

        #* Join first -- may need recursive function
        # number of joins for the question
        numJoins = attribDict['numJoins']
        graph = {}
        for table in dataset.tableSet:
            print(table)
            connections = []
            for column in dataset.tableSet[table].columns:
                if dataset.tableSet[table].columns[column]['references']:
                    print(f"    {dataset.tableSet[table].columns[column]['references']}")
                    connections.append(dataset.tableSet[table].columns[column]['references'])
            graph[table] = connections
        table = rand.choice(list(dataset.tableSet.keys()))
        #randomWalk(graph=graph, startNode=table, numConn=3)
        subgraph = randomSubgraph(graph=graph, n=numJoins)
        joinList = []
        while not set(joinList) == set(subgraph.keys()):
            for node in subgraph:
                if len(joinList) == 0:
                    joinList.append(node)
                for connection in subgraph[node]:
                    if connection in joinList and node not in joinList:
                        joinList.append(node)


        usableColumns = []
        for table in list(subgraph.keys()):
            for column in dataset.tableSet[table].columns:
                usableColumns.append(dataset.tableSet[table].columns[column]['name'])
        #* Projection

        projectedColumns = projection(usableColumns)
        print(projectedColumns)
        
        #* Selection
        selectedColumns = []
        for i in range(rand.randint(1,3)):
            randColumn = rand.choice(usableColumns)
            while randColumn in selectedColumns:
                randColumn =  rand.choice(usableColumns)
            selectedColumns.append(selection(usableColumns, randColumn, subgraph, dataset))

        print(selectedColumns)
        # place tables that have keys newxt to eachother                       
        self.Query = f"{self.Query} {','.join(projectedColumns)} ({self.selectStatement} {' ∨ '.join(selectedColumns)} ({self.naturalJoin.join(joinList)}))"

    def getQuery(self):
        return self.Query

def projection(usableColumns):
    projectedColumns = []
    for i in range(rand.randint(2,5)):
        randColumn = rand.choice(usableColumns)
        while randColumn in projectedColumns:
            randColumn =  rand.choice(usableColumns)
        projectedColumns.append(randColumn)

    return projectedColumns


        
def selection(usableColumns, randColumn,subgraph, dataset):
    for table in subgraph.keys():
        for column in dataset.tableSet[table].columns:
            if randColumn == dataset.tableSet[table].columns[column]['name']:
                match(dataset.tableSet[table].columns[column]['unit']):
                    case 'STRING': return f"{randColumn} = '{rand.choice(dataset.tableSet[table].rows[column])}'" 
                    case 'NUMBER': return f"{randColumn} {rand.choice([ '≥', '≤', '>', '<'])} {rand.choice(dataset.tableSet[table].rows[column])}"
                    case 'DATE': return f"{randColumn} {rand.choice([ '≥', '≤', '>', '<'])} Date('{rand.choice(dataset.tableSet[table].rows[column])}')"
                #print(f"Selection string '{rand.choice(dataset.tableSet[table].rows[column])}'")
                #selectedColumns.append(randColumn)


def dfs(graph, startNode, visited=set(), n=1):
    visited.add(startNode)
    if len(visited) > n:
        return visited
    for child in graph[startNode]:
        if child not in visited:
            dfs(graph, child, visited, n)
            if len(visited) > n:
                return visited
    return visited

def randomSubgraph(graph, n):
    startNode = rand.choice(list(graph.keys()))
    connectedNodes = dfs(graph, startNode, n=n)
    return {node: graph[node] for node in connectedNodes}



#         table = rand.choice(list(dataset.tableSet.keys()))
#         table = dataset.tableSet[table]
#         tableDict = {}
#         for table in dataset.tableSet:
#             for column in dataset.tableSet[table].columns:
#                 if dataset.tableSet[table].columns[column]['references']:
#                     if column not in tableDict:
#                         #print(table)
#                         tableDict[dataset.tableSet[table].columns[column]['references']] = []
#                         tableDict[dataset.tableSet[table].columns[column]['references']].append(table)
#         print(tableDict)
#         keysList = list(tableDict.keys())
#         selectedKey = rand.choice(keysList)
#         joinedTables = []

#         randomWalk(tableDict, selectedKey)

#         for name in tableDict:
#             print(name)
#         for i in range(numJoins):
#             # keysList = list(tableDict.keys())
#             # selectedKey = rand.choice(keysList)
#             # keysList.remove(selectedKey)
#             if selectedKey in tableDict.keys():
#                 output = tableDict.pop(selectedKey)
#             else:
#                 for tableName in joinedTables:
#                     if tableName is tableDict.keys():
#                         output = tableDict.pop(tableName)
#                         print(f"hello: {tableName}")


#             if i == 0:
#                 self.joinSection = selectedKey + self.naturalJoin + output[0]
#             # else:
#                 self.joinSection = self.joinSection + self.naturalJoin + output[0]
#             selectedKey = output[0]
#             joinedTables.append(output[0])

#         print(self.joinSection)
#         # Project Second

#         # Select third 

#         # order by / Group by last


# # Function to perform a random walk on the tree
# def randomWalk(tree, startNode):
#     visited = set()
#     current_node = startNode

#     while current_node is not None:
#         visited.add(current_node)
#         print(current_node, end=" -> ")

#         # Get the children nodes of the current node
#         children = tree.get(current_node)

#         # Filter children to exclude previously visited nodes
#         unvisitedChildren = [child for child in children if child not in visited]

#         if unvisitedChildren:
#             # Choose a random unvisited child node
#             current_node = rand.choice(unvisitedChildren)
#         else:
#             # No unvisited children, end the walk
#             break

#     print("END")
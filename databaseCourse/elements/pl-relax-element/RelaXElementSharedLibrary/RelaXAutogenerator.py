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

def createPreview(data):
    #con = sqlite3.connect("preview.db")
    #cur  = con.cursor()

    commands = data['params']['db_initialize_create'].replace('\n', '').replace('\t', '')
    commands += data['params']['db_initialize_insert_frontend'].replace('\n', '').replace('\t', '')

    #cur.executescript(commands)
    #con.commit()

    correctAnswer = data['correct_answers']['RelaXEditor']
    expectedCode = correctAnswer.replace('\n', ' ').replace('\t', ' ')

    #expectedAns = cur.execute(expectedCode)
    dataRows = expectedAns.fetchall()

    columnNames = [description[0] for description in cur.description]

    htmlTable = "<div class='expectedOutput'><b>Expected Output:</b><div class='scrollable'><table class='output-tables'><thead>"

    for column in columnNames:
        htmlTable += "<th>" + str(column) + "</th>"

    htmlTable += "</thead>"

    for row in dataRows:
        rowString = "<tr>"
        for x in row:
            rowString+= "<th>" + str(x) + "</th>"
        rowString += "</tr>"
        htmlTable += rowString

    htmlTable += "</table></div></div>"

    return htmlTable

def autogenerate(data):

    #expectedOutput = data['params']['html_params']['expectedOutput']
    #if expectedOutput:
    #    data['params']['expectedOutput'] = createPreview(data)
    # Generates a random database
    columns = rand.randint(4, 7)
    joins = returnGreater(rand.randint(2,5), (data['params']['attrib_dict']['numJoins'])) #! Change to joins/rand -> whichever is bigger
    rows = rand.randint(5, 15)
    
    database = db.Database(isSQL=False, columns=columns, joins=joins, rows=rows)

    question = Question(dataset=database, attribDict=data['params']['attrib_dict'])
    # Loads the database into the data variable
    database.loadDatabase(data)
    question.loadQuestion(data)

class Question:
    Query = "π "

    joinSection = ""

    selectStatement = "σ"
    ClauseArray = { "∧", "∨", "¬", "=", "≠", "≥", "≤", ">", "<"}

    orderByStatement = "τ"
    groupByStatement = "γ"

    crossJoin = "⨯"
    naturalJoin = "⨝"
    outerRightJoins="⟖"
    outerLeftJoins="⟕"
    outerFullJoins="⟗"
    semiRightJoins="⋉"
    semiLeftJoins="⋊"
    antiJoins="▷"

    def  __init__(self, dataset, attribDict) -> None:
        #* Load all attribs from data
        self.numJoins = attribDict['numJoins']
        self.numClauses = attribDict['numClauses']
        self.orderByBool = attribDict['orderBy']
        self.groupByBool = attribDict['groupBy']
        self.antiJoinBool = attribDict['AntiJoin']
        self.outerJoinBool = False
        self.semiJoinBool = False
        #* Join first -- may need recursive function
        # number of joins for the question
        if self.semiJoinBool or self.outerJoinBool or self.antiJoinBool:
            self.numJoins = 1

        graph = dataset.toGraph()
        subgraph = randomSubgraph(graph=graph, n=self.numJoins)
        
        self.JoinList = []
        #* Partial Outer Joins
        #  for all rows from table1, null where not exist table2
        #  More ⟕ Less where column less = null 
        if self.outerJoinBool:
            pass

        #* Semi Joins
        #  for row from table1 where match exists in table2
        #  Less ⋊ More
        elif self.semiJoinBool: 
            pass
        #* Anti Joins --> bigger ▷ smaller
        #  for row from table1 not in table2
        elif self.antiJoinBool:
            node1 = rand.choice(list(subgraph.keys()))
            print(node1)
    
            connections = subgraph[node1]
            node2 = rand.choice(connections)

            for column in dataset.tableSet[node1].columns: 
                if dataset.tableSet[node1].columns[column]['references'] == node2:
                    compareColumn = dataset.tableSet[node1].columns[column]["name"]
            
            print(compareColumn)
            
            print(f"node1 {len(set(dataset.tableSet[node1].rows[compareColumn]))}, node2 {len(set(dataset.tableSet[node2].rows[compareColumn]))}")
            if len(set(dataset.tableSet[node1].rows[compareColumn])) > len(set(dataset.tableSet[node2].rows[compareColumn])):
                self.joinStatement = f"{node1}{self.antiJoins}{node2}"
                self.tableListText = f"where <b>{compareColumn}</b> is not in <b>{node2}</b>"
                self.JoinList = [node1]
            else:
                self.joinStatement = f"{node2}{self.antiJoins}{node1}"
                self.tableListText = f"where <b>{compareColumn}</b> is not in <b>{node1}</b>"
                self.JoinList = [node2]
        else:
        
            while not set(self.JoinList) == set(subgraph.keys()):
                for node in subgraph:
                    if len(self.JoinList) == 0:
                        self.JoinList.append(node)
                    for connection in subgraph[node]:
                        if connection in self.JoinList and node not in self.JoinList:
                            self.JoinList.append(node)

            self.joinStatement =f"{self.naturalJoin.join(self.JoinList)}"

            self.tableListText = ", ".join(self.JoinList)
            parts = self.tableListText.rsplit(",", 1)  # Split the string from the right side only once
            self.tableListText = f"<b>{' and'.join(parts)}</b>"

        # neededColumns are one random column from each joined graph 
        # such that all joined tables are utilized in output
        neededColumns = []
        numArray = []
        # usableColumns are all Columns from joined graphs.
        usableColumns = []
        for table in self.JoinList:
            num = rand.randint(0, len(dataset.tableSet[table].columns)-1)
            while num in numArray:
                num = rand.randint(0, len(dataset.tableSet[table].columns))
            numArray.append(num)
            i = 0
            for column in dataset.tableSet[table].columns:
                usableColumns.append(dataset.tableSet[table].columns[column]['name'])
                if i == num:
                   neededColumns.append(dataset.tableSet[table].columns[column]['name']) 
                i+=1
            
        print(neededColumns)
        #* Projection
        projectedColumns = projection(usableColumns)
        if not self.groupByBool:
            self.projectedColumnText = ", ".join(projectedColumns)
            parts = self.projectedColumnText.rsplit(",", 1)  # Split the string from the right side only once
            self.projectedColumnText = f'<b>{" and".join(parts)}</b>'
            #print(self.projectedColumnText)
            self.queryStatement = f"{self.Query} {', '.join(projectedColumns)}"
        
        #* Group By - Replaces Projection
        # γ columnA; count(columnB) → newColumnName(tableName)
        if self.groupByBool:
            projectedColumns = projectedColumns[:3]
            groupByText = []
            for i, column in enumerate(projectedColumns):
                if i == 0:
                    self.groupByStatement = f"{self.groupByStatement} {column};"
                else:
                    func = groupBy(column, subgraph=subgraph, dataset=dataset)
                    groupByText.append(f" the <b>{func}</b> of <b>{column}</b>, <em>mapped</em> to a column named <b>{func}{column}</b>")
                    self.groupByStatement = f"{self.groupByStatement} {func}({column}) → {func}{column},"
            self.queryStatement = self.groupByStatement[:-1]
            self.projectedColumnText = f"<b>{projectedColumns[0]}</b> <em>grouped by</em> {' and'.join(groupByText)}"
        
        #* Order By
        if self.orderByBool:
            randColumn = rand.choice(usableColumns)
            randColumn = randColumn + (rand.choice([' desc', ' asc']))
            self.orderByStatement = f"{self.orderByStatement} {randColumn}"
            self.orderByText = f" <em>ordered by {randColumn.replace('desc', 'in <b>descending order</b>').replace('asc', 'in <b>ascending order</b>')}</em>"

        #* Selection
        selectedColumns = []
        if self.numClauses != 0:
            for i in range(self.numClauses):  
                randColumn = rand.choice(usableColumns)
                while randColumn in selectedColumns:
                    randColumn =  rand.choice(usableColumns)
                selectedColumns.append(selection(usableColumns, randColumn, subgraph, dataset))
            conditions = []
            selectedColumnsArray = []
            for item in selectedColumns:
                randColumn, operator, value = item
                selectedColumnsArray.append(f"{randColumn}{operator}{value}")

                operator = operator.replace(">", "is greater than").replace("<", "is less than").replace("≥", "is greater than or equal to").replace("≤", "is less than or equal to").replace("=", "is").replace("≠", "is not")
                conditions.append(f"<b>{randColumn}</b> <em>{operator}</em> <b>{value}</b>")
            selected = ' ∨ '.join(selectedColumnsArray)
            self.selectStatement =  f"{self.selectStatement} {selected}"
            self.selectStatementText = ' or '.join(conditions)
    def getQuery(self):
        self.Query = self.joinStatement 
        if self.numClauses !=0:
            self.Query = f"{self.selectStatement} ({self.Query})"
        if self.orderByBool:
            self.Query = f"{self.orderByStatement} ({self.Query})"
        self.Query = f"{self.queryStatement} ({self.Query})"
        return self.Query

    def getText(self):

        text = f"Return a table of {self.projectedColumnText}"
        if self.orderByBool:
            text += self.orderByText
        text += f" where {self.selectStatementText} from the tables {self.tableListText}"

        return text

    
    def loadQuestion(self, data):
        data['correct_answers']['RelaXEditor'] = self.getQuery()
        data['params']['questionText'] = self.getText()





def projection(usableColumns):
    projectedColumns = []
    for i in range(rand.randint(2,5)):
        randColumn = rand.choice(usableColumns)
        while randColumn in projectedColumns:
            randColumn =  rand.choice(usableColumns)
        projectedColumns.append(randColumn)

    return projectedColumns

def groupBy(randColumn, subgraph, dataset):
    for table in subgraph.keys():
        for column in dataset.tableSet[table].columns:
            if randColumn == dataset.tableSet[table].columns[column]['name']:
                match(dataset.tableSet[table].columns[column]['unit']):
                    case 'STRING': return "count" 
                    case 'NUMBER': return f"{rand.choice(['avg','sum'])}"
                    case 'DATE': return "count"

        
def selection(usableColumns, randColumn,subgraph, dataset):
    for table in subgraph.keys():
        for column in dataset.tableSet[table].columns:
            if randColumn == dataset.tableSet[table].columns[column]['name']:
                match(dataset.tableSet[table].columns[column]['unit']):
                    case 'STRING': return (randColumn, " = ", f"'{rand.choice(dataset.tableSet[table].rows[column])}'")
                    case 'NUMBER': return (randColumn,f" {rand.choice([ '≥', '≤', '>', '<'])} ", rand.choice(dataset.tableSet[table].rows[column]))
                    case 'DATE': return (randColumn, f" {rand.choice([ '≥', '≤', '>', '<'])} ", f"Date('{rand.choice(dataset.tableSet[table].rows[column])}')")
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
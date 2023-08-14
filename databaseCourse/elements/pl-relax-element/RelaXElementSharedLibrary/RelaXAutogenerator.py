import random as rand
import requests
from datetime import datetime
# This allows DroneCI to see the RASQLib module
import sys
sys.path.append('databaseCourse/serverFilesCourse/')
sys.path.append('/drone/src/databaseCourse/serverFilesCourse/')

from RASQLib import textDatabaseHandler as db
from RASQLib import noisyData as nd


#! change Random number of projected and selected columns to always include 1 column from each table
# do this by creating array first. then pop out whats needed. should be easy


def formatDate(capturedText):
    dateObj = datetime.strptime(capturedText, '%Y-%m-%dT%H:%M:%S.%fZ')
    formattedDate = dateObj.strftime('%Y-%m-%d')
    return formattedDate

# A very basic autogenerate function.
# At the moment, all it does is create a database
# and load it into the data variable.
#
# The functionality that was previously in
# this file has been moved to the database
# and table objects file

# returns the greater number - used to ensure number of tables exceeds number of joins
def returnGreater(num1, num2):
    return num1 if num1 > num2 else num2

def createPreview(data):

    
    db = data['params']['db_initialize_create']
    correctAnswer = data['correct_answers']['RelaXEditor']

    url = data['params']['url']

    # Construct the data to be sent in the GET request
    data_to_send = {
    "database": db,
    "submittedAnswer": correctAnswer,
    "correctAnswer": correctAnswer
    }

    try:
        #print("hello from inside the try")
        response = requests.get(url, json=data_to_send)

        # Assuming the server returns JSON data containing the processed result
        response_data = response.json()

        # Process the response data as needed
        #queriedSA = response_data.get('queriedSA', None)
        queriedCA = response_data.get('queriedCA', None)
    
        #print(queriedCA)
    except Exception as e:
        print("Error:", str(e))
        return "error"
    
    # Begins the HTML required to render the expected outpyt
    htmlTable = "<button  type='button' onclick='togglePreview()' class='expectedOutputButton'>Show Expected Output</button><br><div class='expectedOutput'><div id='output' class='output-tables'><table class='expectedOutputTable' style='display: none;'><thead>"
    if 'schema' not in queriedCA.keys():
        #print(correctAnswer)
        return False
    # loads the data from the query response
    columnNames = queriedCA['schema']['_names']
    columnTypes = queriedCA['schema']['_types']
    dataRows = queriedCA['rows']

    # will loop if the expected output has no rows
    if len(dataRows) == 0:
        return False
    
    # Ensures that the expected output will not exceed 300 rows
    if len(dataRows) > 300:
        dataRows = dataRows[0:299]

    # Records the columns that have type date for proper rendering later on 
    dateRowRecord = []
    # loops to find date columns and to render Expected output headers
    for i, column in enumerate(columnNames):
        if columnTypes[i] == 'date':
            dateRowRecord.append(i)
        htmlTable += "<th>" + str(column) + "</th>"

    htmlTable += "</thead>"

    # Loops to render table rows
    for row in dataRows:
        rowString = "<tr>"
        for i, x in enumerate(row):
            # Uses dateRowRecord from earlier to ensire dates are formatted correctly
            if i in dateRowRecord:
                rowString+= "<td>" + formatDate(str(x)) + "</td>"
            else:
                rowString+= "<td>" + str(x) + "</td>"
        rowString += "</tr>"
        htmlTable += rowString

    htmlTable += "</table></div></div>"

    return htmlTable

def autogenerate(data, outputGuaranteed=True):
    
    #expectedOutput = data['params']['html_params']['expectedOutput']
    #if expectedOutput:
    #  data['params']['expectedOutput'] = createPreview(data)
    # Generates a random database
    columns = rand.randint(4, 7)
    joins = returnGreater(rand.randint(2,4), (data['params']['attrib_dict']['numJoins'])) #! Change to joins/rand -> whichever is bigger
    rows = rand.randint(7, 15)
    
    # Autogenerates the Database and the Questions
    database = db.Database(isSQL=False, columns=columns, joins=joins, rows=rows)
    question = Question(dataset=database, attribDict=data['params']['attrib_dict'], rows=rows)


    # Loads the database into the data variable
    database.loadDatabase(data)
    question.loadQuestion(data)

    # checks
    if outputGuaranteed is False:
        data['params']['html_params']['expectedOutput'] = ''
        return
    

    # Creates and loads preview table
    data['params']['html_params']['expectedOutput'] = createPreview(data)
    while not data['params']['html_params']['expectedOutput']:

        data['params']['db_initialize_create'] = ''
        data['params']['db_initialize_create_backend'] = ''
       
        # generates the Database and the Question string and answer
        database = db.Database(isSQL=False, columns=columns, joins=joins, rows=rows)
        question = Question(dataset=database, attribDict=data['params']['attrib_dict'], rows=rows)


        # Loads the database and question into the data variable
        database.loadDatabase(data)
        question.loadQuestion(data)

        # Creates and loads preview table
        data['params']['html_params']['expectedOutput'] = createPreview(data) 
    

class Question:
    Query = "π "

    joinStatement = ""

    selectStatement = "σ"
    ClauseArray = { "∧", "∨", "¬", "=", "≠", "≥", "≤", ">", "<"}

    orderByStatement = "τ"
    groupByStatement = "γ"

    crossJoin = "⨯"
    naturalJoin = "⨝"
    outerFullJoins="⟗"
    outerRightJoins="⟖"
    outerLeftJoins="⟕"
    semiRightJoins="⋉"
    semiLeftJoins="⋊"
    antiJoins="▷"


    tableListText = ""
    def  __init__(self, dataset, attribDict, rows) -> None:
        #* Load all attribs from data
        self.numJoins = attribDict['numJoins']
        self.numClauses = attribDict['numClauses']
        self.orderByBool = attribDict['orderBy']
        self.groupByBool = attribDict['groupBy']
        self.antiJoinBool = attribDict['antiJoin']
        self.outerJoinBool = attribDict['outerJoin']
        self.semiJoinBool = attribDict['semiJoin']
        self.rangeNum = attribDict['projectedColumns']
        #* Join first
        # number of joins for the question
        self.offLimitsTable = None

        graph = dataset.toGraph()
        
        # List of tables that are joined together in needed order
        self.JoinList = []


        # checks if specific type of join, else loops through natural join to satisfy numJoins
        # Specific join queries (anti, semi, outer) do not have more than one join to ensure output
        if self.antiJoinBool:
            self.antiJoinGeneration(graph=graph,dataset=dataset)
        elif self.semiJoinBool:
            self.semiJoinGeneration(graph=graph,dataset=dataset)
        elif self.outerJoinBool:
            self.outerJoinGeneration(graph=graph,dataset=dataset)
        elif self.numJoins == 0:
            self.JoinList.append(rand.choice(list(graph.keys())))
            self.joinStatement = self.JoinList[0]
        else:
            loopNum = 0 # Joins numJoins of natural joins
            while loopNum != (self.numJoins):
                self.naturalJoinGeneration(graph=graph)
                loopNum+=1

        # neededColumns are one random column from each joined graph 
        # such that all joined tables are utilized in output
        neededColumns = []
        numArray = []
        # usableColumns are all Columns from joined graphs.
        usableColumns = []
        for table in self.JoinList:

            # ensures that num will be unique for each table
            num = rand.randint(0, len(dataset.tableSet[table].columns)-1)
            while num in numArray:
                num = rand.randint(0, len(dataset.tableSet[table].columns))
            numArray.append(num)

            # for loop to fill usable and needed columns
            i = 0
            for column in dataset.tableSet[table].columns:
                usableColumns.append(dataset.tableSet[table].columns[column]['name'])
                if i == num:
                    neededColumns.append(dataset.tableSet[table].columns[column]['name']) 
                i+=1


        #* Projection
        projectedColumns = self.projection(neededColumns, usableColumns, self.rangeNum)
        tempArray = [] # used to add <click> tag that is rendered into a clickable word in renderer.js
        for elem in projectedColumns:
            tempArray.append(f"<click>{elem}</click>")
        # checks to see if groupby attrib is False - then renderers the 
        # projected columns for both the question text and the query statement
        if not self.groupByBool:
            self.projectedColumnText = ", ".join(tempArray) # Question text
            parts = self.projectedColumnText.rsplit(",", 1)  # Split the string from the right side only once
            self.projectedColumnText = f'<b>{" and".join(parts)}</b>' # joins the right most split with `and` for grammatical correctness
            self.queryStatement = f"{self.Query} {', '.join(projectedColumns)}" # renders Projection section of query statement
        
        #* Group By - Replaces Projection
        # γ columnA; count(columnB) → newColumnName(tableName)
        if self.groupByBool:
            # selects 3 columns from projectedColumns to be used
            projectedColumns = projectedColumns[:3]
            groupByText = []
            # loops through selected columns
            for i, column in enumerate(projectedColumns):
                if i == 0: # the fist column is used as what is grouped by
                    self.groupByStatement = f"{self.groupByStatement} {column};"
                else: # the other two are counted/summed/averaged relative to first column
                    func = groupBy(column, graph=graph, dataset=dataset)
                    # Question and query rendering
                    groupByText.append(f" the <b><click>{func}</click></b> of <b><click>{column}</click></b>, <em>mapped</em> to a column named <b><click>{func}{column}</click></b>")
                    self.groupByStatement = f"{self.groupByStatement} {func}({column}) → {func}{column},"
            # removes last `,` from statement
            self.queryStatement = self.groupByStatement[:-1]
            self.projectedColumnText = f"<b><click>{projectedColumns[0]}</click></b> <em>grouped by</em> {' and'.join(groupByText)}"
        
        #* Order By
        if self.orderByBool:
            # changes order based of rng
            randColumn = rand.choice(usableColumns)
            randColumn = randColumn + (rand.choice([' desc', ' asc']))
            # Query and Text rendering
            self.orderByStatement = f"{self.orderByStatement} {randColumn}"
            self.orderByText = f" <em>ordered by {randColumn.replace('desc', 'in <b>descending order</b>').replace('asc', 'in <b>ascending order</b>')}</em>"
        
        #* Selection
        selectedColumns = []
        # Ensures that if numClause is set to zero, or if its set to zero and anti or semi join occurs, nothing happens 
        if self.numClauses <= 0:
            return
        if self.numClauses > 0:

            # Checks to see if only one select clause
            # makes sure that it returns more than 1 output.
            if self.numClauses == 1:

                # NeededColumns is to ensure each table has been used when selected columns
                if len(neededColumns) == 0:
                    randColumn = rand.choice(usableColumns)
                    # Gets table name of which column is a part
                    tableName = dataset.getColumnMap()[randColumn]
                    # Ensures that strings are not used for selection if there is only one select clause
                    index = 0
                    while dataset.tableSet[tableName].columns[randColumn]['unit'] == 'STRING' and index < 20:
                        randColumn = rand.choice(usableColumns)
                        # Gets table name of which column is a part
                        tableName = dataset.getColumnMap()[randColumn]

                        index+=1
                else:
                    randColumn = rand.choice(neededColumns)
                    # Gets table name of which column is a part
                    tableName = dataset.getColumnMap()[randColumn]
                    # Ensures that strings are not used for selection if there is only one select clause
                    index = 0 # ensures that while loop does not last forever
                    while dataset.tableSet[tableName].columns[randColumn]['unit'] == 'STRING' and index < 20:
                        randColumn = rand.choice(neededColumns)
                        # Gets table name of which column is a part
                        tableName = dataset.getColumnMap()[randColumn]

                        index+=1

                # fills SelectedColumn
                selectedColumns.append(selection(usableColumns, randColumn, graph, dataset))
            # Else grabs random columns to fill selection
            else:
                # loops to fill selectedColumns 
                for i in range(self.numClauses):
                    if len(neededColumns) == 0:
                        randColumn = rand.choice(usableColumns)
                        # Ensures That no columns are double called
                        index = 0 # ensures while loop does not last forever
                        while randColumn in selectedColumns or index < 15:
                            randColumn =  rand.choice(usableColumns)
                            index+=1
                    else:
                        randColumn = neededColumns.pop(rand.choice(range(len(neededColumns))))

                    # fills selectedColumns
                    selectedColumns.append(selection(usableColumns, randColumn, graph, dataset))

            
            conditions = [] # Holds the question text for the selection operation 
            selectedColumnsArray = [] # holds the query statement for each selection operation
            for item in selectedColumns:
                randColumn, operator, value, isDate = item
                # Checks and renders columns accordingly - isDate returns the value Date('{value}') only if column is date
                if isDate:
                    selectedColumnsArray.append(f"{randColumn}{operator}{isDate}")
                else:
                    selectedColumnsArray.append(f"{randColumn}{operator}{value}")
                # renders Question text for each operation
                operator = operator.replace(">", "is greater than").replace("<", "is less than").replace("≥", "is greater than or equal to").replace("≤", "is less than or equal to").replace("=", "is").replace("≠", "is not")
                conditions.append(f"<b><click>{randColumn}</click></b> <em>{operator}</em> <b><click>{value}</click></b>")
            # completes render for Query statement and question text
            selected = ' ∨ '.join(selectedColumnsArray)
            self.selectStatement =  f"{self.selectStatement} {selected}"
            self.selectStatementText = ' or '.join(conditions)



    #* Join Generation========================================================
    def outerJoinGeneration(self, graph, dataset):
        #* Partial Outer Joins
        #  for all rows from table1, null where not exist table2
        #  More ⟕ Less where column less = null
        
        # randomly chooses one node in database graph
        node1 = rand.choice(list(graph.keys()))
        connections = graph[node1] # returns all connections the random node has
        node2 = rand.choice(connections) # randomly chooses one connecting node 

        # loops through each column to find which column references node2
        for column in dataset.tableSet[node1].columns:
            if dataset.tableSet[node1].columns[column]['references'] == node2:
                # records the foreign key in CompareColumn
                compareColumn = dataset.tableSet[node1].columns[column]["name"]
        
        # this if orders the tables such that when the outer join is executed the proper table is on the proper side
        if len(set(dataset.tableSet[node1].rows[compareColumn])) > len(set(dataset.tableSet[node2].rows[compareColumn])):
            # renders join Statement
            self.joinStatement = f"{node1}{self.outerLeftJoins}{node2}"
            
            # gets qColumn and its name to create a "selection" statement in the question text
            # this is to ensure students use the outer join
            qColumn = rand.choice(list(dataset.tableSet[node2].columns.keys()))
            querryColumn = dataset.tableSet[node2].columns[qColumn]['name']
            
            index = 0 # ensures that while loop does not last forever
            # loop makes sure compare column is not the compare column - to make the question harder
            while querryColumn is compareColumn or index < 20:
                qColumn = rand.choice(list(dataset.tableSet[node2].columns.keys()))
                querryColumn = dataset.tableSet[node2].columns[qColumn]['name']
                index+=1
            
            # renders question text
            self.tableListText = f"where <b><click>{querryColumn}</click></b> <em>is null</em> in <b><click>{node2}</click></b>"
            # checks if numclauses is 0 - and rendes selection statement accordingly
            if self.numClauses == 0: 
                self.selectStatement =  f"{self.selectStatement} {querryColumn} = null"
                self.numClauses = -1 # signals the getQuery function to render query properly
            else:
                self.selectStatement =  f"{self.selectStatement} {querryColumn} = null ∨"
            self.JoinList = [node1] # adds the node to the join list
        else:
            self.joinStatement = f"{node1}{self.outerRightJoins}{node2}"
            qColumn = rand.choice(list(dataset.tableSet[node1].columns.keys()))
            querryColumn = dataset.tableSet[node1].columns[qColumn]['name']

            index = 0 # ensures that while loop does not last forever
            # loop makes sure compare column is not the compare column - to make the question harder
            while querryColumn is compareColumn or index < 20:
                qColumn = rand.choice(list(dataset.tableSet[node1].columns.keys()))
                querryColumn = dataset.tableSet[node1].columns[qColumn]['name']
                index+=1
            
            # checks if numclauses is 0 - and rendes selection statement accordingly
            if self.numClauses == 0: 
                self.selectStatement =  f"{self.selectStatement} {querryColumn} = null"
                self.numClauses = -1 # signals the getQuery function to render query properly
            else:
                self.selectStatement =  f"{self.selectStatement} {querryColumn} = null ∨"
            self.tableListText = f"where <b><click>{querryColumn}</click></b> <em>is null</em> in <b><click>{node1}</click></b>"
            self.JoinList = [node2, node1] # adds the node to the join list
        
        # adds and for case that numclauses exists
        if self.numClauses > 0:
            self.tableListText = f"and {self.tableListText}"

    def semiJoinGeneration(self, graph, dataset):
        #* Semi Joins
        #  for row from table1 where match exists in table2
        #  Less ⋊ More

        # Select node with most connections
        mcNode = list(graph.keys())[0] # starts with first key
        for column in dataset.tableSet[graph[mcNode][0]].columns:
            if dataset.tableSet[graph[mcNode][0]].columns[column]['references'] == mcNode:
                compareColumn = dataset.tableSet[graph[mcNode][0]].columns[column]["name"]
        
        # Checks which table has the greater unique data in teh compare column
        if len(set(dataset.tableSet[graph[mcNode][0]].rows[compareColumn])) <= len(set(dataset.tableSet[mcNode].rows[compareColumn])):
            for node in graph.keys():
                if len(graph[node]) <= len(graph[mcNode]):
                    mcNode = node
                    # this loop checks all columns of the first connection of mcNode to find the foreign Key
                    for column in dataset.tableSet[graph[mcNode][0]].columns:
                        if dataset.tableSet[graph[mcNode][0]].columns[column]['references'] == mcNode:
                            compareColumn = dataset.tableSet[graph[mcNode][0]].columns[column]["name"]
                    # checks if unique data is larger in mcNode than in connection and breaks
                    if len(set(dataset.tableSet[graph[mcNode][0]].rows[compareColumn])) > len(set(dataset.tableSet[mcNode].rows[compareColumn])):
                        break
        
        # select connecting node
        node1 = graph[mcNode][0]
        node2 = mcNode

        # grabs compare column for rendering
        for column in dataset.tableSet[node1].columns:
            if dataset.tableSet[node1].columns[column]['references'] == node2:
                compareColumn = dataset.tableSet[node1].columns[column]["name"]
        
        # Render Outputs
        self.joinStatement = f"{node1}{self.semiRightJoins}{node2}"
        self.tableListText = f"or where <b><click>{compareColumn}</click></b> exists in <b><click>{node2}</click></b>"
        self.JoinList = [node1]
        self.offLimitsTable = node2
    
    def antiJoinGeneration(self, graph, dataset):
        #* Anti Joins --> bigger ▷ smaller
        #  for row from table1 not in table2

        # Select node with most connections
        mcNode = list(graph.keys())[0]
        for column in dataset.tableSet[graph[mcNode][0]].columns:
            # checks if Column is the foreign Key then records it
            if dataset.tableSet[graph[mcNode][0]].columns[column]['references'] == mcNode:
                compareColumn = dataset.tableSet[graph[mcNode][0]].columns[column]["name"]
        
        # Checks which table has the greater unique data in teh compare column
        if len(set(dataset.tableSet[graph[mcNode][0]].rows[compareColumn])) <= len(set(dataset.tableSet[mcNode].rows[compareColumn])):
            for node in graph.keys():
                # Loops through graph to find smallest connections.
                if len(graph[node]) <= len(graph[mcNode]):
                    mcNode = node
                    for column in dataset.tableSet[graph[mcNode][0]].columns:
                        if dataset.tableSet[graph[mcNode][0]].columns[column]['references'] == mcNode:
                            compareColumn = dataset.tableSet[graph[mcNode][0]].columns[column]["name"]
                    # Breaks loop if unique set of foreign keys in mcNode connection is larger than mcNode
                    if len(set(dataset.tableSet[graph[mcNode][0]].rows[compareColumn])) > len(set(dataset.tableSet[mcNode].rows[compareColumn])):
                        break
        
        # select connecting node
        node1 = graph[mcNode][0]
        node2 = mcNode

        # grabs compareColumn
        for column in dataset.tableSet[node1].columns: 
            if dataset.tableSet[node1].columns[column]['references'] == node2:
                compareColumn = dataset.tableSet[node1].columns[column]["name"]
        
        # renders text and query statements
        self.joinStatement = f"{node1}{self.antiJoins}{node2}"
        self.tableListText = f"where <b><click>{compareColumn}</click></b> is not in <b><click>{node2}</click></b>"
        self.JoinList = [node1]
        self.offLimitsTable = node2


    def naturalJoinGeneration(self, graph):
        jList=[] # temp list
        key = False
        # loops through each node in the graph
        for node in graph:
            # Checks if the its the first node in the graph
            if len(self.JoinList) == 0 and len(jList) == 0:
                jList.append(node) # adds it to the temp list

            # loops through each connecting node in graph            
            for connection in graph[node]:
                # checks if the connecting node is in JoinList, or in jList
                # and checks if node is not in JoinLust
                if (connection in self.JoinList or connection in jList) and node not in self.JoinList:
                    # Checks if table will result in a zero output
                    if node is not self.offLimitsTable:
                        # adds the  node to jList then breaks out of both loops
                        # because the join is satisfied
                        jList.append(node)
                        key = True
                        break
            if key:
                break
            
        # checks if this is first join, renders as such, if not renders as such
        if self.joinStatement == "":
            self.joinStatement =f"{jList[0]}{self.naturalJoin}{jList[1]}"
        else:
            self.joinStatement = f"({self.joinStatement}){self.naturalJoin}{jList[0]}"
        
        parts = self.tableListText.rsplit(",", 1)  # Split the string from the right side only once

        # adds temp list to joinlist
        for node in jList:
            self.JoinList.append(node)



    #* getters=======================================================
    def getQuery(self):
        # starts with the joinstatements
        self.Query = self.joinStatement 
        # checks if there are any selectStatements
        # if < 0 there is a select from an outerjoin
        # if > 0 there is a normal select statement
        if self.numClauses != 0:
            self.Query = f"{self.selectStatement} ({self.Query})"
        # checks if orderby is part of query
        if self.orderByBool:
            self.Query = f"{self.orderByStatement} ({self.Query})"
        # adds projection/groupby statement
        self.Query = f"{self.queryStatement} ({self.Query})"
        return self.Query

    def getText(self):
        # Renders text
        text = f"Return a table of {self.projectedColumnText}"
        # checks if orderby
        if self.orderByBool:
            text += self.orderByText
        # checks if select clauses
        if self.numClauses <= 0:
            text += f" {self.tableListText}"
        else:
            text += f" where {self.selectStatementText} {self.tableListText}"
        # returns text
        return text

    
    # Loasd the Query adn the text into corresponding data variables
    def loadQuestion(self, data):
        data['correct_answers']['RelaXEditor'] = self.getQuery()
        data['params']['questionText'] = self.getText()



    # Returns projected columns
    def projection(self, neededColumns, usableColumns, rangeNum):
        # neededColumns is a list of 1 column from each table in JoinList
        # UseableColumns is a list of all colunms from JoinList
        # rangeNum is the number of projected columns desired
        projectedColumns = [] # array that is filled and returned
        index = 0  # index to ensure that loop does not loop forever
        for i in range(rangeNum):
            # if neededColumn still has value, use it. else dont
            if len(neededColumns) == 0 or self.numJoins == 0:
                randColumn = rand.choice(usableColumns) 
            else:
                randColumn = neededColumns.pop(rand.choice(range(len(neededColumns))))
            # index ensures that while loop does not last forever
            while randColumn in projectedColumns and index < 15:
                randColumn =  rand.choice(usableColumns) # ensures that randomColumn is not already ised
                index+=1
            index = 0
            # add randColumn to projectedColumns 
            projectedColumns.append(randColumn)

        return projectedColumns

# returns single statement for groupby
def groupBy(randColumn, graph, dataset):
    for table in graph.keys():
        for column in dataset.tableSet[table].columns:
            if randColumn == dataset.tableSet[table].columns[column]['name']:
                match(dataset.tableSet[table].columns[column]['unit']):
                    case 'STRING': return "count" 
                    case 'NUMBER': return f"{rand.choice(['avg','sum'])}"
                    case 'DATE': return "count"

# returns single statement for selection clause
def selection(usableColumns, randColumn, graph, dataset):
    for table in graph.keys():
        for column in dataset.tableSet[table].columns:
            if randColumn == dataset.tableSet[table].columns[column]['name']:
                choice = rand.choice(dataset.tableSet[table].rows[column])
                match(dataset.tableSet[table].columns[column]['unit']):
                    case 'STRING': return (randColumn, " = ", f"'{choice}'", None)
                    case 'NUMBER': return (randColumn, f" {rand.choice([ '≥', '≤'])} ", choice, None)
                    case 'DATE':   return (randColumn, f" {rand.choice([ '≥', '≤'])} ", f"{choice}", f"date('{choice}')")
                #print(f"Selection string '{rand.choice(dataset.tableSet[table].rows[column])}'")
                #selectedColumns.append(randColumn)





# Performs a Depth first search to retreave a connected graph
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

# Returns a random subgraph of a desired size. Used to retrieve natural joins.
def randomSubgraph(graph, n):
    startNode = rand.choice(list(graph.keys()))
    connectedNodes = dfs(graph, startNode, n=n)
    return {node: graph[node] for node in connectedNodes}


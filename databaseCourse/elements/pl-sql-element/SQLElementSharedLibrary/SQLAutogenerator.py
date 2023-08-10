import random
import sqlite3
import os
# This allows DroneCI to see the RASQLib module
import sys
sys.path.append('/drone/src/databaseCourse/serverFilesCourse/')

from RASQLib import textDatabaseHandler as db
from RASQLib import noisyData as nd

# Automatically generates an SQL question based on the question's parameters
def autogenerate(data):
    
    # Gets question parameters
    # random = data['params']['html_params']['random']
    # maxGrade = data['params']['html_params']['maxGrade']
    # markerFeedback = data['params']['html_params']['markerFeedback']
    questionType = data['params']['html_params']['questionType']
    difficulty = data['params']['html_params']['difficulty']


    # Checks if the difficulty are valid
    if difficulty not in ['easy', 'medium', 'hard', None]:
        return None

    # Generates the appropriate question
    match questionType:
        case 'create':  generateCreate(data, difficulty)
        case 'insert': generateInsert(data, difficulty)
        case 'update': generateUpdate(data, difficulty)
        case 'delete': generateDelete(data, difficulty)
        case 'query': generateQuery(data, difficulty)
    


    # Generates a new query question if there is expected output
    # but it is empty
    while questionType == 'query' and data['params']['html_params']['expectedOutput'] and '<td>' not in data['params']['expectedOutput']:

        # Clears out the previous create and insert statements
        data['params']['db_initialize_create'] = ''
        data['params']['db_initialize_insert_frontend'] = ''
        data['params']['db_initialize_insert_backend'] = ''

        # Generates the new query
        generateQuery(data, difficulty)

'''
    Begin create-style question
'''

# Generates a 'create' style SQL question
def generateCreate(data, difficulty):

    # Obtains question specific parameters
    columns, joins, tableClauses, queryClauses = getQuestionParameters(data)

    # Creates an appropriate table
    database = None
    match difficulty:

        # This is the only question type that uses static tables still
        case 'easy': database = db.Database(file=random.choice(['airport', 'airplane', 'product', 'customer']), random=False)
        case 'medium': database = db.Database(file=random.choice(['passenger', 'shipment']), random=False)
        case 'hard': database = db.Database(file=random.choice(['flight', 'shippedproduct']), random=False)
        case _: database = db.Database(columns=columns, joins=joins, clauses=tableClauses)

    # Grabs the primary table for easy referencing
    table = database.primaryTable

    # Creates a string to tell the student what they need
    # to do for the qestion
    questionString = f"Create a table named <b>{table.name}</b> with columns"

    # Adds a list of columns and units to the question string
    columnList = list(table.columns.keys())
    columnValues = list(table.columns.values())
    for i in range(len(columnList)):

        # Adds an 'and' at the start of the last iteration
        if i == len(columnList) - 1:
            questionString += ' and'
        
        # Adds the column name
        questionString += f" <b>{columnValues[i]['name']}</b>"



        # Handles the text for units
        match columnValues[i]['unit']:
            case 'INTEGER': questionString += ' (an integer)'
            case 'DECIMAL': questionString += f" (a decimal value with a total of {columnValues[i]['unitOther'].split(',')[0]} digits, {columnValues[i]['unitOther'].split(',')[1]} of which are after the decimal point)"
            case 'CHAR': questionString += f" (a string of exactly {columnValues[i]['unitOther']} characters)"
            case 'VARCHAR': questionString += f" (a string up to {columnValues[i]['unitOther']} characters)"
            case 'DATE': questionString += ' (DATE)'
            case 'DATETIME': questionString += ' (DATETIME)'
            case other: questionString += f" ({columnValues[i]['unit']})"
            
        # Mentions primary key, if necessary
        if columnValues[i]['isPrimary']:
            questionString += ' <em>that is a primary key</em>'

        # Mentions foreign key and its clauses, if necessary
        if columnValues[i]['references']:
            questionString += f" that references <b>{columnValues[i]['references']}</b>\'s <b>{columnValues[i]['foreignKey']}</b>"

            # Handles cascade
            if columnValues[i]['isOnUpdateCascade']:
                questionString += ' <em>that cascades on an update</em>'
            
            # Handles delete set null
            if columnValues[i]['isOnDeleteSetNull']:
                questionString += ' <em>that is set to null when deleted</em>'

        # Mentions other clauses, if necessary
        if columnValues[i]['isNotNull']:
            questionString += ' <em>that cannot be null</em>'
        
        if columnValues[i]['isUnique']:
            questionString += ' <em>where all values are unqiue</em>'

        # Adds a comma at the end of each iteration
        questionString += ', '


    # Remove the last comma and replace it with a period
    questionString = questionString[:-2] + '.'



    # Loads any tables this one references into the schema.
    # This DOES NOT load the primary table into data,
    # since that would give students the answer
    if database.referencedTables:
        for referencedTable in database.referencedTables:
            data['params']['db_initialize_create'] += f"{database.referencedTables[referencedTable].getSQLSchema()}\n"

    # Places the question string into data
    data['params']['questionString'] = questionString

    # Places the solution into data
    data['correct_answers']['SQLEditor'] = createStatement(table)

# Returns the schema for the current table.
def createStatement(table):
    return table.getSQLSchema()

'''
    End create-style question
'''



'''
    Begin insert-style question
'''

# Generates a 'insert' style SQL question
def generateInsert(data, difficulty):

    # Obtains question specific parameters
    columns, joins, tableClauses, queryClauses = getQuestionParameters(data)

    # Based on the difficulty, choose a random amount of columns
    # If no difficulty is specified, uses question parameters instead
    database = None
    match difficulty:
        case 'easy': 
            columns = random.randint(4, 5)
            joins = 1
            database = db.Database(columns=columns, joins=joins)

        case 'medium': 
            columns = random.randint(5, 6)
            joins = random.randint(1, 2)
            database = db.Database(columns=columns, joins=joins)

        case 'hard': 
            columns = random.randint(6, 7)
            joins = random.randint(1, 2)
            database = db.Database(columns=columns, joins=joins)

        case _: 
            database = db.Database(columns=columns, joins=joins, clauses=tableClauses)

    # Grabs the primary table for easy referencing
    table = database.primaryTable

    # Generates some data
    database.generateRows(random.randint(15, 25))



    # Obtains the row to be inserted by removed it
    # from the primary table's rows    
    row = [table.rows[key].pop() for key in table.columns.keys()]
    


    # Creates the question string
    questionString = f"Insert the following values into the <b>{table.name}</b> table:\n({str(row)[1:-1]})"

    # Loads the database
    database.loadDatabase(data)

    # Adds the question string
    data['params']['questionString'] = questionString

    # Creates the answer string
    data['correct_answers']['SQLEditor'] = insertStatement(table, row)

# Generates an insert statement based on the data
def insertStatement(table, row):
    return f"INSERT INTO {table.name} VALUES ({str(row)[1:-1]});\n"

'''
    End insert-style question
'''



'''
    Begin update-stype question
'''

def generateUpdate(data, difficulty):
    
    # Obtains question specific parameters
    columns, joins, tableClauses, queryClauses = getQuestionParameters(data)

    # Chooses a table to load based on quesiton difficulty
    database = None
    match difficulty:

        case 'easy': 
            columns = random.randint(4, 5)
            joins = 1
            database = db.Database(columns=columns, joins=joins)
            queryClauses['conditional'] = 0
            queryClauses['useSubquery'] = False

        case 'medium': 
            columns = random.randint(4, 5)
            joins = random.randint(1, 2)
            database = db.Database(columns=columns, joins=joins)
            queryClauses['conditional'] = random.randint(1, 3)
            queryClauses['conditional'] = random.randint(1, 3)
            queryClauses['useSubquery'] = False

        case 'hard': 
            columns = random.randint(4, 5)
            joins = random.randint(1, 2)
            database = db.Database(columns=columns, joins=joins)
            queryClauses['conditional'] = 0
            queryClauses['useSubquery'] = True
        
        case _:
            database = db.Database(columns=columns, joins=joins, clauses=tableClauses)

    # Gets the primary table for easy referencing
    table = database.primaryTable



    # Checks if the parameters are valid
    nonCascadingForeignKeys = len([key for key in table.columns.keys() if table.columns[key]['references'] and not table.columns[key]['isOnUpdateCascade']])
    if columns - nonCascadingForeignKeys < queryClauses['conditional']:
        print(f"UPDATE question cannot have more conditional clauses than foreign keys that do not cascade on update (was supplied with {queryClauses['conditional']} conditionals and {nonCascadingForeignKeys} non-cascading foreign keys)")

    # Generates a bunch of rows
    database.generateRows(random.randint(15, 25))

    # Selects a random column to affect. Ensures that it cannot
    # select a unique column so ensure that the update won't
    # violate unique constrains

    updateColumn = None
    tindex = 0
    while not updateColumn or nd.isUnique(table, updateColumn):

        # Helps prevent timeouts
        tindex += 1
        if tindex > 50:
            break

        updateColumn = random.choice(list(table.columns.keys()))

    # Generates the updated valued
    updateValue = nd.generateNoisyData(table, updateColumn)[0]

    # If the quesiton should use a condition, set parameters
    conditionalValues = getConditionalValues(queryClauses['conditional'], database, list(table.columns.keys()))



    # Generates the question string
    questionString = f"From the column <b>{updateColumn}</b>, update all values to be <b>{updateValue}</b>"

    # Adds the conditionals
    questionString = questionConditionals(conditionalValues, questionString)

    # Finishes the sentence
    questionString += "."



    # Adds subquery to question string
    subquery = ''
    if queryClauses['useSubquery']:
        subquery, subqueryString = generateSubquery(database)
        questionString += f" {subqueryString}"



    # Adds the important rows to the backend database
    database.addRowsBackend(conditionalValues)

    # Loads data
    database.loadDatabase(data)

    # Sets the question string
    data['params']['questionString'] = questionString

    # Loads the correct answer
    data['correct_answers']['SQLEditor'] = updateStatement(table, updateColumn, updateValue, conditionalValues, subquery)

# Creates an update statement
def updateStatement(table, updateColumn, updateValue, conditionalValues=None, subquery=''):

    # Sets up the statement
    statement = f"UPDATE {table.name} SET {updateColumn} = '{updateValue}'"

    # Adds the conditionals
    conditionalStatement = statementConditionals('', conditionalValues)

    # Removes the leading space, adding a newline in its place
    statement += '\n' + conditionalStatement[1:]
 
    # Adds the subquery and formats the 'WHERE'
    if subquery:
        if 'WHERE' in statement:
            statement += ' AND' + subquery
        else:
            statement += 'WHERE' + subquery
    
    # Add finishing touches and returns
    statement += ';\n'
    return statement

'''
    End update-style question
'''


'''
    Begin delete-style question
'''

def generateDelete(data, difficulty):
    
    # Obtains question specific parameters
    columns, joins, tableClauses, queryClauses = getQuestionParameters(data)

    # Chooses a table to load based on quesiton difficulty
    database = None
    match difficulty:
        case 'easy': 
            columns = random.randint(4, 5)
            joins = 1
            database = db.Database(columns=columns, joins=joins)
            queryClauses['conditional'] = 0
            queryClauses['useSubquery'] = False

        case 'medium': 
            columns = random.randint(4, 5)
            joins = random.randint(1, 2)
            database = db.Database(columns=columns, joins=joins)
            queryClauses['conditional'] = random.randint(1, 3)
            queryClauses['conditional'] = random.randint(1, 3)
            queryClauses['useSubquery'] = False

        case 'hard': 
            columns = random.randint(4, 5)
            joins = random.randint(1, 2)
            database = db.Database(columns=columns, joins=joins)
            queryClauses['conditional'] = 0
            queryClauses['useSubquery'] = True
        
        case _:
            database = db.Database(columns=columns, joins=joins, clauses=tableClauses)

    # Gets the primary table for easy referencing
    table = database.primaryTable

    # Generates a bunch of bogus rows
    database.generateRows(random.randint(15, 25))

    # If the quesiton should use a condition, set parameters
    conditionalValues = getConditionalValues(queryClauses['conditional'], database, list(table.columns.keys()))


    # If there are no
    if conditionalValues:
        questionString = f"Delete all values"
    else:
        questionString = f"Delete all values from the table {table.name}"

    # Adds the 'WHERE's and such
    questionString = questionConditionals(conditionalValues, questionString)
    
    # Finishes the sentence
    questionString += "."



    # Adds subquery to question string
    subquery = ''
    if queryClauses['useSubquery']:
        subquery, subqueryString = generateSubquery(database)
        questionString += f" {subqueryString}"



    # Adds the important rows to the backend database
    database.addRowsBackend(conditionalValues)

    # Loads the database
    database.loadDatabase(data)

    # Sets the question string
    data['params']['questionString'] = questionString

    # Sets the correct answer
    data['correct_answers']['SQLEditor'] = deleteStatement(table, conditionalValues, subquery)

# Creates a delete statement
def deleteStatement(table, conditionalValues=None, subquery=''):

    # Sets up the statement
    statement = f"DELETE FROM {table.name}"

    # Adds the conditionals
    conditionalStatement = statementConditionals('', conditionalValues)

    # Removes the leading space, adding a newline in its place
    if conditionalValues:
        statement += '\n' + conditionalStatement[1:]

    # Adds the subquery and formats the 'WHERE'
    if subquery:
        if 'WHERE' in statement:
            statement += ' AND' + subquery
        else:
            statement += '\nWHERE' + subquery
    
    # Add finishing touches and returns
    statement += ';\n'
    return statement

'''
    End delete-style question
'''


'''
    Begin query-style question
'''

def generateQuery(data, difficulty):
    
    # Obtains question specific parameters
    columns, joins, tableClauses, queryClauses = getQuestionParameters(data)



    # Chooses a table to load based on quesiton difficulty
    database = None
    match difficulty:
        case 'easy': 
            columns = random.randint(5, 6)
            columnsToSelect = random.randint(1, 2)
            joins = 1
            database = db.Database(columns=columns, joins=joins)
            queryClauses['conditional'] = 0

        case 'medium': 
            columns = random.randint(6, 7)
            columnsToSelect = random.randint(2, 4)
            joins = random.randint(1, 2)
            database = db.Database(columns=columns, joins=joins)
            queryClauses['conditional'] = random.randint(1, 3)

        case 'hard': 
            columns = random.randint(7, 8)
            columnsToSelect = random.randint(4, 6)
            joins = random.randint(1, 2)
            database = db.Database(columns=columns, joins=joins)
            queryClauses['useSubquery'] = True
        
        case _:
            database = db.Database(columns=columns, joins=joins, clauses=tableClauses)
    
    # Generates a bunch of rows
    database.generateRows(random.randint(15, 25))



    # Unpacks variables for easy referencing
    table = database.primaryTable
    referenced = database.referencedTables
    
    conditionals = queryClauses['conditional']
    useSubquery = queryClauses['useSubquery']
    columnsToSelect = queryClauses['columnsToSelect']
    orderBy = queryClauses['orderBy']
    groupBy = queryClauses['groupBy']
    having = queryClauses['having']
    limit = queryClauses['limit']
    withClause = queryClauses['with']
    isDistinct = queryClauses['isDistinct']
    useQueryFunctions = queryClauses['useQueryFunctions']

    # Maps table names to the table itself
    #   allTables {
    #       $tableName: $table
    #   }
    allTables = {table.name: table}
    for ref in referenced:
        allTables[ref] = referenced[ref]



    # Randomly selects unique columns
    #   selectedColumns {
    #       $tableName = [
    #           $columnNames
    #       ]
    #   }
    selectedColumns = selectColumns(columnsToSelect, database)



    # Randomly selects some columns to perform a query on
    #   functionColumns {
    #       $columnName = '$fxn'
    # }
    functionColumns = {}
    for key in selectedColumns:
        for column in selectedColumns[key]:

            # The first one is guaranteed. Past that, there's 
            # a one in five chance per column for that
            # column to have a function performed on it
            if useQueryFunctions and not functionColumns:
                functionColumns[column] = getQueryFunction(database, column, useIn=False)
            elif random.random() * 5 < 1 and useQueryFunctions:
                functionColumns[column] = getQueryFunction(database, column, useIn=False)
 


    # Obtains the conditional values
    conditionalValues = getConditionalValues(conditionals, database, restrictive=False)



    # Gets the type of joins.
    # SQLite only supports the following joins:
    #   - JOIN or equivilently INNER JOIN: must specify join condition
    #   - CROSS JOIN: no join condition specified
    #   - LEFT OUTER JOIN: join condition specified
    #       * Right and full outer joins are not supported
    joinTypes = {}
    for selectedTable in selectedColumns:

        # We don't want to join the table to itself
        if selectedTable != table.name:
            joinTypes[selectedTable] = random.choices(['JOIN', 'INNER JOIN', 'CROSS JOIN', 'LEFT OUTER JOIN'], [4, 4, 1, 1])[0]



    # A list of all columns in the joined tables
    joinedColumnList = []
    for selectedTable in selectedColumns:
        for column in allTables[selectedTable].columns.keys():
            joinedColumnList.append(column)

    # Gets the columns to order and whether or not they're
    # ascending
    orderByColumns = {}
    while len(orderByColumns) < orderBy:
        orderByColumns[joinedColumnList.pop(random.choice(range(len(joinedColumnList))))] = random.choice(['ASC', 'DESC'])
    

    # A list of *selected* columns
    selectedColumnList = []
    for selectedTable in selectedColumns:
        for column in selectedColumns[selectedTable]:
            selectedColumnList.append(column)

    # Gets the columns to group
    groupByColumns = []
    while len(groupByColumns) < groupBy:  
        groupByColumns.append(selectedColumnList.pop(random.choice(range(len(selectedColumnList)))))

    
    # A list of *group by* columns
    groupByColumnList = [x for x in groupByColumns]

    # The columns for the having clause. The valid columns
    # are the columns in the groupByColumns list
    #   havingColumns {
    #       $column: $value
    #   }
    havingColumns = getConditionalValues(having, database, groupByColumnList, restrictive=False)



    # Which columns will use aliasing
    withColumns = {}
    ''' Aliasing is works but is not currently used
    tableNames = [selectedTable for selectedTable in selectedColumns]
    withColumns = {}
    while len(withColumns) < withClause:
        tableName = tableNames.pop(random.choice(range(len(tableNames))))

        withColumns[tableName] = tableName[:1].upper()
    '''
    


    # Starts the question string and the column selection section
    if selectedColumns:
        questionString = 'Select'

        # De-pluralizes if necessary
        questionString = removeTrailingChars(questionString, condition=columnsToSelect == 1)
        
        # Lists all the columns to add
        index = 0

        for key in selectedColumns:
            for column in selectedColumns[key]:

                # Adds the and, if necessary
                if index == columnsToSelect - 1 and index > 0:
                    # Removes the comma if there are only two tables
                    if index == 1:
                        questionString = questionString[:-1]

                    questionString += ' and'

                # Adds the function, if necessary
                if column in functionColumns:
                    match functionColumns[column]:
                        case 'COUNT': questionString += ' the <em>count of</em>'
                        case 'MAX': questionString += ' the <em>maximum value of</em>'
                        case 'MIN': questionString += ' the <em>minimum value of</em>'
                        case 'LENGTH': questionString += ' the <em>length of</em>'
                        case 'AVG': questionString += ' the <em>average of</em>'
                
                # Adds the column
                questionString += f" <b>{column}</b>,"

                # Increments the interations
                index += 1

        # Removes the trailing comma
        questionString = removeTrailingChars(questionString)

    # If there are no columns to select, instead select all
    else:
        questionString = 'Select all columns'




    # Adds the conditionals
    questionString = questionConditionals(conditionalValues, questionString)

    # Finishes the sentence
    questionString += '.'



    # Adds the subquery
    subquery = ''
    if useSubquery:
        subquery, subqueryString = generateSubquery(database)
        questionString += f" {subqueryString}"



    # Adds the join types
    if joinTypes:

        # Used to keep track of when and if to add the 'and'
        index = 0

        # Iterates over all joins
        for key in joinTypes:

            # Adds the and, if necessary.
            if index == len(joinTypes) - 1 and index > 0:
                # Removes the comma if there are only two tables
                if index == 1:
                    questionString = questionString[:-1]

                questionString += ' and'

            # Creates the string based on the join type
            match joinTypes[key]:
                case 'INNER JOIN':
                    joinString = f" Only matching rows from <b>{key}</b> are included,"

                case 'JOIN': 
                    joinString = f" Rows from <b>{key}</b> are joined to their matching row,"

                case 'LEFT OUTER JOIN': 
                    joinString = f" All rows from <b>{key}</b> are matched to their single corresponding row,"

                case 'CROSS JOIN':
                    joinString = f" Each row from <b>{key}</b> should be paired with every possible row,"
            
            # Sets the join string to lower case, except when it
            # is the first join and thus starting the sentence
            if not index == 0:
                joinString = joinString.lower()
            
            # Adds the string
            questionString += joinString

            index += 1
        
        # Removes trailing comma and finishes the sentance
        questionString = removeTrailingChars(questionString) + '.'
        


    # Adds the order by
    if orderBy:
        questionString += ' Order the output by the columns'

        # Depluralizes if necessary
        questionString = removeTrailingChars(questionString, 1, orderBy == 1)

        # Adds the order by columns
        orderString, index = dictionaryQuestionString(orderByColumns)

        # Inserts whether or not the order should be
        # ascending or descening
        for key in orderByColumns:

            # Grabs the appropriate string for ascending
            # or descending
            ascOrDesc = ' <em>in ascending order</em>' if orderByColumns[key] == 'ASC' else ' <em>in descending order</em>'

            # Inserts the string after it's corresponding key.
            # The `+ 4` accounts for the length of the '</b>' tag
            orderString = orderString[:orderString.find(key) + len(key) + 4] + ascOrDesc + orderString[orderString.find(key) + len(key) + 4:]

        # Removes trailing comma
        questionString = questionString + removeTrailingChars(orderString, 1, orderBy == 1)




    # Combines the order by and group by sections
    # for more dynamic appearing questions
    if orderBy and groupBy:
        questionString += ' and group'
    elif groupBy:
        questionString += ' Group'
    elif orderBy:
        questionString += '.'

    # Handles group by clause
    if groupBy:
        questionString += ' the columns'

        # De-pluralizes if necessary
        questionString = removeTrailingChars(questionString, condition=columnsToSelect == 1) + ' by'

        questionString = dictionaryQuestionString(groupByColumns, questionString)[0]

        # Removes trailing comma
        questionString = removeTrailingChars(questionString)

        # Finishes the sentence
        questionString += '.'



    # Handles having clause
    if having:

        # Removes the period
        questionString = removeTrailingChars(questionString) + ' having'

        # Gets the string, removes the leading 'where'
        # and adds it to the question string
        havingString = questionConditionals(havingColumns)
        questionString += havingString[6:]

        

        # Finishes the sentence
        questionString += '.'



    # Handles limit clause
    if limit:
        questionString += f" <em>Limit the search to {limit} results"

        # De-pluralizes if necessary
        questionString = removeTrailingChars(questionString, condition=limit == 1)

        questionString += '</em>'

    


    # Combines the limit and distinct sections
    # for more dynamic appearing questions
    if limit and isDistinct:
        questionString += ' and <em>only include distinct values</em>.'
    elif isDistinct:
        questionString += '. <em>Only include distinct values in the search</em>.'
    elif isDistinct:
        questionString += '.'



    # Loads database
    database.loadDatabase(data)

    # Adds the question string to data
    data['params']['questionString'] = questionString
    
    # Sets the correct answer
    data['correct_answers']['SQLEditor'] = queryStatement(database, selectedColumns, joinTypes, conditionalValues, orderByColumns, groupByColumns, havingColumns, withColumns, limit, isDistinct, functionColumns, subquery)


    if os.path.exists("preview.db"):
        os.remove("preview.db")
    expectedOutput = data['params']['html_params']['expectedOutput']
    if expectedOutput:
        data['params']['expectedOutput'] = createPreview(data)

# Creates a query
def queryStatement(database, selectedColumns, joinTypes={}, conditionalValues={}, orderByColumns={}, groupByColumns={}, havingColumns={}, withColumns={}, limit=0, isDistinct=False, functionColumns={}, subquery=''):
    
    table = database.primaryTable
    keyMap = table.getKeyMap()

    # Begins the query string
    queryString = 'SELECT'



    # Adds distinct clause
    if isDistinct:
        queryString += ' DISTINCT'



    # Adds the columns to the query string
    # All columns use a '$table.' to specify
    for key in selectedColumns:
        for column in selectedColumns[key]:

            if functionColumns and column in functionColumns:
                queryString += f" {functionColumns[column]}({column}),"
            else:
                queryString += f" {column},"
    
    # Adds the star for select all
    if not selectedColumns:
        queryString += ' * '
    
    # Removes trailing comma
    queryString = queryString[:-1] + f"\nFROM {table.name}"

    # Adds the tables to be selected from
    for key in joinTypes:
        queryString += f" {joinTypes[key]} {key}"



    # Begins the conditionals block
    queryString += '\nWHERE'

    # Specifies how the tables are joined together
    if joinTypes:
        for key in keyMap:
            if keyMap[key]['references'] in joinTypes and joinTypes[keyMap[key]['references']] in ['JOIN', 'INNER JOIN', 'FULL OUTER JOIN']:
                queryString += f" {table.name}.{key} = {keyMap[key]['references']}.{keyMap[key]['foreignKey']} AND"
    

    # Adds the conditional values
    if conditionalValues:
        queryString = statementConditionals(queryString, conditionalValues, clauseType='')

    # Adds the subquery and formats the 'WHERE'
    if 'WHERE' in queryString[-7:] and subquery:
        queryString += subquery
    elif 'WHERE' in queryString[-7:]:
        queryString = queryString[:queryString.find('WHERE')]
    elif subquery and 'AND' not in queryString[-4:]:
        queryString += ' AND' + subquery
    elif subquery:
        queryString += subquery
        


    # Removes the final 'AND' if necessary
    if 'AND' in queryString[-4:]:
        queryString = queryString[:-4]

    # Adds the group by clause
    if groupByColumns:

        # Begins the section
        queryString += '\nGROUP BY'

        # Iterates over the array
        for value in groupByColumns:
            queryString += f" {value},"
        
        # Removes trailing comma
        queryString = removeTrailingChars(queryString)



    # Adds the having clause
    if havingColumns:
        queryString += '\n'
        queryString = statementConditionals(queryString, havingColumns, 'HAVING')



    # Adds the order clause
    if orderByColumns:

        # Begins the section
        queryString += '\nORDER BY'

        # Iterates over all the columns to order by
        for key in orderByColumns:
            queryString += f" {key} {orderByColumns[key]},"
        
        # Removes the trailing comma
        queryString = removeTrailingChars(queryString)



    # Adds the limit clause
    if limit:
        queryString += f"\nLIMIT {limit}"



    # Returns, appending the finishing touches
    return queryString + ";\n"



# Creates a subquery
def generateSubquery(database):

    # Grabs some parameters for easy referencing
    table = database.primaryTable

    columnMap = database.getColumnMap(tableNames=False)
    


    # All columns that are not in the primary table
    foreignColumnList = [column for column in columnMap if column not in table.columns]

    # Assigns weights to columns by data type. If the
    # data type is not present, it gets a weight of 100.
    #   - INTEGER and DECIMAL have plenty of interesting
    #     functions, such as SUM() so they get the highest
    #     weighting
    #   - VARCHAR has LENGTH() and COUNT() so it's not bad
    #   - DATE, and DATETIME only have COUNT(), MIN(), and 
    #     MAX() so they're also not too bad
    #   - CHAR only has COUNT(), so it has a small weight
    weightMap = {
        'INTEGER': 20,
        'DECIMAL': 20,
        'VARCHAR': 5,
        'CHAR': 1,
        'DATE': 5,
        'DATETIME': 5
    }

    # Uses the weight map to create weights for selecting a
    # foreign column
    foreignWeights = [weightMap[columnMap[key].columns[key]['unit']] for key in foreignColumnList]

    # Gets all units in the primary tables to ensure that the
    # foreign column has the same units as at least one
    # column in a primary table
    unitsInPrimary = set(table.columns[key]['unit'] for key in table.columns)

    # Chooses a foreign column for the subquery's SELECT. Can
    # only select columns which have at least one column in the
    # primary table with the same unit
    selectedColumn = None
    while not selectedColumn or columnMap[selectedColumn].columns[selectedColumn]['unit'] not in unitsInPrimary:
        selectedColumn = random.choices(foreignColumnList, foreignWeights)[0]

    # Checks whether or not a query function is valid for this
    # subquery. All query clauses produce a number, so they
    # must be compared against a number.
    canUseQueryFunction = 'INTEGER' in unitsInPrimary or 'DECIMAL' in unitsInPrimary



    # Declares some variables for later
    comparisonOperator = ''
    queryFunction = ''
    conditionalValues = {}
    


    # Only use the 'IN' clause if there is no other option. Unless
    # the data between the selected and conditional column is very
    # similar, an 'IN' clause will produce few–if any–rows
    if not canUseQueryFunction:

        # Get all columns in the primary that match the data-type
        # of the selected column
        conditionalColumnList = []
        for column in table.columns:
            if table.columns[column]['unit'] == columnMap[selectedColumn].columns[selectedColumn]['unit']:
                conditionalColumnList.append(column)

        # Chooses a random column from the list
        conditionalColumn = random.choice(conditionalColumnList)


        # Guarantees some conditional values
        conditionalValues = getConditionalValues(random.choices([1, 2, 3], [100, 10, 1])[0], database, columnList=[column for column in columnMap[selectedColumn].columns], restrictive=False)
        statement = subqueryStatement(conditionalColumn, 'IN', selectedColumn, columnMap[selectedColumn].name, conditionalValues=conditionalValues)
        questionString = subqueryQuestionString(database, conditionalColumn, 'IN', selectedColumn, queryFunction, conditionalValues=conditionalValues)
        return statement, questionString



    # Selects the query function
    queryFunction = getQueryFunction(database, selectedColumn, conditionalValues, useIn=False)



    # Gets all columns in the primary table that match the data-type
    # required for query functions, i.e. number-like data-types
    conditionalColumnList = []
    for column in table.columns:

        # If the unit is date-like, the conditional column can also
        # be a date-like so long as the function isn't 'COUNT'
        if columnMap[selectedColumn].columns[selectedColumn]['unit'] in ['DATE', 'DATETIME'] and queryFunction not in ['COUNT']:
            if table.columns[column]['unit'] in ['DATE', 'DATETIME']:
                conditionalColumnList.append(column)

        # Otherwise, it has to be compared to a number-like
        elif table.columns[column]['unit'] in ['INTEGER', 'DECIMAL']:
            conditionalColumnList.append(column)
        
    # Chooses a random column from the list
    conditionalColumn = random.choice(conditionalColumnList)



    # A small chance to include conditionals
    if random.random() * 3 < 1:

        # Drastically prefers selecting only one column
        conditionalValues = getConditionalValues(random.choices([1, 2, 3], [100, 10, 1])[0], database, columnList=[column for column in columnMap[selectedColumn].columns], restrictive=False)



    # Selects an appropriate operator.
    # Prefers 'greater than's since we prefer larger query 
    # results
    if queryFunction in ['COUNT', 'MIN']:
        comparisonOperator = random.choices(['>', '>=', '<', '<=', '=', '!='], [20, 20, 2, 2, 1, 1])[0]
    
    # Similarly, 'less than's works best for MAX function
    elif queryFunction in ['MAX']:
        comparisonOperator = random.choices(['>', '>=', '<', '<=', '=', '!='], [2, 2, 20, 20, 1, 1])[0]
    
    # For the LENGTH function, the returned number tends to
    # be small so we prefer 'greater than's
    elif queryFunction in ['LENGTH']:
        comparisonOperator = random.choices(['>', '>=', '<', '<=', '=', '!='], [20, 20, 2, 2, 1, 1])[0]

    # No chance of the 'equals'
    else:
        comparisonOperator = random.choices(['>', '>=', '<', '<=', '=', '!='], [20, 20, 20, 20, 1, 1])[0]



    # Gets the subquery statement
    statement = subqueryStatement(conditionalColumn, comparisonOperator, selectedColumn, columnMap[selectedColumn].name, queryFunction, conditionalValues=conditionalValues)

    # Gets the question string
    questionString = subqueryQuestionString(database, conditionalColumn, comparisonOperator, selectedColumn, queryFunction, conditionalValues=conditionalValues)

    return statement, questionString

def subqueryQuestionString(database, conditionalColumn, comparisonOperator, selectedColumnName, queryFunction='', conditionalValues={}):

    # Begins the question string
    questionString = f"Use a subquery (if necessary) to get the values where"

    # Prepares the string for an 'IN' clause
    if comparisonOperator == 'IN':
        questionString += ' the values of'

    # Adds the conditional column
    questionString += f" <b>{conditionalColumn}</b>"

    # Adds the comparison operator
    match comparisonOperator:
        case '>': questionString += ' <em>is greater than</em>'
        case '>=': questionString += ' <em>is greater than or equal to</em>'
        case '<': questionString += ' <em>is less than</em>'
        case '<=': questionString += ' <em>is less than or equal to</em>'
        case '=': questionString += ' <em>is equals to</em>'
        case '!=': questionString += ' <em>is not equal to</em>'
        case 'IN': questionString += ' <em>are in</em>'

    # Adds the query function
    if queryFunction:
        match queryFunction:
            case 'COUNT': questionString += ' the <em>count of</em>'
            case 'MAX': questionString += ' the <em>maximum value of</em>'
            case 'MIN': questionString += ' the <em>minimum value of</em>'
            case 'LENGTH': questionString += ' the <em>length of</em>'
            case 'AVG': questionString += ' the <em>average of</em>'
            case '': questionString += ' the <em>set of</em>'
    
    # Adds the selected column
    questionString += f" <b>{selectedColumnName}</b>"

    # If present, adds the conditional values
    if conditionalValues:
        questionString = questionConditionals(conditionalValues, questionString)
    
    # Finishes the sentence
    questionString += '.'

    return questionString

def subqueryStatement(conditionalColumn, comparisonOperator, selectedColumnName, tableName, queryFunction='', conditionalValues={}):

    # Begins the statement
    statement = f" {conditionalColumn} {comparisonOperator} (SELECT"

    # Wraps the selected column in parenthesis if there
    # is a function
    if queryFunction:
        statement += f" {queryFunction}({selectedColumnName})"
    else:
        statement += f" {selectedColumnName}"
    
    # Adds the table name
    statement += f" FROM {tableName}"



    # Adds conditional values, if they're present
    if conditionalValues:
        statement = statementConditionals(statement, conditionalValues)



    # Finishes the subquery
    statement += ')'

    return statement



# A simle list of all tables.
# Will return a list of column names (as strings) by
# default, otherwise it will return the columns themselves
def getColumnList(tableMap, columnNames=True):
    columnList = []
    for key in tableMap:
        if columnNames:
            columnList += [column for column in tableMap[key].columns]
        else:
            columnList += [tableMap[key].columns[column] for column in tableMap[key].columns]
    return columnList

def selectColumns(columnsToSelect, database):

    # Gets a list of all columns, where the key is the 
    # column name and the value is the table name. Since
    # the columns of each table are uniquely named, this
    # is used to randomly select unique columns
    #   allColumns {
    #       $columnName: $tableName
    #   }
    columnMap = database.getColumnMap()



    # Holds the columns that have been selected for the query
    #   selectedColumns {
    #       $tableName = [
    #           $columnNames
    #       ]
    #   }
    selectedColumns = {}

    # Selects the columns for the query
    for i in range(columnsToSelect):
        
        # Obtains a random column from a table, removing it
        # from the list of columns to preserve uniqueness
        column = random.choice(list(columnMap.keys()))
        tableName = columnMap.pop(column)

        # Creates an array for this key if it does not
        # already exist
        if tableName not in selectedColumns:
            selectedColumns[tableName] = []
        
        # Adds this item to the array
        selectedColumns[tableName].append(column)
    
    return selectedColumns

# Returns an appropriate query function based up the column's
# datatype. Weights functions such that functions that tend
# to produce good output are favoured
def getQueryFunction(database, key, conditionalValues={}, useIn=True):

    columnMap = database.getColumnMap(tableNames=False)

    # INTEGERs and DECIMALs
    if columnMap[key].columns[key]['unit'] in ['INTEGER', 'DECIMAL']:

        # Selects an appropraite function.
        # Prefers AVG since it compares the best to noisy data's
        # randomly generated integers. Comparing to MAX, MIN, or
        # COUNT could easily lead to an empty or near-empty query.
        # If there are conditional values, then all are weighted
        # the same except for COUNT since that one is still bad
        # for our noisy data
        queryFunction = random.choices(['AVG', 'COUNT', 'MAX', 'MIN'], [4, 1, 1, 1] if not conditionalValues else [2, 1, 2, 2])[0]



    # DATEs and DATETIMEs
    if columnMap[key].columns[key]['unit'] in ['DATE', 'DATETIME']:
        
        # Selects an appropraite function.
        # Without conditional values, they're all about as bad
        # in terms of their output. With conditional values, 
        # MIN and MAX are prefered since then they'll have
        # better outputs
        queryFunction = random.choices(['COUNT', 'MAX', 'MIN'], [1, 1, 1] if not conditionalValues else [1, 3, 3])[0]



    # VARCHARs
    if columnMap[key].columns[key]['unit'] in ['VARCHAR']:
        
        # Selects an appropraite function.
        # LENGTH will produce good queries relative to the data
        # that the noisy data gen create, so we give it a big
        # weight. Conditional values doesn't affect either 
        # function much
        queryFunction = random.choices(['COUNT', 'LENGTH'], [1, 6])[0]

    

    # CHARs
    if columnMap[key].columns[key]['unit'] in ['CHAR']:

        # Selects an appropraite function.
        # Either it's the count, or we do an 'IN' subquery.
        # The latter is a better option
        if useIn:
            queryFunction = random.choices(['COUNT', ''], [1, 3])[0]
        else:
            queryFunction = 'COUNT'

    return queryFunction

# Removes the last character of a string 
def removeTrailingChars(string, qty=1, condition=True):
    if condition:
        string = string[:-1 * qty]
    return string

# Adds the columns or tables of a dictionary to a question string.
# This questionString code is used a few times, so here
# is a somewhat general version of it.
def dictionaryQuestionString(dictionary, string='', iterations=None, index=0, tag='b'):
    
    # If there's nothing supplied, return the string
    if not dictionary:
        return string, 0

    # Sets a default value for iterations
    if not iterations:
        iterations = len(dictionary)
    
    # Iterates over all items in the dictionary
    for key in dictionary:

        # Adds the and, if necessary
        if index == iterations - 1 and index > 0:
            # Removes the comma if there are only two tables
            if index == 1:
                string = string[:-1]

            string += ' and'

        # Adds the key to the string
        if tag:
            string += f" <{tag}>{key}</{tag}>,"
        else:
            string += f" {key},"

        # Increments the interations
        index += 1

    # Returns
    return string, index

'''
    End query-style question
'''



'''
    Begin helper functions
'''

# Returns a string for an SQL conditional
def conditionalStatement(column, condition):
    return f"WHERE {column} = '{condition}'"

# Adds a set of conditionals to a question string
def questionConditionals(conditionalValues, string=''):
    
    # If there aren't any conditionals, just return
    if not conditionalValues:
        return string

    # Adds the 'where' if necessary
    string += ' where'

    for key in conditionalValues.keys():

        # Adds the column
        string += f" <b>{key}</b>"

        # Adds the appropraite comparing operator
        match conditionalValues[key]['comparator']:
            case '>': string += ' <em>is greater than</em>'
            case '>=': string += ' <em>is greater than or equal to</em>'
            case '<': string += ' <em>is less than</em>'
            case '<=': string += ' <em>is less than or equal to</em>'
            case '=': string += ' <em>is equal to</em>'
            case '!=': string += ' <em>is not equal to</em>'
        
        # Adds the value
        string += f" <b>{conditionalValues[key]['value']}</b>"

        # Adds the logical operator
        if conditionalValues[key]['connector'] == 'OR':
            string += ' or'
        else:
            string += ' and'
    
    # Removes the trailing connector.
    # This isn't as efficient as I would prefer, but
    # I was getting an odd issue on other approaches
    # where it also chopped off the trailing '>' and
    # cause a great-many rendering issues.
    while string[-1] != '>':
        string = string[:-1]
    
    return string

# Adds a set of conditionals to a statement
def statementConditionals(statement='', conditionalValues={}, clauseType=' WHERE'):
    
    # If there aren't any conditionals, just return
    if not conditionalValues:
        return statement
    
    statement += clauseType

    # Includes the conditional if they exist as
    # well as the condtional connector. Notice the
    # string quotes are the opposite of the normal
    # choice; this is due to requiring the `"`
    # quote as part of the string such that SQL
    # values such as "St John's" don't break the 
    # SQLite
    for key in conditionalValues:
        statement += f' {key} {conditionalValues[key]["comparator"]} "{conditionalValues[key]["value"]}" {conditionalValues[key]["connector"]}'

    # Removes trailing 'OR' or 'AND' if necessary
    if statement[-3] == ' ':
        statement = statement[:-3]
    else:
        statement = statement[:-4]

    return statement



# Get a set of conditional values
#   conditionalValues {
#       $column: $value
#   }
def getConditionalValues(conditionals, database, columnList=[], restrictive=True):

    # Holds the values
    conditionalValues = {}

    # Maps column name to its table
    columnMap = database.getColumnMap(tableNames=False)

    # Gets a list of all columns present between
    # the provided tables, if it was not provided
    if not columnList:
        columnList = getColumnList(database.getTableMap())

    # A list from 0 to n where n is the number of rows.
    # The `.values()` and `list()[0]` is to just get the
    # 'first' item in the dictionary
    indexList = [i for i in range(len(list(list(columnMap.values())[0].rows.values())[0]))]

    # Creates weights for each column, drastically
    # preferring INTEGER, DECIMAL, DATE, and DATETIME 
    # columns. This is to improve query results since 
    # these data types support more comparisons than
    # the restrictive `=`
    weights = [90 if columnMap[column].columns[column]['unit'] in ['INTEGER', 'DECIMAL', 'DATE', 'DATETIME'] else 10 for column in columnList]



    # Iterates over the amount of conditionals
    while len(conditionalValues) < conditionals:

        # Selects a random column to affect.
        conditionalColumn = nd.popRandom(columnList, weights)
        

        # In the case that columnList becomes empty
        # due to the pops (thus returns NULL), then
        # break out of the loop
        if conditionalColumn == 'NULL':
            break

        # Prevents a selection of a column that is both foreign
        # and does not update on cascade, only if 'restrictive'
        if restrictive and columnMap[conditionalColumn].columns[conditionalColumn]['references'] and not columnMap[conditionalColumn].columns[conditionalColumn]['isOnUpdateCascade']:
                continue



        # Randomly chooses a logical operator to
        # connect the conditionals. Prefers to use
        # 'or's since they result in more rows
        logical = random.choices(['OR', 'AND'], [2, 1])[0]


        
        # If the column can support querries of the form 
        # `>`, `<`, `>=`, `<=`, then create a random value
        # to place in conditionalValues
        if columnMap[conditionalColumn].columns[conditionalColumn]['unit'] in ['INTEGER', 'DECIMAL', 'DATE', 'DATETIME']:

            # Generate a handful of random values of the appropriate
            # type and sort them
            vals = sorted(nd.generateNoisyDataNoFile(columnMap[conditionalColumn], conditionalColumn, 10, True))

            # Selects the value.
            # Return the middle value. Since the list was sorted, the
            # middle value is also the median value. Since an even number
            # of items were created, this is biased towards smaller numbers,
            # but only slightly
            #
            # Selects the comparison operator.
            # Drastically prefers comparison operators that will return
            # many values even when the column is unique. Also is biased
            # against `!=` since, unlike for CHAR and VARCHAR, the value
            # has no guarantee of being in conditionalValues, so a query
            # with `WHERE $col != $val` will often be equivalent to the
            # cluase's absence
            conditionalValues[conditionalColumn] = {
                'value': vals[len(vals) // 2],
                'connector': logical,
                'comparator': random.choices(['>', '>=', '<', '<=', '=', '!='], [5, 5, 5, 5, 2, 1])[0]
            }

            # Skips the rest of the loop, since we don't want to override this
            # value with an existing one, as through the lines below
            continue


            
        # Chooses a random value from the generated data to be updated
        randomValueIndex = nd.popRandom(indexList)

        # Grabs the randomly selected values
        conditionalValues[conditionalColumn] = {
            'value': columnMap[conditionalColumn].rows[conditionalColumn][randomValueIndex],
            'connector': logical,
            'comparator': random.choices(['=', '!='], [2, 1])[0]
        }
    
    # Returns the conditionals
    return conditionalValues



# Grabs the question's required parameters
def getQuestionParameters(data):

    numberOfColumns = None
    numberOfJoins = None
    try:
        numberOfColumns = data['params']['html_params']['columns']
        numberOfJoins = data['params']['html_params']['joins']
    except:
        numberOfColumns = 5
        numberOfJoins = 1

    # Constructs table clauses.
    # Parameters:
    #   - primaryKeys
    #   - isNotNull
    #   - isUnique
    #   - isOnUpdateCascade
    #   - isOnDeleteSetNull
    tableClauses = {}
    try:
        for clause in data['params']['html_table_clauses']:
            if data['params']['html_table_clauses'][clause]:
                tableClauses[clause] = data['params']['html_table_clauses'][clause]
    except:
        pass

    # Constructs query clauses.
    # Parameters:
    #   - conditional
    #   - useSubquery
    #   - columnsToSelect
    #   - orderBy
    #   - groupBy
    #   - having
    #   - limit
    #   - with
    #   - isDistinct
    #   - useQueryFunctions
    queryClauses = {}
    try:
        for clause in data['params']['html_query_clauses']:
            queryClauses[clause] = data['params']['html_query_clauses'][clause]
    except:
        queryClauses = {
            'conditional': 1,
            'useSubquery': False,
            'columnsToSelect': 3,
            'orderBy': 0,
            'groupBy': 0,
            'having': 0,
            'limit': 0,
            'with': 0,
            'isDistinct': 0,
            'useQueryFunctions': False
        }
    
    return numberOfColumns, numberOfJoins, tableClauses, queryClauses




# Returns a table with a specified number of columns
def loadTrimmedTable(columnCount, joinCount=0):

    # Checks to see if the column count is valid
    if(columnCount <= 0 or joinCount < 0):
        return None

    # Gets all random tables so a random one may be chosen
    possibleTables = db.getAllTableFiles()

    # Keeps trying random tables until it finds one with enough columns
    # and a enough foreign keys
    table = None
    while not table or len(table.columns) < columnCount or len(table.getKeyMap()) < joinCount:

        # Checks to see if there are no possible tables left.
        # This will only occur if there are no tables with enough
        # columns to satisfy the requirements.
        if len(possibleTables) == 0:
            return None

        # Pops the current table so there's no repeats
        possibleTable = possibleTables.pop(random.choice(range(len(possibleTables))))
        table = db.Table(possibleTable, random=False)

    # Removes columns until there is an appropriate amount left
    doomCounter = 10
    while len(table.columns) > columnCount:

        # If the doom counter reaches 0, it means that we are unable to remove
        # enough columns because they are PKs or necessary FKs. In that case,
        # just return the table, even if it has too many columns
        if doomCounter == 0:
            return table

        # We have to convert keys to a list because of subscriptables
        tryPop = random.choice(list(table.columns.keys()))

        # Don't remove...
        # primary keys, or
        # foreign keys if it would cause there to be not enough joins
        if not table.columns[tryPop]['isPrimary'] and (not table.columns[tryPop]['references'] or len(table.getKeyMap()) > joinCount):
            table.columns.pop(tryPop)
        else:
            doomCounter -= 1
    
    return table

# solutioncode (Str) => html table code (str)
# runs solution code on sqlite3 and gets results and puts that in html table format
def createPreview(data): 
    con = sqlite3.connect("preview.db")
    cur  = con.cursor()

    commands = data['params']['db_initialize_create'].replace('\n', '').replace('\t', '')
    commands += data['params']['db_initialize_insert_frontend'].replace('\n', '').replace('\t', '')

    cur.executescript(commands)
    con.commit()

    correctAnswer = data['correct_answers']['SQLEditor']
    expectedCode = correctAnswer.replace('\n', ' ').replace('\t', ' ')

    expectedAns = cur.execute(expectedCode)
    dataRows = expectedAns.fetchall()

    columnNames = [description[0] for description in cur.description]

    con.close()

    htmlTable = "<button  type='button' onclick='togglePreview()' class='expectedOutputButton'>Show Expected Output</button><br><br><div class='expectedOutput'><div class='scrollable'><table class='expectedOutputTable' style='display: none;'><thead>"

    for column in columnNames:
        htmlTable += "<th>" + str(column) + "</th>"

    htmlTable += "</thead>"

    if len(dataRows) > 300:
        dataRows = dataRows[0:299]

    for row in dataRows:
        rowString = "<tr>"
        for x in row:
            rowString+= "<td>" + str(x) + "</td>"
        rowString += "</tr>"
        htmlTable += rowString

    htmlTable += "</table></div></div>"

    return htmlTable
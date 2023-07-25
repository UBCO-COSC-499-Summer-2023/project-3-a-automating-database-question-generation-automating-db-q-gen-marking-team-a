import random

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
            data['params']['db_initialize'] += f"{database.referencedTables[referencedTable].getSQLSchema()}\n"

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
        case 'easy': database = db.Database(file=loadTrimmedTable(random.randint(3, 4), 0), columns=0)
        case 'medium': database = db.Database(file=loadTrimmedTable(random.randint(4, 6), 0), columns=0)
        case 'hard': database = db.Database(file=loadTrimmedTable(random.randint(5, 8), 0), columns=0)
        case _: database = db.Database(columns=columns, joins=joins, clauses=tableClauses)

    # Grabs the primary table for easy referencing
    table = database.primaryTable

    # Generates some data
    database.generateRows(random.randint(3, 7))



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
            database = db.Database(file=loadTrimmedTable(random.randint(3, 4)), columns=0, random=False)
            queryClauses['conditional'] = 0
            queryClauses['useSubquery'] = False

        case 'medium': 
            database = db.Database(file=loadTrimmedTable(random.randint(4, 6)), columns=0, random=False)
            queryClauses['conditional'] = random.randint(1, 3)
            queryClauses['useSubquery'] = False

        case 'hard': 
            database = db.Database(file=loadTrimmedTable(random.randint(5, 8)), columns=0, random=False)
            queryClauses['conditional'] = 0
            queryClauses['useSubquery'] = True
            return None # Not yet implemented; first requires quesryStatement() to be completed
        
        case _:
            database = db.Database(columns=columns, joins=joins, clauses=tableClauses)

    # Gets the primary table for easy referencing
    table = database.primaryTable



    # Checks if the parameters are valid
    nonCascadingForeignKeys = len([key for key in table.columns.keys() if table.columns[key]['references'] and not table.columns[key]['isOnUpdateCascade']])
    if columns - nonCascadingForeignKeys < queryClauses['conditional']:
        print(f"UPDATE question cannot have more conditional clauses than foreign keys that do not cascade on update (was supplied with {queryClauses['conditional']} conditionals and {nonCascadingForeignKeys} non-cascading foreign keys)")

    # Generates a bunch of rows
    database.generateRows(random.randint(6, 10))

    # Selects a random column to affect
    updateColumn = random.choice(list(table.columns.keys()))

    # Generates the updated valued
    updateValue = nd.generateNoisyData(table, updateColumn)[0]

    # If the quesiton should use a condition, set parameters
    conditionalValues = getConditionalValues(queryClauses['conditional'], database, list(table.columns.keys()))



    # Generates the question string
    questionString = f"From the table <b>{table.name}</b> and in the column <b>{updateColumn}</b>, change all values to be <b>{updateValue}</b>"

    # Keeps track of when to use 'and' vs 'or'
    questionString, conditionalConnectors, conditionalComparators = questionConditionals(conditionalValues, questionString, database)

    # Adds subquery to question string
    # TODO: this
    if queryClauses['useSubquery']:
        questionString += f""

    # Finishes the sentence
    questionString += "."



    # Loads data
    database.loadDatabase(data)

    # Sets the question string
    data['params']['questionString'] = questionString

    # Loads the correct answer
    data['correct_answers']['SQLEditor'] = updateStatement(table, updateColumn, updateValue, conditionalValues, conditionalConnectors, conditionalComparators, queryClauses['useSubquery'])

# Creates an update statement
def updateStatement(table, updateColumn, updateValue, conditionalValues=None, conditionalConnectors={}, conditionalComparators={}, subquery=None):

    # Sets up the statement
    statement = f"UPDATE {table.name} SET {updateColumn} = '{updateValue}'"

    # Adds the conditionals
    statement = statementConditionals(statement, conditionalValues, conditionalConnectors, conditionalComparators)
    
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
            database = db.Database(file=loadTrimmedTable(random.randint(3, 4)), columns=0, random=False)
            queryClauses['conditional'] = 0
            queryClauses['useSubquery'] = False

        case 'medium': 
            database = db.Database(file=loadTrimmedTable(random.randint(4, 6)), columns=0, random=False)
            queryClauses['conditional'] = random.randint(1, 3)
            queryClauses['useSubquery'] = False

        case 'hard': 
            database = db.Database(file=loadTrimmedTable(random.randint(5, 8)), columns=0, random=False)
            queryClauses['conditional'] = 0
            queryClauses['useSubquery'] = True
            return None # Not yet implemented; first requires quesryStatement() to be completed
        
        case _:
            database = db.Database(columns=columns, joins=joins, clauses=tableClauses)

    # Gets the primary table for easy referencing
    table = database.primaryTable

    # Generates a bunch of bogus rows
    database.generateRows(random.randint(3, 7))

    # If the quesiton should use a condition, set parameters
    conditionalValues = getConditionalValues(queryClauses['conditional'], database, list(table.columns.keys()))



    # Generates the question string
    questionString = f"From the table <b>{table.name}</b>, delete all values"

    # Adds the 'WHERE's and such
    questionString, conditionalConnectors, conditionalComparators = questionConditionals(conditionalValues, questionString, database)

    # Adds subquery to question string
    # TODO: this
    if queryClauses['useSubquery']:
        questionString += f""
    
    # Finishes the sentence
    questionString += "."



    # Loads the database
    database.loadDatabase(data)

    # Sets the question string
    data['params']['questionString'] = questionString

    # Sets the correct answer
    data['correct_answers']['SQLEditor'] = deleteStatement(table, conditionalValues, conditionalConnectors, conditionalComparators, queryClauses['useSubquery'])

# Creates a delete statement
def deleteStatement(table, conditionalValues=None, conditionalConnectors={}, conditionalComparators={}, subquery=None):

    # Sets up the statement
    statement = f"DELETE FROM {table.name}"

    # Adds the conditionals
    statement = statementConditionals(statement, conditionalValues, conditionalConnectors, conditionalComparators)
    
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
            columns = random.randint(3, 4)
            joins = 0
            database = db.Database(columns=columns, joins=joins)
            queryClauses['conditional'] = 0

        case 'medium': 
            columns = random.randint(4, 6)
            joins = random.randint(1, 2)
            database = db.Database(columns=columns, joins=joins)
            queryClauses['conditional'] = random.randint(1, 3)

        case 'hard': 
            columns = random.randint(5, 8)
            joins = random.randint(1, 2)
            database = db.Database(columns=columns, joins=joins)
            queryClauses['useSubquery'] = True
        
        case _:
            database = db.Database(columns=columns, joins=joins, clauses=tableClauses)
    
    # Generates a bunch of rows.
    # This is more rows than other questions, since we
    # want to increase the liklihood that a query will
    # return more than a few rows
    database.generateRows(random.randint(10, 15))



    # Unpacks variables for easy referencing
    table = database.primaryTable
    referenced = database.referencedTables

    keyMap = table.getKeyMap()

    tableMap = {key: referenced[keyMap[key]['references']] for key in keyMap}
    tableMap[table.name] = table

    conditionals = queryClauses['conditional']
    useSubquery = queryClauses['useSubquery']
    columnsToSelect = queryClauses['columnsToSelect']
    orderBy = queryClauses['orderBy']
    groupBy = queryClauses['groupBy']
    having = queryClauses['having']
    limit = queryClauses['limit']
    withClause = queryClauses['with']
    isDistinct = queryClauses['isDistinct']



    # Randomly selects unique columns
    #   selectedColumns {
    #       $tableName = [
    #           $columnNames
    #       ]
    #   }
    selectedColumns = selectColumns(columnsToSelect, database)



    # Obtains the conditional values
    conditionalValues = getConditionalValues(conditionals, database, restrictive=False)



    # Gets the type of joins.
    # SQLite only supports the following joins:
    #   - JOIN or equivilently INNER JOIN: must specify join condition
    #   - NATURAL JOIN: no join condition specified
    #   - CROSS JOIN: no join condition specified
    #   - LEFT OUTER JOIN: join condition specified
    #       * Right and full outer joins are not supported
    joinTypes = {}
    for selectedTable in selectedColumns:

        # We don't want to join the table to itself
        if selectedTable != table.name:
            joinTypes[selectedTable] = random.choices(['JOIN', 'INNER JOIN', 'NATURAL JOIN', 'CROSS JOIN', 'LEFT OUTER JOIN'], [2, 2, 4, 1, 1])[0]



    # A list of all columns in the table.
    columnList = getColumnList(tableMap)

    # Gets the columns to order and whether or not they're
    # ascending
    orderByColumns = {}
    while len(orderByColumns) < orderBy:
        orderByColumns[columnList.pop(random.choice(range(len(columnList))))] = random.choice(['ASC', 'DESC'])
    

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
    


    # Begins the question string
    questionString = 'From the tables'

    # De-pluralizes if necessary
    questionString = removeTrailingChars(questionString, condition=len(selectedColumns) == 1)



    # Lists all the tables to add
    questionString, index = dictionaryQuestionString(selectedColumns, questionString, tag='b')
    ''' Aliasing is works but is not currently used
    index = 0
    for key in selectedColumns:
        
        # Adds the and, if necessary.
        if index == len(selectedColumns) - 1 and index > 0:
            # Removes the comma if there are only two tables
            if index == 1:
                questionString = questionString[:-1]

            questionString += ' and'

        
        # Adds the table
        questionString += f" <b>{key}</b>"

        # Includes aliasing if necessary
        if key in withColumns:
            questionString += f" <em>with the alias {withColumns[key]}</em>"
        
        questionString += ','

        index += 1
    '''
    


    # Starts the column selection section
    questionString += ' select the columns'

    # De-pluralizes if necessary
    questionString = removeTrailingChars(questionString, condition=columnsToSelect == 1)
    
    # Lists all the columns to add
    index = 0
    for selectedTable in selectedColumns:
        questionString, index = dictionaryQuestionString(selectedColumns[selectedTable], questionString, columnsToSelect, index, tag='b')

    # Removes the trailing comma
    questionString = removeTrailingChars(questionString)



    # Adds the conditionals
    questionString, conditionalConnectors, conditionalComparators = questionConditionals(conditionalValues, questionString, database)

    # Finishes the sentence
    questionString += '.'



    # Adds the join types
    if joinTypes:

        # Used to keep track of when and if to add the 'and'
        index = 0

        # Starts the string
        questionString += f" Use"

        # Iterates over all joins
        for key in joinTypes:

            # Adds the and, if necessary.
            if index == len(joinTypes) - 1 and index > 0:
                # Removes the comma if there are only two tables
                if index == 1:
                    questionString = questionString[:-1]

                questionString += ' and'

            questionString += ' a'

            # Reduces ambiguity for the unspecified join
            if joinTypes[key] == 'JOIN':
                questionString += ' regular'
            
            # Adds the join and table to the question string
            questionString += f" <em>{joinTypes[key].lower()}</em> for the table <b>{key}</b>,"

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
        questionString += '. Group'
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
    havingConnectors = {}
    havingComparators = {}
    if having:

        # Removes the period
        questionString = removeTrailingChars(questionString) + ' having'

        # Gets the string, removes the leading 'where'
        # and adds it to the question string
        havingString, havingConnectors, havingComparators = questionConditionals(havingColumns, database=database)
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

    generateSubquery(database)

    # Loads database
    database.loadDatabase(data)

    # Adds the question string to data
    data['params']['questionString'] = questionString
    
    # Sets the correct answer
    data['correct_answers']['SQLEditor'] = queryStatement(database, selectedColumns, joinTypes, conditionalValues, conditionalConnectors, conditionalComparators, orderByColumns, groupByColumns, havingColumns, havingConnectors, havingComparators, withColumns, limit, isDistinct)



# Creates a query
def queryStatement(database, selectedColumns, joinTypes={}, conditionalValues={}, conditionalConnectors={}, conditionalComparators={}, orderByColumns={}, groupByColumns={}, havingColumns={}, havingConnectors={}, havingComparators={}, withColumns={}, limit=0, isDistinct=False):
    
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
            queryString += f" {column},"
    
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

        # Removes the final 'AND' if necessary
        if not conditionalValues:
            queryString = queryString[:-4]
    


    # Adds the conditional values
    if conditionalValues:
        queryString = statementConditionals(queryString, conditionalValues, conditionalConnectors, conditionalComparators, clauseType='')
    
    # Removes the WHERE clause if necessary
    if 'WHERE' in queryString[-6:]:
        queryString = queryString[:-6]

    

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
        queryString = statementConditionals(queryString, havingColumns, havingConnectors, havingComparators, 'HAVING')



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
    referenced = database.referencedTables

    keyMap = table.getKeyMap()
    tableMap = database.getTableMap()
    columnMap = database.getColumnMap(tableNames=False)

    #tableMap = {key: self.referencedTables[keyMap[key]['references']] for key in keyMap}
    # All columns that are in the database but not in
    # the primary table
    foreignColumnList = [column for column in columnMap if column not in table.columns]


    
    # Assigns weights to columns by data type. If the
    # data type is not present, it gets a weight of 100.
    #   - INTEGER and DECIMAL have plenty of interesting
    #     functions, such as SUM() so they get the highest
    #     weighting
    #   - VARCHAR has LENGTH() and COUNT() so it's not bad
    #   - CHAR, DATE, and DATETIME only have COUNT() so
    #     they get the smallest weight
    weightMap = {
        'INTEGER': 200,
        'DECIMAL': 200,
        'VARCHAR': 75,
        'CHAR': 25,
        'DATE': 25,
        'DATETIME': 25
    }
    weights = [weightMap[columnMap[column].columns[column]['unit']] if columnMap[column].columns[column]['unit'] in weightMap else 100 for column in foreignColumnList]

    # Selects a random column based on the weights
    selectedColumn = random.choices(foreignColumnList, weights)[0]



    # Holds the operator and function
    comparisonOperator = ''
    queryFunction = ''
    


    # There's a small chance to eschew caring about the datatype
    # and instead use an `IN (SELECT ...)`
    if random.random() * 10 < 1:

        # ...And another less small chance to use conditionals
        # on this type of subquery
        if random.random() * 3 < 1:
            pass

        return subqueryStatement('IN', selectedColumn, columnMap[selectedColumn].name)


    # Chooses 
    if columnMap[selectedColumn].columns[selectedColumn]['unit'] in ['INTEGER', 'DECIMAL']:
        pass

    if columnMap[selectedColumn].columns[selectedColumn]['unit'] in ['DATE', 'DATETIME']:
        pass

    if columnMap[selectedColumn].columns[selectedColumn]['unit'] in ['VARCHAR']:
        pass

    statement = subqueryStatement(comparisonOperator, selectedColumn, columnMap[selectedColumn].name, queryFunction)
    print(statement)


    # INTEGER functions
    #AVG() – returns the average value of a group.
    #COUNT() – returns the number of rows that match a specified condition
    #MAX() – returns the maximum value in a group.
    #MIN() – returns the minimum value in a group
    #SUM() – returns the sum of values

    # STRING functions
    #LENGTH()

    # Select column

    # Select function (if function)

    # Select comparator based on column data type

    # Build subquery

def subqueryStatement(comparisonOperator, selectedColumnName, tableName, queryFunction=''):
    return f" {comparisonOperator} (SELECT {queryFunction}({selectedColumnName}) FROM {tableName})" if queryFunction else f" {comparisonOperator} (SELECT {selectedColumnName} FROM {tableName})"



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
        return string

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
def questionConditionals(conditionalValues, string='', database=None):
    
    # If there aren't any conditionals, just return
    if not conditionalValues:
        return string, {}


    if database:
        columnMap = database.getColumnMap(tableNames=False)

    # Adds the 'where' if necessary
    string += ' where'
    
    # Keeps track of when to use which comparisons:
    # `>`, `<`, `>=`, `<=`, `!=`, `=`
    conditionalComparators = {}

    # Keeps track of when to use 'and' vs 'or'
    conditionalConnectors = {}


    for key in conditionalValues.keys():

        # Selects the comparison operator.
        # Drastically prefers comparison operators that will return
        # many values even when the column is unique. Also is biased
        # against `!=` since, unlike for CHAR and VARCHAR, the value
        # has no guarantee of being in conditionalValues, so a query
        # with `WHERE $col != $val` will often be equivalent to the
        # cluase's absence
        if columnMap and columnMap[key].columns[key]['unit'] in ['INTEGER', 'DECIMAL', 'DATE', 'DATETIME']:
            conditionalComparators[key] = random.choices(['>', '>=', '<', '<=', '=', '!='], [5, 5, 5, 5, 2, 1])[0]
        
        # Weights `!=` as less likely mainly because it looks worse
        else:
            conditionalComparators[key] = random.choices(['=', '!='], [2, 1])[0]

        # Randomly chooses a logical operator to
        # connect the conditionals. Prefers to use
        # 'or's since they result in more rows
        conditionalConnectors[key] = random.choices(['OR', 'AND'], [2, 1])[0]



        # Adds the column
        string += f" <b>{key}</b>"

        # Adds the appropraite comparing operator
        match conditionalComparators[key]:
            case '>': string += ' <em>is greater than</em>'
            case '>=': string += ' <em>is greater than or equal to</em>'
            case '<': string += ' <em>is less than</em>'
            case '<=': string += ' <em>is less than or equal to</em>'
            case '=': string += ' <em>is equal to</em>'
            case '!=': string += ' <em>is not equal to</em>'
        
        # Adds the value
        string += f" <b>{conditionalValues[key]}</b>"

        # Adds the logical operator
        if conditionalConnectors[key] == 'OR':
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
    
    return string, conditionalConnectors, conditionalComparators

# Adds a set of conditionals to a statement
def statementConditionals(statement='', conditionalValues={}, conditionalConnectors={}, conditionalComparators={}, clauseType=' WHERE'):
    
    # If there aren't any conditionals, just return
    if not conditionalValues:
        return statement
    
    statement += clauseType

    # Includes the conditional if they exist as
    # well as the condtional connector
    for key in conditionalValues:
        statement += f" {key} {conditionalComparators[key]} '{conditionalValues[key]}' {conditionalConnectors[key]}"

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
        
        # Prevents a selection of a column that is both foreign
        # and does not update on cascade, only if 'restrictive'
        if restrictive and columnMap[conditionalColumn].columns[conditionalColumn]['references'] and not columnMap[conditionalColumn].columns[conditionalColumn]['isOnUpdateCascade']:
            continue

        
        # If the column can support querries of the form 
        # `>`, `<`, `>=`, `<=`, then create a random value
        # to place in conditionalValues
        if columnMap[conditionalColumn].columns[conditionalColumn]['unit'] in ['INTEGER', 'DECIMAL', 'DATE', 'DATETIME']:

            # Generate a handful of random values of the appropriate
            # type and sort them
            vals = sorted(nd.generateNoisyDataNoFile(columnMap[conditionalColumn], conditionalColumn, 10, True))

            # Return the middle value. Since the list was sorted, the
            # middle value is also the median value. Since an even number
            # of items were created, this is biased towards smaller numbers,
            # but only slightly
            conditionalValues[conditionalColumn] = vals[len(vals) // 2]

            # Skips the rest of the loop, since we don't want to override this
            # value with an existing one, as through the lines below
            continue


            
        # Chooses a random value from the generated data to be updated
        randomValueIndex = nd.popRandom(indexList)

        # Grabs the randomly selected values
        conditionalValues[conditionalColumn] = columnMap[conditionalColumn].rows[conditionalColumn][randomValueIndex]
    
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
    #   - distinct
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
            'isDistinct': 0
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

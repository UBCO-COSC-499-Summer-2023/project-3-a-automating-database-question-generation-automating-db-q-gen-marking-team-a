import os
from random import choice, randint

# This allows DroneCI to see the RASQLib module
import sys
sys.path.append('/drone/src/databaseCourse/serverFilesCourse/')

from RASQLib import noisyData as nd



# Used for modelling a database and tables during question 
# generation and loading table data from text files

# Models a group of tables
class Database:
    def __init__(self, isSQL=True, file='', columns=5, joins=0, depth=3, clauses={}, constraints={'': {'name': '', 'unit': 'INTEGER', 'unitOther': None}}, rows=0, random=True):

        self.isSQL = isSQL
        


        # For SQL databases
        if isSQL:

            columnNames = parseColumnsFromFile('randomColumnsSQL')

            # When columns are set to zero, it indicates that
            # a table is being pased in (used to support old
            # difficulty-class questions). Otherwise, create
            # the primary table
            if columns == 0:
                self.primaryTable = file
            else:
                self.primaryTable = Table(file=file, columns=columns, joins=joins, clauses=clauses, constraints=constraints, rows=rows, database=self, isSQL=isSQL, random=random, columnNames=columnNames)
            
            # Gets the referenced tables
            self.referencedTables = self.primaryTable.getReferencedTables(static=not random, columnNames=columnNames)
        

        
        # For RelaX databases
        else:
            columnNames = parseColumnsFromFile('randomColumnsRelaX')
            self.generateTableSet(columns=columns, joins=joins, depth=depth, rows=rows, columnNames=columnNames)
            
        

    # Generates a table set for RelaX
    def generateTableSet(self, columns=5, joins=5, depth=3, rows=0, columnNames=[]) -> dict:

        # Gets a list of possible table names
        self.tableSet = {}
        
        # The primary table should have more columns
        for i in range(joins + 1):
            #dataset[i] = Table(columns=columns, columnNames=columnNames, joins=2, isSQL=False)
            self.tableSet[i] = Table(columns=columns, joins=2, isSQL=False, columnNames=columnNames)
            ''' Skyler here,
                I'm getting rid of a random amount of tables
                in favour of using the `columns` parameter.
                Not to mention a table should NEVER have
                less than 3 columns, as would be possible
                in the `else` statement
            if i == 0:
                dataset[i] = Table(columns=randint(3,5), columnNames=columnNames, joins=2)
            else:    
                dataset[i] = Table(columns=randint(2,4), columnNames=columnNames, joins=2)
            '''

        # Populates the table with data
        if rows:
            self.generateRows(rows)

        # Links tables such that there is a depth
        # of `d`
        for i in range(depth-1):
            self.tableSet[i].link(self.tableSet[i+1])

        # The rest of the joins link the remaining
        # table to a random one in the depth chain
        for i in range(depth, joins + 1):
            self.tableSet[randint(0,depth-1)].link(self.tableSet[i])



    # Populates the database with rows of data
    #
    # Note: This function respects references so a foreign key
    # reference between two tables will holds the same value
    def generateRows(self, qty):
        if self.isSQL:
            self.generateRowsSQL(qty)
        else:
            self.generateRowsRelaX(qty)

    # Note: this CAN throw a "UNIQUE constraint failed" IF the
    # primary table has two references to the same table (such
    # as the static `flight` table) AND there exists a duplicate
    # value between the different tables. THIS CAN NEVER HAPPEN
    # ON RANDOM TABLES since a random primary table will never
    # hold more than one reference to a given secondary random
    # table. In other words, no worries.
    def generateRowsSQL(self, qty):
        # Generates the primary table's rows
        self.primaryTable.generateRows(qty)

        # Generates referenced table's rows.
        # Foreign key constrains are violated here.
        for table in self.referencedTables:
            self.referencedTables[table].generateRows(qty)

        # Gets the primary's key map for easy references
        keyMap = self.primaryTable.getKeyMap()

        # Overrides the foreign column in the referenced table
        # to be the foreign key's column in the primary table.
        # The list() performs a deep copy rather than a shallow one.
        for key in keyMap:
            self.referencedTables[keyMap[key]['references']].rows[keyMap[key]['foreignKey']] = list(self.primaryTable.rows[key])
    
    # This adds all rows from conditionalValues into
    # the appropriate table's backend rows
    def addRowsBackend(self, conditionalValues):
        
        # Gets a list of all tables.
        # The list comprehension allows for a deep copy of
        # the dictionary (but not its values)
        allTables = {self.referencedTables[key].name: self.referencedTables[key] for key in self.referencedTables}
        allTables[self.primaryTable.name] = self.primaryTable
        
        for table in allTables:

            # Each conditional value will get their own row
            for key in conditionalValues:

                # Check if the value should be associated with
                # this table
                if key in allTables[table].columns:
                    row = {}

                    keyMap = self.primaryTable.getKeyMap()
                    for mKey in keyMap:
                        if keyMap[mKey]['foreignKey'] == key:
                            table = self.primaryTable

                    # Fills in the entire row
                    for column in allTables[table].columns:
                        if key == column:
                            row[column] = [conditionalValues[key]]
                        else:
                            row[column] = nd.generateNoisyData(allTables[table], column)

                    # Adds the row to the appropriate table
                    allTables[table].addRowBackend(row)
    
    # Generates backend rows such that each table will have
    # a number of rows equal to qty; it does not necessarily
    # generate qty number of rows.
    def generateRowsBackend(self, qty=0):

        if not qty:
            # Generates plenty of rows for the backend
            # database
            if self.primaryTable.rows:
                qty = len(list(self.primaryTable.rows.values())[0]) * 2

            # If we shouldn't generate rows, just return
            else:
                return

        # Subtracts the current amount of backend rows
        # from the amount needed to be generated
        amount = qty if not self.primaryTable.rowsBackend else qty - len(list(self.primaryTable.rowsBackend.values())[0])
        self.primaryTable.generateRowsBackend(amount)

        for table in self.referencedTables:

            # Subtracts the current amount of backend rows
            # from the amount needed to be generated
            amount = qty if not self.referencedTables[table].rowsBackend else qty - len(list(self.referencedTables[table].rowsBackend.values())[0])
            self.referencedTables[table].generateRowsBackend(amount)
        
        # Gets the primary's key map for easy references
        keyMap = self.primaryTable.getKeyMap()

        # Overrides the foreign column in the referenced table
        # to be the foreign key's column in the primary table.
        # The list() performs a deep copy rather than a shallow one.
        for key in keyMap:
            self.referencedTables[keyMap[key]['references']].rowsBackend[keyMap[key]['foreignKey']] = list(self.primaryTable.rowsBackend[key])



    # Ensuring consistency across FKs is done in Table.link(),
    # but does require the rows to be generated BEFORE the
    # tables are linked
    def generateRowsRelaX(self, qty):
        for table in self.tableSet:
            self.tableSet[table].generateRows(qty)
    


    # Adds the tables' schema to data
    def loadColumns(self, data):

        # Iterate over tables, if there are any
        # Add their schema to the initialize string
        if self.referencedTables:
            for table in self.referencedTables:
                data['params']['db_initialize_create'] += f"{self.referencedTables[table].getSQLSchema()}\n"
        
        # Adds the primary table afterwards.
        # Since the primary table may reference the foreign
        # tables but NOT vice versa, it is required that the
        # primary table is loaded after such that foreign
        # key constrains are satisfied.
        data['params']['db_initialize_create'] += self.primaryTable.getSQLSchema()
    
    # Adds the tables' rows to the data
    def loadRows(self, data):

        # Iterate over tables, if there are any
        # Add their inserts to the initialize string
        if self.referencedTables:
            for table in self.referencedTables:
                if self.referencedTables[table].rows:
                    data['params']['db_initialize_insert_frontend'] += self.referencedTables[table].getInserts()
        
        # Adds the primary table afterwards.
        # Since the primary table may reference the foreign
        # tables but NOT vice versa, it is required that the
        # primary table is loaded after such that foreign
        # key constrains are satisfied.
        data['params']['db_initialize_insert_frontend'] += self.primaryTable.getInserts()
    
    def loadRowsBackend(self, data):

        # Iterate over tables, if there are any
        # Add their inserts to the initialize string
        if self.referencedTables:
            for table in self.referencedTables:
                if self.referencedTables[table].rowsBackend:
                    data['params']['db_initialize_insert_backend'] += self.referencedTables[table].getInsertsBackend()
        
        # Adds the primary table afterwards.
        # Since the primary table may reference the foreign
        # tables but NOT vice versa, it is required that the
        # primary table is loaded after such that foreign
        # key constrains are satisfied.
        data['params']['db_initialize_insert_backend'] += self.primaryTable.getInsertsBackend()
    
    def loadRelaX(self, data):
        for table in self.tableSet:
            data['params']['db_initialize_create'] += self.tableSet[table].getRelaXSchema()
        data['params']['db_initialize_create'] = data['params']['db_initialize_create'][:-1]
        #with open("./RelaXElementSharedLibrary/ShipmemtDatabase.txt") as f:
        #    data['params']['db_initialize'] = f.read()
    
    # Adds everything necessary for each table to the data variable
    def loadDatabase(self, data):
        if self.isSQL:
            # CREATE statement
            self.loadColumns(data)

            # INSERT statements for the frontend DB
            self.loadRows(data)



            # Fills in the backend rows
            self.generateRowsBackend()

            # INSERT statement for the backend DB
            self.loadRowsBackend(data)
        else:
            self.loadRelaX(data)
    


    def getTableMap(self):
        keyMap = self.primaryTable.getKeyMap()
        tableMap = {key: self.referencedTables[keyMap[key]['references']] for key in keyMap}
        tableMap[self.primaryTable.name] = self.primaryTable
        return tableMap

    # Column map is the opposite of tableMap. Given a column,
    # it returns the table it originated from.
    #   columnMap {
    #       $columnName: $table
    #   }
    def getColumnMap(self, tableNames=True):
        tableMap = self.getTableMap()
        columnMap = {}
        for key in tableMap:
            for column in tableMap[key].columns:
                if tableNames:
                    columnMap[column] = tableMap[key].name
                else:
                    columnMap[column] = tableMap[key]
        return columnMap


    # Prints the schema of all tables in the database
    def __str__(self):
        if self.isSQL:
            return f"{self.primaryTable.getSQLSchema()}{''.join([self.referencedTables[referencedTable].getSQLSchema() for referencedTable in self.referencedTables])}"
        else:
            return f"{''.join([self.tableSet[table].getRelaXSchema() for table in self.tableSet])}"



# Models a table for easy question generation
class Table:

    # A table has a name and some columns.
    # File name and table name are equivalent.
    #   File: the name of the text file if it exists OR the name of the random table
    #   Columns: the number of columns in the table
    def __init__(self, file='', columns=5, joins=0, clauses={}, constraints={}, rows=0, database=None, isSQL=True, random=True, columnNames=[]):
        self.name = file
        self.database = database
        self.columns = {}
        self.rows = {}
        self.rowsBackend = {}
        self.isSQL = isSQL

        # If no constrains are present, guarantees the
        # existance of a basic INTEGER/NUMBER type column.
        # Useful for generating random queries.
        if not constraints:
            if isSQL:
                constraints = {'': {'name': '', 'unit': 'INTEGER', 'unitOther': None}}
            else:
                constraints = {'': {'name': '', 'unit': 'NUMBER', 'unitOther': None}}

        # Adds columns.
        # Also passes in column names from the file if they
        # were not supplied, which only happens for testing.
        self.load(file, columns, joins, clauses, constraints, random, columnNames if columnNames else parseColumnsFromFile('randomColumnsSQL'))

        # Adds data
        self.generateRows(rows)



    # Loads a table object based on the file.
    # All parameters other than file only matter to
    # random tables, not static tables; for random tables.
    # f"{file}" will become the table name if it is
    # provided, otherwise a random name will be chosen
    def load(self, file, columns, joins, clauses, constraints, random, columnNames):

        if not random:
            self.loadFromText(file)
        else:
            self.loadRandom(self.name, columns, joins, clauses, constraints, columnNames)

    # Given the path to a text file, loads its data
    def loadFromText(self, file):

        # If the file is not set but the question uses
        # a static table, find a static table
        tableFiles = getAllTableFiles()
        if not file or file not in tableFiles:
            file = choice(tableFiles)
        
        # Gets the path to that file
        filePath = relativeTableFilePath(file)

        # Only includes lines that aren't exclusively
        # white text and strips them of trailing/leading
        # white text
        lines = []
        with open(filePath, 'r') as tableFile:
            lines = [line.strip() for line in tableFile if not line.isspace()]
        

        # Creates the column and adds it
        # The first line contains the table name so ignore it
        # The last line contains '};' so ignore it
        for line in lines[1:-1]:

            # Gets the words from the line
            words = line.split(' ')

            # Handles the case where the line describes a foreign key
            if 'FOREIGN KEY' in line.upper():

                # Gets the foreign key
                # Removes the parenthesis
                column = words[2][1:-1]

                # Get the table it references
                references = words[4]

                # Gets the column it references
                # Removes parentheses
                foreignKey = words[5][words[5].find('(') + 1 : words[5].find(')')]

                # Checks additional clauses
                isOnUpdateCascade = 'ON UPDATE CASCADE' in line.upper()
                isOnDeleteSetNull = 'ON DELETE SET NULL' in line.upper()

                # Updates the column
                self.columns[column]['references'] = references
                self.columns[column]['foreignKey'] = foreignKey
                self.columns[column]['isOnUpdateCascade'] = isOnUpdateCascade
                self.columns[column]['isOnDeleteSetNull'] = isOnDeleteSetNull

            # Handles the case where the line describes a primary key
            elif 'PRIMARY KEY' in line.upper():
                
                # Gets a list of primary keys
                primaryKeys = line[line.find('(') + 1 : line.find(')')].split(',')

                # Sets the column as a primary key
                for primaryKey in primaryKeys:
                    self.columns[primaryKey.strip()]['isPrimary'] = True
                

            # Otherwise add the column
            else:

                # The first word is always the name of the column
                name = words[0]

                # The second word is the unit
                # Removes the comma if it is present
                unit = words[1].upper() if ',' not in words[1] else words[1][:-1].upper()

                # If there is some additional clause for the unit, such
                # as the length of a CHAR, grab it and remove parenthesis
                unitOther = None
                if words[1].find('(') != -1:
                    unitOther = unit[unit.find('(') + 1 : unit.find(')')]
                    unit = unit[: unit.find('(')]


                # Checks if the line has a NOT NULL clause
                isNotNull = 'NOT NULL' in line.upper()

                # Checks if the line has the UNIQUE clause
                isUnique = 'UNIQUE' in line.upper()

                # Adds the column
                self.columns[name] = {
                    'name': name,
                    'unit': unit,
                    'unitOther': unitOther,
                    'isPrimary': False,
                    'isNotNull': isNotNull,
                    'isUnique': isUnique,
                    'references': None,
                    'foreignKey': None,
                    'isOnUpdateCascade': False,
                    'isOnDeleteSetNull': False
                }



    # Creates a random table
    def loadRandom(self, name, columns, joins, clauses, constraints, columnNames):

        # Checks whether the parameters are legal
        #
        # Columns must be at least three otherwise there is
        # a high chance of PL throwing a timeout exception.
        # It's due to the line `self.columns[columnName] = {...}`
        # BUT HOW!? How does *that* line get a timeout iff the
        # count of columns is either 1 or 2? It makes no sense!
        if columns < 3:
            print(f"Table requires at least 3 columns (was supplied with {columns} columns)")
            return None
        
        if joins < 0:
            print(f"Table cannot have negative amount of foreign keys (was supplied with {joins} foreign keys)")
            return None
        
        if joins > columns:
            print(f"Table cannot have more foreign keys than columns (was supplied with {columns} columns and {joins} foreign keys)")
            return None

        # Tests if the clauses are valid
        primaryKeys = 0
        for clause in clauses:

            # Grabs the value of the clause
            value = clauses[clause]

            # Checks if any clause has a negative amount
            if value < 0:
                print(f"Table cannot have negative amount of a clause (was supplied with {value} '{clause}')")
                return None

            # Checks if given clause has too many
            match clause:
                case 'primaryKeys':
                    if value > columns - joins:
                        print(f"Table cannot have more primary keys than columns and foreign keys (was supplied with {value} primary keys, {columns} columns, and {joins} foreign keys)")
                        return None
                    primaryKeys = value
                case 'isNotNull':
                    if value > columns - joins - primaryKeys:
                        print(f"Table cannot have more NO NULL clauses than columns, primary keys, and foreign keys (was supplied with {value} clauses, {columns}, columns, {primaryKeys} primary keys, and {joins} foreign keys)")
                        return None
                case 'isUnique':
                    if value > columns - joins - primaryKeys:
                        print(f"Table cannot have more UNIQUE clauses than columns, primary keys, and foreign keys (was supplied with {value} clauses, {columns}, columns, {primaryKeys} primary keys, and {joins} foreign keys)")
                        return None
                case 'isOnUpdateCascade':
                    if value > joins:
                        print(f"Table cannot have more ON UPDATE CASCADE clauses than foreign keys (was supplied with {value} clauses and {joins} foreign keys)")
                        return None
                case 'isOnDeleteSetNull':
                    if value > joins:
                        print(f"Table cannot have more ON DELETE SET NULL clauses than foreign keys (was supplied with {value} clauses and {joins} foreign keys)")
                        return None
                    


        # Selects a random name if none are provided
        if not name:
            self.name = choice(getRandomTableNames())


        # Adds foreign key constraints
        if constraints:
            for key in constraints.keys():

                # If the default contraint, then choose
                # an applicable name for an INTEGER
                if not key:
                    constraints[key]['name'] = choice(['num', 'id', f"{self.name[:1].lower()}id"])

                self.columns[constraints[key]['name']] = {
                    'name': constraints[key]['name'],
                    'unit': constraints[key]['unit'],
                    'unitOther': constraints[key]['unitOther'],
                    'isPrimary': True, # Must be true to prevent SQLite FK constraint error
                    'isNotNull': False,
                    'isUnique': False,
                    'references': None,
                    'foreignKey': None,
                    'isOnUpdateCascade': False,
                    'isOnDeleteSetNull': False
                }


        # Keeps adding columns until there are enough
        while len(self.columns) < columns:

            # Chooses a random column to add
            # Pops the column to ensure no duplicates
            addColumn = columnNames.pop(choice(range(len(columnNames))))

            # Checks if the column would override an existing 
            # column. This could only occur due to foreign key
            # constraints adding a column then the pop() function
            # giving the same column. Requires at most one more
            # pop() to fix
            if addColumn[0] in self.columns.keys():
                addColumn = columnNames.pop(choice(range(len(columnNames))))

            # Grabs parameters
            columnName = addColumn[0]
            columnUnit = addColumn[1]

            # Grabs the unit specification as necessary
            columnUnitOther = None
            match columnUnit:
                case 'DECIMAL': columnUnitOther = f"{choice(addColumn[2])},{choice(addColumn[3])}"
                case 'CHAR': columnUnitOther = f"{choice(addColumn[2])}"
                case 'VARCHAR': columnUnitOther = f"{choice(addColumn[2])}"

            # Adds the column.
            # (Usually) times-out if columns == 1 or 2
            self.columns[columnName] = {
                    'name': columnName,
                    'unit': columnUnit,
                    'unitOther': columnUnitOther,
                    'isPrimary': False,
                    'isNotNull': False,
                    'isUnique': False,
                    'references': None,
                    'foreignKey': None,
                    'isOnUpdateCascade': False,
                    'isOnDeleteSetNull': False
                }



        # This copy ensures we don't duplicately
        # Select a column
        columnsCopy = list(self.columns.keys())

        # Gets a list of random tables
        randomTables = getRandomTableNames()

        # Keeps adding joins until there are enough
        while len(self.getKeyMap()) < joins:

            # Chooses a random column to become foreign.
            # Prevents certain columns from becoming FKs
            # due to uniqueness causing issues when
            # later creating random data for the rows
            foreignColumn = None
            while not foreignColumn or 'Airport' in foreignColumn or 'province' in foreignColumn:

                # Breaks out of the loop if there are no
                # fitting columns. This will assaing a 
                # 'bad' column to the FK, but there is
                # still only a small chance of a crash
                if len(columnsCopy) == 0:
                    break

                # Grabs a random column
                foreignColumn = columnsCopy.pop(choice(range(len(columnsCopy))))



            # Selects a random table to reference
            self.columns[foreignColumn]['references'] = randomTables.pop(choice(range(len(randomTables))))

            # Tries another random name if this table's
            # name happens to match the random name. 
            # Note: no need for a while loop; because of the
            # pop(), it is guaranteed that a second attempt
            # will provide a unique name.
            if self.name == self.columns[foreignColumn]['references']:
                self.columns[foreignColumn]['references'] = randomTables.pop(choice(range(len(randomTables))))



            # Alters the column names.
            # The first letter of the FKs on either side will
            # be the name fo their respective table. Otherwise,
            # the column names will be the same.

            # Changes the foreign key's name
            self.columns[foreignColumn]['foreignKey'] = f"{self.columns[foreignColumn]['references'][0:1].lower()}{foreignColumn}"

            # Changes this table's column name
            self.columns[foreignColumn]['name'] = f"{self.name[0:1].lower()}{foreignColumn}"

            # Removes the old column while updateting the new
            self.columns[f"{self.name[0:1].lower()}{foreignColumn}"] = self.columns.pop(foreignColumn)



        # Accounts for existing PKs due to table defaults
        try:
            clauses['primaryKeys'] -= len(self.getPrimaryKeys())
        except:
            pass

        # Adds clauses
        for clause in clauses:

            # All clauses are of the form...
            #   clause: INTEGER
            # ...so iterate over the integer until a sufficient
            # number of columns have been selected.
            for i in range(clauses[clause]):

                match clause:

                    # Selects primary keys
                    case 'primaryKeys':

                        # Keeps choosing columns until one is valid
                        column = None
                        while not column or self.columns[column]['references'] or self.columns[column]['isPrimary']:
                            column = choice(list(self.columns.keys()))

                        self.columns[column]['isPrimary'] = True

                    # NOT NULL constraint
                    case 'isNotNull':
                        
                        # Keeps choosing columns until one is valid
                        column = None
                        while not column or self.columns[column]['references'] or self.columns[column]['isPrimary']:
                            column = choice(list(self.columns.keys()))

                        self.columns[column]['isNotNull'] = True

                    # UNIQUE constraint
                    case 'isUnique':

                        # Keeps choosing columns until one is valid
                        column = None
                        while not column or self.columns[column]['references'] or self.columns[column]['isPrimary']:
                            column = choice(list(self.columns.keys()))

                        self.columns[column]['isUnique'] = True

                    # CASCADE ON UPDATE clause
                    case 'isOnUpdateCascade':
                        
                        # Keeps choosing columns until one is valid
                        column = None
                        while not column or not self.columns[column]['references'] or self.columns[column]['isOnUpdateCascade']:
                            column = choice(list(self.columns.keys()))

                        self.columns[column]['isOnUpdateCascade'] = True

                    # SET NULL ON DELETE clause
                    case 'isOnDeleteSetNull':

                        # Keeps choosing columns until one is valid
                        column = None
                        while not column or not self.columns[column]['references'] or self.columns[column]['isOnDeleteSetNull']:
                            column = choice(list(self.columns.keys()))

                        self.columns[column]['isOnDeleteSetNull'] = True

                    # Crashes if the clause is not valid
                    case _:
                        assert False, f"Clause {clause} is invalid"



    # Links one table to another
    # Used with RelaX
    def link(self, foreignTable):     
        column = (choice(list(self.columns.keys())))
        foreignTable.columns[column] = {
            'name' : column,
            'unit' : self.columns[column]['unit'],
            'references' : None,
            'foreignKey' : column,
            #'columnData' : {}
        }

        if foreignTable.rows:
            foreignTable.rows[column] = self.rows[column]



    # Returns a dictionary that maps the foreign key of the supplied
    # table to the referenced tables. If the unique parameter is true,
    # this dictionary contains a set of tables: no duplicated. Otherwise,
    # there may be duplicate tables with unique foreign keys.
    def getReferencedTables(self, unique=True, static=False, columnNames=[]):
        
        # Uses a dictionary to store the tables and a set to keep track
        # of unique table names
        tables = {}
        tableSet = set()

        # Iterates over the table's foreign keys
        for key in self.getKeyMap().keys():

            # Checks to see if the table name is already in the set.
            # Only matters if unique is True.
            if self.columns[key]['references'] not in tableSet:

                # Chooses the number of columns to exist in the random
                # referenced tables
                columns = randint(4, 6)

                # Ensures foreign key consistency across generated tables
                #   name of the column in the foreign table: {
                #       'unit': the data type of the column
                #       'unitOther': the other information related to the data type
                #   }
                constraints = {
                    self.columns[key]['foreignKey']: {
                        'name': self.columns[key]['foreignKey'],
                        'unit': self.columns[key]['unit'],
                        'unitOther': self.columns[key]['unitOther']
                    }
                }

                # Loads an approrpiate table into the dictionary
                tables[self.columns[key]['references']] = Table(file=self.columns[key]['references'], columns=columns, constraints=constraints, database=self.database, isSQL=True, random=not static, columnNames=columnNames)

                # Adds the table name to the set if unique is True
                if unique:
                    tableSet.add(self.columns[key]['references'])

        # Returns a dictionary of all referenced tables
        #   table name: respective Table object
        return tables



    # Returns a dictionary with the following mapping:
    #   column: (if the column is a foreign key)
    #       'references': the table referenced
    #       'foreignKey': the column in the referenced table
    def getKeyMap(self):
        return {key: {'references': self.columns[key]['references'], 'foreignKey': self.columns[key]['foreignKey']} for key in self.columns.keys() if self.columns[key]['references']}
    
    # Returns all primary key columns
    def getPrimaryKeys(self):
        return {key: self.columns[key] for key in self.columns.keys() if self.columns[key]['isPrimary']}
    


    # Populates the table's rows    
    def generateRows(self, qty):
        if qty:

            # Generates the data
            columns = nd.generateColumns(self, qty)

            for key in columns:

                # Creates the column if it does not already exist
                if not key in self.rows:
                    self.rows[key] = []

                # Adds the column
                self.rows[key] += columns[key]
    
    def generateRowsBackend(self, qty=0):
        if not qty:

            # Generates plenty of rows for the backend
            # database
            if self.rows:
                qty = len(list(self.rows.values())[0]) * 2

            # If we shouldn't generate rows, just return
            else:
                return

        # Generates the data
        columns = nd.generateColumns(self, qty)

        for key in columns:

            # Creates the column if it does not already exist
            if not key in self.rowsBackend:
                self.rowsBackend[key] = []

            # Adds the column
            self.rowsBackend[key] += columns[key]

    
    # Adds a row to this table
    def addRow(self, row, index=0):
        for key in self.columns.keys():
            if key not in self.rows:
                self.rows[key] = []
            self.rows[key].append(row[key][index])
    
    def addRowBackend(self, row, index=0):
        for key in self.columns.keys():
            if key not in self.rowsBackend:
                self.rowsBackend[key] = []
            self.rowsBackend[key].append(row[key][index])



    # Returns the table's DDL schema
    def getSQLSchema(self):

        # Creates the first line
        schema = f"CREATE TABLE {self.name}" + " (\n"

        # Adds each column
        for column in self.columns:
            schema += f"\t{self.columns[column]['name']} {self.columns[column]['unit']}"

            # Includes the unit other in parentheses
            if self.columns[column]['unitOther']:
                schema += f"({self.columns[column]['unitOther']})"
            
            # Includes the NOT NULL clause if necessary
            if self.columns[column]['isNotNull']:
                schema += ' NOT NULL'

            # Includes the UNIQUE clause if necessary
            if self.columns[column]['isUnique']:
                schema += ' UNIQUE'

            # Adds a comma at the end
            schema += ',\n'
        


        # Adds the primary keys
        for column in self.columns:

            # Adds a primary key
            if self.columns[column]['isPrimary']:

                # For the first primary key
                if "PRIMARY KEY" not in schema:
                    schema += f"\tPRIMARY KEY ({self.columns[column]['name']}"
                # For all subsequent primary keys
                else:
                    schema += f", {self.columns[column]['name']}"
        
        # Finishes the line, if necessary
        if "PRIMARY KEY" in schema:
            schema += "),\n"



        # Adds the foreign keys
        for column in self.columns:
            if self.columns[column]['references']:
                schema += f"\tFOREIGN KEY ({self.columns[column]['name']}) REFERENCES {self.columns[column]['references']} ({self.columns[column]['foreignKey']})"

                # Set null clause
                if self.columns[column]['isOnDeleteSetNull']:
                    schema += ' ON DELETE SET NULL'

                # Cascade clause
                if self.columns[column]['isOnUpdateCascade']:
                    schema += ' ON UPDATE CASCADE'

                # Comma and newline
                schema += ",\n"
        
        # Removes the comma at the end; closes schema
        schema = schema[0:-2] + "\n);\n"

        return schema
    
    # Returns insert statements for this table's rows
    def getInserts(self):
        return ''.join([f"INSERT INTO {self.name} VALUES ({str([self.rows[key][i] for key in self.rows])[1:-1]});\n" for i in range(len(list(self.rows.values())[0]))]) if self.rows else ''
    
    def getInsertsBackend(self):
        return ''.join([f"INSERT INTO {self.name} VALUES ({str([self.rowsBackend[key][i] for key in self.rowsBackend])[1:-1]});\n" for i in range(len(list(self.rowsBackend.values())[0]))]) if self.rowsBackend else ''



    # Returns the entire schema for RelaX
    def getRelaXSchema(self):
        
        schema = ''

        # Iterates over all columns
        for key in self.columns:
            schema += f"{self.name}.{key}:{self.columns[key]['unit'].lower()}, "
        schema = schema[:-2] + '\n'


        # Iterates over rows and columns
        for row in range(len(list(self.rows.values())[0])):
            for key in self.rows:

                # Adds the line, with quotes.
                # Strings will break the editor if they do
                # not have quotes. All other data types will
                # break the editor if they do have quotes.
                #
                # Notice that, unlike most string formating,
                # the single quotes are on the outside. It is
                # important that the double quotes are on the
                # inside due to apostrophes in names like
                # "St. John's"
                if self.columns[key]['unit'].upper() == 'STRING':
                    schema += f'"{self.rows[key][row]}", '

                # Adds the line, without quotes
                else:
                    schema += f"{self.rows[key][row]}, "
        
            # Removes the trailing comma and adds a newline
            schema = schema[:-2] + '\n'

        # Wraps the output in braces
        return "{\n"+schema+"};"
        


    # The same as calling Table.getSchema()
    def __str__(self):
        if self.isSQL:
            return self.getSQLSchema()
        else:
            return self.getRelaXSchema()



# Helper functions

# Returns the file path to the table file
def relativeTableFilePath(file):
    return f"{absoluteDirectoryPath()}/randomTables/{file}.txt"

# Returns the file path to the table metadata file
def relativeTableDataFilePath(file):
    return f"{absoluteDirectoryPath()}/randomTableData/{file}.txt"

# Returns the absolute directory of RASQLib
def absoluteDirectoryPath():
    currentDirectory = os.path.abspath(os.curdir)

    if 'RASQLib' in currentDirectory:
        return currentDirectory
    else:
        courseFile = currentDirectory[:currentDirectory.find('/elements')]
        return f"{courseFile}/serverFilesCourse/RASQLib"

# Returns the create table statement from the
# text file
def getStaticSchema(file):
    try:
        with open(relativeTableFilePath(file)) as file:
            return file.read()
    except:
        return None

# Lists all table files in the specified path
def getAllTableFiles(path=f"{absoluteDirectoryPath()}/randomTables"):
    try:
        # Removes the file extension of all files, if they exist
        return [file[:file.find('.')] for file in os.listdir(path)]
    except:
        return []

# Returns a list of names for random tables
def getRandomTableNames(path=relativeTableDataFilePath('randomTableNames')):
    try:
        with open(path) as file:
            # Strips out whitespace and only considers lines
            # that aren't exclusively whitespace
            return [line.strip() for line in file.readlines() if not line.isspace()]
    except:
       return []
    

# Given a marked-up textfile, return an array
# of possible columns for random table generation.
# A helper function for loadRandom
def parseColumnsFromFile(file):

    # Holds all the columns that can be selected
    columnNames = []

    # Reads the text file
    with open(relativeTableDataFilePath(file)) as columnsFile:

        # Iterates over each line
        for line in columnsFile:

            # Only cares about non-whitespace lines
            if line and not line.isspace():

                # Formats the line correctly.
                # Removes leading and trailing whitespace from
                # each word, as deliminated by ',' in the line
                words = [word.strip() for word in line.split(',')]

                # Grabs the parameters
                name = words[0]
                unit = words[1]
                unitOther = None



                # Handles the cases where the unitOther is not none
                if 'DECIMAL' == unit or 'CHAR' == unit or 'VARCHAR' == unit:
                    unitOther = parseRange(words[2])
                    
                    # Decimal needs two bits of data to
                    # describe its unitOther; hence length of 4
                    if unit == 'DECIMAL':
                        columnNames.append([name, unit, unitOther, parseRange(words[3])])
                    # The other columns with uniOther only require 3
                    else:
                        columnNames.append([name, unit, unitOther])
                
                # Adds columns without unitOther
                else:
                    columnNames.append([name, unit])
        
    # Returns the populated array
    return columnNames

# Given a range in the form of `xx-yy-zz` or
# `xx-yy`, returns a range. If there is no `-`,
# then return it unchanged as a string.
# A helper funciton of parseColumnsFromFile()
def parseRange(string):

    # Checks if it is a range
    if '-' in string:

        # Split over '-'
        split = string.split('-')

        # The format is:
        #   First item is the start
        #   Second item is the stop (inclusive!)
        #   Third item is the step (optional)
        start = int(split[0])
        stop = int(split[1]) + 1

        # Obtains the step, if it is included.
        # otherwise it defualts to 1
        step = 1
        if len(split) > 2:
            step = int(split[2])
        
        # Returns the range
        return range(start, stop, step)
    
    # If it is not a range, return as a string
    else:
        return f"{string}"
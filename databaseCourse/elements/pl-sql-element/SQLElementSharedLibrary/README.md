# SQLElementSharedLibrary

As a note, this document was last updated July 11th and in specific reference to the most up-to-date SQLAutogenerator branch at the time (`product-table-generation`).

`TODO`
- Describe each function in Autogenerator
- Update Autogenerator functions to include HTML parameterization
- Describe each function in Noisy Data
- Update Custom Grader to match SQLite backend when completed
- Describe each function in Text Database Handler
- Add `randomTableMetadata` folder, in which `randomColumns.txt` and `randomTableNames.txt` are placed


## __init__

Python libraries require an `__init__.py` file to be recognized as a library. The file is blank since it is only required to be present such that this folder is recognized as a library.


## Text Files

Text files include all the .txt files one directory level down, so all files in any of the following folders:
- lab2Databases
- lab3Databases
- noisyData
- randomTables
- randomTableMetadata (`TODO`)  
Such text files are used either to aid in random question generation or to hold DDL for static lab questions. These files are read during `pl-sql-element.py`'s `prepare()` function, either directly or when this library is invoked. The files used to aid random question generation holds lists of example data, where items are randomly chosen to create "clean" looking data.


## SQLAutogenerator

The autogenerator is responsible for creating random questions and initializing the front-end databases accordingly.


### autogenerate(data)

The autogenerate function calls the appropriate question generation function as specified by the passed HTML parameters, which were stored in the `data` variable. This function is called by `pl-sql-element.py` during its `prepare()` function.


### generateCreate(data, difficulty)

This function creates a random question for the CREATE-style question. 
Based on the difficulty and specified parameters of the question, it will select (`TODO` update to create rather than select) a random table appropriately. It creates a corresponding Table object which is used to facilitate the creation of the quesiton string; the Table object is iterated over where the details of each column are appended to the question string as prose.  
If the table generated references any other tables, those other tables are loaded by calling the `loadSchemas(data, Table[])` function, where `getReferencedTablesSet(Table)` is passed in.  
The solution is set by calling the `createStatement(Table)` function, which returns the table's schema. Since the generated table was used to create the question string, its schema corresponds to the CREATE statement solution.


### createStatement(Table)

The create statement function makes a CREATE statement for a given table. It does so by calling the table's `getSchema()` method.  
This function is called by `generateCreate()` to set the solution.


### generateInsert(data, difficulty)

This function creates a random question for the insert-style question. 
Based on the difficulty and specified parameters of the question, it will generate a table appropriately. It will then generate one row of data using the `generateRow(Table)` function. The generate row of data is used to create the question string.  
If the table generated references any other tables, those other tables are loaded by calling the `loadSchemas(data, Table[])` function, where `getReferencedTablesSet(Table)` is passed in.  
The solution is set by calling the `insertStatement(Table, row)` function, which returns the formatted SQL INSERT statement with the values of the row.


### insertStatement(Table, row)

The insert statement function creates an INSERT statement for a given table and a given row of data. It returns a string of the statement.
This function is called by `generateInsert()` to set the solution and it is also called by `loadNoisyData()` to set the database initialisation string in `data`.


### generateUpdate(data, difficulty)

This function creates a random question for the UPDATE-style question. 
Based on the difficulty and specified parameters of the question, it will generate a table appropriately and determine whether or not to use a conditional in the statement. Rows of random data will be generated. A random column from the table will be selected and a random value matching that column's data type will be generated. If a conditional is being used, a random value matching the selected column's data type will be selected from the generated rows. Using all selected data, a question string is generated.  
If the table generated references any other tables, those other tables are loaded by calling the `loadSchemas(data, Table[])` function, where `getReferencedTablesSet(Table)` is passed in. Additionally, all tables will have data generated that will be used to populate them.  
The solution is set by calling the `updateStatement(Table, updateColumn, updateValue, conditionalColumn, conditionalValue)` function, which returns the formatted SQL UPDATE statement corresponding to the parameters.


### updateStatement(Table, updateColumn, updateValue, conditionalColumn, conditionalValue)

The update statement function creates an UPDATE statement for a given table. The updateColumn parameter determines which column will be updated and it will be updated to match updateValue. If there is a conditionalColumn and conditionalValue (which are optional parameters), it will generate a statement where values from the conditionalColumn's column match conditionalValue's value. 
This function is called by `generateUpdate()` to set the solution.


### generateDelete(data, difficulty)

This function creates a random question for the DELETE-style question. 
Based on the difficulty and specified parameters of the question, it will generate a table appropriately. Rows of random data will be generated. A random column from the table will be selected and a random value matching that column's data type will be selected from the rows of generated data. Using all selected data, a question string is generated.
If the table generated references any other tables, those other tables are loaded by calling the `loadSchemas(data, Table[])` function, where `getReferencedTablesSet(Table)` is passed in. Additionally, all tables will have data generated that will be used to populate them.  
The solution is set by calling the `deleteStatement(Table, column, condition)` function, which returns the formatted SQL DELETE statment corresponding to the parameters.


### deleteStatement(Table, column, condition)

The delete statement function creates a DELETE statement for a given table. The column parameter specifies from which column the value needs to be deleted and condition is the condition.  
This function is called by `generateDelete()` to set the solution.


### generateQuery(data, difficulty)

This function creates a random question for the query-style question. 
Based on the difficulty and specified parameters of the question, it will create a table with an appropriate amount of columns, joins, and clauses. It then creates the referenced tables. It them selects a number of columns from all tables, ensuring that at least one column is taken from each table. Given the selected columns and joined tables, the question string is constructed.  
If the table generated references any other tables, those other tables are loaded by calling the `loadSchemas(data, Table[])` function, where the referenced tables are passed in. Additionally, all tables will have data generated that will be used to populate them.  
The solution is set by calling the `queryStatement(Table, keyMap, foreignKeyMap, selectedColumns, clauses)` function, which returns the formatted SQL SELECT statment corresponding to the parameters.


### queryStatement(Table, keyMap, foreignKeyMap, selectedColumns, clauses)

The query statement function creates a SELECT statement for a given table. The keyMap parameter is used to map the primary table's foreign keys to other tables. The parameter foreignKeyMap is used similarly to keyMap except it also includes the primary table (in other words, it also maps back to itself). The parameter selectedColumns holds the columns the SELECT statement must select, and clauses keep track of other conditional values and clauses.
This function is called by `generateQuery()` to set the solution.


## SQLCustomGrader

The custom grader compares the student's supplied answer against a pre-defined correct solution. It compares the similarity and grants a grade proportionally. If the student gets above some threshold, whose default value is 0.75 or 75%, they are given full marks on the question. Similarities below 0.75 are mapped as such: (0, 0.75) -> (0, 1).


## SQLNoisyData

The noisy data Python file generates random data given an SQL data type. If the column name matches against a list, a random value is drawn from the appropriate text file; this is done to generate human-readable random data. Otherwise, if the column name does not match, "noisy" random data is generated instead. This noisy data is worse than gibberish for data types such as VARCHAR or CHAR (since generating human-readable gibberish is difficult), but are generated from constrained ranges for data types such as INTEGER or DATETIME (and as such are human-readable).


## textDatabaseHandler

The text database handler models a simplified database and table system, used to assist random question generation. Its functionality focuses on a table as a set of columns as well as converting text file-stored values into memory.
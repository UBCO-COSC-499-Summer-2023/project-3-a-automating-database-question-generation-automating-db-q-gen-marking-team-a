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
- noisyData
- randomTableData
- randomTables
Such text files are used to aid in random question generation. These files are read during `pl-sql-element.py`'s `prepare()` function when this library is invoked. The files hold lists of example data, where items are randomly chosen to create "clean" looking data. The `noisyData` file contains common values for strings/VARCHAR datatypes; `randomTableData` contains names for tables, columns (with specifications for both RelaX and SQL table metadata), and a file that maps a column name to the appropriate file in `noisyData`; and, `randomTables` contains table DDL statements for various tables, but this is only used in difficulty-type questions for autogenerate CREATE questions.


## noisyData

This Python file generates random data given an SQL data type. If the column name matches against a list, a random value is drawn from the appropriate text file; this is done to generate human-readable random data. Otherwise, if the column name does not match, "noisy" random data is generated instead. This noisy data is worse than gibberish for data types such as VARCHAR or CHAR (since generating human-readable gibberish is difficult), but are generated from constrained ranges for data types such as INTEGER or DATETIME (and as such are human-readable).


### generateNoisyData(table, key, qty=1)

When an array of random data is desired, this function is called and it is responsible for calling the appropriate data-generating function. The `table` and `key` (a.k.a. column) parameters are used to determine the data-type of the column as well as whether or not to enforce distinct values. This function also checks if the column (`key`) is mapped to a file in the `noisyData` folder and, if so, grabbing values from said folder.


### generateNoisyDataNoFile(table, key, qty=1, unique=False)

If the key was not mapped to a file in `noisyData`, as determined by `generateNoisyData()`, then this function checks whether or not the table is a RelaX table or an SQL table, calling the next function as appropriate.


### generateNoisyDataNoFileSQL(table, key, qty=1, unique=False)

If the key was not mapped to a file in `noisyData`, as determined by `generateNoisyData()`, and the table was found to be an SQL table, as determined by `generateNoisyDataNoFile()`, then this function obtains the data-type and the data-type's metadata to determine which specific data-generating function to call.
The possible data-types are: INTEGER, DECIMAL, CHAR, VARCHAR, DATE, and DATETIME.


### generateNoisyDataNoFileRelaX(table, key, qty=1, unique=False)

If the key was not mapped to a file in `noisyData`, as determined by `generateNoisyData()`, and the table was found to be a RelaX table, as determined by `generateNoisyDataNoFile()`, then this function obtains the data-type and the data-type's metadata to determine which specific data-generating function to call.
The possible data-types are: NUMBER, DATE, and STRING.
In the case that the data-type is NUMBER and the key is `price`, then this function will return a float/decimal value. Otherwise, when the data-type is NUMBER, it will return an integer.


### generateNoisyInteger(unique, qty)

This function generates and returns an array of integers of size `qty` from the range [1, 1000]. If `unique` is true, then the returned array is guaranteed to contain only unique values.


## noisyData_test

This file contains a suite of tests for the `noisyData` file.


## textDatabaseHandler

The text database handler models a simplified database and table system, used to assist random question generation. Its functionality focuses on a table as a set of columns as well as converting text file-stored values into memory.
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=11208034&assignment_repo_type=AssignmentRepo)
# Project-Structure
```
.
├── docs                    # Documentation files (alternatively `doc`)
│   ├── scope-charter       # Scope and Charter
│   ├── design              # Design documents
│   ├── final               # Final documents
│   ├── weekly logs         # Team and Individual Logs
│   ├── marking             # Documents for grading
│   ├── porting             # Documentation for porting code editors
│   ├── communication       # Documentation for communication with client
│   ├── archived            # Documentation from autoER group
│   └── mvp                 # Documentation used for MVP
│
├── databaseCourse          # Course files
├── drone                   # Automated tests (Old)
├── tests                   # Selenium Front-end testing
├── README.md
├── .drone.yml              # Automated tests
└── docker-compose.yml      # Creating docker container

```
Also, update your README.md file with the team and client/project information.  You can find details on writing GitHub Markdown [here](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) as well as a [handy cheatsheet](https://enterprise.github.com/downloads/en/markdown-cheatsheet.pdf).   

Roles:  
Project Manager:    Nishant Srinivasan  
Client Liason:      Matthew Obirek  
Technical Lead:     Skyler Alderson  
Integration Lead:   Andrei Zipis  


# What this Project Includes

This project adds two new elements to PrairieLearn: the RelaX element (`pl-relax_element`) and the SQL element (`pl-sql-element`). Each element adds their appropriate editor into PrairieLearn with additional functionality. These elements also add automatic generation and grading of Relational Algebra and SQL questions.  
To facilitate the generation and grading of questions, two new items were added into `serverFilesCourse`. The first item is Python's native `difflib.py` which allows nuanced grading of student's solutions without execution. The second item is `RASQLib`, a custom library to aid in automatic quesiton generation.  
This project also imports the existing COSC 304 labs into PrairieLearn. These can be found in the `questions` directory.  
Finally, this project includes a seperate Docker container that allows for the execution of Relational Algebra queries using the RelaX API. This is required to safetly obtain the expected output of Relational Algebra queries as well as to grade Relational Algebra queries based on their execution output.  


# Docker

This project requires two Docker containers. The first Docker container runs PrairieLearn and the course instance. The second Docker container hosts a server to run RelaX queries, which is required for grading relational algebra and displaying expected outputs for relational algebra questions.


## Docker Documentation for PrairieLearn

1. Install docker, docker-compose, and docker-desktop(optional)

2. git clone this repository: `https://github.com/UBCO-COSC-499-Summer-2023/project-3-a-automating-database-question-generation-automating-db-q-gen-marking-team-a.git`

3. In your terminal, navigate to cloned directory.

4. In your terminal run `docker-compose up`

5. (Optional) To check if the docker container is running, run `docker-compose ps`. if the response is empty, run `docker-compose ps -a`, and it will show the status of the closed docker container.


## Creating the relaxAPI container

1. Visit repository found at `https://github.com/azipis/RelaXQueryAPI`

2. Follow directions found at that repository.


# Relational Algebra and SQL Assessments and Questions

All questions are represented by a folder within the `databaseCourse/questions` directory. In order to create a new Relational Algebra or SQL question, a new folder must be created within the `question` directory or one of its subdirectories. The question's folder must contain the following files: `info.json` and `question.html`. Optionally the question's folder may have a `clientFilesQuestion` directory which contains resources, such as images, used for the question. For more information, see the [PrairieLearn documentation](https://prairielearn.readthedocs.io).  
Randomly generated questions are handled differently than normal static questions. A random question's `question.html` file is empty aside from a single set of tags: `<pl-relax-element>` for Relational Algebra questions and `<pl-sql-element>` for SQL questions. Unlike a static question which stores texts and creates elements within various HTML tags, randomly generated questions create and load their text when the page is loaded. *To specify the parameters for random question, use variables in the HTML tag.*  
Relational Algebra and SQL have several shared parameters and unique parameters. All parameters have a default value should they not be specified.  


## Shared Question Parameters

`random`, *boolean* (false): Specifies whether the question will be randomly generated or static.  
`maxGrade`, **TODO**  
`markerFeedback`, **TODO**  
`expectedOutput`, *boolean* (false): if true, then the question will display the query's result to the student. *Only applicable for Relational Algebra questions and SQL SELECT questions*. Warning: for complex relational algebra questions, this can lead to a timeout on load; the time taken to execute the query to obtain the feedback may exceed PrairieLearn's timeout limit. This is not an issue for SQL questions due to SQL query execution time.  
`guaranteeOutput`, *boolean* (true): if true, then if the question's query output were to produce zero rows then a new question is generated; this guarantees the query produces at least one row. *Only applicable for Relational Algebra questions and SQL SELECT questions*. Warning: for complex relational algebra questions, this can lead to a timeout on load; the time taken to execute the query to obtain a valid question may exceed PrairieLearn's timeout limit. This is not an issue for SQL questions due to SQL query execution time. **TODO**: make this parameter consistent with what is implemented on the RelaX side.  


## Relational Algebra Question Parameters

**TODO**


## SQL Question Parameters

There are five supported SQL question types: CREATE, INSERT, UPDATE, DELETE, and SELECT. In addition, there are several parameters that can be used for all question types.  


### Shared SQL Question Parameters

`questionType`, *string* (`'query'`): specifies the type of question and can be one of these values: `'create'`, `'insert'`, `'update''`, `'delete'`, or `'query'`.  
`questionDifficulty`, *string* or *None* (`None`): instead of specifing question-type specific parameters, a difficulty can be used. The question difficulties are `'easy'`, `'medium'`, and `'hard'`. Alternatively the difficulty can be `None` whereupon the question instead uses the parameters specified in the HTML tag. *It is suggested to use a difficulty of `None`. Difficulties are deprecated*.  
`conditional`, *integer* (0): the number of conditional clauses in the question's WHERE section. *Only applicable for UPDATE, DELETE, and SELECT questions*.  
`useSubquery`, *boolean* (false): if true, then the question will contain a subquery. *Only applicable for UPDATE, DELETE, and SELECT questions*.  


### CREATE Question Parameters

All parameters for CREATE questions can be used for other SQL questions. If these parameters are used for other question types, then they will specify the metadata for the question's primary table.  

`columns`, *integer* (5): specifies how many columns the table will contain. *The minimum value for this parameter is 3*.  
`joins`, *integer* (0): specifies how many foreign keys this table will contain. *The maximum value for this parameter is equal to the number of columns*.  
`primaryKeys`, *integer* (1): the number of primary keys this table will contain. *This parameter must be less than the number of columns minus the number of foreign keys (a.k.a. joins)*.  
`isNotNull`, *integer* (0): the number of columns with the 'IS NOT NULL' clause. *This parameter must be less than the number of columns minus the number of foreign keys (a.k.a. joins) minus the number of primary keys*.  
`isUnique`, *integer* (0): the number of columns with the 'IS UNIQUE' clause. *This parameter must be less than the number of columns minus the number of foreign keys (a.k.a. joins) minus the number of primary keys*.  
`isOnUpdateCascade`, *integer* (0): the number of foreign keys with the 'ON UPDATE CASCADE' clause. *This parameter cannot be greater than the number of foreign keys (a.k.a. joins)*.  
`isOnDeleteSetNull`, *integer* (0): the number of foreign keys with the 'ON DELETE SET NULL' clause. *This parameter cannot be greater than the number of foreign keys (a.k.a. joins)*.  


### SELECT Questions

These parameters are used exclusively for SELECT type questions.  

`columnsToSelect`, *integer* (0): the number of columns that will appear after SELECT in the query. *If there are zero columns to select, the question will instead select all columns*.  
`orderBy`, *integer* (0): the number of columns that will appear after the ORDER BY in the query. *If this parameter is zero, then the question will not contain an ORDER BY*.  
`groupBy`, *integer* (0): the number of columns that will appear after the GROUP BY in the query. *If this parameter is zero, then the question will not contain a GROUP BY*.  
`having`, *integer* (0): the number of columns that will appear after the HAVING in the query. *This parameter cannot be greater than the `groupBy` parameter. If this parameter is zero, then the question will not contain a HAVING*.  
`limit`, *integer* (0): the number of rows the query is limited to. *If this parameter is zero, then the question will not contain a LIMIT*.  
`isDistinct`, *boolean* (false): specifies whether or not the query must contain distinct values.  
`useQueryFunctions`, *boolean* (false): specifies whether or not query functions can appear after the SELECT in the query. *It is suggested to leave this as false since query functions aggregate the data, resulting in only one row of output. The exception to this is if `groupBy` is greater than one.*


# Linters

This project makes use of two linters, ESLint for JavaScript and pylint for Python.  


## ESLint

ESLint requires Node.js to be installed locally. To download Node.js, visit `https://nodejs.org/en`. Navigate to the project folder and run the command `npm install eslint`. ESLint can then be run either through the console (visit `https://eslint.org/docs/latest/` for more information) or the recommended route of installing it through Visual Studio Code's extensions. The linter automatically runs when used through Visual Studio Code.  
To adjust ESLinter's configuration, use the `.eslintrc.json` file and adjust the `"rules"` block. Visit `https://eslint.org/docs/latest/rules/` for a complete list of rules.  


## pylint

pylint must be installed in the project folder. Navigate to the project folder and run the command `pip install pylint`. pylint can be run through either the console (visits `https://docs.pylint.org/index.html` for more information) or the recommended route of installing it through Visual Studio Code's extensions.  The linter automatically runs when used through Visual Studio Code.  
To adjust pylint's configuration, use the `.pylintrc` file. Visit `https://docs.pylint.org/index.html` for more information about pylint configuration.

# RelaXElementSharedLibrary

Last Updated August 8, 2023

## __init__

Python libraries require an `__init__.py` file to be recognized as a library. The file is blank since it is only required to be present such that this folder is recognized as a library.


## Text Files



## RelaXAutogenerator

The autogenerator is responsible for creating random questions and initializing the front-end and back-end databases accordingly.

Parameters:

- `projectedColumns` : Specifies the number of desired Projected Columns - random if not specified
- `numClauses` : Specifies the number of desired selection clauses
- `orderBy` : Specifies if an order by clauses is wanted
- `groupBy` : Specifies if a groupby clauses is wanted instead of a projection clause
- `numJoins` : Specifies number of natural Joins wanted
- `antiJoin` : Specifies if antiJoin is desired [1 join only]
- `semiJoin` : Specifies if semiJoin is desired [1 join only]
- `outerJoin` : Specifies if outerJoin is desired [1 join only]

Note on joins: due to the time cost to guarantee outputs, we have limited anti/semi/outer joins to only 1 join per query. We can guarantee output in the generation process, thus saving that time cost. The risk of a zero row output still exists, but is very low.

Functions:
- `autogenerate(data, outputGuaranteed=True)` : This function is the only function called in the `pl-relax-element.py`. It first generates the database, and then generates the question text and the corresponding answer querry. storing them in there respective data variables
  - Database: `data['params']['db_initialize_create']`
  - CorrectAnswer: `data['correct_answers']['RelaXEditor']`
  - QuestionText: `data['params']['questionText']` 
The `outputGuaranteed` parameter is used to trigger whether or not the question and database will be re-generated upon an zero row output.   
  
  - `createPreview(data)`: queries relaxAPI and returns the expected output of the question
  
  Join Functions:
  - `outerJoinGeneration(self, graph, dataset)`: Generates outerJoin data
  - `semiJoinGeneration(self, graph, dataset)`: Generates semiJoin data
  - `antiJoinGeneration(self, graph, dataset)`: Generates antiJoin data
  - `naturalJoinGeneration(self, graph)`: Generates naturalJoin data
  
  Getters:
  - `getQuery(self)`: returns the Relational Algebra query string 
  - `getText(self)`: returns question Text
  - `loadQuestion(self, data)`: loads query and text into data variable

  Operators:
  - `Projection(self, neededColumns, usableColumns, rangeNum)`: Returns projected Columns
  - `groupBy(randColumn, graph, dataset)`: returns single statement for groupby
  - `selection(usableColumns, randColumn, graph, dataset)`: returns single statement for groupby

  Misc Functions:
  - `returnGreater(num1, num2)`: Returns the greater of two numbers
  - `formatDate(capturedText)`: formats date to `yyyy-mm-dd`
  - `dfs(graph, startNode, visited=set(), n=1)`: Performs a Depth first search to retreave a connected graph
  - `randomSubgraph(graph, n)`: Returns a random subgraph of a desired size. Used to retrieve natural joins.
 
## RelaXCustomGrader

Weights:

- `outputScoreWeight`: The percent of marks given based on output matching.
  - `orderWeight`: Percent of marks given for having rows in the correct order.
  - `rowWeight`: Percent of marks given for having correct number of rows.
  - `colWeight`: Percent of marks given for having correct number and match of columns.
  - `valueMatchWeight`: Percent of marks given for having correct match of values.
- `inputScoreWeight`: The percent of marks given based on string matching the submitted query string vs. the correct query string.
  - `threshold`: When input string matching, this is the minimum percent of similarity required between strings to receive 100%.

Extra Note on the input string matching:
The custom grader compares the student's supplied answer against a pre-defined correct solution. It compares the similarity and grants a grade proportionally. If the student gets above some threshold, whose default value is 0.75 or 75%, they are given full marks on the question. Similarities below 0.75 are mapped as such: (0, 0.75) -> (0, 1).

Functions:  
- `customGrader(data)`: Called by element.py to grade a submission. Sets feedback based on flag. Calls `gradeQuery(data, feedback)`; if output score is 100%, gives 100% overall. If query is unable to execute, grading is done through input string matching and given a penalty of 15%. Returns score based on weights.
- `gradeQuery(data, feedback)`: Packages database, submitted answer, and correct answer into json and sends a GET request to the relaxAPI container. If json is received in response, it runs `rowMatch()`, `colMatch()`, `valueMatch()` and returns an outputScore based on weights.
  - `rowMatch(rowsSA, rowsCA)`: Returns an unweighted score for number of correct rows.
  - `rowMatch(colsSA, colsCA)`: Returns an unweighted score for correctly matching columns.
  - `valueMatch(valueSA, valueCA)`: Returns an unweighted score for correctly matching values in rows.
- `addFeedback(data, category, submitted, correct)`: Adds feedback to the data parameter to be dispalyed.
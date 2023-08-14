# RelaXElementSharedLibrary

Last Updated August 8, 2023

## __init__

Python libraries require an `__init__.py` file to be recognized as a library. The file is blank since it is only required to be present such that this folder is recognized as a library.


## Text Files



## RelaXAutogenerator

The autogenerator is responsible for creating random questions and initializing the front-end and back-end databases accordingly.

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
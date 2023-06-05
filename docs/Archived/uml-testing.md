# UML Python Testing

- The Python files that test the custom UML element can be found in `elements/pl-uml-element`.
- The two files that are being tested are `randomgeneration.py` and `randomgrader.py`.
    - Both of these files have a test file for unit tests and a test file for integration tests, totaling 4 test files.

---

## Test Structure

- Each Python module has two associated test files: a unit_test file, and an integration_test file.
- The testing is done with the use of the `unittest` library and `pytest` framework

---

## Running the tests

- In order to run the test suite for this element locally, you must make sure you natively install some libraries using `pip`:
    - `pip install pytest` - Allows you to run the tests.
    - `pip install gibberish` - Necessary to run the `randomgeneration.py` module.
- Then, change your directory to the directory where the python test files are located: [here](./../elements/pl-uml-element). (`elements/pl-uml-element`)
- When inside of the testing directory, run this command to run all 4 test files related to the element:
    - `python3 -m pytest`
- For more information about testing, which includes running tests in Javascript and other Python tests that are not a part of this element, please refer to the [local installation](./installingLocal.md#running-the-test-suite) file.

---

## Test coverage

### randomgrader.py
- This module has 87% total line coverage out of 679 lines of code.
    - The `*_unit_test.py` file consists of 28 tests; one for each function found in the `randomgrader.py` file.
    - The `*_integration_test.py` file consists of 5 tests. These tests combine different functions in each test in order to more accurately simulate a complete run through the program. A couple of examples include: answering a question correctly, answering a question with changed grading parameters, and answering a question where the grading parameters entered were invalid.

### randomgeneration.py
- This module has 94% total line coverage out of 496 lines of code.
    - The `*_unit_test.py` file consists of 15 tests for all functions in the `randomgeneration.py` file.
    - The `*_integration_test.py` file consists of 18 tests. These tests combine different functions in each test in order to more accurately simulate a complete run through the program. This test focuses on the 3 main units:
        - **data structure**: The returned data containing 4 elements: `question`, `answer`, `maximum_attempts`, `penalty_type`.
        - **data values**: The returned 4 elements having valid values that are not empty.
        - **data detail**: The returned elements containing consistent data, such as: the same number of strong/weak entities, the same number of relationships, and relationships with matching values.

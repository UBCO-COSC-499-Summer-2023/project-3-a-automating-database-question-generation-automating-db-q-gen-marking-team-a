import RASQLCustomGrader as grader
import SQLQueryQuestionData as qd


def imports(data):
    import RASQLCustomGrader as grader
    import SQLQueryQuestionData as qd
    
def generate(data):
    # Specifies editor type so we know the grading scheme
    data["params"]["grader"] = "SQLEditor"

    # Sets the files to be read to initialise the database and solutions
    data["params"]["databaseSchemaFile"] = "../lab3_db.txt"
    data["params"]["databaseAnswerFile"] = "../lab3_ans.txt"

    # Adds the database data to data
    qd.generateQuestionData(data, 8)
    
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    grader.customGrader(data)
    pass
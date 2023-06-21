<<<<<<< HEAD
import SQLCustomGrader as grader

textfile = open("../lab3_db.txt","r")
textfile1 = open("../lab3_ans.txt","r")
lines = textfile.read().splitlines()
lines1 = textfile1.read().splitlines()
textfile.close()
textfile1.close()
=======
import RASQLCustomGrader as grader
>>>>>>> sql/ddl-question-setup

def imports(data):
    import RASQLCustomGrader as grader
    
def generate(data):
<<<<<<< HEAD
    data["params"]["ddl"] = lines
    data["params"]["grader"] = "SQLEditor"
    data["correct_answers"]["SQLEditor"] = lines1[4]
    pass
=======
    data['params']['grader'] = 'SQLEditor'
>>>>>>> sql/ddl-question-setup
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
<<<<<<< HEAD
    grader.customGrader(data)
    pass
    
=======
    # Runs the custom grader
    grader.customGrader(data)
>>>>>>> sql/ddl-question-setup

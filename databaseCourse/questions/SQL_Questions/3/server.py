import RASQLCustomGrader as grader

textfile = open("../lab3_db.txt","r")
textfile1 = open("../lab3_ans.txt","r")
lines = textfile.read().splitlines()
lines1 = textfile1.read().splitlines()
textfile.close()
textfile1.close()

def imports(data):
    import RASQLCustomGrader as grader
    
def generate(data):
    data["params"]['db_initialize'] = lines
    data["params"]["grader"] = "SQLEditor"
    data["correct_answers"]["SQLEditor"] = lines1[2]
    pass
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    grader.customGrader(data)
    pass
    

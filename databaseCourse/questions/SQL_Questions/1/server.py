textfile = open("../lab3_db.txt","r")
lines = textfile.read().splitlines()
textfile.close()

def imports(data):
    pass
    
def generate(data):
    data["params"]["ddl"] = lines
    #data["correct_answers"]["SQLEditor"]
    pass
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass
    

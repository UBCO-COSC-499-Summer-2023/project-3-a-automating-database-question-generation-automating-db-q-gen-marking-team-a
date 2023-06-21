import RASQLCustomGrader as grader


def imports(data):
    pass
    
def generate(data):
    data['params']['grader'] = 'RelaXEditor'
    data["correct_answers"]["RelaXEditor"] = "hello"


#   End generate()

    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    grader.customGrader(data)
    pass
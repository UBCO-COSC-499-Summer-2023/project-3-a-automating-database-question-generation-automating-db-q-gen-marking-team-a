import RASQLCustomGrader as grader

def imports(data):
    pass
    #import RASQLCustomGrader as grader
    
def generate(data):
    data['params']['grader'] = 'SQLEditor'
    data['correct_answers']['SQLEditor'] = """CREATE TABLE airplane (
        id CHAR(10),
        model CHAR(20),
        manufacture_date DATE
        );"""

    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    # Runs the custom grader
    grader.customGrader(data)
import RASQLCustomGrader as grader

def imports(data):
    import RASQLCustomGrader as grader
    
def generate(data):
    data['params']['grader'] = 'SQLEditor'
    data['correct_answers']['SQLEditor'] = """CREATE TABLE airplane (
        id VARCHAR(10),
        model VARCHAR(20),
        manufacture_date DATE,
        PRIMARY KEY (id)
        );"""

    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    # Runs the custom grader
    grader.customGrader(data)
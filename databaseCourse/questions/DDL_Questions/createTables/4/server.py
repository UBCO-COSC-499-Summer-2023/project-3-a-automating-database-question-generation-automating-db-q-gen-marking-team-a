import RASQLCustomGrader as grader

def imports(data):
    import RASQLCustomGrader as grader
    
def generate(data):
    data['params']['grader'] = 'SQLEditor'
    data['correct_answers']['SQLEditor'] = """CREATE TABLE passenger(
        id INTEGER,
        first_name VARCHAR(30),
        last_name VARCHAR(30),
        birthdate DATE,
        street CHAR(50),
        city CHAR(40),
        province CHAR(20),
        country CHAR(20),
        PRIMARY KEY (id)
    );"""
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    # Runs the custom grader
    grader.customGrader(data)

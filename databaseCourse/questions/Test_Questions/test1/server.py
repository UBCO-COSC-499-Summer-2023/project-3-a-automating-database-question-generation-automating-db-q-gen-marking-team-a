import random

def imports(data):
    import random
    
def generate(data):
    #   Generates a random int
    #   Used for a parameter
    testAnswer = random.randint(3,10)

    #   Sets the parameter
    #   This will show up in the question with the help of Mustache
    data["params"]["testParam"] = testAnswer

    #   Sets the correct answer
    #   This is what the internal grader uses to grade
    data["correct_answers"]["testCorrect"] = testAnswer
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass
    

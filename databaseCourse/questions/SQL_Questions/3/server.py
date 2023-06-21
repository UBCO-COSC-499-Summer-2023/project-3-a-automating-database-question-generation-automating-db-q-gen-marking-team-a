import SQLCustomGrader as grader

textfile = open("../lab3_db.txt","r")
textfile1 = open("../lab3_ans.txt","r")
lines = textfile.read().splitlines()
lines1 = textfile1.read().splitlines()
textfile.close()
textfile1.close()

def imports(data):
    import RASQLCustomGrader as grader
    
def generate(data):
    data["params"]["ddl"] = lines
    data["params"]["grader"] = "SQLEditor"
    data["correct_answers"]["SQLEditor"] = """SELECT pname AS product_name, price, inventory, (price * inventory) AS inventoryValue FROM product WHERE price > 20 ORDER BY pname ASC;"""
    pass
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    grader.customGrader(data)
    pass
    

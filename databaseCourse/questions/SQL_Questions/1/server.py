textfile = open("../lab3_db.txt","r")
textfile1 = open("../lab3_ans.txt","r")
lines = textfile.read().splitlines()
lines1 = textfile1.read().splitlines()
textfile.close()
textfile1.close()

def imports(data):
    pass
    
def generate(data):
    data["params"]["ddl"] = lines
    print(lines1[0])
    data["params"]["grader"] = "SQLEditor"
    data["correct_answers"]["SQLEditor"] = """SELECT pname AS product_name, price, inventory, (price * inventory) AS inventoryValue FROM product WHERE price > 20 ORDER BY pname ASC;"""
    pass
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass
    

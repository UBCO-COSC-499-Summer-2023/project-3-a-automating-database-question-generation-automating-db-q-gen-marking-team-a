def imports(data):
    pass
    
def generate(data):
    
    #   Holds each table of the database as a string of an array
    data["params"]["initDatabase"] = [
        "Customer = {\
            cid:number, 	cname:string, 		address:string, 		city:string, 		state:string\
            1, 		'Fred Smith', 		'101 Evergreen Terrace', 	'Springfield', 		'IL'\
            2, 		'Joe Smithsonian', 	'245 Straight Street', 		'Iowa City', 		'IA'\
            3, 		'Steve Stevenson', 	'24 Michigan Ave.', 		'Chicago', 		'IL'\
            4, 		'Russell Johnson', 	'1 Hollywood Drive', 		'Hollywood', 		'CA'\
            5, 		'John Doe', 		'34 Dead End Lane', 		'Detroit', 		'MI'\
            6, 		'Scott Charles', 	'748 Mayflower', 		'Huntington Beach', 	'CA'\
            7, 		'Robert Dean', 		'234 Greenwood Drive', 		'Morristown', 		'NJ'\
            8, 		'Shannon Rose', 	'Rural Route', 			'Wyandotte', 		'MI'\
            9, 		'Beth Rosebud', 	'1 First Street', 		'Muscatine', 		'IA'\
            10, 		'Suzanne May', 		'2 Second Street', 		'Iowa City', 		'IA'\
        }",

        "Product = {\
            pid:number, 	pname:string, 			price:number, 	inventory:number\
            1, 		'Swiss Chocolate', 		32.99, 		10\
            2, 		'Wooden Chair', 		52, 		8\
            3, 		'Teddy Bear', 			5.99, 		22\
            4, 		'Chocolate Bar', 		3.95, 		12\
            5, 		'Desk', 			122.99, 	100\
            6, 		'Table', 			71, 		44\
            7, 		'Deluxe Sweet Collection', 	41.55, 		83\
        }",

        "Shipment = {\
            sid:number, 	cid:number, 	shipdate:date\
            3, 		2, 		2013-03-05\
            4, 		3, 		2014-05-13\
            5, 		4, 		2014-05-17\
            6, 		4, 		2014-02-02\
            7, 		4, 		2015-09-04\
            8, 		4, 		2015-05-19\
            9, 		2, 		2015-03-07\
            10,		2, 		2011-03-09\
            11,		6, 		2015-04-04\
            12,		7, 		2015-05-05\
            13, 		6, 		2014-02-24\
            14, 		6, 		2013-12-22\
        }",

        "ShippedProduct = {\
            sid:number, 	pid:number, 	amount:number\
            3, 		1, 		20\
            4, 		1, 		5\
            5, 		2, 		13\
            6, 		1, 		4\
            6, 		2, 		1\
            7, 		1, 		3\
            8, 		4, 		25\
            9, 		2, 		32\
            10, 		2, 		2\
            11, 		2, 		5\
            12, 		3, 		1\
            12, 		4, 		10\
        }"
]

#   End generate()

    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass
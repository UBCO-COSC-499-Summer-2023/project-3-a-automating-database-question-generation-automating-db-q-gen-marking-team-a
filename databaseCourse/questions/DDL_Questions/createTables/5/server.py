import RASQLCustomGrader as grader

def imports(data):
    import RASQLCustomGrader as grader
    
def generate(data):
    data['params']['grader'] = 'SQLEditor'
    data['params']['db_initialize'] = """
    CREATE TABLE airplane (id VARCHAR(10),model VARCHAR(20),manufacture_date DATE,PRIMARY KEY (id));
    CREATE TABLE airport ( id CHAR(5), name VARCHAR(30), city VARCHAR(40), province VARCHAR(20), country VARCHAR(20), PRIMARY KEY (id) );
    CREATE TABLE flight(number CHAR(5),departure_date DATETIME, departAirport VARCHAR(30), arriveAirport VARCHAR(30), arrival_date DATETIME, actual_departure_date DATETIME, actual_arrival_date DATETIME,
        airplane_id VARCHAR(10), PRIMARY KEY (number, departure_date), FOREIGN KEY (departAirport) REFERENCES airport(name)ON DELETE SET NULL ON UPDATE CASCADE, FOREIGN KEY (arriveAirport) REFERENCES airport(name)
        ON DELETE SET NULL ON UPDATE CASCADE, FOREIGN KEY (airplane_id) REFERENCES airplane (id) ON DELETE SET NULL ON UPDATE CASCADE);
    CREATE TABLE passenger(id INTEGER, first_name VARCHAR(30), last_name VARCHAR(30), birthdate DATE, street CHAR(50), city CHAR(40), province CHAR(20), country CHAR(20), PRIMARY KEY (id));
    """
    data['correct_answers']['SQLEditor'] = """CREATE TABLE onFlight(
        passenger_id INTEGER,
        flight_number CHAR(5),
        flight_departure DATETIME,
        seat_number CHAR(4),
        FOREIGN KEY (passenger_id) REFERENCES passenger (id)
            ON DELETE NO ACTION ON UPDATE CASCADE,
        FOREIGN KEY (flight_number) REFERENCES flight(number)
            ON DELETE NO ACTION ON UPDATE CASCADE,
        FOREIGN KEY (flight_departure) REFERENCES flight (departure_date)
            ON DELETE NO ACTION ON UPDATE CASCADE
        );"""
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    # Runs the custom grader
    grader.customGrader(data)
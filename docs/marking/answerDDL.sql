DROP TABLE IF EXISTS Airplane;
DROP TABLE IF EXISTS Airport;
DROP TABLE IF EXISTS Flight;
DROP TABLE IF EXISTS OnFlight;
DROP TABLE IF EXISTS Passenger;

CREATE TABLE Airplane (
	id VARCHAR(10), 	
	model VARCHAR(20),
	manufactureDate DATE,
	PRIMARY KEY (id)
);

CREATE TABLE Airport (
	id CHAR(5), 	
	name VARCHAR(30),
	city VARCHAR(40),
	province VARCHAR(20),
	country VARCHAR(20),
	PRIMARY KEY (id)
);

CREATE TABLE Flight (
	num CHAR(5), 	
	departAirport CHAR(5),
	arriveAirport CHAR(5),
	airplaneId VARCHAR(10),
	departDateTime DATETIME,
	arriveDateTime DATETIME,			
	actualDepartDT DATETIME,
	actualArriveDT DATETIME,	
	PRIMARY KEY (num,departDateTime),
	FOREIGN KEY (departAirport) REFERENCES Airport(id) ON DELETE SET NULL ON UPDATE CASCADE,
	FOREIGN KEY (arriveAirport) REFERENCES Airport(id) ON DELETE SET NULL ON UPDATE CASCADE,
	FOREIGN KEY (airplaneId) REFERENCES Airplane(id) ON DELETE SET NULL ON UPDATE CASCADE
);


CREATE TABLE Passenger (
	id int, 	
	firstname VARCHAR(30),
	lastname VARCHAR(30),
	birthdate DATE,
	street VARCHAR(50),
	city VARCHAR(40),
	province VARCHAR(20),
	country VARCHAR(20),
	PRIMARY KEY (id)
);

CREATE TABLE OnFlight (
	passengerId int,
	flightNum CHAR(5),
	departDateTime DATETIME,
	seatNum CHAR(4)	NOT NULL,
	PRIMARY KEY (passengerId, flightNum, departDateTime),
	FOREIGN KEY (passengerId) REFERENCES Passenger(id) ON DELETE NO ACTION ON UPDATE CASCADE,
	FOREIGN KEY (flightNum, departDateTime) REFERENCES Flight(num,departDateTime) ON DELETE NO ACTION ON UPDATE CASCADE
);

INSERT INTO Airplane VALUES ('AC911','Boeing 747', '2001-01-25');
INSERT INTO Airplane VALUES ('WJ455', 'Airbus A380', '2008-11-15');

INSERT INTO Airport VALUES ('YLW', 'Kelowna Airport', 'Kelowna','British Columbia', 'Canada');
INSERT INTO Airport VALUES ('YWG', 'Winnipeg Airport', 'Winnipeg','Manitoba', 'Canada');

INSERT INTO Flight VALUES ('AC35', 'YLW', 'YWG', 'AC911', '2009-03-14 07:00:00', '2009-03-14 15:00:00', '2009-03-14 07:05:00', '2009-03-14 15:30:00');
INSERT INTO Flight VALUES ('WJ111', 'YWG', 'YLW', 'WJ455', '2009-03-15 10:00:00', '2009-03-15 12:00:00', '2009-03-15 09:55:00', '2009-03-14 11:49:55');

INSERT INTO Passenger VALUES (1, 'Joe', 'Smith', '1970-12-15', '1350 Springfield Road', 'Kelowna', 'British Columbia', 'Canada');
INSERT INTO Passenger VALUES (2, 'Fred', 'Brothers', '1950-01-02', '22 Pembina Highway', 'Winnipeg', 'Manitoba', 'Canada');

INSERT INTO OnFlight VALUES (1, 'AC35', '2009-03-14 07:00:00', '1A');
INSERT INTO OnFlight VALUES (1, 'WJ111', '2009-03-15 10:00:00', '10C');
INSERT INTO OnFlight VALUES (2, 'AC35', '2009-03-14 07:00:00', '2A');
INSERT INTO OnFlight VALUES (2, 'WJ111', '2009-03-15 10:00:00', '10D');

-- Update Command
UPDATE Flight SET actualDepartDT = DATE_ADD(actualDepartDT, INTERVAL 1 HOUR) WHERE departAirport = 'YLW'; 

-- with a subquery
UPDATE Flight SET actualDepartDT = DATE_ADD(actualDepartDT, INTERVAL 1 HOUR) WHERE departAirport = (SELECT id from Airport WHERE city = 'Kelowna');


-- Delete Command
-- No subqueries
DELETE FROM OnFlight WHERE passengerId = 2;

-- With a subquery
DELETE FROM OnFlight WHERE passengerId = (SELECT id FROM Passenger WHERE firstname = 'Fred' and lastname = 'Brothers');



/* Create the tables */

CREATE TABLE buses (
  reg_no VARCHAR(15) NOT NULL PRIMARY KEY,
  no_of_seats INT NOT NULL
);

CREATE TABLE passengers (
  passenger_id INT NOT NULL PRIMARY KEY,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email_address VARCHAR(100) NOT NULL,
);

CREATE TABLE tours (
  tour_id INT NOT NULL PRIMARY KEY,
  origin VARCHAR(50) NOT NULL,
  destination VARCHAR(50) NOT NULL
);

CREATE TABLE timetables (
  timetable_id INT NOT NULL PRIMARY KEY,
  tour_id INT NOT NULL,
  reg_no VARCHAR(15) NOT NULL,
  no_of_remaining_seats INT NOT NULL,
  departure_time DATETIME NOT NULL,
  arrival_time DATETIME NOT NULL,
  FOREIGN KEY (reg_no) REFERENCES buses(reg_no),
  FOREIGN KEY (tour_id) REFERENCES tours(tour_id)
);

CREATE TABLE bookings (
  booking_id INT NOT NULL PRIMARY KEY,
  passenger_id INT NOT NULL,
  seat_number INT NOT NULL,
  booking_date DATETIME NOT NULL,
  timetable_id INT NOT NULL,
  tour_id INT NOT NULL,
  FOREIGN KEY (passenger_id) REFERENCES passengers(passenger_id),
  FOREIGN KEY (timetable_id) REFERENCES timetables(timetable_id),
  FOREIGN KEY (tour_id) REFERENCES tours(tour_id)
);

/* Populate the tables */

INSERT INTO buses (reg_no, no_of_seats) VALUES 
('191-TS-80569', 25),
('202-D-126885', 50),
('231-G-23575', 55);

INSERT INTO passengers (passenger_id, first_name, last_name, email_address) VALUES 
(1, 'Jon', 'Snow', 'jon.snow@gmail.com'),
(2, 'Cassandra', 'Bowden', 'cas.bowden@hotmail.com'),
(3, 'Jackson', 'Avery', 'jackson.avery@yahoo.com');

INSERT INTO tours (tour_id, origin, destination) VALUES 
(1, 'Dublin', 'Belfast'),
(2, 'Limerick', 'Galway'),
(3, 'Belfast', 'Antrim');

INSERT INTO timetables (timetable_id, tour_id, reg_no, no_of_remaining_seats, departure_time, arrival_time) VALUES 
(1, 1, '191-TS-80569', 24, '12:00:00', '18:00:00'),
(2, 2, '202-D-126885', 49, '11:00:00', '16:00:00'),
(3, 3, '231-G-23575', 54, '13:00:00', '15:30:00');


INSERT INTO bookings (booking_id, passenger_id, seat_number, booking_date, timetable_id, tour_id) VALUES 
(1, 1, 1, '2023-02-28', 1, 1),
(2, 2, 1, '2023-04-30', 2, 2),
(3, 3, 1, '2023-03-24', 3, 3);

/* To be ran after the apps are created and identity status in app is set to on */
/* App Service - prod slot */
CREATE USER AislingsBusTours FROM EXTERNAL PROVIDER; 
ALTER ROLE db_datareader ADD MEMBER AislingsBusTours;
GRANT SELECT TO AislingsBusTours; 
/* App Service - staging slot */
CREATE USER [aislingsbustours/slots/testing] FROM EXTERNAL PROVIDER;
ALTER ROLE db_datareader ADD MEMBER [aislingsbustours/slots/testing];


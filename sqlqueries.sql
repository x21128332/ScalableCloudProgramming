/* Create the tables */

CREATE TABLE buses (
  reg_no VARCHAR(15) NOT NULL PRIMARY KEY,
  no_of_seats INT NOT NULL
);

CREATE TABLE passengers (
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email_address VARCHAR(100) NOT NULL PRIMARY KEY,
);

CREATE TABLE tours (
  tour_id INT NOT NULL PRIMARY KEY,
  tour_date DATE NOT NULL,
  origin VARCHAR(50) NOT NULL,
  destination VARCHAR(50) NOT NULL
);

CREATE TABLE timetables (
  timetable_id INT NOT NULL PRIMARY KEY,
  tour_id INT NOT NULL,
  reg_no VARCHAR(15) NOT NULL,
  departure_time TIME NOT NULL,
  arrival_time TIME NOT NULL,
  FOREIGN KEY (reg_no) REFERENCES buses(reg_no),
  FOREIGN KEY (tour_id) REFERENCES tours(tour_id)
);

CREATE TABLE bookings (
  booking_id INT NOT NULL PRIMARY KEY IDENTITY(1,1),
  email_address VARCHAR(100) NOT NULL,
  booking_date DATETIME NOT NULL,
  tour_id INT NOT NULL,
  FOREIGN KEY (email_address) REFERENCES passengers(email_address),
  FOREIGN KEY (tour_id) REFERENCES tours(tour_id)
);

/* Populate the tables */

INSERT INTO buses (reg_no, no_of_seats) VALUES 
('191-TS-80569', 25),
('202-D-126885', 50),
('231-G-23575', 55);

INSERT INTO passengers (first_name, last_name, email_address) VALUES 
('Jon', 'Snow', 'jon.snow@gmail.com'),
('Cassandra', 'Bowden', 'cas.bowden@hotmail.com'),
('Jackson', 'Avery', 'jackson.avery@yahoo.com');

INSERT INTO tours (tour_id, tour_date, origin, destination) VALUES 
(1, '2023-04-14', 'Dublin', 'Belfast'),
(2, '2023-04-20', 'Limerick', 'Galway'),
(3, '2023-04-26', 'Belfast', 'Antrim');

INSERT INTO timetables (timetable_id, tour_id, reg_no, departure_time, arrival_time) VALUES 
(1, 1, '191-TS-80569', '12:00:00', '18:00:00'),
(2, 2, '202-D-126885', '11:00:00', '16:00:00'),
(3, 3, '231-G-23575', '13:00:00', '15:30:00');


/* To be ran after the apps are created and identity status in app is set to on */
/* App Service - prod slot */
CREATE USER AislingsBusTours FROM EXTERNAL PROVIDER; 
ALTER ROLE db_datareader ADD MEMBER AislingsBusTours;
GRANT SELECT TO AislingsBusTours;
GRANT EXECUTE TO AislingsBusTours;
/* App Service - staging slot */
CREATE USER [aislingsbustours/slots/testing] FROM EXTERNAL PROVIDER;
ALTER ROLE db_datareader ADD MEMBER [aislingsbustours/slots/testing];
GRANT EXECUTE TO [aislingsbustours/slots/testing];
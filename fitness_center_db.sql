CREATE DATABASE fitness_center_db;

CREATE TABLE Members (
	id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT
);

CREATE TABLE WorkoutSessions (
	session_id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT,
    session_date DATE,
    duration_minutes INT,
    calories_burned INT,
    FOREIGN KEY (member_id) REFERENCES Members (id)
);

SELECT * FROM Members;
SELECT * FROM WorkoutSessions;

INSERT INTO Members (name, age)
VALUES ('Jeff Stevenson', 30),
('Carla Moore', 22),
('Bob Roberts', 57),
('Jane Doe', 33);

INSERT INTO WorkoutSessions (member_id, session_date, duration_minutes, calories_burned)
VALUES (1, '2024-08-15', '40', '250'),
(2, '2024-08-17', '60', '350'),
(3, '2024-08-13', '40', '250'),
(3, '2023-08-15', '60', '300'),
(4, '2024-08-14', '50', '300'),
(4, '2024-08-16', '30', '200');
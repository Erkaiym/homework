-- #1

CREATE DATABASE health 
CHARACTER SET utf8
COLLATE utf8_general_ci;

USE health;

CREATE TABLE doctor
(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(255) NOT NULL,
surname VARCHAR(255) NOT NULL);


INSERT INTO doctor (id, name, surname)
VALUES 
(NULL, 'Noah', 'Wyle'), 
(NULL, 'Laura', 'Innes'), 
(NULL, 'Maura', 'Tierney'),
(NULL, 'Goran', 'Visnjic'),
(NULL, 'Yvette', 'Freeman'),
(NULL, 'Anthony', 'Edwards'),
(NULL, 'Eriq', 'La Salle'),
(NUll, 'Emily', 'Pickman'),
(NULL, 'Alex', 'Kingston'),
(NULL, 'Lynn', 'Henderson'),
(NULL, 'Sherry', 'Stringfield'),
(NULL, 'Abraham', 'Benrubi'),
(NULL, 'Gregory', 'Partt');


CREATE TABLE patient
(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(255) NOT NULL,
surname VARCHAR(255) NOT NULL);


INSERT INTO patient (id, name, surname)
VALUES
(NULL, 'Troy', 'Evans'),
(NULL, 'Lily', 'Mariye'),
(NULL, 'Paul', 'McCrane'), 
(NULL, 'Montae', 'Russel'),
(NULL, 'Ellen', 'Crawford'),
(NULL, 'Conni', 'Brazelton'),
(NULL, 'Scott', 'Grimes'),
(NULL, 'Gloria', 'Reuben'),
(NULL, 'Brian', 'Lester'),
(NULL, 'John', 'Aylward'),
(NULL, 'Dinah', 'Lenney'),
(NULL, 'Kristin', 'Minter'),
(NULL, 'Shane', 'West');

CREATE TABLE doctor_patient
(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
id_doc INT NOT NULL,
id_pat INT NOT NULL,
FOREIGN KEY (id_doc)
REFERENCES doctor(id)
ON DELETE NO ACTION
ON UPDATE NO ACTION,
FOREIGN KEY (id_pat)
REFERENCES patient(id)
ON DELETE NO ACTION
ON UPDATE NO ACTION);

INSERT INTO doctor_patient (id, id_doc, id_pat)
VALUES 
(NULL, 2, 1),
(NULL, 2, 2),
(NULL, 1, 1),
(NULL, 3, 1),
(NULL, 3, 5),
(NULL, 4, 5),
(NULL, 4, 6),
(NULL, 5, 7),
(NULL, 5, 4),
(NULL, 6, 6),
(NULL, 7, 3),
(NULL, 7, 10),
(NULL, 8, 4),
(NULL, 8, 13),
(NULL, 8, 9),
(NULL, 10, 8),
(NULL, 10, 11),
(NULL, 11, 12),
(NULL, 12, 11),
(NULL, 13, 1),
(NULL, 13, 4);

-- #2

one to many:
TABLE employees and TABLE titles,
TABLE employees and TABLE salaries.

many to many:
TABLE employees and TABLE departments (via TABLE dept_manager),
TABLE employees and TABLE departments (via TABLE dept_emp).

-- #3

CREATE DATABASE courses 
CHARACTER SET utf8
COLLATE utf8_general_ci;

USE courses;

CREATE TABLE students
(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(255) NOT NULL,
surname VARCHAR(255) NOT NULL),
gender ENUM('M', 'F') not null);


INSERT INTO students (id, name, surname, gender)
VALUES 
(NULL, 'Noah', 'Wyle', 'M'), 
(NULL, 'Laura', 'Innes', 'F'), 
(NULL, 'Maura', 'Tierney', 'F'),
(NULL, 'Goran', 'Visnjic', 'M'),
(NULL, 'Yvette', 'Freeman', 'F'),
(NULL, 'Anthony', 'Edwards', 'M'),
(NULL, 'Eriq', 'La Salle', 'M'),
(NUll, 'Emily', 'Pickman', 'F'),
(NULL, 'Alex', 'Kingston', 'F'),
(NULL, 'Lynn', 'Henderson', 'F'),
(NULL, 'Sherry', 'Stringfield', 'F'),
(NULL, 'Abraham', 'Benrubi', 'M'),
(NULL, 'Gregory', 'Partt', 'M');


CREATE TABLE course
(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
title VARCHAR(255) NOT NULL);

INSERT INTO course (id, title)
VALUES 
(NULL, 'уроки вождения'),
(NULL, 'программирование'),
(NULL, 'уроки русского языка'),
(NULL, 'бух. учет'),
(NULL, 'плавание'),
(NULL, 'игра на скрипке'),
(NULL, 'уроки китайского языка'),
(NULL, 'финансовый менеджмент'),
(NULL, 'живопись'),
(NULL, 'медецинская помощь');

CREATE TABLE student_course
(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
id_student INT NOT NULL,
id_course INT NOT NULL,
FOREIGN KEY (id_student)
REFERENCES students(id)
ON DELETE NO ACTION
ON UPDATE NO ACTION,
FOREIGN KEY (id_course)
REFERENCES course(id)
ON DELETE NO ACTION
ON UPDATE NO ACTION);

INSERT INTO student_course (id, id_student, id_course)
VALUES 
(NULL, 1, 9),
(NULL, 1, 7),
(NULL, 2, 6),
(NULL, 3, 1),
(NULL, 4, 10),
(NULL, 5, 1),
(NULL, 5, 1),
(NULL, 6, 2),
(NULL, 6, 1),
(NULL, 7, 3),
(NULL, 8, 2),
(NULL, 9, 5),
(NULL, 9, 4),
(NULL, 10, 9),
(NULL, 11, 5),
(NULL, 12, 1),
(NULL, 12, 6),
(NULL, 12, 7),
(NULL, 13, 8);


SELECT title, name, surname FROM student_course
JOIN students
ON students.id = student_course.id_student
JOIN course
ON course.id = student_course.id_course;
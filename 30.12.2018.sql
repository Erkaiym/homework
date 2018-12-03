 -- 28.12.2018
 -- #1
 SELECT first_name, last_name, title, from_date 
 FROM employees JOIN titles ON employees.emp_no = titles.emp_no 
 WHERE (titles.emp_no, from_date) 
 IN (SELECT titles.emp_no, MAX(from_date) FROM titles);

-- #2
SELECT dept_name, first_name, last_name 
FROM dept_manager JOIN departments 
ON departments.dept_no = dept_manager.dept_no 
JOIN employees 
ON employees.emp_no = dept_manager.emp_no 
WHERE (employees.emp_no, to_date)
IN (SELECT employees.emp_no, MAX(to_date) FROM dept_manager)
ORDER BY departments.dept_no;


-- 30.12.2018
-- Практика
-- #1.1
SELECT hd FROM Laptop 
UNION
SELECT hd FROM PC 
GROUP BY hd 
ORDER BY hd ASC;

-- #1.2
SELECT speed, AVG(price) AS av_price
FROM (SELECT speed, price FROM PC 
UNION 
SELECT speed, price FROM Laptop) AS a 
GROUP BY speed;

-- #1.3
SELECT ram, AVG(price) AS av_price 
FROM (SELECT ram, price FROM PC 
UNION 
SELECT ram, price FROM Laptop) AS a 
GROUP BY ram HAVING av_price > 500;


-- #2
SELECT first_name, last_name, hire_date
FROM employees 
WHERE hire_date > '2000-01-01';


-- #3
SELECT first_name, last_name, title, hire_date 
FROM employees JOIN titles 
ON employees.emp_no = titles.emp_no 
WHERE hire_date > '2000-01-01';


-- Домашнее задание
-- #1
SELECT first_name, last_name, title, salary 
FROM employees JOIN titles 
ON employees.emp_no = titles.emp_no 
JOIN salaries 
ON salaries.emp_no = employees.emp_no 
WHERE title = 'Senior Engineer' 
AND (salaries.emp_no, salaries.to_date) 
IN (SELECT salalries.emp_no, MAX(salaries.to_date) FROM salaries
GROUP BY salaries.emp_no);


-- #2 - 3
/* SELECT gender, COUNT(gender) AS quantity 
FROM employees JOIN salaries 
ON employees.emp_no = salaries.emp_no 
GROUP BY gender; 

SELECT gender, AVG(salary) AS av_salary 
FROM employees JOIN salaries 
ON employees.emp_no = salaries.emp_no 
GROUP BY gender; */

SELECT gender, COUNT(gender) AS quantity, AVG(salary) AS av_salary 
FROM employees JOIN salaries 
ON employees.emp_no = salaries.emp_no 
GROUP BY gender;


-- #4
SELECT YEAR(hire_date) AS year, COUNT(YEAR(hire_date)) AS quantity 
FROM employees 
WHERE YEAR(hire_date) > '1992' 
GROUP BY YEAR(hire_date);


-- #5
SELECT YEAR(birth_date) AS year, COUNT(YEAR(birth_date)) AS quantity 
FROM employees 
GROUP BY YEAR(birth_date);
create database lab6;

CREATE TABLE locations(
    location_id SERIAL PRIMARY KEY,
    street_address VARCHAR(25),
    postal_code VARCHAR(12),
    city VARCHAR(30),
    state_province VARCHAR(12)
);

CREATE TABLE departments(
    department_id SERIAL PRIMARY KEY,
    department_name VARCHAR(50) UNIQUE,
    budget INTEGER,
    location_id INTEGER REFERENCES locations
);

CREATE TABLE employees(
    employee_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(50),
    phone_number VARCHAR(20),
    salary INTEGER,
    manager_id INTEGER REFERENCES employees,
    department_id INTEGER REFERENCES departments
);

CREATE TABLE job_grades(
    grade CHAR(1),
    lowest_salary INTEGER,
    highest_salary INTEGER
);

SELECT e.first_name,e.last_name, d.department_name, l.city, l.state_province FROM employees e
    JOIN departments d ON e.department_id = d.department_id
    JOIN locations l ON d.location_id = l.location_id
           WHERE e.last_name LIKE '%b%';

SELECT d.department_name,l.city,l.state_province FROM departments d
JOIN locations l ON d.location_id = l.location_id;

SELECT e.first_name as "Employee",m.first_name as "Manager" FROM employees e
LEFT OUTER JOIN employees m ON e.manager_id = m.employee_id;

SELECT j.grade, AVG(e.salary) FROM employees e, job_grades j
WHERE e.salary BETWEEN j.lowest_salary AND j.highest_salary GROUP BY j.grade;

SELECT e.first_name,e.last_name FROM employees e
JOIN departments d ON e.department_id = d.department_id
JOIN locations l ON l.location_id = d.location_id WHERE l.city = 'London';






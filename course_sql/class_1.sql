SELECT first_name FROM employees;
SELECT * FROM employees;
SELECT DISTINCT gender FROM employees;
SELECT first_name, last_name, gender FROM employees
WHERE gender='M' AND first_name='Denis';

SELECT first_name, last_name, gender FROM employees
WHERE gender='M' OR gender='F' AND first_name='Denis';

SELECT first_name FROM employees
WHERE first_name IN ('Mark', 'Denis');

SELECT first_name FROM employees
WHERE first_name LIKE ('Mar%');

SELECT first_name FROM employees
WHERE first_name LIKE ('Mar_');

SELECT *
FROM employees
WHERE birth_date IS NULL
OR first_name IS NULL
OR last_name IS NULL;

SELECT emp_no, salary
FROM salaries
ORDER BY salary DESC
LIMIT 50;

SELECT first_name, last_name
FROM employees
WHERE emp_no IN (47978, 109334);

SELECT *
FROM departments
WHERE (dept_name = 'Quality Management');

SELECT *
FROM dept_manager
WHERE (dept_no = 'd006');

SELECT *
FROM employees
WHERE emp_no = 110854;

SELECT max(salary) FROM salaries;

SELECT count(*) FROM employees;

SELECT count(distinct gender) FROM employees;

SELECT count(distinct gender) as gndr FROM employees;

SELECT count(*), gender
FROM employees
GROUP BY gender;

SELECT * from salaries;

SELECT sum(salary)/12
FROM salaries
where to_date > '2018-01-01';


SELECT *
FROM employees
#where (hire_date >= '1995-01-01') and (hire_date <= '1995-12-31')
WHERE hire_date BETWEEN '1995-01-01' and '1995-12-31'
ORDER BY birth_date
LIMIT 3;

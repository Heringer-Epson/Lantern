###################################################
#Q1
###################################################
SELECT DISTINCT title 
FROM titles
WHERE to_date = '9999-01-01';

###################################################
#Q2
###################################################
SELECT *
FROM employees
WHERE gender='F'
ORDER by birth_date DESC
LIMIT 30;

###################################################
#Q3
###################################################
SELECT e.*
FROM employees AS e, titles AS t
WHERE e.first_name LIKE ('Nic%') AND e.gender='F'
ORDER BY e.birth_date ASC
LIMIT 1;

SELECT title
FROM titles
WHERE emp_no = 87724;
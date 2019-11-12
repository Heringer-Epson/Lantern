SELECT emp_no, MAX(salary) - MIN(salary) as sal_growth
FROM salaries
GROUP BY emp_no
ORDER BY sal_growth DESC;

SELECT *
FROM employees AS e LEFT JOIN salaries AS s
ON e.emp_no = s.emp_no;

SELECT gender, count(*), AVG(s.salary)
FROM employees AS e LEFT JOIN salaries AS s
ON s.emp_no = e.emp_no
WHERE s.to_date > '2018-01-01'
GROUP BY e.gender;

SELECT gender, count(DISTINCT e.emp_no), AVG(s.salary)
FROM employees AS e LEFT JOIN salaries AS s
ON s.emp_no = e.emp_no
WHERE s.to_date > '2018-01-01'
GROUP BY e.gender;
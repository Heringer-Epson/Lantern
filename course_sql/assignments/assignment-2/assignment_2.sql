#Employess schema
#Q1
SELECT dt.dept_name, SUM(s.salary)
FROM employees e
	INNER JOIN salaries s
    ON e.emp_no = s.emp_no
    INNER JOIN dept_emp d
    ON e.emp_no = d.emp_no
    LEFT JOIN departments dt
    ON d.dept_no = dt.dept_no
WHERE (
	s.to_date > '2018-01-01'
	AND d.to_date > '2018-01-01' )
GROUP BY d.dept_no
HAVING (dt.dept_name = 'Finance'
		OR dt.dept_name = 'Sales');

#Q2    
SELECT e.first_name, e.last_name, dm.dept_no, s.salary
FROM employees e
	INNER JOIN dept_manager dm
    on e.emp_no = dm.emp_no 
	INNER JOIN salaries s
    ON e.emp_no = s.emp_no
WHERE (
	s.to_date > '2018-01-01'
	AND dm.to_date > '2018-01-01' )
ORDER BY s.salary ASC;

#Q3
SELECT t.title, AVG(s.salary) AS salary_avg, COUNT(t.title)
FROM salaries s
INNER JOIN titles t
    ON s.emp_no = t.emp_no
WHERE (
	s.to_date > '2018-01-01'
	AND t.to_date > '2018-01-01' )
GROUP BY t.title
ORDER BY salary_avg;

#Classic Models schema.

#Q4
SELECT p.productCode, p.productName, SUM(od.quantityOrdered) qtty
FROM orderdetails od
	INNER JOIN products p
    ON od.productCode = p.productCode
GROUP BY p.productCode
ORDER BY qtty DESC;

#Q5
SELECT 
	c.customerNumber, c.customerName, c.phone,
	c.addressLine1, COUNT(c.customerNumber) n_target
FROM customers c
	INNER JOIN orders o
    ON c.customerNumber = o.customerNumber
GROUP BY c.customerNumber
HAVING n_target > 5
UNION DISTINCT
SELECT 
	c.customerNumber, c.customerName, c.phone,
	c.addressLine1, SUM(p.amount) n_target
FROM customers c
	INNER JOIN payments p
    ON c.customerNumber = p.customerNumber
GROUP BY c.customerNumber
HAVING n_target > 150000;

#Q6
SELECT o.officeCode, SUM(p.amount) total, SUM(p.amount/100) bonus
FROM employees e
	INNER JOIN offices o
    ON e.officeCode = o.officeCode 
    INNER JOIN customers c
    ON c.salesRepEmployeeNumber = e.employeeNumber
    INNER JOIN payments p
    ON p.customerNumber = c.customerNumber
GROUP BY o.officeCode
ORDER BY total DESC;

#Q7
SELECT
	p.productCode, p.productName, AVG(od.priceEach) inc, AVG(p.buyPrice) cost,
	(AVG(od.priceEach) - AVG(p.buyPrice))/AVG(p.buyPrice) marg_profit
FROM products p
	INNER JOIN orderdetails od
    ON p.productCode = od.productCode
GROUP BY p.productCode
ORDER BY marg_profit DESC;

#Q8
SELECT c.customerName, c.creditLimit, SUM(od.quantityOrdered * od.priceEach) target
FROM customers c
	INNER JOIN orders o
    ON c.customerNumber = o.customerNumber
    INNER JOIN orderdetails od
    ON o.orderNumber = od.orderNumber
GROUP BY c.customerNumber
HAVING target > c.creditLimit + 40000
UNION DISTINCT
SELECT c.customerName, c.creditLimit, c.creditLimit target
FROM customers c
WHERE c.creditLimit = 0;

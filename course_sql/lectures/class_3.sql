SELECT e.first_name, e.last_name, s.salary
FROM dept_manager AS d
	INNER JOIN salaries AS s ON s.emp_no = d.emp_no
	INNER JOIN employees as e ON s.emp_no = e.emp_no
WHERE (d.to_date > '2018-01-01' AND s.to_date > '2018-01-01' )
ORDER BY s.salary ASC
LIMIT 5;

SELECT t.title, AVG(s.salary), COUNT(DISTINCT s.emp_no)
FROM salaries AS s
    INNER JOIN titles as t on s.emp_no = t.emp_no
    INNER JOIN employees as e on s.emp_no = e.emp_no
WHERE (t.to_date > '2018-01-01' AND s.to_date > '2018-01-01' )
GROUP BY t.title
ORDER BY AVG(s.salary);

#Same as above, exluding the unused employees table.
SELECT t.title,
	AVG(s.salary) avg_salary,
    COUNT(DISTINCT s.emp_no) cnt_personel
FROM salaries AS s
    INNER JOIN titles as t on s.emp_no = t.emp_no
WHERE (t.to_date > '2018-01-01' AND s.to_date > '2018-01-01' )
GROUP BY t.title
ORDER BY AVG(s.salary);

#Now using the mysqlsampledatabase.sql
#SELECT p.productName, COUNT(od.productCode) AS product_cnt
SELECT p.productName, p.productDescription, SUM(od.quantityordered) AS product_cnt
FROM orderdetails AS od RIGHT JOIN products AS p
	ON od.productCode = p.productCode
GROUP BY od.productCode
ORDER BY product_cnt DESC;

#SELECT *
#FROM orders AS o
#	INNER JOIN customers AS c
#    ON c.customerNumber = o.customerNumber
#	INNER JOIN orderdetails AS od
#	ON od.orderNumber = o.orderNumber;

SELECT c.customerName, c.phone
FROM orders AS o
	INNER JOIN customers AS c
    ON c.customerNumber = o.customerNumber
GROUP BY o.customerNumber
HAVING COUNT(o.customerNumber) > 3
UNION DISTINCT
SELECT c.customerName, c.phone
FROM payments AS p
	INNER JOIN customers AS c
    ON c.customerNumber = p.customerNumber
GROUP BY c.customerNumber
HAVING SUM(p.amount) > 100000;

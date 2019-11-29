##Find out the salary of people hired after 2000-01-01
##THe first method is computationally more expensive, but faster with smaller data sets
select emp_no, salary from salaries 
where emp_no in
(select  emp_no from employees
where hire_date> "2000-01-01" );

select e.emp_no, first_name, last_name, s.salary from employees e
join salaries s
on e.emp_no=s.emp_no
where e.hire_date> "2000-01-01";

select c.customerNumber, c.customerName, sum(amount) total from customers c
join payments p  
on p.customerNumber=c.customerNumber
group by c.customerNumber
having sum(amount)>100000 
##order by total desc
union 
select c.customerNumber, c.customerName, count( distinct orderNumber) counter from customers c 
join orders o 
on o.customerNumber=c.customerNumber
group by c.customerNumber
having counter>3;

##what products are the people queries above buying?
select * from products p 
join orderdetails od
on p.productCode=od.productCode
join orders o
on od.orderNumber=o.orderNumber
where o.customerNumber in
(SELECT c.customerNumber, count(distinct orderNumber)  num_or_amt_of_purchase
FROM customers c INNER JOIN orders
ON c.customerNumber = orders.customerNumber
GROUP BY customerNumber,customerName,phone,postalCode,addressLine1,addressLine2
HAVING num_or_amt_of_purchase > 3
UNION ALL
SELECT c.customerNumber,SUM(amount)  num_or_amt_of_purchase
FROM customers c INNER JOIN payments pa
ON c.customerNumber = pa.customerNumber
GROUP BY customerNumber,customerName,phone,postalCode,addressLine1,addressLine2
HAVING num_or_amt_of_purchase > 100000);

##IF NULL(name,"unknown") -> will replace Null values of column name with "unknown"

select *, IFNULL(comments,"no comment") comment_or_not, datediff(shippedDate,orderDate) days_to_ship , 
case when datediff(shippedDate,orderDate)<= 3 then 'express shipping'
when datediff(shippedDate,orderDate)> 15 then 'delayed shipping'
when datediff(shippedDate,orderDate)<=15 and datediff(shippedDate,orderDate)>3 then "regular shipping"
else 'unknown'
end shipping_class
from orders;

##Inser your name into employees table

insert into employees (emp_no, birth_date, first_name, last_name, gender, hire_date)
values ("500000","1990-01-01", "Sasha", "Hajy", "M", "2000-01-01");

select * from employees
order by emp_no desc;

insert into employees (emp_no, birth_date, first_name, last_name, gender, hire_date)
values ("500000","1990-01-01", "Sasha", "Hajy", "M", "2000-01-01");

select * from employees where emp_no between 499994 and 499999;


 
 INSERT INTO employees(SELECT emp_no+5000000,birth_date, first_name, last_name, gender,hire_date
FROM employees WHERE emp_no BETWEEN 499994 AND 499999);
 
 select * from employees
 order by emp_no desc;
 
 update employees
 set last_name ="Hajy Hasani"
 where emp_no=500000;
  

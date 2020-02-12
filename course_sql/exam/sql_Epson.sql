/*
Change this sql file to your name (save as)
You have 75 mins to do this exam (until 8:30 pm)
It is closed book exam, no book, no power point, no etc.
No connection to the internet please.
Whenever you are done, raise your hand. then we will connect to the internet and email your sql file to me:
amirsina.e@gmail.com
Technical questions are not answered.

###############################################################################
1- Which one is INCORRECT? (2.5 marks)
    a. SQL is a procedural language
    b. MySQL is an example of relational database management systems (RDBMS)
	c. SQL is focused on 'what' rather than 'how'
    d. Data modeler is a person who designs databases

ANSWER:
c
###############################################################################
2- Which one is NOT an example of DML command (data manupulation language)? (2.5 marks)
	a. SELECT command
	b. UPDATE command
	c. CREATE command
	d. INSERT command

ANSWER:
c
###############################################################################
3- Choose the query that searches for the names having 's' as the second letter in table_1. (2.5 marks)
	a. SELECT name FROM table_1 WHERE name LIKE '%s%'
	b. SELECT name FROM table_1 WHERE name LIKE '_s%'
	c. SELECT name FROM table_1 WHERE name LIKE '_s_'
	d. SELECT name FROM table_1 WHERE name LIKE '%s_'

ANSWER:
b
###############################################################################
4- Which one is CORRECT? (2.5 marks)
	a. Primary key is a unique column that can be NULL in a table
	b. Unique key is same as primary key
	c. Foreign key is a column that has unique values and used to connect tables
	d. Nono of the above

ANSWER:
d
-2.5
*/
###############################################################################
############## REMAINING QUESTIONS ARE ABOUT SAKILA DATABASE ##################

#5- Write a query that returns distinct first name of inactive customers with address_id between 290 and 545.
#(10 marks)

SELECT DISTINCT c.first_name
FROM customer as c
WHERE (c.address_id BETWEEN 290 AND 545) AND c.active = 0;

###############################################################################
#6- Write a query that returns the top 10 longest movies, which are not among these ratings: PG, G, NC-17
#(12 marks)

SELECT f.title, f.rating, f.length
FROM film AS f
WHERE (f.rating != 'PG' AND f.rating != 'G' AND f.rating != 'NC-17')
ORDER BY f.length DESC
LIMIT 10;

###############################################################################
#7- Considering payments before 2005-08-01, find out customer ids that have total payments more than $100.
#(15 marks)


SELECT p.customer_id, SUM(AMOUNT) AS total_payment
FROM payment as p
WHERE p.payment_date < '2005-08-01'
GROUP BY p.customer_id
HAVING total_payment > 100
ORDER BY total_payment DESC;

###############################################################################
/*8- The management is looking for a list of movies that are:
	Either from store id 1 and has been rented more than 17 times,
    OR from store id 2 and has been rented more than 18 times.
	Provide this list of movies (film id, title, and number of rents) in a single query.
    (20 marks)
*/

SELECT i.film_id, f.title, COUNT(i.film_id) AS number_of_rents
FROM rental AS r
    INNER JOIN inventory as i
    ON r.inventory_id = i.inventory_id
    INNER JOIN store as s
    ON s.store_id = i.store_id
    INNER JOIN film AS f
    ON f.film_id = i.film_id
WHERE i.store_id = 1
GROUP BY i.film_id
HAVING number_of_rents > 17
UNION DISTINCT
SELECT i.film_id, f.title, COUNT(i.film_id) AS number_of_rents
FROM rental AS r
    INNER JOIN inventory as i
    ON r.inventory_id = i.inventory_id
    INNER JOIN store as s
    ON s.store_id = i.store_id
    INNER JOIN film AS f
    ON f.film_id = i.film_id
WHERE i.store_id = 2
GROUP BY i.film_id
HAVING number_of_rents > 18;


###############################################################################
/*9- The management office would like to give a cash bonus to the customers who has purchased more than $200 so far.
However, he wants to make sure that the data is up-to-date.
Write a query for those customers, and return their customer id, and last update of their payments and payments' amount.
(20 marks)
*/

#Note need inner query to get payment amount. I forgot the syntax.
SELECT c.customer_id, MAX(p.payment_date)
FROM customer AS c
	INNER JOIN payment AS p
	ON c.customer_id = p.customer_id
GROUP BY c.customer_id
HAVING SUM(p.amount) > 200;

#-12

###############################################################################
/*10- The database administrator recently realised that all mising information on rental id columns in payment table is about rental id 16050.
So we need to do some modifications in database (13 marks in total):

a- Write a query that returns two columns: payment_id, and rental_id filling null values with 16050 (3 marks).

b- Insert a new row to rental table with information below: (5 marks)
(16050, '2005-06-18', 323, 562, '2005-06-25', 1, '2019-12-05')

c- Update and fill the missing values of rental_id column in payment table with correct value 
(Be careful, first do part b and then c to avoid getting an error).
(5 marks)
*/


UPDATE rental ifnull (rental_id, 16050);

INSERT (16050, '2005-06-18', 323, 562, '2005-06-25', 1, '2019-12-05') IN RENTAL;

#-3
#-3
#-4


#***********************************
#MARK: 75.5


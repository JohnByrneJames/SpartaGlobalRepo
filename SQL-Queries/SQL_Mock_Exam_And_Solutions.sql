/* 
The format of this SQL document is as follow..
~ QUESTION ~
~ ATTEMPT ~
~ COMMENTS ~
_____________
~ ANSWER ~
 */


/*1. Create a report showing the title of courtesy and the first and last name
of all employees whose title of courtesy is not "Ms." or "Mrs.".*/
SELECT * FROM Employees

SELECT e.TitleOfCourtesy, e.FirstName, e.LastName
FROM Employees e
WHERE e.TitleOfCourtesy != 'Ms.' AND e.TitleOfCourtesy != 'Mrs.'

-- DIFFERENT WAY BUT SAME ANSWER

SELECT e.TitleOfCourtesy, e.FirstName, e.LastName
FROM employees e WHERE e.TitleOfCourtesy NOT IN ('Ms.', 'Mrs.')

/*2. Create a report that shows the company name, contact title, city and country of all customers 
in Mexico or in any city in Spain except Madrid(in Spain).*/

SELECT * FROM customers 

SELECT c.CompanyName, c.ContactTitle, c.City, c.Country
FROM Customers c 
WHERE c.Country IN ('Spain', 'Mexico') AND c.City <> 'Madrid'

-- DIFFERENT WAY BUT SAME ANSWER

SELECT c.CompanyName, c.ContactTitle, c.City, c.Country
FROM customers c WHERE Country IN ('Mexico','Spain') AND CITY NOT IN ('Madrid')

/*3. Create a report showing the title of courtesy and the first and
last name of all employees whose title of courtesy begins with "M" and
is followed by any character and a period (.).*/

SELECT e.TitleOfCourtesy, CONCAT(e.FirstName, ' ', e.LastName)
FROM Employees e
WHERE e.TitleOfCourtesy LIKE 'M_.' 

--- DIFFERENT ANSWER ? -- ASK ASTHA ABOUT THIS IT DOESN'T SEEM CORRECT

SELECT e.TitleOfCourtesy, e.FirstName, e.LastName
FROM Employees e WHERE e.TitleOfCourtesy LIKE ('M%.')


/*4. Create a report showing the first and last names of
all employees whose region is defined.*/

SELECT e.FirstName, e.LastName
FROM Employees e 
WHERE e.Region IS NOT NULL

-- SAME ANSWER

SELECT e.FirstName, e.LastName
FROM Employees e WHERE e.Region IS NOT NULL

/*5. Select the Title, FirstName and LastName columns from the Employees table.
Sort first by Title in ascending order and then by LastName 
in descending order.*/

SELECT e.Title, e.FirstName, e.LastName 
FROM Employees e 
ORDER BY e.Title ASC, e.LastName DESC

--- ANSWER IS CORRECT, IT SAYS TITLE NOT TITLEOFCOURTESY 

SELECT e.TitleOfCourtesy, e.FirstName, e.LastName
FROM Employees e ORDER BY e.TitleOfCourtesy, e.LastName DESC


/*6. Write a query to get the number of employees with the same job title.*/

SELECT e.Title, COUNT(e.EmployeeID) AS "Number of employees with same job title"
FROM Employees e 
GROUP BY e.Title

--- ANSWER IS CORRECT 

SELECT e.Title,COUNT(e.EmployeeID) AS "Count of Number of Employees with same job title"
FROM Employees e
GROUP BY e.Title

/*7.
Create a report showing the Order ID, the name of the company that placed the order,
and the first and last name of the associated employee.
Only show orders placed after January 1, 1998 that shipped after they were required.
Sort by Company Name.*/
SELECT * FROM Orders

SELECT o.OrderID, c.CompanyName, e.FirstName, e.LastName 
FROM Customers c
INNER JOIN Orders o ON c.CustomerID = o.CustomerID
INNER JOIN Employees e ON o.EmployeeID = e.EmployeeID
WHERE o.OrderDate > '1998-01-01'

--- WRONG DID NOT READ THE WHOLE QUESTION...

SELECT o.OrderID, c.CompanyName, e.FirstName, e.LastName
FROM Employees e
	JOIN Orders o ON (e.EmployeeID = o.EmployeeID)
	JOIN Customers c ON (c.CustomerID = o.CustomerID)
WHERE o.ShippedDate > o.RequiredDate AND o.OrderDate > '1998-01-01'
ORDER BY c.CompanyName;

/*8.
Create a report that shows the total quantity per product (from the OrderDetails table) ordered. Only show records for 
products for which the quantity ordered is fewer than 200. The report should return*/

SELECT * FROM Products

SELECT od.ProductID, SUM(od.Quantity) AS "Total Units"
FROM [Order Details] od
GROUP BY ProductID
HAVING SUM(Quantity) < 200

--- CORRECT ANSWER EXCEPT I PRINTED THE PRODUCT ID INSTEAD OF PRODUCT NAME


SELECT p.ProductName, SUM(od.Quantity) AS "TotalUnits"
FROM [Order Details] od JOIN Products p ON
	(p.ProductID = od.ProductID)
GROUP BY p.ProductID,p.ProductName
HAVING SUM(od.Quantity) < 200;

/*9.Create a report that shows the total number of orders by Customer since December 31, 1996. 
The report should only return rows for which the NumOrders is greater than 15. 
*/

SELECT c.ContactName, COUNT(o.CustomerID) AS "NumOrders"
FROM Customers c 
FULL JOIN Orders o ON c.CustomerID = o.CustomerID -- LEFT JOIN
WHERE o.OrderDate >= '1996-12-31'
GROUP BY c.ContactName
HAVING COUNT(o.CustomerID) > 15

-- CORRECT ANSWER THERE WAS NO PART OF THE QUESTION ASKING TO ORDER BY DESC

SELECT c.CustomerID, COUNT(o.OrderID) AS "NumOrders"
FROM Customers c JOIN Orders o ON
	(c.CustomerID = o.CustomerID)
WHERE OrderDate >= '31-Dec-1996'
GROUP BY c.CustomerID
HAVING COUNT(o.OrderID) > 15
ORDER BY NumOrders DESC;


/*10.  SQL statement will return all customers, and number of orders they might have placed. 
Include those customers as well who have not placed any orders.*/

SELECT * FROM Customers
SELECT * FROM Orders 

SELECT c.ContactName, COUNT(o.CustomerID) AS "Number of Orders"
FROM Customers c 
FULL JOIN Orders o ON c.CustomerID = o.CustomerID -- LEFT JOIN
GROUP BY c.ContactName
ORDER BY COUNT(o.CustomerID) DESC

-- CORRECT ANSWER EXCEPT I SORTED IN DESC ORDER FOR CLARITY HERE AND I USED A FULL JOIN INSTEAD OF LEFT JOIN

SELECT c.CustomerID, COUNT(o.OrderID) AS "Number Of Orders Placed by Customer"
FROM Customers c LEFT JOIN Orders o
ON c.CustomerID=o.CustomerID
GROUP BY c.CustomerID
ORDER BY COUNT(o.orderID) DESC
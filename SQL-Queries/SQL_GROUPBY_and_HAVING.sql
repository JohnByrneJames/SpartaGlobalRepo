SELECT * FROM Employees

SELECT * FROM Orders

USE Northwind 

SELECT COUNT(CustomerID), City 
FROM Customers
GROUP BY City
HAVING COUNT(CustomerID) > 2

SELECT Employees.LastName, COUNT(Orders.OrderID) AS NumberOfOrders
FROM Orders
INNER JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID
WHERE LastName = 'Davolio' OR LastName = 'Fuller'
GROUP BY LastName
HAVING COUNT(Orders.OrderID) > 5;

SELECT Orders.OrderID, Customers.ContactName, Orders.OrderDate
FROM Orders
INNER JOIN Customers ON Orders.CustomerID=Customers.CustomerID;

SELECT COUNT(CustomerID)
FROM Customers;

SELECT AVG(UnitPrice)
FROM Products

SELECT COUNT(ProductID), UnitPrice
FROM Products
GROUP BY UnitPrice
HAVING UnitPrice > 20

SP_HELP Employees

-- List the number of customers in each country. 
-- Only include countries with more than 10 customers. 
SELECT COUNT(c.CustomerID), c.Country 
FROM Customers c
GROUP BY c.Country
HAVING COUNT(c.CustomerID) > 10

SELECT COUNT(c.CustomerID), c.Country 
FROM Customers c
GROUP BY c.Country
WHERE COUNT(c.CustomerID) > 10

-- List the number of customers in each country, except the USA, sorted high to low. 
-- Only include countries with 9 or more customers. 
SELECT COUNT(c.CustomerID), Country 
    FROM Customers c
    WHERE Country IS NULL 'USA'
    GROUP BY Country
HAVING COUNT(c.CustomerID) >= 9
    ORDER BY COUNT(c.CustomerID) DESC

-- This statement is displaying all the employees that have registered more than 10 orders
SELECT e.LastName, COUNT(o.OrderID) AS "NumberOfOrders" 
FROM (Orders o INNER JOIN Employees e ON o.EmployeeID=e.EmployeeID)
GROUP BY e.LastName
HAVING COUNT(o.OrderID) > 10;

SELECT COUNT(c.CustomerID), c.Country
FROM Customers c
GROUP BY c.Country
ORDER BY COUNT(c.CustomerID) DESC


SELECT * FROM Customers
SELECT * FROM Orders 
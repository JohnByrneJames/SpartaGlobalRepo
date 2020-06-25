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
USE Northwind

SELECT * FROM Customers

-- 1.1	Write a query that lists all Customers in either Paris or London. 
-- Include Customer ID, Company Name and all address fields.

SELECT 
c.CustomerID, 
c.CompanyName, 
CONCAT(c.Address, ', ', c.City, ', ', c.Country, ', ' , c.PostalCode) AS "Address"
FROM Customers c
WHERE c.City = 'Paris' OR c.City = 'London'


-- 1.2	List all products stored in bottles.

SELECT * FROM Products

SELECT p.ProductName
FROM Products p
WHERE p.QuantityPerUnit LIKE '%bottles'


-- 1.3	Repeat question above, but add in the Supplier Name and Country.

SELECT p.ProductName, s.CompanyName, s.Country
FROM Products p
INNER JOIN Suppliers s ON p.SupplierID = s.SupplierID
WHERE p.QuantityPerUnit LIKE '%bottles'


-- 1.4	Write an SQL Statement that shows how many products there are in each category. 
-- Include Category Name in result set and list the highest number first.

SELECT * FROM Categories

SELECT COUNT(p.ProductID) AS "Products in Category", c.CategoryName
FROM Products p
INNER JOIN Categories c ON p.CategoryID = c.CategoryID
GROUP BY c.CategoryName

-- 1.5	List all UK employees using concatenation to join their title of courtesy, first name and last name together. 
-- Also include their city of residence.

SELECT * FROM Employees

SELECT CONCAT(e.TitleOfCourtesy, ' ', e.FirstName, ' ', e.LastName, ' From ', e.City) AS "UK Employees"
FROM Employees e 
WHERE e.Country = 'UK'


-- 1.6	List Sales Totals for all Sales Regions (via the Territories table using 4 joins) with a Sales Total greater than 1,000,000. 
-- Use rounding or FORMAT to present the numbers. 

SELECT * FROM Orders
SELECT * FROM Region
SELECT * FROM Customers 
SELECT * FROM Employees
SELECT * FROM Territories

SELECT SUM(od.Quantity * UnitPrice) AS "Total Sales", r.RegionDescription
FROM [Order Details] od
INNER JOIN Orders o ON o.OrderID = od.OrderID
INNER JOIN EmployeeTerritories et ON et.EmployeeID = o.EmployeeID
INNER JOIN Territories t ON t.TerritoryID = et.TerritoryID
INNER JOIN Region r ON r.RegionID = t.RegionID
GROUP BY r.RegionDescription
HAVING SUM(od.Quantity * UnitPrice) > 1000000

-- 
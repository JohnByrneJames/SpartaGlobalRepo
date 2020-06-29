USE Northwind

SELECT * FROM Customers

-- 1.1	Write a query that lists all Customers in either Paris or London. 
-- Include Customer ID, Company Name and all address fields.

SELECT c.CustomerID, c.CompanyName, CONCAT(c.Address, ', ', c.City, ', ', c.PostalCode, ', ' , c.Country) AS "Address" -- Concatenate all the address fields in the customer table as they are related
FROM Customers c
WHERE c.City = 'Paris' OR c.City = 'London'

-- 1.2	List all products stored in bottles.

SELECT p.ProductName
FROM Products p
WHERE p.QuantityPerUnit LIKE '%bottle%' -- Used %bottle% as some products are stored in a single bottle and others in bottles

-- 1.3	Repeat question above, but add in the Supplier Name and Country.

SELECT p.ProductName, s.CompanyName AS "Supplier Name", s.Country
FROM Products p
INNER JOIN Suppliers s ON p.SupplierID = s.SupplierID
WHERE p.QuantityPerUnit LIKE '%bottle%'

-- 1.4	Write an SQL Statement that shows how many products there are in each category. 
-- Include Category Name in result set and list the highest number first.

SELECT c.CategoryName, COUNT(p.ProductID) AS "Products in Category"
FROM Products p
INNER JOIN Categories c ON p.CategoryID = c.CategoryID
GROUP BY c.CategoryName
ORDER BY [Products in Category] DESC

SELECT  c.CategoryName "Category Name", COUNT(*) as "No of Products"
FROM Products p
  		INNER JOIN Categories c ON p.CategoryID=c.CategoryID
GROUP BY c.CategoryName
ORDER BY COUNT(*) DESC

-- 1.5	List all UK employees using concatenation to join their title of courtesy, first name and last name together. 
-- Also include their city of residence.

SELECT CONCAT(e.TitleOfCourtesy, ' ', e.FirstName, ' ', e.LastName, ' From ', e.City) AS "UK Employees"
FROM Employees e 
WHERE e.Country = 'UK'

-- 1.6	List Sales Totals for all Sales Regions (via the Territories table using 4 joins) with a Sales Total greater than 1,000,000. 
-- Use rounding or FORMAT to present the numbers. 
-- (ANSWER) Northern, Eastern and Western

-- WITHOUT DISCOUNT

SELECT SUM(od.UnitPrice * od.Quantity) AS "Total Sales", r.RegionDescription
FROM [Order Details] od
INNER JOIN Orders o ON o.OrderID = od.OrderID
INNER JOIN EmployeeTerritories et ON et.EmployeeID = o.EmployeeID
INNER JOIN Territories t ON t.TerritoryID = et.TerritoryID
INNER JOIN Region r ON r.RegionID = t.RegionID
GROUP BY r.RegionDescription
HAVING ROUND(SUM(od.UnitPrice * od.Quantity),2)  > 1000000

-- WITH DISCOUNT 

SELECT ROUND(SUM((od.UnitPrice * od.Quantity) - (od.UnitPrice * od.Discount * od.Quantity)), 2) AS "Total Sales", r.RegionDescription
FROM [Order Details] od
INNER JOIN Orders o ON o.OrderID = od.OrderID -- Join Orders to Order Details
INNER JOIN EmployeeTerritories et ON et.EmployeeID = o.EmployeeID -- Join EmployeeTerritories to Orders
INNER JOIN Territories t ON t.TerritoryID = et.TerritoryID -- Join Territories to EmployeeTerritories
INNER JOIN Region r ON r.RegionID = t.RegionID -- Join Region to terriroties
GROUP BY r.RegionDescription
HAVING ROUND(SUM((od.UnitPrice * od.Quantity) - (od.UnitPrice * od.Discount * od.Quantity)), 2)  > 1000000 -- Round price with discount to 2 decimal points

-- Revealed answer

SELECT r.RegionID, r.RegionDescription AS Region, 
FORMAT(SUM((UnitPrice * Quantity) * (1-Discount)),'C') 
AS "Sales Total by Region"
    FROM Orders AS o
    	INNER JOIN [Order Details] AS od ON od.OrderID = o.OrderID
    	INNER JOIN EmployeeTerritories AS et ON o.EmployeeID = et.EmployeeID
    	INNER JOIN Territories AS t ON et.TerritoryID = t.TerritoryID
    	INNER JOIN Region AS r ON t.RegionID = r.RegionID
    GROUP BY r.RegionDescription, r.RegionID
    HAVING SUM((UnitPrice * Quantity) * (1-Discount)) > 1000000
    ORDER BY "Sales Total by Region" DESC;

-- 1.7	Count how many Orders have a Freight amount greater than 100.00 and either USA or UK as Ship Country. 
-- (ANSWER) 49

SELECT * FROM Orders

SELECT Count(o.orderID) AS "Frieght Greater than 100.00"
FROM Orders o 
WHERE o.Freight > 100.000 AND o.ShipCountry IN ('UK', 'USA')

-- 1.8	Write an SQL Statement to identify the Order Number of the Order with the highest amount(value) of discount 
-- applied to that order.
-- (Answer) = 10353 and 103372

SELECT TOP 1 od.OrderID, od.UnitPrice, od.Quantity, od.Discount, (od.UnitPrice * od.Discount * od.Quantity) AS "Total Discount" -- UnitPrice * Discount * Quantity = Total Discount
FROM [Order Details] od
ORDER BY [Total Discount] DESC

-- Actual answer 

SELECT OrderID AS 'Order ID', 
       FORMAT((UnitPrice * Quantity) * Discount,'C') AS 'Discount Amount'
    FROM [Order Details]
    ORDER BY [Discount Amount] DESC;
    
-- 2.1 Write the correct SQL statement to create the following table:
-- Spartans Table – include details about all the Spartans on this course. 
-- Separate Title, First Name and Last Name into separate columns, and include University attended, course taken and mark achieved. 
-- Add any other columns you feel would be appropriate. DO NOT INCLUDE DATEOFBIRTH

CREATE DATABASE Mini_projectDB_John

USE Mini_projectDB_John

CREATE TABLE [Spartans] (
    [SpartansID] INTEGER NOT NULL IDENTITY(1, 1),
    [Title] VARCHAR(255) NULL,
    [FirstName] VARCHAR(255) NULL,
    [Surname] VARCHAR(255) NULL,
    [University] VARCHAR(255) NULL,
    [Course] VARCHAR(255) NULL,
    [Mark] VARCHAR(255) NULL,
    PRIMARY KEY ([SpartansID])
);

-- 2.2 Write SQL statements to add the details of the Spartans in your course to the table you have created.	

INSERT INTO Spartans([Title],[FirstName],[Surname],[University],[Course],[Mark]) 
VALUES('Mrs.','Georgina','Bartlett','Newcastle University','Archaeology','2:1'),
('Mr.','Humza','Malak','University of Kent','Computing with Games Development','2:2'),
('Mr.','Ibrahim','Bocus','University of Leicester','Computer Science','2:1'),
('Mr.','Bari','Allali','Lancaster University','Business Economics','2:2'),
('Mr.','Nola','Alston','University of Warwick','International Business & Management','3:3'),
('Dr.','Aspen','Reed','University of Leicester','Computing with Games Development','3:3'),
('Ms.','Ezekiel','Espinoza','University of Greenwich','Product Design','2:2'),
('Mr.','Aretha','Berry','Newcastle University','Aerospace Engineering','1:1'),
('Dr.','Ivan','Harrell','Edinburgh','Computing with Games Development','2:1'),
('Mrs.','Sydnee','Evans','Aston University','International Business & Management','2:2');

SELECT * FROM Spartans

SELECT CONCAT(s.title, ' ', s.FirstName, ' ', s.Surname) AS "Students Who Attended Greenwich"
FROM Spartans s 
WHERE s.University = 'University of Greenwich'

-- 3.1 List all Employees from the Employees table and who they report to. No Excel required.

USE Northwind

SELECT CONCAT(e1.FirstName,' ', e1.LastName, ' Reports to') AS "Employee", CONCAT(e2.FirstName,' ', e2.LastName) AS "Superior" 
FROM Employees e1, Employees e2 -- This is done by using a SELF JOIN to compare two instances of a table against eachother
WHERE e1.ReportsTo = e2.employeeID 

-- Answer from sheet

SELECT e.FirstName + ' ' + e.LastName AS "Employee Name",
		b.FirstName + ' ' + b.LastName AS "Reports To"
	FROM Employees e 
	LEFT JOIN Employees b ON e.ReportsTo=b.EmployeeID
	ORDER BY "Reports To","Employee Name";


-- 3.2 List all Suppliers with total sales over $10,000 in the Order Details table. 
-- Include the Company Name from the Suppliers Table and present as a bar chart as below: (5 Marks)

SELECT s.CompanyName, ROUND(SUM((od.UnitPrice * od.Quantity) - (od.UnitPrice * od.Discount * od.Quantity)), 2) AS "Total Sales" -- work out total of order - discount of order
FROM Suppliers s
INNER JOIN Products p ON s.SupplierID = p.SupplierID
INNER JOIN [Order Details] od ON p.ProductID = od.ProductID 
GROUP BY s.CompanyName
HAVING SUM((od.UnitPrice * od.Quantity) - (od.UnitPrice * od.Discount * od.Quantity)) > 10000 
ORDER BY SUM((od.UnitPrice * od.Quantity) - (od.UnitPrice * od.Discount * od.Quantity)) DESC

-- 3.3 List the Top 10 Customers YTD (year to date) for the latest year in the Orders file. 
-- Based on total value of orders shipped. No Excel required. (10 Marks)

SELECT TOP 10
	c.CustomerID,
    c.CompanyName,  
    ROUND(SUM((od.UnitPrice * od.Quantity) - (od.UnitPrice * od.Discount * od.Quantity)), 2) AS "Total value of orders shipped"
FROM Customers c
INNER JOIN Orders o ON c.CustomerID = o.CustomerID
INNER JOIN [Order Details] od ON o.OrderID = od.OrderID
WHERE YEAR(o.OrderDate) = (SELECT MAX(YEAR(orderDate)) FROM Orders) AND o.ShippedDate IS NOT NULL -- Do not count orders that haven't been shipped yet AKA NULL INNER Query to find latest year
GROUP BY c.CustomerID, c.CompanyName
ORDER BY [Total value of orders shipped] DESC -- List in DESC to reveal top 10 with highest value

-- ANSWER sheet 

SELECT TOP 10 c.CustomerID AS "Customer ID", c.CompanyName As "Company",
FORMAT(SUM(UnitPrice * Quantity * (1-Discount)),'C') 
AS "YTD Sales"
FROM Customers c
 		INNER JOIN Orders o ON o.CustomerID=c.CustomerID
 		INNER JOIN [Order Details] od ON od.OrderID=o.OrderID
	WHERE YEAR(OrderDate)=(SELECT MAX(YEAR(OrderDate)) From Orders)
AND o.ShippedDate IS NOT NULL
	GROUP BY c.CustomerID, c.CompanyName
 	ORDER BY SUM(UnitPrice * Quantity * (1-Discount)) DESC;


-- 3.4 Plot the Average Ship Time by month for all data in the Orders Table using a line chart as below. (10 Marks)

SELECT CONCAT(YEAR(o.OrderDate),'-', MONTH(o.OrderDate)) AS "Year-Month", -- Combine year and month of orderdate
AVG(DATEDIFF(d, o.OrderDate, o.ShippedDate)) AS "Average Ship Time" -- Get the days difference between order and ship date
FROM Orders o 
GROUP BY YEAR(o.OrderDate), MONTH(o.OrderDate) -- Group By Year, then group it by months
ORDER BY YEAR(o.OrderDate), MONTH(o.OrderDate) ASC

SELECT CONCAT(DATENAME(month, o.OrderDate), '-', DATENAME(year, o.OrderDate)) AS  "Year-Month",
AVG(DATEDIFF(d, o.OrderDate, o.ShippedDate)) AS "Average Ship Time" 
FROM Orders o

-- ANSWER Sheet

SELECT MONTH(OrderDate) Month, YEAR(OrderDate) Year, 
AVG(CAST(DATEDIFF(d, OrderDate, ShippedDate) As DECIMAL(10,2))) As ShipTime
	FROM orders 
	WHERE ShippedDate IS NOT NULL
	GROUP BY YEAR(OrderDate),MONTH(OrderDate)
	ORDER BY Year ASC, Month ASC
	   
--- 
-- Super formatted way below - from Ibrahim

 
SELECT
CONCAT(sq1.MonthName,' ', sq1.YearOrdered) "Date Ordered"
    ,AVG("ShipTimePerproductindays") "AverageShipTimePerproductindays"/*This uses the subquery information and averages the amount of shipping time for the column*/
FROM

        (SELECT
DATEDIFF(d,o.orderdate,o.ShippedDate) "ShipTimePerproductindays"
            ,MONTH(o.OrderDate) "MonthOrdered"
            ,YEAR(o.orderdate) "YearOrdered"
            ,DateName(MONTH,DATEADD(MONTH,MONTH(o.orderdate) , 0 ) -1 ) "MonthName"/* This converts the month number to month name */
FROM
            Orders o) sq1 /* This subquery gives the time it took to ship each order, and also the month that the order was made*/
GROUP BY
     sq1.YearOrdered /*This tells the AVG function to only average the shiptimes for each month*/
    ,sq1.MonthName
    ,sq1.MonthOrdered
ORDER BY
CONVERT(datetime, CONCAT(sq1.YearOrdered,'/',sq1.MonthOrdered,'/','1'))/* This puts it in a nice format for excel*/


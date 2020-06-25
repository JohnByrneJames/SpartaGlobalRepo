-- WHERE clause-filter the data
SELECT * FROM Customers
WHERE City = 'Paris'

-- How many employees have home city of London ?
SELECT * FROM Employees 
WHERE City = 'London'

SELECT COUNT(*) AS "Employees living in London" FROM Employees
WHERE City = 'London'

-- Which Employee is a Doctor ?
SELECT * FROM Employees
WHERE TitleOfCourtesy = 'Dr.'

-- Good way to query with a count of how many = 1 Doctor
SELECT COUNT(*) AS "Number of employees with title doctor" FROM Employees
WHERE TitleOfCourtesy = 'Dr.'

-- How many products are discountinued ?
SELECT * FROM Products 
WHERE Discontinued = 1
-- 1 = TRUE / 0 = FALSE

SELECT COUNT(*) AS "Products that are discontinued" FROM Products
WHERE Discontinued = 1


SELECT * FROM customers WHERE CompanyName = 'Anais''s'

-- TABLE ALIASING (FROM Comes first then start select)
SELECT c.CompanyName, c.City, c.Country, c.Region
FROM Customers c
WHERE c.Region = 'BC'

-- SELECT THE TOP 100 rows
SELECT TOP 100 CompanyName, City FROM Customers
WHERE Country = 'France'

/*AND/OR*/
-- AND-all criteria needs to be fulfilled
-- OR-either criteria needs to be fulfilled
SELECT ProductName, UnitPrice FROM Products
Where CategoryID = 1 AND Discontinued = 0

SELECT ProductName, UnitPrice FROM Products
Where CategoryID = 1 OR Discontinued = 0

-- Operators being used with Key words
SELECT ProductName, UnitPrice FROM Products
WHERE UnitsInStock > 0 AND UnitPrice < 29.99

SELECT ProductName, UnitPrice FROM Products
WHERE UnitsInStock > 0 OR UnitPrice < 29.99

-- This can be useful for returning unique values
SELECT DISTINCT c.Country 
FROM Customers c

SELECT DISTINCT Country FROM Customers
WHERE ContactTitle = 'Owner'

-- Wildcards
--% ANYTHING ENDING WITH A
SELECT DISTINCT c.Country
FROM Customers c WHERE Country LIKE '%a'

--% ANYTHING STARTING WITH G
SELECT DISTINCT c.Country
FROM Customers c WHERE Country LIKE 'g%'

/*Countries start with U, ending with letter 'A'*/
SELECT DISTINCT c.Country
FROM Customers c WHERE Country LIKE 'U%A'

/*Countries either starting with U or A or M*/
SELECT DISTINCT c.Country 
FROM Customers c WHERE Country LIKE '[UAM]%'
ORDER By c.Country DESC 

-- ORDER BY c.Country ASC

/*Countries ending with either U or A or M */
SELECT DISTINCT c.Country 
FROM Customers c WHERE Country LIKE '%[UAM]'

/*Countries not starting with U or A or M */
SELECT DISTINCT c.Country 
FROM Customers c WHERE Country LIKE '%[^UAM]'

/*Countries who 3rd letter is A, _ means it can be anything */
SELECT DISTINCT c.Country
FROM Customers c WHERE Country LIKE '__A%'

/*Bring back any products that begin with the letters 'Ch'*/
SELECT p.ProductName
FROM Products p WHERE p.ProductName LIKE 'Ch%'

SELECT * FROM Customers
WHERE Region LIKE '_A'

-- Here the IN statement specifies places in the regions of 'WA' and 'SP'
SELECT * FROM Customers 
WHERE Region IN ('WA','SP')

-- Same as IN but uses the OR operator
SELECT * FROM Customers 
WHERE (Region = 'WA' OR Region = 'SP') AND Country = 'Brazil'

SELECT * FROM Customers
WHERE Region IN('WA', 'SP') AND Country IN ('Brazil', 'USA')


-- BETWEEN allow us to find a range of values BETWEEN two values
SELECT * FROM EmployeeTerritories
WHERE TerritoryID BETWEEN 06800 AND 09999

-- What are the names and product IDs of the products with a unit price below 5.00?
SELECT p.ProductName, p.ProductID
FROM Products p
WHERE p.UnitPrice < 5.00

-- Which categories have a category name with initials beginning with B or S
SELECT c.CategoryName, c.Description
FROM Categories c 
WHERE c.CategoryName LIKE 'B%' OR c.CategoryName LIKE 'S%'

SELECT c.CategoryName
FROM Categories c
WHERE c.CategoryName LIKE '[BS]%'

-- How many orders are there for employeeIDs 5 and 7 (the total for both)
SELECT Count(o.EmployeeID)
FROM Orders o
WHERE o.EmployeeID = 5 OR o.EmployeeID = 7

-- GROUP BY groups the data based on the employee ID in this example - [Employee ID] - [Amount of Orders]
SELECT o.EmployeeID, Count(o.EmployeeID) AS "Count of orders placed by Employees 5 and 7"
FROM Orders o
WHERE EmployeeID IN (5, 7)
GROUP BY o.EmployeeID

SELECT * FROM Categories
SELECT * FROM Orders

SELECT Count(*) 
FROM Orders o 

-- Concatenate two different table values into one with an Alias applied by AS
SELECT CompanyName + ' Contactable at ' + Phone  AS "Company Info", City +',' + Country AS "City"
FROM Customers

SElECT c.CompanyName AS "Company Name",
CONCAT(c.City, ', ',c.Country) AS "City"
FROM Customers c

SELECT * FROM Customers

-- Write a SELECT using the employees table and concat first and last name
SELECT CONCAT(e.FirstName, ' ' ,e.LastName) AS "Employee Name"
FROM Employees e

-- In order to filter based on NULL simply use IS NULL or IS NOT NULL

SELECT c.CompanyName AS "Company Name", City + ',' + Country AS 'City'
FROM Customers c
WHERE c.Region IS NOT NULL

SELECT * FROM Region 
SELECT * FROM Customers

-- Write a select statement to list six countries that have region codes in the customers table

SELECT DISTINCT CONCAT('Country: ', c.Country, ' AND Region: ', c.Region) AS "Countries with Region"
FROM Customers c
WHERE Region IS NOT NULL

-- Apples-->Price-->2pounds, quanity = 10, discount-25%
-- Gross Total (The cost apple excluding the discount)
-- Net total (The amount I pay the shopkeer is at the end) = (25/100) * 20 = £5.00 (Discount) / Net Amount = (£20.00 - £5.00)

-- HERE we are working out the Gross (discount amount) and Net (Amount without Discount) Totals
-- We also added ROUND (..., 2) which rounds the numbers after the point to 2 numbers.

-- USE ORDER BY to identify the two (TOP 2) HIGHEST NET TOTAL - identify two highest total (added od.OrderID into the SELECT)
SELECT od.UnitPrice, od.Quantity, od.Discount, od.OrderID,
od.UnitPrice*od.Quantity AS "Gross Total",
ROUND((od.UnitPrice*od.Quantity) - (od.UnitPrice * od.Discount * od.Quantity), 2)  AS "Net Total"
FROM [Order Details] od 
ORDER BY [Net Total] DESC

SELECT TOP 2 od.UnitPrice, od.Quantity, od.Discount, od.OrderID,
od.UnitPrice*od.Quantity AS "Gross Total",
ROUND((od.UnitPrice*od.Quantity) - (od.UnitPrice * od.Discount * od.Quantity), 2)  AS "Net Total"
FROM [Order Details] od 
ORDER BY [Net Total] DESC

-- STRING FUNCTIONS
SELECT e.FirstName, CHARINDEX('a', e.FirstName) AS "Position of Character"
FROM Employees e

-- RETURNS the index of the letter a if it is in a string, otherwise it returns 0
-- INDEXS START 1 in SQL NOT 0

SELECT e.FirstName, SUBSTRING(e.FirstName, 1, 3) AS "Extracted String"
FROM Employees e

-- RETURNS THE 1ST to 3RD CHARACTER

SELECT e.FirstName, RIGHT(e.FirstName, 2) AS 'Extracted String'
FROM Employees e 

-- RETURNS last two characters of a string

SELECT e.FirstName, LEFT(e.FirstName, 2) AS 'Extracted String'
FROM Employees e 

-- RETURNS first two characters

SELECT e.FirstName, RTRIM(e.firstName) AS 'Trimmed String'
FROM Employees e 

-- REMOVES white spaces from start of string

SELECT e.FirstName, LTRIM(e.firstName) AS 'Trimmed String'
FROM Employees e 

-- REMOVE white spaces from end of string

SELECT e.FirstName, REPLACE(e.firstName, 'a', '!') AS 'Replaced String'
FROM Employees e

-- REPLACE the letter 'a' with the '!' symbol

SELECT e.FirstName, LEN(e.firstName) AS 'Length of String' 
FROM Employees e 

-- RETURNS the length of a string (counts white spaces)

SELECT e.Firstname, UPPER(e.FirstName) AS 'Upper Case Conversion', LOWER(e.FirstName) AS 'Lower Case Conversion'
FROM Employees e

-- RETURNS THE UPPER CASE AND LOWER CASE VERSION OF A TABLES CONTENT (STRING ONLY)





-- NESTED FUNCTIONS IN SQL
-- Finds the Postal code, scans it until it encounters a blank space, it then minuses one of that to get 
-- the index of the character before that blank space.
SELECT PostalCode "Post Code",
LEFT(PostalCode, CHARINDEX(' ', PostalCode)-1) AS "Post Code Region",
    CHARINDEX(' ', PostalCode) AS "Space Found", Country 
FROM Customers 
WHERE Country = 'UK'

-- USE charindex to list only product names that contain a single quote
SELECT p.ProductName "Product Names",
CHARINDEX('''',p.ProductName) AS "Index of Quote"
FROM Products p 
WHERE CHARINDEX('''',p.ProductName) > 0

SELECT p.ProductName
FROM Products p
WHERE p.ProductName LIKE '%''%'

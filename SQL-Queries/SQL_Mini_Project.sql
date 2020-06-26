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
-- (ANSWER) Northern, Easteen and Western
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
HAVING ROUND(SUM(od.Quantity * UnitPrice), 2)  > 1000000

-- 1.7	Count how many Orders have a Freight amount greater than 100.00 and either USA or UK as Ship Country. 
-- (ANSWER) 187

SELECT * FROM Orders

SELECT Count(o.orderID) AS "Frieght Greater than 100.00"
FROM Orders o 
WHERE o.Freight > 100.000

-- 1.8	Write an SQL Statement to identify the Order Number of the Order with the highest amount(value) of discount 
-- applied to that order.
-- (Answer) = 10353 and 103372

SELECT * FROM [Order Details]
SELECT * FROM Orders

-- 25% of £20 is £5, therefore the item is £15
SELECT od.OrderID, od.UnitPrice, od.Quantity, od.Discount, 
(od.UnitPrice * od.Discount * od.Quantity) AS "Total Discount" 
FROM [Order Details] od
ORDER BY [Total Discount] DESC

-- 2.1 Write the correct SQL statement to create the following table:
-- Spartans Table – include details about all the Spartans on this course. 
-- Separate Title, First Name and Last Name into separate columns, and include University attended, course taken and mark achieved. 
-- Add any other columns you feel would be appropriate. DO NOT INCLUDE DATEOFBIRTH
-- 2.2 Write SQL statements to add the details of the Spartans in your course to the table you have created.	
CREATE DATABASE Mini_projectDB_John

USE Mini_projectDB_John

DROP TABLE [Spartans];

SELECT * FROM Spartans

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


INSERT INTO Spartans([Title],[FirstName],[Surname],[University],[Course],[Mark]) VALUES('Mrs.','Georgina','Bartlett','Newcastle University','Archaeology','2:1'),('Mr.','Humza','Malak','University of Kent','Computing with Games Development','2:2'),('Mr.','Ibrahim','Bocus','University of Leicester','Computer Science','2:1'),('Mr.','Bari','Allali','Lancaster University','Business Economics','2:2'),('Mr.','Nola','Alston','University of Warwick','International Business & Management','3:3'),('Dr.','Aspen','Reed','University of Leicester','Computing with Games Development','3:3'),('Ms.','Ezekiel','Espinoza','University of Greenwich','Product Design','2:2'),('Mr.','Aretha','Berry','Newcastle University','Aerospace Engineering','1:1'),('Dr.','Ivan','Harrell','Edinburgh','Computing with Games Development','2:1'),('Mrs.','Sydnee','Evans','Aston University','International Business & Management','2:2');
INSERT INTO Spartans([Title],[FirstName],[Surname],[University],[Course],[Mark]) VALUES('Dr.','Molly','Spencer','University of Leicester','International Business & Management','3:3'),('Ms.','Omar','Morton','University of Kent','Ancient History','1:1'),('Mrs.','Jackson','Blair','University of Warwick','Modern Languages','2:2'),('Dr.','Emi','Ramirez','University of Nottingham','Philosophy and Economics','1:1'),('Mr.','Imogene','Cooley','Aston University','Aerospace Engineering','2:2'),('Mrs.','Demetria','Schneider','Edinburgh','International Business & Management','2:2'),('Dr.','Lunea','Salazar','University of Warwick','Aerospace Engineering','2:2'),('Ms.','Liberty','Tran','University of Birmingham','Computing with Games Development','1:1'),('Ms.','Alexandra','Vasquez','Edinburgh','Philosophy and Economics','3:3'),('Mrs.','Wesley','Herrera','Brunel University London','Computer Science','3:3');
INSERT INTO Spartans([Title],[FirstName],[Surname],[University],[Course],[Mark]) VALUES('Mr.','Mara','Glover','Lancaster University','Aerospace Engineering','2:2'),('Mrs.','Lucius','Chen','University of Leicester','Computing with Games Development','3:3'),('Mr.','Jamalia','Lott','University of Leicester','Computing with Games Development','2:2'),('Mr.','Murphy','Mcmahon','Brunel University London','Mechanical Engineering','1:1'),('Dr.','Ginger','Bishop','University of Birmingham','Archaeology','3:3'),('Mrs.','Colette','Swanson','Newcastle University','Aerospace Engineering','1:1'),('Mrs.','Reece','Russell','University of Leicester','Philosophy and Economics','1:1'),('Mrs.','Todd','Booth','University of Greenwich','Computer Science','3:3'),('Mr.','Colby','Chan','University of Birmingham','Archaeology','1:1'),('Mr.','Macey','Nichols','University of Kent','Product Design','2:2');
INSERT INTO Spartans([Title],[FirstName],[Surname],[University],[Course],[Mark]) VALUES('Mrs.','Buffy','Moody','Brunel University London','Product Design','3:3'),('Mrs.','Emmanuel','Terry','University of Greenwich','Mechanical Engineering','1:1'),('Mr.','Brett','Rich','Brunel University London','Modern Languages','2:2'),('Mr.','Bert','Casey','Newcastle University','Mechanical Engineering','3:3'),('Dr.','Emery','Parrish','Edinburgh','International Business & Management','3:3'),('Mr.','Tatiana','Sharpe','Brunel University London','Mechanical Engineering','3:3'),('Mrs.','Hadassah','Sutton','Aston University','Archaeology','1:1'),('Dr.','Barrett','Cohen','University of Leicester','Communications and Media Studies','2:1'),('Mrs.','Levi','Acosta','University of Kent','Computing with Games Development','2:2'),('Mrs.','Asher','Rodgers','Edinburgh','Aerospace Engineering','3:3');
INSERT INTO Spartans([Title],[FirstName],[Surname],[University],[Course],[Mark]) VALUES('Mrs.','Michelle','Sykes','University of Birmingham','Aerospace Engineering','3:3'),('Dr.','Lunea','Smith','University of Hertfordshire','Archaeology','2:2'),('Ms.','Cleo','Valencia','Brunel University London','Ancient History','2:2'),('Ms.','Summer','Daniel','Edinburgh','Product Design','2:1'),('Mr.','Jeanette','Morales','University of Nottingham','Mechanical Engineering','3:3'),('Mrs.','Christen','Levy','University of Leicester','Archaeology','1:1'),('Ms.','Merritt','Howell','University of Nottingham','Business Economics','2:2'),('Mr.','Camille','Whitehead','University of Hertfordshire','Product Design','2:1'),('Mr.','Giacomo','Avery','Aston University','Philosophy and Economics','3:3'),('Mrs.','Stuart','Bowers','University of Warwick','Philosophy and Economics','2:1');
INSERT INTO Spartans([Title],[FirstName],[Surname],[University],[Course],[Mark]) VALUES('Mr.','India','Zamora','Newcastle University','Computer Science','2:1'),('Mr.','Sara','Wilcox','University of Warwick','Aerospace Engineering','2:2'),('Mr.','Sharon','Frederick','Aston University','Computing with Games Development','3:3'),('Mr.','Octavia','Tillman','University of Leicester','Archaeology','3:3'),('Dr.','Kaye','Barrera','University of Kent','International Business & Management','3:3'),('Mr.','Jane','Gomez','University of Birmingham','International Business & Management','2:1'),('Ms.','Larissa','Fitzgerald','University of Hertfordshire','Mechanical Engineering','3:3'),('Dr.','Oren','Becker','University of Hertfordshire','Mechanical Engineering','2:2'),('Ms.','Faith','Joyce','Edinburgh','Aerospace Engineering','3:3'),('Mr.','Kiara','Everett','Lancaster University','Aerospace Engineering','2:2');
INSERT INTO Spartans([Title],[FirstName],[Surname],[University],[Course],[Mark]) VALUES('Mr.','Kenyon','Nguyen','Newcastle University','Aerospace Engineering','1:1'),('Ms.','Victor','Murray','University of Hertfordshire','Communications and Media Studies','2:1'),('Mrs.','Nevada','Gibson','Lancaster University','Business Economics','1:1'),('Dr.','Mara','Rose','Newcastle University','Computer Science','2:2'),('Ms.','Hunter','Silva','University of Greenwich','Aerospace Engineering','2:1'),('Ms.','Amena','Zamora','University of Nottingham','Business Economics','2:1'),('Ms.','Paloma','Ellison','Edinburgh','Modern Languages','2:1'),('Dr.','Chaney','Larson','University of Birmingham','Business Economics','3:3'),('Dr.','Freya','Faulkner','Aston University','International Business & Management','3:3'),('Mr.','Ciaran','Oneill','Brunel University London','Archaeology','2:1');
INSERT INTO Spartans([Title],[FirstName],[Surname],[University],[Course],[Mark]) VALUES('Mr.','Leonard','Logan','Lancaster University','Aerospace Engineering','2:2'),('Ms.','Galena','Cleveland','University of Brighton','Modern Languages','3:3'),('Ms.','Clinton','Murphy','University of Birmingham','Archaeology','3:3'),('Ms.','Hope','Grant','University of Leicester','Philosophy and Economics','1:1'),('Mr.','Mollie','Marsh','University of Kent','Computer Science','1:1'),('Dr.','Nomlanga','Mendez','University of Hertfordshire','Computing with Games Development','2:1'),('Dr.','Danielle','Meyer','Lancaster University','Philosophy and Economics','1:1'),('Dr.','Oscar','Norman','University of Birmingham','Mechanical Engineering','2:2'),('Dr.','Quemby','Roberts','Brunel University London','Computer Science','1:1'),('Mrs.','Nasim','Holman','University of Warwick','Product Design','3:3');
INSERT INTO Spartans([Title],[FirstName],[Surname],[University],[Course],[Mark]) VALUES('Dr.','Blythe','Sharp','University of Leicester','Product Design','1:1'),('Mr.','Anthony','Norton','Newcastle University','Communications and Media Studies','3:3'),('Mrs.','Cleo','Reilly','Lancaster University','Archaeology','2:1'),('Mrs.','Tobias','David','University of Leicester','Politics and International Studies','2:2'),('Mr.','Isabelle','Mcgee','University of Hertfordshire','Philosophy and Economics','2:2'),('Ms.','Summer','Holder','University of Brighton','Computer Science','2:2'),('Ms.','Jasmine','Roberts','University of Kent','Computer Science','2:1'),('Mrs.','Mohammad','Joyce','Lancaster University','Mechanical Engineering','2:2'),('Mrs.','Britanney','Powell','University of Leicester','Ancient History','1:1'),('Mrs.','Candace','Gaines','Newcastle University','Communications and Media Studies','2:1');
INSERT INTO Spartans([Title],[FirstName],[Surname],[University],[Course],[Mark]) VALUES('Mr.','Quentin','Cantu','Edinburgh','Philosophy and Economics','2:1'),('Mrs.','Dai','Tyson','University of Nottingham','Computer Science','2:1'),('Dr.','Leonard','Barrera','Aston University','Ancient History','2:2'),('Dr.','Kasper','Roach','University of Leicester','Archaeology','2:1'),('Mr.','Dylan','Mccray','University of Kent','Communications and Media Studies','2:1'),('Ms.','Athena','Hooper','Aston University','Aerospace Engineering','1:1'),('Dr.','Aladdin','Neal','Newcastle University','Product Design','2:1'),('Mrs.','Randall','Martinez','Aston University','Product Design','2:2'),('Dr.','Acton','Dixon','University of Brighton','Philosophy and Economics','1:1'),('Dr.','Sarah','Bryan','University of Greenwich','Philosophy and Economics','2:1');

SELECT * FROM Spartans

-- 3.1 List all Employees from the Employees table and who they report to. No Excel required.

SELECT * FROM Employees
SP_HELP Employees

SELECT * 
FROM Employees e
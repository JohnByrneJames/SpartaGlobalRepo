/* Weekend Exercises 
    - https://www.w3resource.com/mysql-exercises/northwind/products-table-exercises/

*/

USE Northwind

-- 1. Write a query to get a Product Name and quantity/Unit 

SELECT p.ProductName, p.QuantityPerUnit
FROM Products p

-- 2. Write a query to get current product list (product ID and Name)

SELECT p.ProductID, p.ProductName
FROM Products p

-- 3. Write a query to get Product list (id, name, unit price) where products cost between $15 and $25

SELECT p.ProductID, p.ProductName, p.UnitPrice
FROM Products p
WHERE p.UnitPrice BETWEEN 15 AND 25
ORDER BY p.UnitPrice DESC

-- 4. Write a query to get Product list (name, unit price) of above average price. 

SELECT DISTINCT p.ProductName, p.UnitPrice
FROM Products p 
WHERE UnitPrice > (SELECT AVG(UnitPrice) FROM Products)
ORDER BY UnitPrice

-- 5. Write a query to get Product list (name, unit price) of ten most expensive products. 

SELECT TOP 20 p.ProductName, p.UnitPrice
FROM Products p 
ORDER BY p.UnitPrice DESC

-- 6. Write a query to show discontinued and continued items in a COUNT

SELECT COUNT(p.ProductID) AS "Products"
FROM Products p 
GROUP BY p.Discontinued

SELECT * FROM [Order Details]
WHERE [Order Details].Quantity > 100

-- List products with order quantities greater than 100. 

SELECT p.ProductName
FROM Products p
WHERE p.ProductID IN (SELECT od.ProductId 
                    FROM [Order Details] od
                   WHERE od.Quantity > 100)

-- 
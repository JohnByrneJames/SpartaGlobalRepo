###### Sparta Global Training Day 9
###### Continuing with SQL and presenting on `GROUP BY` and `HAVING`
___

> 9:00 AM - Daily Stand Up **[Morning meetup]**

Things that I enjoyed from yesterday as well as the blockers from yesterday.

**Enjoy** ... <br> 
I enjoyed learning about the wildcards **%** and **_** as they are useful 
for finding data based on a set of conditions and not exact search terms. I can see how 
this would be useful in industry whilst doing querying.

**Blockers** ... <br>
Need to go over some `DELETE CASCADE` a little more as well as 
go over **DDL**, **DML**, **DCL** and **TCL**. I need to know the **DDL** and **DML** off by 
heart so that in the future I can easily serve that information if ever asked in the future.

**Graduation Presentation**... <br>
At the end of the graduation at Sparta Global there will be a presentation given to 
all of Sparta Global, Sales Team and students. **PREPARE** and research their interests and 
technology they are using.

* **Date Functions**

**GETDATE** - `SELECT GETDATE()` to return the current date and time 

**SYSDATETIME** -  `SELECT SYSDATETIME()` to return the date and time of the computer being used

**DATEADD** `DATEADD(d, 5, OrderDate) AS "Due Date"` to add 5 days. 
The `d` extracts todays date and adds the 5.

**DATEDIFF** `DATEDIFF(d, OrderDate, ShippedDate) AS "Ship Time"` to calculate difference between dates

**YEAR** `SELECT YEAR(OrderDate) AS "Order year"` to extract the year from a date

**MONTH** `SELECT MONTH(OrderDate) AS "Order Month"` to extract the month from a date

**DAY** `SELECT DAY(OrderDate) AS "Order Day"` to extract the day from a date

**d** = `day`, **m** = `month` and **y** = `year` <br>

_• **DATEADD** has 3 arguments, `d` or `dd` means day, `m` or `mm` months, `yy` or `yyyy` year, the date to be added to and how many 
units to add_ <br>
```sql
SELECT DATEADD(d, 5, OrderDate) AS "Due Date",
    DATEDIFF(d,OrderDate, ShippedDate) AS "Ship Days"
FROM Orders
```

_• Working out the age of everyone in the employees table, also try to figure out months, days too._ <br>
```sql
SELECT CONCAT(e.EmployeeID, ', ', e.FirstName,' ', e.LastName) AS "Employee",
CONCAT(DATEDIFF(yyyy, e.BirthDate, GETDATE()), '.',
DATEDIFF(mm, e.BirthDate, GETDATE()), '.', 
DATEDIFF(d, e.BirthDate, GETDATE())) AS "Year.Month.Days"
FROM Employees e
```

* **CASE**

A `CASE` statement can be useful when you need varying results output based on different data. 
Pay close attention to `WHEN` `THEN` `ELSE` and `END`. Use single quotes for data and double quotes 
for column aliases.

* **Aggregate Functions**

The following aggregate functions can be used to calculate totals usually in conjunction with `GROUP BY` clause.

_• **Aggregate Functions** can be used be used with a `GROUP BY`, but without a `GROUP BY` 
you get one row (total) as a result. IF you use an aggregate function in a select statement, 
all other columns must either be an aggregate or in the `GROUP BY` clause._ <br>
 
* **SUM** - `SUM(OrderTotal)` for the grand total of a column for all rows selected 

* **AVG** - `AVG(UnitPrice)` for the average of a column for all rows selected

* **MIN** - `MIN(UnitPrice)` for the smallest value in a column for all rows selected

* **MAX** - `MAX(UnitPrice)` for the largest value in a column for all rows selected 

* **COUNT** - `COUNT(*)` for the number of NOT NULL rows selected. If * is used all rows are counted.
 
_• This finds the `SUM` `AVG` `MIN` and `MAX` for each supplier and adding a group, will show all the suppliers 
grouped by their ID, essentially categorising the results based on the supplier._ <br>
```sql
SELECT SUM(p.UnitsOnOrder) AS "Total on Order",
    AVG(p.UnitsOnOrder) AS "Avg On Order",
    MIN(p.UnitsOnOrder) AS "Min On Order",
    MAX(p.UnitsOnOrder) AS "Max On Order"
FROM Products p
GROUP BY supplierID
```
 
_•Use `GROUP BY` to calculate the average reorder level for all products by CategoryID.
Remember the `SELECT` clause must match the `GROUP BY` clause apart from any aggregates.
You need to make sure you actually `ORDER BY` with the same as what has been selected, and only 
order by the reorder otherwise it won't show the average._ <br>
```sql
SELECT
AVG(p.ReorderLevel) AS "Average Reorder Level"
FROM Products p 
GROUP BY p.CategoryID
ORDER BY AVG(p.ReorderLevel) DESC 
```
_• `HAVING` is used instead of `WHERE` when filtering on subtotals/ grouped data.
Columns aliases cannot be used in the `HAVING` clause. Aggregate functions are not 
available for use in the `WHERE` clause due to the SQL processing sequence._

```sql 
SELECT SupplierID,
SUM(UnitsOnOrder) AS "Total On Order",
    AVG(UnitsOnOrder) AS "Avg On Order"
FROM Products 
GROUP BY SupplierID 
HAVING AVG(UnitsOnOrder) > 5
```

* **LOGICAL** (syntax) Sequence

1. **SELECT** <br>
2. **WHERE** <br>
3. **GROUP BY** <br>
4. **HAVING** <br>
5. **SELECT** <br>
6. **DISTINCT** <br>
7. **ORDER BY** 

:star: **Edgar F.Codd** is the one who coined the term relational database :star:

___

> 2:00 PM - Presentation, continuation with SQL  **[Afernoon]**

We presented the `GROUP BY` and `HAVING` clauses to the class. It went well
however when we presented we tried to involve the audience we should have tried 
to involve the audience as much as possible and ask them if they want to move on ECT, 
question people in the class if they understand to reinforce the information. 

* **GROUP BY**

Its a key word that will categorise the same values in the column. 

Its often used with a aggregate functions ( `COUNT`, `MAX`, `MIN`, `SUM`, `AVG` )
to group the result-set by one or more columns.

You can also use `GROUP BY` in conjunction with `ORDER BY`


_• Using the Northwind database, list the number of customers in each country using the
`GROUP BY` function._ <br>

```sql
SELECT COUNT (c.CustomerID) AS "Number of people living in the country", c.Country
FROM Customers c
GROUP BY c.Country
```

_• Using your Northwind database, list the number of customers in each country sorted high to low
 function._ <br>
 
```sql
SELECT COUNT (c.CustomerID) AS "Number of people living in the country", c.Country
FROM Customers c
GROUP BY c.Country
ORDER BY COUNT(c.CustomerID) DESC
```

* **HAVING**

It is an alternative to the `WHERE` clause and was added to work
with aggregate functions. `WHILE` is only used to `SELECT` queries, which contain aggregate 
functions or `GROUP BY` which is correct.

`HAVING` clause is used to filter summarized data or grouped data in SQL to use with or 
without the `GROUP BY` function. In `GROUP BY` the logical execution sequence means it executes 
before the `HAVING` clause.

_• Using your Northwind database, list the number of customers in each country using the `GROUP BY` clause. 
Only include countries with more than 10 customers using the `HAVING` clause._ <br>
```sql 
SELECT COUNT(c.CustomerID), c.Country 
FROM Customers c
GROUP BY c.Country
HAVING COUNT(c.CustomerID) < 10
```

_•Using the Northwind database list the number of customers in each country (`GROUP BY`), except the USA (`WHERE`) sorted high to low (`DESC)` and only include countries with 9 more customers (`HAVING`)._ <br>
```sql 
SELECT COUNT(c.CustomerID), Country 
    FROM Customers c
    WHERE Country <> 'USA'
    GROUP BY Country
HAVING COUNT(c.CustomerID) >= 9
    ORDER BY COUNT(c.CustomerID) DESC
```



---
**Homework**

* Exercises in the Northwind database as it is good practice, exercise and solutions.

**[W3Schools Northwind Exercises](https://www.w3resource.com/mysql-exercises/northwind/products-table-exercises/)**

* SQL Online Test at TESTDOME

**[TESTDOME SQL Test](https://www.testdome.com/tests/sql-online-test/12)**

* SQL test that has a small certificate

**[W3Schools Quiz](https://www.w3schools.com/quiztest/quiztest.asp?qtest=SQL)**


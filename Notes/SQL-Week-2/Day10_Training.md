###### Sparta Global Training Day 10
###### Continuing with SQL and presenting on `GROUP BY` and `HAVING`
___

> 9:00 AM - Daily Stand Up **[Morning meetup]**

**Bockers**... and what I **enjoyed** about the day yesterday. I actually really enjoyed yesterday 
although I am still not fully in an understanding of **`JOINS`** and I think that it is the only
thing I don't really get so I am gonna spend a large part of my weekend going over that. 

**Presentation Re-watch** :
- I need to fix my posture
- I need to look at the screen before interacting with the audience and try to get them involved 
as it can be a little boring otherwise.
- I need to speak in less of a monotone voice as it sometimes can dull down the enthusiasm I have for 
a topic. I need to add more power words into the presentation as it can help you present yourself in 
a positive light.

I am looking forward to the rest of today...

**Exercise** from yesterday.

_List Orders from the Orders table and `JOIN` to the Customers and Employees table to include 
Customer Name (Company Name) and Employee Name (First and Last Name). From the Orders table, include OrderID, OrderDate
and Freight._ <br>

```sql
SELECT o.OrderID, o.OrderDate, o.Freight, CONCAT(e.firstName, ' ', e.LastName) AS "Employee Name"
FROM Customers c 
INNER JOIN Orders o ON o.CustomerID = c.CustomerID
INNER JOIN Employees e ON o.EmployeeID = e.EmployeeID
```

**Formatting Date and Time**

Prior to SQL Server 2012 `CONVERT` was used to format dates 

IN 2020 `FORMAT()` was introduced to make it easier.

**[Time Formats and Code on W3 Schools.](https://www.w3schools.com/sql/func_sqlserver_convert.asp)**

**[SQL Server FORMATS with examples](https://www.mssqltips.com/sqlservertip/2655/format-sql-server-dates-with-format-function/)**

_The 103 is code for time standard in British/France_ <br>
```sql 
SELECT OrderID, CONVERT(VARCHAR(10), OrderDate, 103) AS [dd/MM/yyyy]
FROM Orders
```

```sql 
SELECT orderID, FORMAT(OrderDate, 'dd/MM/yyyy')
```

* **Sub Queries**

This is an example of subquery in the `WHERE` clause, check to see which customers 
have not place any orders. This could also be achieving `JOINS`

```sql 
SELECT CompanyName AS "Customer"
FROM Customers 
WHERE CustomerID NOT IN 
    (SELECT CustomerID FROM Orders)
```

_Same Problem as above but using a `JOIN` this can only be accomplished using 
an outer `JOIN` like the `FULL`, `LEFT` and `RIGHT`._

```sql 
SELECT c.CompanyName AS "Customer"
FROM Customers c 
LEFT JOIN Orders o ON c.CustomerID = o.CustomerID
WHERE o.CustomerID IS NULL
```

_This is an example of a nested subquery in the `SELECT` clause (acts like a column). 
Subqueries must be contained by parenthesis (excluding any alias). Outputs the highest price in the table 
on every row in the result set._

_This is useful because it allows use of aggregate functions alongside normal columns. The 
inner query is executed first then the outer query._

```sql 
SELECT OrderID, ProductID, UnitPrice, Quantity, Discount,
    (SELECT MAX(UnitPrice) FROM [Order Details] od) AS "Max Price"
FROM [Order Details]
```

_Although this example is out of the scope of the exam, it is a good example 
of inline view (`SELECT` in the `FROM` clause: acts like a table). The inline sq1 calculates 
the total for each product which is used to calculate percent of total. This is quite an advanced query._

```sql 
SELECT od.ProductID, sq1.totalamt AS "Total Sold for this Product",
od.UnitPrice, (UnitPrice * quantity)/sq1.totalamt * 100 AS "% of Total"
    FROM [Order Details] od 
    INNER JOIN 
        (SELECT o.ProductID, SUM(o.UnitPrice *o.Quantity) AS totalamt 
        FROM [Order Details] o
        GROUP BY o.ProductID ) sq1 ON sq1.ProductID=od.ProductID
```

**Exercise** <br>
_Using a subquery in `WHERE` clause, list all Orders (Order ID, Product ID, Unit Price, Quantity 
 and Discount) from the [Order Details] table `WHERE` the product has been discontinued. Repeated with more joins._

_SubQuery Version_ <br>
```sql
SELECT od.OrderID, od.productID, od.UnitPrice, od.Quantity, od.Discount 
FROM [Order Details] od 
WHERE od.ProductID IN (SELECT p.ProductID FROM Products p WHERE p.Discontinued = 1)
```

_`JOIN` Version_ <br>
```sql
SELECT od.OrderID, od.ProductID, od.UnitPrice, od.Quantity, od.Discount, p.Discontinued
FROM Products p 
INNER JOIN [Order Details] od ON p.ProductID = od.ProductID
WHERE p.Discontinued = 1
```

* **UNION / UNION ALL**

**`UNION`** operator is used to combine the result-set of two more more `SELECT` statements. 
* Each `SELECT` statement within `UNION` must have the same number of columns 
* The columns  must also have similar data types 
* The columns in each `SELECT` statement must also be in the same order.

_This is a contrived example, show how you could list all employee IDs in the same column as all supplier IDs._ <br>
_`UNION ALL` returns 38 rows, `UNION` remove any duplicates and returns 29 rows._<br>
_Both `SELECT` statements must have the sam number of columns in the `SELECT` clause (same type). Only the column alias in the first_
_`SELECT` will be applied. `ORDER BY` 1 may be more appropriate if column names differ_

_**DOES NOT** support duplicates._
```sql 
SELECT EmployeeID AS "Employee/Supplier"
FROM Employees 
UNION 
SELECT SupplierID 
FROM Suppliers
```

_**DOES** support duplicates._<br>
```sql 
SELECT EmployeeID AS "Employee/Supplier"
FROM Employees 
UNION ALL
SELECT SupplierID 
FROM Suppliers
```

**[Very Useful Extensions to visualise data](https://docs.microsoft.com/en-us/sql/azure-data-studio/sanddance-extension?view=sql-server-ver15)**

**Mock Test after Break** - **Marked by partner**

**Mock Test** 

>**Mock Test - Questions, Answers and Feedback** [HERE](/SQL-Queries/Mock_Exam_Day10.sql)

>**SELECT Queries SQL Sheet** [HERE](/SQL-Queries/Mock_Exam_Day10.sql)

**One-to-One** with Sharukh<br>

**Agenda**
- We will time-box our meeting for 10 minutes
- Please take notes, as you will be expect to email us the summary of our conversations...
- How did you think this week went?
> **"** This week went very well for myself, it was constructive, informative and over all allowed us to 
>go through the information in a orderly fashion with the all important practical examples which drill the information
>that much more into your head. Astha is a really good teacher, she is calm, collected and always willing to help 
>anyone who thinks they do not understand what is needed to be done. At the time I felt like the course was going at a speed I 
>couldn't quite keep up with, but with my new 'Determined' and 'Successful' mind-set I managed to spend a good amount of time going 
>over each concept that I did not fully understand, this was displayed on the last day when I was breezing through the questions on the Mock-exam.  
>As for the weekend I will spend it going over SQL topics I am still not fully comfortable with such as `JOINS`,
>`CASE SELECT` and SubQueries.**"**
- From the behavioural competencies one competencies do you think you are excelling and which competencies you need to work one?
> **"** Like last week I think I am becoming more determined that I have ever been and really want to finish this course, with the best 
>possible outcome, therefore I am putting everything I have into making sure I have my notes formatted and uploaded by the end of the day 
>and pushing them to GitHub for easy access from any of my devices. I think I am improving on critical thinking and the way I convey
>information to my peers and supervisors but I still need to practice it a lot more, also I think my presentation skills need a lot 
>of work. This can only be achieved through presenting multiple times which I hope I will be doing many more times in the coming weeks. **"**
- One thing to start doing? 
> **"** Thinking about the way I formulate information and pass and receive information. Sometimes I find it hard to articulate questions 
>or a point I want to get across to others. **"**
- One thing to stop doing? 
> **"** Work on my presentation in the class, I was told that I have been laughing too much - therefore I will try to 
>dull it down but I refuse to look miserable all the time as I am enjoying the course and getting to know people so I want to express 
>my happiness towards that.**"**
- One thing to continue?
> **"** Keep up with the note-taking and interaction that I am giving in the classroom, clearly it is working as I have had a lot of positive 
>feedback from both Astha and Sharukh about my behaviour and involvement in the class **"**

* **Positive feedback** <br>
 > **"** Happy with performance throughout the class, able to keep up with everything and 
 ask questions whenever is needed, not afraid to admit when don't know something either. Overall am happy with
 progress so far...**"**

* **Constructive feedback** <br>
> **"** Do not Laugh during class... and do not eat (I have not eaten during class). It is 
 important to remain professional throughout the day and whenever you are learning as the classes are recorded and can be 
 viewed by anyone anytime from outside the class, as well as from people who join whilst we are having the class too. Before
 answering a question in the future make sure you read through the question twice before answering it, this way you 
 are less likely to miss information.**"**

Thanks for the feedback I will take everything into consideration for sure and am looking forward to the next week. 

___ 
**Homework**
* Go over `CASE` statements - `END` `WHEN` `ELSE` `THEN`

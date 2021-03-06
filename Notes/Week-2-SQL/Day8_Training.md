###### Sparta Global Training Day 8
###### Continuing with SQL...
___

> 9:00 AM - Daily Stand Up **[Morning meetup]**

Stand up and blockers for yesterday. I **enjoyed** learning about the types of data 
control you can have in a database, I have done **SQL** before but still was learning bits
here and there throughout the day. Think the best part was learning about **Normal Form** as I 
find it quite an interesting topic. In my course we went to **4NF** so its good to see how others teach it.

**No Blockers...**

> **"** We did our Trello Board and added all of yesterday DONE tasks and stuff for this weeks
>sprint. **"**


* **ON DELETE CASCADE**

This is a constraint that can be added to foreign key columns in a table, this allows this foreign key to be deleted if its corresponding parent
key is deleting. This allows for data integrity as it clears all data connected means there won't be any data 
floating around with no connections. 

**An example** is if you `DELETE` `film_id` **1** from `film_table` it will `DELETE` all
the rows in the `director_table` which has that `film_id` (**1**) as a `FOREIGN KEY`.

* **ALTER** 
```sql
ALTER TABLE director
ADD CONSTRAINT foreign_key_onFilmId FOREIGN KEY (film_id)
REFERENCES film_table (film_id) ON DELETE CASCADE;
```

* **CREATE**
```sql
CREATE TABLE critics (
critic_id INT PRIMARY KEY IDENTITY,
critic_name VARCHAR(255) NOT NULL,
reputation VARCHAR(10) NOT NULL,
film_id INT NOT NULL,
FOREIGN KEY (film_id)
    REFERENCES film_table (film_id)
    ON DELETE CASCADE );
```
        

**SELECT CLAUSES**

- Demonstrate the ability to connect to a database and query it
- Write simple SQL statements to alter and add data
- Write simple queries to extract and compare data
- Demonstrate an ability to research and learn technical skills independently

**WHERE**

**WHERE** is used to filter data, city is a column in the customers table and you 
are asking it to find only the entries which contain **Paris** as the city.
 
```sql
SELECT * FROM Customers
WHERE City = 'Paris'
```

**Exercise**
* **Q** : How many employees have home city of London ?
* **A** : **4**
```sql
SELECT * FROM Employees
`WHERE City = 'London'`
```
* **A-Returns Count** 
```sql
SELECT COUNT(*) AS 'Employees living in London' FROM Employees
WHERE City = 'London'`
```
___

* **Q** : Which Employee is a Doctor ?
* **A** : Dr. **Andrew Fuller**
```sql
SELECT * FROM Employees
WHERE TitleOfCourtesy = 'Dr.'
```

* **A-Returns Count** : 
```sql
SELECT COUNT(*) AS "Number of employees with title doctor" FROM Employees
`WHERE TitleOfCourtesy = 'Dr.'
```
___

* **Q** : How many products are discontinued ?
* **A** : **8**
```sql
SELECT * FROM Products
WHERE Discontinued = 1
```
* **A-Returns Count** : 
```sql
SELECT COUNT(*) AS "Products that are discontinued" FROM Products
WHERE Discontinued = 1
```
___
 
___

> 11:00 AM - SQL SELECT CLAUSE and QUERIES **[Late-Morning]**
 
 
**TIP** - For coding games make sure you use double quotes **"** for 
strings after **`AS`** it is not as intelligent as the Azure Data Studio

An **Apostrophe** **'** is a Reserved character, what happens when querying the example below?

Placing two apostrophe in the location, will tell the SQL query that this is part of the string.

```sql
SELECT * FROM products WHERE ProductName = 'Anais''s'`
```

**Table Aliasing** is SO useful when querying a database as it can help avoid 
spelling mistakes and makes it a lot faster and easier.

```sql
SELECT c.CompanyName, c.City, c.Country, c.Region
FROM Customers c
WHERE c.Region = 'BC'
```

It can be useful to write the **FROM** part first as it will 
attach an alias `C` to the `Customers` table, this allows the `SELECT` part to suggest the 
columns after the point.

* **TOP**

**TOP** is quite useful as it can specify a specific amount of rows to select from a table, 
starting from the top. For example `TOP 100` will select 100 rows 
from that table.

```sql
SELECT TOP 100 CompanyName, City FROM Customers
WHERE Country = 'FRANCE'
```

* **AND** 

**AND** is a keyword that means all criterias in a condition need to met, for example:
```sql
Region = EU AND Age = 11
```
```sql
SELECT ProductName, UnitPrice FROM Products
Where CategoryID = 1 AND Discontinued = 0
```
* **OR**

**OR** is a keyword that means only one of multiple criteria have to meet 
the condition, for example:
```sql
Region = EU OR Age = 11
```
```sql
SELECT ProductName, UnitPrice FROM Products
WHERE CategoryID = 1 OR Discontinued = 0
```
* **Operators**

**<>** Or **!=** <br>
**<** Less than <br>
**>** More than <br>
**<=** Less than or equal to <br>
**>=** Greater than or equal to <br>

```sql
SELECT ProductName, UnitPrice FROM Products
WHERE UnitsInStock > 0 AND UnitPrice > 29.99
```

* **DISTINCT**

**DISTINCT** will remove duplicates from a `SELECT` CLAUSE and only return 
unique values. Return distinct values. `No Duplicates`

```sql
SELECT DISTINCT Country FROM Customers
WHERE ContactTitle = 'Owner'
```

* **WILDCARDS**

**Wildcards** can be usd as a substitute for any other character in a string when using 
the `LIKE` operator.
* **%** A substitute for zero or more characters
* **_** A substitute for a single character
* **[Charlist]** Sets the ranges of characters to match i.e. `LIKE` [ABC]% This will bring back anything starting with any of those letters.
* **[^Charlist]** Sets and ranges of characters that don't match i.e. `LIKE` [^ABC]% This will 
bring back anything that does not start with those letters.

_• Select anything ending with a_ <br>
```sql
SELECT DISTINCT c.Country
FROM Customers c WHERE Country LIKE '%a'
```

_• Countries starting with U, A or M_ <br>
```sql
SELECT DISTINCT c.Country
FROM Customers c WHERE Country LIKE '%[UAM]'
```

_• Countries NOT starting with U, A or M_
```sql
SELECT DISTINCT c.Country
FROM Customers c WHERE Country LIKE '%[^UAM]'
```

_• Countries which have a 3rd letter of A_<br>
```sql
SELECT DISTINCT c.Country
FROM Customers c WHERE Country LIKE '__A%'
```

**BREAK**
> 2:00 PM - SQL SELECT CLAUSE and QUERIES continued... **[Afternoon]**

* **IN**

**IN** is a simple keyword that will return results of something that occurs in a table, 
so for example `WHERE Region IN('WA','SP')` is the same as saying `WHERE Region = 'WA' OR Region = 'SP'`

_• Using the **IN** operator_<br>
```sql
SELECT * FROM Customers
WHERE Region IN ('WA','SP')
```

_• Using the **OR** operator_<br>
```sql
SELECT * FROM Customers
WHERE Region = 'WA' OR Region = 'SP'
```

_• Following the rules of **BIDMAS** brackets seperate operations_<br>
```sql
SELECT * FROM Customers
WHERE (Region = 'WA' OR Region = 'SP')
AND (Country = 'Brazil' OR Country = 'USA')
```

_• Instead **IN** is more efficient as it takes less syntax 
to do the same query_ <br>
```sql
SELECT * FROM Customers
WHERE Region IN('WA', 'SP') AND Country IN ('Brazil', 'USA')
```

* **BETWEEN**

The **BETWEEN** key word includes values between and as well as the boundary 
values, for example 1 - 10 would return 1 and 10 as well as any in between if they are 
in the database.

```sql
SELECT * FROM EmployeeTerritories
WHERE TerritoryID BETWEEN 06800 AND 09999
```

**exercise** Three Questions...

_• What are the names and product IDs of the product with a unit price below 5.00?_ <br>
```sql
SELECT p.ProductName, p.ProductID
FROM Products p
WHERE p.UnitPrice < 5.00
```

_• Which Categories have a category name with initials beginning with 'B' or 'S'?_ <br>
```sql
SELECT c.CategoryName, c.Description
FROM Categories c
WHERE c.CategoryName LIKE 'B%' OR c.CategoryName LIKE 'S%'
```

_Option 2_ <br>
```sql
SELECT c.CategoryName
FROM Categories c
WHERE c.CategoryName LIKE '[BS]%'
```

_• How many orders are there for employees 5 and 7? Display the total for both._ <br>
```sql
SELECT Count(o.EmployeeID)
FROM Orders o
WHERE o.EmployeeID = 5 OR o.EmployeeID = 7
```

_Option 2_ <br>
```sql
SELECT o.EmployeeID, Count(o.EmployeeID) AS "Count of orders placed by Employees 5 and 7"
FROM Orders o
WHERE EmployeeID IN (5, 7)
GROUP BY o.EmployeeID
```

* **CONCAT**

Concatenate using **+** along with single quotes. Add two strings, values 
together means to concatenate them. This is helpful to concatenate two pieces of information 
into a single column, for example the city and country.

```sql
SELECT CompanyName AS 'Company Name', City +',' + Country AS "City"
FROM Customers
```

_• This adds an additional Phone number with the company name for contacting them._ <br>
```sql
SELECT CompanyName + ' Contactable at ' + Phone  AS 'Company Info', City +',' + Country AS "City"
FROM Customers
```

_• This does the same thing but with the key word `CONCAT`_ <br>
```sql
SElECT c.CompanyName AS "Company Name",
CONCAT(c.City, ', ',c.Country) AS "City"
FROM Customers c
```

```sql
SELECT CONCAT(e.FirstName, ' ' ,e.LastName) AS "Employee Name"
FROM Employees e
```

* **IS**

**IS** is a special operator for dealing with **NULL** values. In order to filter based on NULLs 
simply use **IS NULL** or **IS NOT NULL**.

```sql
SELECT c.CompanyName AS "Company Name", City + ',' + Country AS 'City'
FROM Customers c
WHERE c.Region IS NOT NULL
```

```sql
SELECT c.CompanyName AS "Company Name", City + ',' + Country AS 'City'
FROM Customers c
WHERE c.Region IS NULL
```

_• Write a select statement to list six countries that have region codes in the customers table._ <br>
```sql
SELECT DISTINCT c.Country, c.Region
FROM Customers c
WHERE Region IS NOT NULL
```

* **Arithmetic** 

>**+** Addition (Can be used on DATETIME Columns.) <br>
**-** subtraction (can be used on DATETIME Columns.) <br> 
**x** Multiplication <br>
**/** Division <br>
**%** Percentage (Modulo) - Returns the integer remainder of a division . For example,
12 % 5 = 2 because the reminder of 12 divided by 5 is 2.

**Maths** in Querys

Working out the **Gross** and **Net** total of an item that has been discounted using 
an SQL Query.

**exercise** on using arithmetic

If an apple costs £2.00, and there are a quantity of 10 apples with 
an applied discount of 25% (0.25).

**Gross Total** The cost of the apple excluding the discount  <br>
`UnitPrice * Quantity = Gross Total`

**Net Total** The cost of the apple with the discount applied.
`(UnitPrice * Quanity) - (UnitPrice * Discount * Quantity) = Net Total`

_• Work out the Gross total and Net Total of the items in the order table, then identify the **TOP 2** with the
highest net total._ <br>
```sql
SELECT TOP 2 od.UnitPrice, od.Quantity, od.Discount, od.OrderID,
od.UnitPrice*od.Quantity AS "Gross Total",
ROUND((od.UnitPrice*od.Quantity) - (od.UnitPrice * od.Discount * od.Quantity), 2)  AS "Net Total"
FROM [Order Details] od
ORDER BY [Net Total] DESC
```


* **ORDER BY** 

This allows you to order columns into either ascending **ASC** or 
descending **DESC** order, for example a table showing the net total of 
a sales column you could **DESC**, which would order the column showing the largest net total at the top.

```sql
SELECT TOP 2 od.UnitPrice, od.Quantity, od.Discount, od.OrderID,
od.UnitPrice*od.Quantity AS "Gross Total",
ROUND((od.UnitPrice*od.Quantity) - (od.UnitPrice * od.Discount * od.Quantity), 2)  AS "Net Total"
FROM [Order Details] od
ORDER BY [Net Total] DESC
```

* **STRING Functions**

The following string functions can be used to manipulate text in various ways in the `SELECT` CLAUSE.

| FUNCTION       |    Description         |
|----------------|-----------------------------------------------------------------------------------------|
| **SUBSTRING**      | `SUBSTRING(Expression, start, length)` <br> `SUBSTRING(name, 1, 1)` for the initial   |
| **CHARINDEX**      | `CHARINDEX('a', 'text')` to search for a string e.g. find   'a' in a column called 'text' |
| **LEFT** or **RIGHT**  | `LEFT(name, 5)` for the first (or last) 5 characters                                      |
| **LTRIM** or **RTRIM** | Used to remove spaces at the beginning or end of a string                               |
| **LEN**            | `LEN(name)` for length of the name                                                        |
| **REPLACE**        | `REPLACE(name,' ', '_')` to replace spaces with underscores                               |
| **UPPER** or **LOWER** | `UPPER(name)` to convert to all upper (or lower) case                                     |

Further **examples** :

_• **INDEXES Start from 1 in SQL**_ <br>
_• RETURNS the index of the letter a if it is in a string, otherwise it returns 0._ <br>
```sql
SELECT e.FirstName, CHARINDEX('s', e.FirstName) AS "Position of Character"
FROM Employees e
```

_• Returns the first and third character of a string._ <br>
```sql
SELECT e.FirstName, SUBSTRING(e.FirstName, 1, 3) AS "Extracted String"
FROM Employees e
```

_• Returns the last two characters (from the right of a string)._ <br>
```sql
SELECT e.FirstName, RIGHT(e.FirstName, 2) AS 'Extracted String'
FROM Employees e
```

_• Returns the first two characters (from the left of a string)._ <br>
```sql
SELECT e.FirstName, LEFT(e.FirstName, 2) AS 'Extracted String'
FROM Employees e
```

_• Removes white space from the end of a string._ <br> 
```sql
SELECT e.FirstName, RTRIM(e.firstName) AS 'Trimmed String'
FROM Employees e
```

_• Removes white space from the start of a string._ <br> 
```sql
SELECT e.FirstName, LTRIM(e.firstName) AS 'Trimmed String'
FROM Employees e
```

_• Replace the letter 'a' with the symbol '!'._ <br> 
```sql
SELECT e.FirstName, REPLACE(e.firstName, 'a', '!') AS 'Replaced String'
FROM Employees e
```

_• Returns the length of a string._ <br> 
```sql
SELECT e.FirstName, LEN(e.firstName) AS 'Length of String'
FROM Employees e
```

_• Returns the UPPER and LOWER case versions of a string._ <br> 
```sql
SELECT e.Firstname, UPPER(e.FirstName) AS 'Upper Case Conversion', LOWER(e.FirstName) AS 'Lower Case Conversion'
FROM Employees e
```

_• This gets the Postcode and extracts the 
letters on the left of the blank place, this is signified from the -1. 
So if there are 4 then its -1 to get the 3rd Index, before the blank space._ <br>
```sql
SELECT PostalCode "Post Code",
LEFT(PostalCode, CHARINDEX(' ', PostalCode)-1) AS "Post Code Region",
    CHARINDEX(' ', PostalCode) AS "Space Found", Country
FROM Customers
WHERE Country = 'UK'
```

**Exercise** to return only the product names that contain a single quote **'** <br>

```sql
SELECT p.ProductName "Product Names",
CHARINDEX('''',p.ProductName) AS "Index of Quote"
FROM Products p
WHERE CHARINDEX('''',p.ProductName) > 0
```

This returns the indexes of the point in the string where the apostrophe occurred if a string 
does not contain one it will return a 0, therefore we don't show those.

___
**Homework**
* Set up Presentation `GROUP BY` and `HAVING` also add examples
    * **Group is** : `John`, `Lucio` and `Sohaib`
    
~~* go to notes from yesterday and today and change it to SQL inline like below:~~

```sql
CREATE TABLE Student(s_id int NOT NULL, Name varchar(60), Age int);
```
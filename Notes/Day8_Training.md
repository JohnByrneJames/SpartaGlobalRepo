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
    * `ALTER TABLE director` <br>
    `ADD CONSTRAINT foreign_key_onFilmId FOREIGN KEY (film_id)` <br>
    `REFERENCES film_table (film_id) ON DELETE CASCADE;`

* **CREATE**
    * `CREATE TABLE critics (` <br>
    `critic_id INT PRIMARY KEY IDENTITY,` <br>
    `critic_name VARCHAR(255) NOT NULL,` <br>
    `reputation VARCHAR(10) NOT NULL,` <br>
    `film_id INT NOT NULL,` <br>
    `FOREIGN KEY (film_id)` <br>
        `REFERENCES film_table (film_id)` <br>
        `ON DELETE CASCADE );`
        

**SELECT CLAUSES**

- Demonstrate the ability to connect to a database and query it
- Write simple SQL statements to alter and add data
- Write simple queries to extract and compare data
- Demonstrate an ability to research and learn technical skills independently

**WHERE**

**WHERE** is used to filter data, city is a column in the customers table and you 
are asking it to find only the entries which contain **Paris** as the city.
 
* `SELECT * FROM Customers` <br>
`WHERE City = 'Paris'`

**Exercise**
* **Q** : How many employees have home city of London ?
* **A** : `SELECT * FROM Employees` <br>
`WHERE City = 'London'` ~ **4**
* **A-Returns Count** : <br>`SELECT COUNT(*) AS 'Employees living in London' FROM Employees` <br>
`WHERE City = 'London'`
___

* **Q** : Which Employee is a Doctor ?
* **A** : `SELECT * FROM Employees` <br>
`WHERE TitleOfCourtesy = 'Dr.'`~ **1**
* **A-Returns Count** : <br>`SELECT COUNT(*) AS "Number of employees with title doctor" FROM Employees` <br>
`WHERE TitleOfCourtesy = 'Dr.'`
___

* **Q** : How many products are discontinued ?
* **A** : `SELECT * FROM Products` <br>
`WHERE Discontinued = 1` <br> ~ **8**
* **A-Returns Count** : <br>`SELECT COUNT(*) AS "Products that are discontinued" FROM Products` <br>
`WHERE Discontinued = 1` 
___
 
**TIP** - For coding games make sure you use double quotes **"** for 
strings after **`AS`** it is not as intelligent as the Azure Data Studio

An **Apostrophe** **'** is a Reserved character, what happens when querying the example below?

`'29 King''s Way'`

`SELECT * FROM products WHERE ProductName = 'Anais''s'`

**Table Aliasing** is SO useful when querying a database as it can help avoid 
spelling mistakes and makes it a lot faster and easier.

* `SELECT c.CompanyName, c.City, c.Country, c.Region` <br>
`FROM Customers c` <br>
`WHERE c.Region = 'BC'`

It can be useful to write the **FROM** part first as it will 
attach an alias `C` to the `Customers` table, this allows the `SELECT` part to suggest the 
columns after the point.

* **TOP**

**TOP** is quite useful as it can specify a specific amount of rows to select from a table, 
starting from the top. For example `TOP 100` will select 100 rows 
from that table.

`SELECT TOP 100 CompanyName, City FROM Customers` <br>
`WHERE Country = 'FRANCE'`

* **AND** 

**AND** is a keyword that means all criterias in a condition need to met, for example
`Region = EU AND Age = 11`

`SELECT ProductName, UnitPrice FROM Products` <br>
`Where CategoryID = 1 AND Discontinued = 0`

* **OR**

**OR** is a keyword that means only one of multiple criteria have to meet 
the condition, for example `Region = EU OR Age = 11`

`SELECT ProductName, UnitPrice FROM Products` <br>
`WHERE CategoryID = 1 OR Discontinued = 0`

* **Operators**

**<>** Or **!=** <br>
**<** Less than <br>
**>** More than <br>
**<=** Less than or equal to <br>
**>=** Greater than or equal to <br>

`SELECT ProductName, UnitPrice FROM Products` <br>
`WHERE UnitsInStock > 0 AND UnitPrice > 29.99` 

* **DISTINCT**

**DISTINCT** will remove duplicates from a `SELECT` CLAUSE and only return 
unique values. Return distinct values. `No Duplicates`

`SELECT DISTINCT Country FROM Customers` <br>
`WHERE ContactTitle = 'Owner'`

* **WILDCARDS**

**Wildcards** can be usd as a substitute for any other character in a string when using 
the `LIKE` operator.
* **%** A substitute for zero or more characters
* **%** A substitute for a single character
* **[Charlist]** Sets the ranges of characters to match i.e. `LIKE` [ABC]% This will bring back anything starting with any of those letters.
* **[^Charlist]** Sets and ranges of characters that don't match i.e. `LIKE` [^ABC]% This will 
bring back anything that does not start with those letters.

_Select anything ending with a_ <br>
`SELECT DISTINCT c.Country` <br>
`FROM Customers c WHERE Country LIKE '%a'`

_Countries starting with U, A or M_ <br>
`SELECT DISTINCT c.Country`
`FROM Customers c WHERE Country LIKE '%[UAM]'`

_Countries NOT starting with U, A or M_
`SELECT DISTINCT c.Country` <br>
`FROM Customers c WHERE Country LIKE '%[^UAM]'`

_Countries which have a 3rd letter of A_<br>
`SELECT DISTINCT c.Country` <br>
`FROM Customers c WHERE Country LIKE '__A%'`



___
**Homework**
* Set up Presentation `GROUP BY` and `HAVING` also `handson`
    * **Group is** : `John`, `Lucio` and `Sohaib`
    
* Look into `ON DELETE CASCADE` a little more, and research a bit more into the existing **constraints**.

* go to notes from yesterday and today and change it to SQL inline like below:
    * ```sql CREATE TABLE```
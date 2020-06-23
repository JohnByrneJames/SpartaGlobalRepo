###### Sparta Global Training Day 6
###### Continuing with SQL...
___

> 9:00 AM - Daily Stand Up **[Morning meetup]**

**Tutors** are in morning meeting therefore we are expected to hold our own 
standup and talk about what we enjoyed yesterday as well as any blockers. This will hopefully lead 
to our group becoming more independent.

**Blockers** and what I **Enjoyed** from yesterday. Yesterday I enjoyed going over the SQL keys and 
seeing the different ways it is interpreted by different people. I Really like the way we have access to 
a **Northwind** database in Azure data studio, because it allows me to test out queries I am curious about. 
I am more of a practical learner so I agree with Anais, I would prefer more practical examples with real databases 
rather than theory.

> ![alt text](../Images/Northwind_Relational_Database_Structure.png "Relational Database structure for northwind database")

**No Blockers**...
> **"** Perhaps it will be better if we do more practical work as this is the best way to learn something like databases, 
>particularly getting to grips with the DBMS. **"**

___

> 9:42 AM - Introduction Database SQL continued... **[Morning]**

**Structured Query langauge**

* Data Manipulation language
    * Manipulate the data within your tables and `INSERT`, `UPDATE`, `DELETE` and `SELECT` the data.
* Data Definition Language
    * Define the data you want to `CREATE` in a table, `ALTER` data, `DROP` tables or `TRUNCATE`. `TRUNCATE` empties your table/ database, `DROP` 
    deletes your table/ database.
* Data Control Language
    * Control user privilege/ rights for the user, usually assigned by the database administrator. 
    Allow to `GRANT` certain rights such as `SELECT` and `UPDATE` but Not `DROP` or `DELETE`. Later 
    `REVOKE` these privileges away from this person.
* Transaction Control Language
    * A update has been done, the `COMMIT` will push these changes to the database. `ROLLBACK` is to go back to a previous 
    version of the database, due to a issue or bug. The `SAVEPOINT` is made when you make a 
    change to the database, this is a point where you can `ROLLBACK` to.

**DML**
* `SELECT`
* `INSERT`
* `UPDATE`
* `DELETE`

**DDL**
* `CREATE`
* `ALTER`
* `DROP`
* `TRUNCATE`

**DCL**
* `GRANT`
* `REVOKE`

**TCL**
* `COMMIT`
* `ROLLBACK`
* `SAVEPOINT`

**Good practice** is to add a drop database line before yours as if a database already 
exists with the same name, it will drop that and allow you to create yours.

___

> 10:50 AM - Introduction Database SQL continued... **[Mid-Morning]**

**Challenge** Create a database and create a table with some data

`CREATE DATABASE JohnByrne_db`

`CREATE TABLE customers (`

`   customerID INT IDENTITY(1, 1) NOT NULL,
    FirstName VARCHAR(100) NOT NULL, 
    LastName VARCHAR(100) NOT NULL,
    DateOfBirth DATE`
    
`)`

Then I decided to insert some data into the database.

`INSERT INTO Customers (FirstName, LastName, DateOfBirth)`

`VALUES ('Barry', 'B. Barlow', '1996-10-20');
`

**Data Types** (part 1)
* **VARCHAR**
    * Adaptable to different lengths of characters. Records MAX size.
    * Memory efficient `VARCHAR(20)` will use up to 20 but release what isn't used.
    * `VARCHAR(MAX)` goes to a max of 65,535 bytes but is bad practice.
* **CHARACTER** or **CHAR**
    * Data must be at a fixed length. Fixed amount of space used.
    * Fixed length `CHAR(10)` uses all the spaces and fills the blank space with white space. **50% faster** than 
    `VARCHAR`. E.G License plate always same length.
* **INT**
    * Holds a whole number/ integer value (see all BIGINT, SMALLINT and TINYINT) positive or negative.
    * `INT(11)`
* **DATE** or **TIME** or **DATETIME**
    * Stores Date, Time or both date and time.
    
**Data Types** (part 2)
* **DECIMAL or NUMERIC**
    * Fixed Precision and scale (digits to right of decimal point) numbers.
    * For `DECIMAL(4, 2)` the `4` is the amount of numbers before and after the decimal point, the `2`
    is the amount of numbers after the point.
* **BINARY**
    * Use to store binary data such as an image or file
* **FLOAT**
    * Scientific use (very large numbers)
* **BIT**
    * Equivalent to binary (0,1 or NULL)
    
**Challenge** add Data types to this table - 

| Column Name  | Description                                   | Example     | Data Type  |
|--------------|-----------------------------------------------|-------------|------------|
| Post Code    | 6 to 8 Characters                             | WV1 8JD     | `VARCHAR(8)` |
| Phone Number | 11 Digits, no punctuation                     | 07971781325 | `CHAR(11)`   |
| Birth Date   | dd/mm/yyyy                                    | 31/01/1980  | `DATE or DATETIME`       |
| Weight in Kg | A number with a decimal place                 | 63.5029     | `DECIMAL(6,4) `     |
| Comments     | Large block of text, more than 255 characters | ........    | `VARCHAR(3000)`   |


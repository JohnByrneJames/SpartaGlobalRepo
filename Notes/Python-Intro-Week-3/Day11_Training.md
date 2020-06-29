###### Sparta Global Training Day 11
###### Agenda for this week is Python however the SQL test is also organised for Tuesday morning.
___

> 9:00 AM - Daily Stand Up **[Morning meetup]**

**Astha** and **Sharukh** gone to training meeting so we are revising for databases until 9:30
when they are back.

- We went over the questions in the mini-project to compare what answers we got. No one exchanged 
answers only tips of what to do.

**Blockers** and stuff I **enjoyed** about last week and the weekend.

I spent a while on the project over the weekend, I have finished the project now but I 
found the last question specifically a little bit mind boggling. It specifically was not 
something I had seen before and I only got it through multiple attempts. I couldn't 
get it formatted in a way that showed the month as a name and year as a number using the format
as I think it converts it to a `VARCHAR`. 

| DML    | DDL      | DCL    | TCL       |
|--------|----------|--------|-----------|
| `SELECT` | `CREATE`   | `GRANT`  | `COMMIT`    |
| `INSERT` | `ALTER`    | `REVOKE` | `ROLLBACK`  |
| `UPDATE` | `DROP`     |          | `SAVEPOINT` |
| `DELETE` | `TRUNCATE` |          |           |

**Re-Iteration** of table for revision.

___

> 10:45 AM - Started CodingGames Mock test

There were 2 questions, one was a question that required 4 `INNER JOINS` the other was a theory question 
asking about a conjunction table and what is does. I ended with :star: **100%** :star: 

**Test** for SQL tomorrow Rules
- **Questions** - Do not ask any technical questions during the test.

_Modify the query to select only the ids of customers having purchased at least one product in the "Books" and "Garden" category.
Output should have no duplicates and should be sorted in ascending order._ <br> 
:warning: **`DO EXACTLY IS ASKED`** :warning:

> ![alt text](../../Images/SQL_MockExam_CodinGames.PNG "Question 1 in the mock exam")


```sql 
SELECT DISTINCT c.customer_id
FROM Customer c
INNER JOIN PURCHASE_ORDER po ON c.Customer_id = po.customer_id
INNER JOIN ORDER_PRODUCT op ON po.order_id = op.order_id 
INNER JOIN PRODUCT p ON op.product_Id = p.product_id
INNER JOIN PRODUCT_CATEGORY ON p.product_category_id = pc.product_category_id
WHERE pc.name IN ('Books', 'Garden')
ORDER BY c.customer_id DESC
```
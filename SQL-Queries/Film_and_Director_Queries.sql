CREATE DATABASE John_db 

USE John_db

CREATE TABLE film_table
(
    film_id INT IDENTITY(1, 1) PRIMARY KEY,
    film_name VARCHAR(20),
    film_type VARCHAR(20),
    date_of_release DATE, 
    director VARCHAR(40),
    writer VARCHAR(100),
    star VARCHAR(100),
    film_language CHAR(2),
    official_website VARCHAR(100),
    plot_summary VARCHAR(1000)
)

SP_HELP film_table

DROP TABLE film_table

ALTER TABLE film_table
ADD release_date DATETIME;

--THIS IS A COMMENT--

-- ALTER TABLE -- MAKE COLUMN NOT NULL (ALWAYS REQUIRES A VALUE)
ALTER TABLE film_table
ALTER COLUMN film_name VARCHAR(10) NOT NULL

-- INSERT INTO -- INSERT DATA INTO YOUR TABLE
INSERT INTO film_table (film_name, film_type, date_of_release, director, writer, star, film_language, official_website, plot_summary)
VALUES ('The Joker', 'Thriller', '2019-10-04',  'Todd Philips', 'Scott Silver',' Joaquin Phoenix', 'en', 'www.joker.movie', 'Forever alone in a crowd, failed comedian Arthur Fleck seeks connection as he walks the streets of Gotham City. Arthur wears two masks -- the one he paints for his day job as a clown, and the guise he projects in a futile attempt to feel like hes part of the world around him. Isolated, bullied and disregarded by society, Fleck begins a slow descent into madness as he transforms into the criminal mastermind known as the Joker.');

INSERT INTO film_table (film_name, film_type, date_of_release, director, writer, star, film_language, official_website, plot_summary)
VALUES ('Nemo', 'Adventure', '1997-10-04',  'Andrew Stanton', 'pixar',' Nemo', 'en', 'www.Nemo.movie', 'Nemo is lost and his dads tries to find him.');


-- SELECT EVERYTHING AND DISPLAY
SELECT * FROM film_table

-- UPDATE A COLUMN FROM PARTICULAR TABLE WHERE A CONDITION IS MET
UPDATE film_table
SET film_id = 1
WHERE film_name = 'SQL'

-- ALTER A TABLE BY DROPPING A COLUMN 
ALTER TABLE film_table
DROP COLUMN release_date;

-- Clears the tables data rows without dropping the structure
TRUNCATE TABLE film_table

SELECT film_name, writer FROM film_table 

-- CREATE DIRECTOR TABLE --
CREATE TABLE director(
    director_id INT IDENTITY(1, 5),
    director_name VARCHAR(50),
    city VARCHAR(20) DEFAULT 'LONDON',
    film_id INT, 
    PRIMARY KEY(director_id),
    FOREIGN KEY(film_id) REFERENCES film_table(film_id)
)

DROP TABLE director

SELECT * FROM director
SELECT * FROM film_table

-- INSERT INTO -- DIRECTOR
INSERT INTO director (director_name, city, film_id)
VALUES ('Scott Silver', 'New York', 1), ('Todd Philips', 'Chicago', 1), ('John Byrne', 'London', 1), ('Ozzy Osborne', 'California', 1)

INSERT INTO director (director_name, film_id)
VALUES ('Rory the Racing Car', 1)

-- If you added this without having a second film then it would throw an error due to data integrity
INSERT INTO director (director_name, film_id)
VALUES ('Rory the Racing Car', 2)

-- Short hand but required all the tables that require a value and is in column order
INSERT INTO director VALUES ('Batman', 1)

-- DELETE  / cannot delete this as this primary key is a foreign key in another table
DELETE FROM film_table WHERE film_id = 1 

-- ALTER TABLE TO ADD CASCADE
ALTER TABLE director 
DROP CONSTRAINT film_id
FOREIGN KEY (film_id)
REFERENCES film_table (film_id) ON DELETE CASCADE;
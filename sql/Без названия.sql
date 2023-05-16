-- Database: publick

-- DROP DATABASE IF EXISTS publick;

--CREATE DATABASE publick
   -- WITH
    --OWNER = postgres
    --ENCODING = 'UTF8'
    --LC_COLLATE = 'C'
    --LC_CTYPE = 'C'
    --TABLESPACE = pg_default
    --CONNECTION LIMIT = -1
    --IS_TEMPLATE = False;
SELECT * FROM items;
SELECT price FROM items WHERE price > 80;
SELECT price FROM items WHERE price >= 300;
SELECT last_name FROM customers WHERE last_name LIKE 'Smith';
SELECT * FROM customers WHERE last_name LIKE 'Jones';
SELECT * FROM customers WHERE last_name NOT LIKE 'Scott';

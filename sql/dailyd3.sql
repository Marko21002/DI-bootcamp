-- create table customer(
-- id serial primary key,
-- first_name VARCHAR(50) NOT NULL,
-- last_name VARCHAR(50) NOT NULL
-- );
-- create table customerprofile(
-- id serial primary key,
-- isLoggedIn BOOLEAN DEFAULT false,
-- customer_id INT UNIQUE,
-- FOREIGN KEY (customer_id) REFERENCES customer(id)
-- );
-- insert into customer(first_name,last_name) values
-- ('john', 'Doe'),
-- ('Jerome', 'Lalu'),
-- ('Lea', 'Rive');

-- insert into customerprofile(isLoggedIn, customer_id)
-- values 
-- (true,(select id from customer where first_name = 'john' and last_name = 'Doe'))
-- (false,(select id from customer where first_name = 'Jerome'));

-- select * from customerprofile;

-- select first_name
-- from customer 
-- join customerprofile on customer.id = customerprofile.customer_id
-- where customerprofile.isLoggedIn = true;

-- select customer.first_name,customerprofile.isLoggedIn
-- from customer 
-- join customerprofile on customer.id = customerprofile.customer_id;

-- SELECT COUNT(*) AS NumNotLoggedIn
-- FROM Customer c
-- LEFT JOIN CustomerProfile cp ON c.id = cp.customer_id
-- WHERE cp.isLoggedIn IS NULL;

-- CREATE TABLE Book (
--   book_id SERIAL PRIMARY KEY,
--   title TEXT NOT NULL,
--   author TEXT NOT NULL
-- );

-- INSERT INTO Book (title, author)
-- VALUES ('Alice In Wonderland', 'Lewis Carroll'),
--        ('Harry Potter', 'J.K Rowling'),
--        ('To kill a mockingbird', 'Harper Lee');


-- CREATE TABLE Student (
--   student_id SERIAL PRIMARY KEY,
--   name TEXT NOT NULL UNIQUE,
--   age INTEGER CHECK (age <= 15)
-- );
-- INSERT INTO Student (name, age)
-- VALUES ('John', 12),
--        ('Lera', 11),
--        ('Patrick', 10),
--        ('Bob', 14);

-- CREATE TABLE Library (
--   book_fk_id INTEGER REFERENCES Book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
--   student_fk_id INTEGER REFERENCES Student(student_id) ON DELETE CASCADE ON UPDATE CASCADE,
--   borrowed_date DATE,
--   PRIMARY KEY (book_fk_id, student_fk_id)
-- );
-- INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
-- VALUES (
--   (SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'),
--   (SELECT student_id FROM Student WHERE name = 'John'),
--   '2022-02-15'
-- );

-- INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
-- VALUES (
--   (SELECT book_id FROM Book WHERE title = 'To kill a mockingbird'),
--   (SELECT student_id FROM Student WHERE name = 'Bob'),
--   '03/03/2021'
-- );


-- INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
-- VALUES (
--   (SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'),
--   (SELECT student_id FROM Student WHERE name = 'Lera'),
--   '2021-05-23'
-- );
-- INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
-- VALUES (
-- (SELECT book_id FROM Book WHERE title = 'Harry Potter'),
-- (SELECT student_id FROM Student WHERE name = 'Bob'),
-- '2021-08-12');

-- select * from Library;


-- select Student.name,Book.title
-- from Student
-- join Library on Library.student_fk_id = Student.student_id
-- join Book on Library.book_fk_id = Book.book_id;
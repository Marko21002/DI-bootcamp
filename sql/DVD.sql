-- select * from customer;
--  SELECT first_name || ' ' || last_name AS full_name
--  FROM customer;

-- select DISTINCT create_date from customer 
-- SELECT * FROM customer ORDER BY first_name DESC;
-- SELECT film_id,title,description,release_year,rental_rate from film  ORDER BY rental_rate ASC;

-- select c1.first_name, c2.last_name as last_name from customer as c1
-- join customer as c2 on c1.first_name = c2.first_name(thats for me)
-- select address,phone from address where district = 'Texas';
-- select * from film where film_id = 15 OR film_id = 150;
-- SELECT film_id, title, description, length, rental_rate
-- FROM film
-- WHERE title = 'YOUR_FAVORITE_MOVIE_TITLE';
-- SELECT film_id, title, description, length, rental_rate
-- FROM film
-- WHERE title ILIKE 'Yo%';
-- select title,rental_rate from film order by rental_rate ASC limit 10;
-- SELECT title, rental_rate 
-- FROM film 
-- ORDER BY rental_rate ASC 
-- OFFSET 10 ROWS 
-- FETCH NEXT 10 ROWS ONLY;
-- SELECT cu.first_name, cu.last_name, p.amount, p.payment_date 
-- FROM customer cu 
-- INNER JOIN payment p ON cu.customer_id = p.customer_id 
-- ORDER BY cu.customer_id ASC;
-- SELECT film.title
-- FROM film
-- LEFT JOIN inventory ON film.film_id = inventory.film_id
-- WHERE inventory.inventory_id IS NULL;
-- select ci.city,co.country
-- from city ci
-- join country co on ci.city_id = co.country_id;






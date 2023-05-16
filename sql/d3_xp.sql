-- -- select * from language;
-- select film.title, film.description , language.name from film
-- join language on film.language_id = language.language_id;

-- SELECT film.title, film.description, language.name
-- FROM language
-- LEFT JOIN film ON language.language_id = film.language_id;

-- CREATE TABLE new_film (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(255) NOT NULL
-- );

-- INSERT INTO new_film (name)
-- VALUES ('Movie 1'), ('Movie 2'), ('Movie 3');
-- CREATE TABLE customer_review (
--     review_id SERIAL PRIMARY KEY,
--     film_id INTEGER NOT NULL REFERENCES new_film(id) ON DELETE CASCADE,
--     language_id INTEGER NOT NULL REFERENCES language(language_id),
--     title VARCHAR(255) NOT NULL,
--     score INTEGER NOT NULL CHECK (score >= 1 AND score <= 10),
--     review_text TEXT NOT NULL,
--     last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );
-- INSERT INTO customer_review (film_id, language_id, title, score, review_text)
-- VALUES (1, 1, 'Great movie!', 9, 'I really enjoyed this film. The acting was excellent and the storyline was engaging.');

-- INSERT INTO customer_review (film_id, language_id, title, score, review_text)
-- VALUES (2, 2, 'Disappointing', 4, 'I was really looking forward to this movie, but it fell short of my expectations. The plot was weak and the characters were underdeveloped.');
-- delete from new_film where name = 'Movie 1'
-- select * from customer_review;
-- ex2

-- update film
-- set language_id = 2
-- where film_id = 5;
-- SELECT COUNT(*)
-- FROM rental
-- WHERE return_date IS NULL ;


-- SELECT film.title, rental.rental_date, inventory.inventory_id, payment.amount
-- FROM rental
-- JOIN inventory ON rental.inventory_id = inventory.inventory_id
-- join film on inventory.film_id = film.film_id
-- join payment on payment.rental_id = rental.rental_id
-- where rental.return_date is NULL
-- order by payment.amount DESC
-- limit 30;
 
 
-- SELECT title
-- FROM film
-- WHERE description LIKE '%sumo wrestler%'

-- SELECT title
-- FROM film
-- WHERE length < 60
-- AND rating = 'R';

-- SELECT film.title 
-- FROM film 
-- JOIN inventory ON inventory.film_id = film.film_id
-- JOIN rental ON inventory.inventory_id = rental.inventory_id
-- JOIN customer ON customer.customer_id = rental.customer_id
-- JOIN payment ON payment.rental_id = rental.rental_id
-- WHERE customer.first_name = 'Matthew' AND customer.last_name = 'Mahan'
-- AND payment.amount > 4.0 AND rental.return_date BETWEEN '2005-07-28' AND '2005-08-01';


-- SELECT film.title 
-- FROM film
-- WHERE (film.title LIKE '%boat%' OR film.description LIKE '%boat%')
-- AND film.replacement_cost > 30;

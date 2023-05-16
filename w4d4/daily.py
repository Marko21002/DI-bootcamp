import requests
import random
import psycopg2

response = requests.get('https://restcountries.com/v3.1/all')


countries = response.json()


random_countries = random.sample(countries, 10)

conn = psycopg2.connect(
    host="localhost",
    database="test",
    user="postgres",
    password="m210702g"
)


cur = conn.cursor()

# Insert each country into the database
for country in random_countries:
    name = country['name']['common']
    capital = country['capital'][0]
    flag = country['flags'][0]
    subregion = country['subregion']
    population = country['population']

    cur.execute(
        "INSERT INTO countries (name, capital, flag, subregion, population) VALUES (%s, %s, %s, %s, %s)",
        (name, capital, flag, subregion, population)
    )

# Commit the changes and close the cursor and connection
conn.commit()
cur.close()
conn.close()

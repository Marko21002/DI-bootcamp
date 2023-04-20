import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'm210702g'
DATABASE = 'dvdrental'

connection = psycopg2.connect(host=HOSTNAME, user=USERNAME,
                              password=PASSWORD, dbname=DATABASE)
cursor = connection.cursor()
query = "select * from city"
with connection.cursor() as cursor:
    cursor.execute(query)
    result = cursor.fetchall()
print(result)


def select_column(column_name, table_name):
    query = f"select {column_name} from {table_name}"
    return query

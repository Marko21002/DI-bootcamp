import psycopg2


class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def save(self):
        conn = psycopg2.connect(database="test", user="postgres",
                                password="m210702g", host="localhost", port="5432")
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO menu_item (name, price) VALUES (%s, %s)", (self.name, self.price))
        conn.commit()
        cur.close()
        conn.close()

    def delete(self):
        conn = psycopg2.connect(database="test", user="postgres",
                                password="m210702g", host="localhost", port="5432")
        cur = conn.cursor()
        cur.execute("DELETE FROM menu_item WHERE name=%s", (self.name,))
        conn.commit()
        cur.close()
        conn.close()

    def update(self, new_name, new_price):
        conn = psycopg2.connect(database="test", user="postgres",
                                password="m210702g", host="localhost", port="5432")
        cur = conn.cursor()
        cur.execute("UPDATE menu_item SET name=%s, price=%s WHERE name=%s",
                    (new_name, new_price, self.name))
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def all():
        conn = psycopg2.connect(database="test", user="postgres",
                                password="m210702g", host="localhost", port="5432")
        cur = conn.cursor()
        cur.execute("SELECT * FROM menu_item")
        rows = cur.fetchall()
        menu_items = []
        for row in rows:
            menu_items.append(MenuItem(row[0], row[1]))
        cur.close()
        conn.close()
        return menu_items

    @staticmethod
    def get_by_name(name):
        conn = psycopg2.connect(database="test", user="postgres",
                                password="m210702g", host="localhost", port="5432")
        cur = conn.cursor()
        cur.execute("SELECT * FROM menu_item WHERE name=%s", (name,))
        row = cur.fetchone()
        cur.close()
        conn.close()
        if row:
            return MenuItem(row[0], row[1])
        else:
            return None


item = MenuItem('Burger', 35)
item.save()
item.delete()
item.update('Veggie Burger', 37)
item2 = MenuItem.get_by_name('Beef Stew')
items = MenuItem.all()

from models.__init__ import CURSOR, CONN

class Restaurant:

    def __init__(self, name='Restaurant', cuisine='unknown', city_id=None, id=None):
        self.id = id
        self.name = name
        self.cuisine = cuisine
        self.city_id = city_id

    def save(self):
        sql = """
            INSERT INTO restaurants(name, cuisine, city_id)
            VALUES (?, ?, ?);
        """
        CURSOR.execute(sql, (self.name, self.cuisine, self.city_id))
        CONN.commit()

        self.ID = CURSOR.lastrowid

    def delete(self):
        if not self.id:
            print('no id')
            return None
        sql = """
            DELETE FROM restaurants
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        print("successfully deleted from database")
        self.id = None

    def __repr__(self):
        return f'<Restaurant name={self.name} city_id={self.city_id}>'
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS restaurants(
                id INTEGER PRIMARY KEY,
                name TEXT,
                cuisine TEXT,
                city_id INTEGER
            );
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS restaurants;"
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def create(cls, name, cuisine, city_id):
        new_restaurant = cls(name=name, cuisine=cuisine, city_id=city_id)
        new_restaurant.save()
        return new_restaurant 

    @classmethod
    def create_instance(cls, row):
        return cls(id=row[0], name=row[1], cuisine=row[2], city_id=row[3])
    
    @classmethod
    def display_all(cls):
        sql = "SELECT * FROM restaurants;"
        restaurant_rows = CURSOR.execute(sql).fetchall()
        return [cls.create_instance(row) for row in restaurant_rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM restaurants
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.create_instance(row)
    

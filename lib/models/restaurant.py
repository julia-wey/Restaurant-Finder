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

    def __repr__(self):
        return f'<Restaurant name={self.name} city_id=self.city_id>'
    

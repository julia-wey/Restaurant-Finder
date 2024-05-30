from models.__init__ import CURSOR, CONN
from models.city import City

class Restaurant:

    def __init__(self, name='Restaurant', cuisine='unknown', city_id=None, id=None):
        self.id = id
        self.name = name
        self.cuisine = cuisine
        self.city_id = city_id

    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string."
            )
        
    @property
    def cuisine(self):
        return self._cuisine 
    
    @cuisine.setter
    def cuisine(self, cuisine):
        if isinstance(cuisine, str) and len(cuisine):
            self._cuisine = cuisine
        else:
            raise ValueError(
                "Cuisine must be a non-empty string."
            )

    @property
    def city_id(self):
        return self._city_id 
    
    @city_id.setter
    def city_id(self, city_id):
        if type(city_id) is int and City.find_by_id(city_id):
            self._city_id = city_id
        else:
            raise ValueError(
                "city_id must reference a city in the database."
            )

    def save(self):
        sql = """
            INSERT INTO restaurants(name, cuisine, city_id)
            VALUES (?, ?, ?);
        """
        CURSOR.execute(sql, (self.name, self.cuisine, self.city_id))
        CONN.commit()

        self.ID = CURSOR.lastrowid

    def delete(self):
        if not self.name:
            #print('no id')
            return None
        sql = """
            DELETE FROM restaurants
            WHERE name = ?
        """
        CURSOR.execute(sql, (self.name,))
        CONN.commit()
        print(f'{self.name} successfully deleted from database.')
        
    def __repr__(self):
        city_name = "Unknown"
        if self.city_id is not None:
            city = City.find_by_id(self.city_id)
            if city:
                city_name = city.name
        return f'<Restaurant = {self.name}, City = {city_name}>'
    
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
    def find_restaurant_by_name(cls, name):
        sql = """
            SELECT * FROM restaurants
            WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        if row:
            return cls.create_instance(row)
        else:
            None

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM restaurants
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        if row:
            return cls.create_instance(row)
        else:
            None
    
from models.__init__ import CURSOR, CONN

class City:
    def __init__(self, name, state, id=None):
        self.id = id
        self.name = name
        self.state = state
    
    def __repr__(self):
        return f'<City name = {self.name}>'
    
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
    def state(self):
        return self._state 
    
    @state.setter
    def state(self, state):
        if isinstance(state, str) and len(state) == 2:
            self._state = state
        else:
            raise ValueError(
                "U.S. State must be a two-letter abbreviation."
            )
    
    def save(self):
            sql = """
                INSERT INTO cities(name, state)  
                VALUES (?,?);
            """
            CURSOR.execute(sql, (self.name, self.state))
            CONN.commit()
            self.id = CURSOR.lastrowid 

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS cities(
                id INTEGER PRIMARY KEY,
                name TEXT,
                state TEXT
                );
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS cities;"
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def create(cls, name, state):
        new_city = cls(name=name, state=state)
        new_city.save()
        return new_city
    
    @classmethod
    def create_instance(cls, row):
        return cls(id=row[0], name=row[1], state=row[2])

    @classmethod
    def display_all(cls):
        sql = "SELECT * FROM cities;"
        city_rows = CURSOR.execute(sql).fetchall()
        return [cls.create_instance(row) for row in city_rows]
    
    def delete(self):
        if not self.id:
            print('no id')
            return None
        sql = """
            DELETE FROM cities
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        print("successfully deleted from database")
        self.id = None

    @classmethod
    def find_city_by_name(cls, name):
        sql = """
            SELECT * FROM cities
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
            SELECT * FROM cities
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        if row:
            return cls.create_instance(row)
        else:
            None

    def restaurants(self):
        """Return list of restaurants associated with current city"""
        from models.restaurant import Restaurant
        sql = """
            SELECT * FROM restaurants
            WHERE city_id = ?
        """
        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()
        return [
            Restaurant.create_instance(row) for row in rows
        ]
       
    
        
         
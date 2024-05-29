from models.__init__ import CURSOR, CONN
#from models.restaurant import Restaurant

class City:
    def __init__(self, name, state, id=None):
        self.id = id
        self.name = name
        self.state = state
    
    def __repr__(self):
        return f'<City name={self.name}>'
    
    def save(self):
            sql = """
                INSERT INTO cities(name, state)  
                VALUES (?,?);
            """
            CURSOR.execute(sql, (self.name, self.state))
            CONN.commit()
            #import ipdb; ipdb.set_trace()
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
    #import ipdb; ipdb.set_trace()

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
    
    def __repr__(self):
        return f'<City name={self.name}>'
import sqlite3
from __init__ import CONN, CURSOR

class Dog:
    
    all = []

    def __init__(self, name, breed):
        self.id = None
        self.name = name
        self.breed = breed

    @classmethod
    def create_table(self):
        sql = """
            CREATE TABLE IF NOT EXISTS dogs(
                id INTEGER PRIMARY KEY,
                name TEXT,
                breed TEXT
            )
        """ 
        CURSOR.execute(sql)

    @classmethod
    def drop_table(cls):
        sql ="""
            DROP TABLE IF EXISTS dogs
        """
        CURSOR.execute(sql)        
    
    def save(self):
        sql ="""
            INSERT INTO dogs(name, breed)
            values(?,?)
        """    
        CURSOR.execute(sql, (self.name, self.breed))
        self.id = CURSOR.execute("SELECT last_insert_rowid() FROM dogs").fetchone()[0]

    @classmethod
    def create(cls, name, breed):
        dog = cls( name, breed) 
        dog.save()   
        return dog

    @classmethod
    def new_from_db(cls,row):
        if row is not None:
            dog = cls(row[1], row[2])  
            dog.id = row[0]  
            return dog
        else:
            return None    

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM dogs
        """

        all_rows = CURSOR.execute(sql).fetchall()    

        if all_rows is not None:
            cls.all = [cls.new_from_db(row) for row in all_rows] 
        else:
            cls.all = []    

    @classmethod
    def find_by_name(cls, name):  
        sql = """
            SELECT *
            FROM dogs
            WHERE name = ?
            LIMIT 1
        """
        dog = CURSOR.execute(Sql, (name,)).fetchone()   
        if dog is not None:
            return cls.new_from_db(dog)     
        else:
            return None    

    @classmethod
    def find_by_id(cls, name):
        sql = """
            SELECT *
            FROM dogs
            WHERE id = ?
            LIMIT 1
        """ 
        dog = CURSOR.execute(sql, (id)) .fetchone()
        if dog is not None:
            return cls.new_from_db(dog)
        else:
            return None    
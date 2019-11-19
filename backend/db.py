#!/srv/bin/env python3

import pymongo

class mongo_connection:
    conn = None

    def connect(self):
        client = pymongo.MongoClient("mongodb+srv://[DB_URL]")
        self.conn = client['bookstore']['books']
        
        
    def query(self, sql):
        cursor = self.conn.find(sql)  
        return cursor
    
    def insert(self, item):
        self.conn.insert(item)
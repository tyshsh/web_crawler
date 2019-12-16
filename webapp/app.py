#!/srv/bin/env python3

import pymongo
import settings

class mongo_connection:
    conn = None

    def connect(self):
        client = pymongo.MongoClient(settings.MONGODB_SERVER)
        self.conn = client[settings.MONGODB_DB][settings.MONGODB_COLLECTION]

    def query(self, sql):
        cursor = self.conn.find(sql)
        return cursor

    def insert(self, item):
        self.conn.insert(item)

db = mongo_connection()
db.connect()



from flask import Flask,render_template,request,make_response,jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/api/finder', methods=['GET'])
def getbooks():
            
    title = request.args.get('title', default='')
    
    filters = {
        'title': {'$regex': title, "$options" : "i"}
    }
    
    cursor = db.query(filters)
    books = []
    
    for book in cursor:
        del book['_id']
        books.append(book)
        #print(book)
    
    return jsonify(books)
    
if __name__ == "__main__":
    app.run(host=settings.HOST, port=settings.PORT, debug=True)

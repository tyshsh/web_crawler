#!/srv/bin/env python3

from db import mongo_connection

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
    app.run(host='0.0.0.0',port=54321,debug=True)
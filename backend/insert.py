#!/srv/bin/env python3

from db import mongo_connection

db = mongo_connection()
db.connect()

import json

books = []

with open("items.json", "r") as f:
    for row in f.read().split(",\n"):
        books.append(json.loads(row))

for book in books:
    db.insert(book)
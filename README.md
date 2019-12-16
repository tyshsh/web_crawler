# Python Web Crawler

This is mini framework to achieve a simple web content crawler with a live [demo](http://wenxinli.info:8080/) of searching book information gathered from an online bookseller. It contains following three components:

1. A MongoDB object database.
2. Backend Python scripts for content crawling and data injection.
3. Frontend Python/Flask application for web-UI.



```
conda install -c conda-forge scrapy
conda install -c anaconda pymongo
conda install -c anaconda dnspython
```

```
scrapy crawl books
```

```
conda install -c anaconda werkzeug
conda install -c anaconda flask
```

```
python app.py
```

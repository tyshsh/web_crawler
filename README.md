# Python Web Crawler

This is mini framework to achieve a simple web content crawler with a live [demo](http://wenxinli.info:8080/) of searching book information gathered from an online bookseller. It contains following three components:

1. A MongoDB object database.
2. Backend Python scripts for content crawling and data injection.
3. Frontend Python/Flask application for web-UI.

## prerequisites

This framework is developed under **Python3** (Python>=3.7.0) and using the `Scrapy` and `Flask` packages. Both `PIP` and `Conda` can be used to configure the environment and install required libraries, and [Anaconda3](https://www.anaconda.com/distribution/) is recommended.

After cloning or downloading this repo, run following command in the source folder to install the required packages:

```
conda install --file requirements.txt
```

Or, manually install them and their dependencies by:

```
conda install -c conda-forge scrapy
conda install -c anaconda pymongo
conda install -c anaconda dnspython
conda install -c anaconda werkzeug
conda install -c anaconda flask
```

## Quick Guide

### 1. Build up MongoDB

A simple and free MongoDB instance can be built on the Atlas Cloud service at https://cloud.mongodb.com/. Following this [tutorial](https://docs.atlas.mongodb.com/tutorial/deploy-free-tier-cluster/) to create a database for this software, which including following steps:

  1. Create a new project
  2. Inside the project, create a new cluster
  3. Inside the cluster, click to view the colletions
  4. Create a new collection with the database name "**bookstore**" and collection name "**books**"
  5. In the left side-bar, Click "Database Access" under the "SECURITY" group.
  6. Add new user using username/password method and with read/write permissions.

### 2. Crawl books information

Go into the source folder of scrapy/books project, make a new setting file from `settings.py.sample`:

```
cd books/books
cp settings.py.sample settings.py
```

Open the file `settings.py`, change the values of following three variables corresponding to the configuration in step 1.

```
MONGODB_SERVER = "mongodb+srv://[USERNAME]:[PASSWORD]@[DBCLUSTERNAME].mongodb.net/test?retryWrites=true&w=majority"
MONGODB_DB = '[DBNAME]'
MONGODB_COLLECTION = '[COLLECTIONNAME]'
```

Execute the crawling for the bookstore website:

```
cd ..
scrapy crawl books
```

### 3. Launch web application

Go into the source folder of `webapp`, make a new setting file from `settings.py.sample`:

```
cd ../webapp
cp settings.py.sample settings.py
```

Open the file `settings.py`, change the values of following three variables corresponding to the configuration in step 1.

```
MONGODB_SERVER = "mongodb+srv://[USERNAME]:[PASSWORD]@[DBCLUSTERNAME].mongodb.net/test?retryWrites=true&w=majority"
MONGODB_DB = '[DBNAME]'
MONGODB_COLLECTION = '[COLLECTIONNAME]'
```

Launch the web application by:

```
python app.py
```

Open a web-browswer and direct to the URL: **http://127.0.0.1:8888**. In the search box, type "boy" and submit.





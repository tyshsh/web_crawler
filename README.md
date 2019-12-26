# Python Web Crawler

This is mini framework to achieve a simple web content crawler with a live [demo](http://wenxinli.info:8080/) of searching book information gathered from an online bookseller. It contains following three components:

1. A MongoDB object database.
2. Backend Python scripts for content crawling and data injection.
3. Frontend Python/Flask application for web-UI.

## prerequisites

This framework is developed under Python3 and using the `Scrapy` and `Flask` packages. Both `PIP` and `Conda` can be used to configure the environment and install required libraries, and [Anaconda3](https://www.anaconda.com/distribution/) is recommended.

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


### Crawl books information

```
cd books
scrapy crawl books
```

### 2. Launch web application

```
cd webapp
python app.py
```

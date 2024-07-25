#!/usr/bin/env python3
"""DB Module
"""
from pymongo import MongoClient
from shorturl import ShortURL


class DB():
    """MongoDB class
    """

    def __init__(self):
        """Instantiates
        """
        self.__client = MongoClient('localhost', 27017)
        self.__db = self.__client.url_shortener
        self.__collection = self.__db.shorturls

    def create_shorturl(self, url: str) -> None:
        """Inserts a new ShortURL instance in database
        """
        shorturl = ShortURL(url)
        self.__collection.insert_one(shorturl.to_json())
        return shorturl.shorturl

    def delete_shorturl(self, shorturl: str):
        """Deletes shortUrl instance from database
        """
        self.__collection.delete_one({'shorturl': shorturl})

    def get_url(self, shorturl: str):
        """"""
        data = self.__collection.find_one({'shorturl': shorturl})
        if data:
            return data.get('url')
        else:
            return None

    def get_shorturls(self):
        """Returns all shortUrl instances in database
        """
        return self.__collection.find()


if __name__ == '__main__':
    db = DB()
    short = db.create_shorturl('https://facebook.com/@me')
    url = db.get_url(short)
    print(url)

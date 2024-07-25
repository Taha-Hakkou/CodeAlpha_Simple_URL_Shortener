#!/usr/bin/env python3
"""ShortURL Module
"""
import base62
from datetime import datetime


class ShortURL():
    """ShortURL Data Model
    """

    def __init__(self, url: str, duration: int = 3600):
        """Instantiates a ShortURL instance
        """
        self.url = url
        self.shorturl = base62.generate()
        self.created_at = datetime.now()
        self.valid_duration = duration

    def __repr__(self):
        """"""
        return f'{self.shorturl} -> {self.url} | {self.created_at} + {self.valid_duration}'

    def to_json(self):
        """"""
        return {
            'url': self.url,
            'shorturl': self.shorturl,
            'created_at': self.created_at,
            'valid_duration': self.valid_duration
        }

if __name__ == '__main__':
    shorturl = ShortURL('www.google.com')
    print(shorturl)
    shorturl2 = ShortURL('https://linkedin.com/feed', 4500)
    print(shorturl2)

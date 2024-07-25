#!/usr/bin/env python3
"""base62 Module
"""
import string
import random
from db import DB

db = DB()
BASE62 = string.digits + string.ascii_letters
SEQUENCE_LENGTH = 7


def generate():
    """Generates a random base62 string
    """
    sequence = random.choices(BASE62, k=SEQUENCE_LENGTH)
    shorturl = ''.join(sequence)
    if db.get_url(shorturl):
        return shorturl
    return generate()


if __name__ == '__main__':
    print(generate())

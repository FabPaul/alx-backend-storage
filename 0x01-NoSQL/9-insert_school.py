#!/usr/bin/env python3
""" Inserts a new document in collection """

import pymongo


def insert_school(mongo_collection, **kwargs):
    """ Function that inserts a new document in a collection, return id """
    document_id = mongo_collection.insert(kwargs)
    return document_id

#!/usr/bin/env python3
""" Lists all elements in a collection"""

import pymongo


def list_all(mongo_collection):
    """ Function that lists all docs in a collection """

    if not mongo_collection:
        return []
    
    documents = mongo_collection.find()
    return [document for document in documents]
#!/usr/bin/env python3
""" Fetches the list of schools having a specific topic """

import pymongo


def schools_by_topic(mongo_collection, topic):
    """ Returns the list of schools having a specific topic"""
    return mongo_collection.find({"topic" : topic})

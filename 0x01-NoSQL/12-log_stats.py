#!/usr/bin/env python3
"""Python script that provides some stats about nginx logs stored in MongoDB"""

from pymongo import MongoClient
import pymongo


def get_nginx_logs_stats(mongo_collection):
    """ function that provides nginx logs status """
    print(f"{mongo_collection.estimated_document_count()} logs")

    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = mongo_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    number_of_gets = mongo_collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{number_of_gets} status check")


if __name__ == "__main__":
    mongo_collection = MongoClient('mongodb://127.0.0.1:27017/').logs.nginx
    get_nginx_logs_stats(mongo_collection)

#!/usr/bin/env python3
"""Python script that provides some stats about nginx logs stored in MongoDB"""

from pymongo import MongoClient
import pymongo


def get_nginx_logs_stats(mongo_collection):
    """ function that provides nginx logs status """
 
    # get total logs
    total_logs = mongo_collection.estimated_document_count({})
    print(f"{total_logs} logs")

    # get HTTP methods stats
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = mongo_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # number of status log checked
    status_count = mongo_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_count} status check")


if __name__ == "__main__":
    mongo_collection = MongoClient('mongodb://127.0.0.1:27017/').logs.nginx
    get_nginx_logs_stats(mongo_collection)

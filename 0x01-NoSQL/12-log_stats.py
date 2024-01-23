#!/usr/bin/env python3
"""Python script that provides some stats about nginx logs stored in MongoDB"""

from pymongo import MongoClient
import pymongo


def get_nginx_logs_stats():
    """ function that provides nginx logs status """
 
    # get total logs
    total_logs = collection.estimated_document_count({})
    print(f"{total_logs} logs")

    # get HTTP methods stats
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # number of status log checked
    status_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_count} status check")


if __name__ == "__main__":
    collection = MongoClient('mongodb://localhost:27017/').logs.nginx
    get_nginx_logs_stats(collection)

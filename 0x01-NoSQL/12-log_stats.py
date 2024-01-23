#!/usr/bin/env python3
"""Python script that provides some stats about nginx logs stored in MongoDB"""

from pymongo import MongoClient


def get_nginx_logs_stats():
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client.logs
    collection = db.nginx

    # Get total logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Get HTTP methods stats
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Number of status log checked
    status_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_count} status check")

if __name__ == "__main__":
    get_nginx_logs_stats()

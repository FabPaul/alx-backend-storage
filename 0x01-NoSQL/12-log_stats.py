#!/usr/bin/env python3
"""Python script that provides some stats about nginx logs stored in MongoDB"""

from pymongo import MongoClient
import pymongo


# connect to mongodb
client = MongoClient('mongodb://localhost:27017/')
db = client.logs
collection = db.nginx

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

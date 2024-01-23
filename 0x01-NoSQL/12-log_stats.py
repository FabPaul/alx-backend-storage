#!/usr/bin/env python3
"""Python script that provides some stats about nginx logs stored in MongoDB"""

from pymongo import MongoClient


if __name__ == "__main__":

    # Initialize the database
    client = MongoClient('mongodb://localhost:27017')
    nginx_collection = client.logs.nginx

    # generate list of methods
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    # Get total
    number_of_logs = nginx_collection.count_documents({})

    # Get count by methods
    count_by_methods = [nginx_collection.count_documents({"method": method}) for method in methods]

    count_status = nginx_collection.count_documents({"path": "/status"})

    # Prints
    print(f"{number_of_logs} logs")
    print("Methods:")

    for method, count in zip(methods, count_by_methods):
        print(f"\tmethod {method}: {count}")
    
    print(f"{count_status} status check")

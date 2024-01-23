#!/usr/bin/env python3
""" improved 12-logs_states.py by adding the top 10 of the most present
IPs in the collection nginx of the database logs

-The IPs top must be sorted (like the example below)
"""

from pymongo import MongoClient


if __name__ == "__main__":

    # generate the database
    client = MongoClient('mongodb://localhost:27017')
    nginx_collection = client.logs.nginx

    # generate list of methods
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    # Get total
    number_of_logs = nginx_collection.count_documents({})

    # Get count by methods
    count_by_methods = [nginx_collection.count_documents({"method": method}) for method in methods]

    count_status = nginx_collection.count_documents({"path": "/status"})

    # Get top 10 most present IPs
    top_ips = nginx_collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])

    # Prints
    print(f"{number_of_logs} logs")
    print("Methods:")

    for method, count in zip(methods, count_by_methods):
        print(f"\tmethod {method}: {count}")

    print(f"{count_status} status check")

    print("IPs:")
    for ip_info in top_ips:
        print(f"/t{ip_info['_id']}: {ip_info['count']}")

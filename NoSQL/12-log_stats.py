#!/usr/bin/env python3
"""Pymongo nginx script"""
if __name__ == '__main__':
    import pymongo

    mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
    mongo_db = mongo_client["logs"]
    mongo_collection = mongo_db["nginx"]
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print(f'{mongo_collection.count_documents({})} logs')
    print('Methods:')
    for method in methods:
        logs_count = mongo_collection.count_documents({'method': method})
        print(f'\tmethod {method}: {logs_count}')

    st = mongo_collection.count_documents({'method': 'GET', 'path': '/status'})
    print(f'{st} status check')

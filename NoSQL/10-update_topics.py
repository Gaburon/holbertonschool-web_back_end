#!/usr/bin/env python3
"""Pymongo update document"""


def update_topics(mongo_collection, name, topics):
    """Updates document"""
    to_update = {'name': name}
    to_add = { "$set": {'topics': topics} }
    mongo_collection.update_many(to_update, to_add)

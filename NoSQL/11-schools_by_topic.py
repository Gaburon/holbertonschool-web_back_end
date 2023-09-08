#!/usr/bin/env python3
"""Pymongo queries document"""


def schools_by_topic(mongo_collection, topic):
    """Queries document"""
    to_search = {'topics': topic}
    return mongo_collection.find(to_search)

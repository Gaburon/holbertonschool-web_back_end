#!/usr/bin/env python3
"""Pymongo insert document"""


def insert_school(mongo_collection, **kwargs):
    """Inserts kwargs into collection"""
    inserted_doc = mongo_collection.insert_one(kwargs)
    return inserted_doc.inserted_id

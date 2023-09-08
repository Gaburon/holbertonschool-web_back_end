#!/usr/bin/env python3
"""Pymongo lists all document"""


def list_all(mongo_collection):
    """Queries all documents in collection"""
    return mongo_collection.find()

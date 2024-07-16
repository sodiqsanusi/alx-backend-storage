#!/usr/bin/env python3
"""
Get all documents of a mongoDB collection
"""
import pymongo


def list_all(mongo_collection):
    """
    It lists all the documents in the provided collection
    """
    if not mongo_collection:
        return []
    return list(mongo_collection.find())

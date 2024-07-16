#!/usr/bin/env python3
"""
Adds a new document to a mongoDB collection
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into the passed mongoDB collection
    Returns the ID of the newly created document
    """
    return mongo_collection.insert_one(kwargs).inserted_id

#!/usr/bin/env python3
"""
Update the properties of a specific document in mongoDB
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    Updates the properties of the passed mongoDB collection with
    given details
    """
    return mongo_collection.update_many(
                {"name": name}, {$set: {"topics": topics}}
    )

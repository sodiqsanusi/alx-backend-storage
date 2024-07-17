#!/usr/bin/env python3
"""
Search a collection for specific documents
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    Search the given collection for all documents having the specific topic
    """
    return mongo_collection.find({"topics": topic})

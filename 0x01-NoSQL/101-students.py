#!/usr/bin/env python3
"""
Sort data gotten from a mongoDB collection
"""
import pymongo


def top_students(mongo_collection):
    """
    Perform an average operation on the scores of students in the collection
    Return the score average in descending order
    """
    return mongo_collection.aggregate([
        {
            "$project":
                {
                    "name": "$name",
                    "averageScore": {"$avg": "$topics.score"}
                }
        },
        {
            "$sort":
                {
                    "averageScore": -1
                }
        }
    ])

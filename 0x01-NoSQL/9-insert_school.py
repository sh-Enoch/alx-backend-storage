#!/usr/bin/env python3
"""Insert_school."""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """Insert new document in a collection."""
    mongo_dict = {}
    for key, value in kwargs.items():
        mongo_dict[key] = value
    new_doc = mongo_collection.insert_one(mongo_dict)
    obj_key = new_doc.inserted_id
    return obj_key

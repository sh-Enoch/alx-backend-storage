#!/usr/bin/env python3
"""Insert_school."""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """Insert new document in a collection."""
    mongo_dict = {}
    for key, value in kwargs.items():
        mongo_dict[key] = value
    result = mongo_collection.insert_one(mongo_dict)
    inserted_id = result.inserted_id
    obj_key =  mongo_collection.find_one({"_d": inserted_id})
    return obj_key

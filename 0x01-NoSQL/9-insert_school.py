#!/usr/bin/env python3
"""Insert_school."""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """Insert new document in a collection."""
    post_id = mongo_collection.insert(kwargs).inserted_id
    return post_id

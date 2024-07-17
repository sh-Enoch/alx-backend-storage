#!/usr/bin/env python3
"""Update topics."""
import pymongo


def update_topics(mongo_collection, name, topics):
    """Change all topics of a school document based on the name."""
    new_doc = mongo_collection.update_many({"name": name},
                                           {"$set": {"topics": topics}})

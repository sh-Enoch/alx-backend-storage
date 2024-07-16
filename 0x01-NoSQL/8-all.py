#!/usr/bin/env python3
"""List_all."""
import pymongo


def list_all(mongo_collection):
    """List all document in a collection."""
    if not mongo_collection:
        return []
    return list(mongo_collection.find())

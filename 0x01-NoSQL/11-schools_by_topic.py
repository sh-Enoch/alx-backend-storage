#!/usr/bin/env python3
"""School_by_topic."""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """Return list of school with a specific topic."""
    return list(mongo_collection.find({"topics": topic}))

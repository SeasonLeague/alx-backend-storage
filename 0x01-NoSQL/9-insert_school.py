#!/usr/bin/env python3 
"""MOngo Operations with python uisng pymongo"""


def insert_school(mongo_collection, **kwargs):
    """insert a new documents ini a collection based on kwargs"""
    return mongo_collection.insert(kwargs)

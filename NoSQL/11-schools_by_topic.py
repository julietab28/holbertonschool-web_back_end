#!/usr/bin/env python3
"""
Module - List of schools by topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    List of schools by topic
    """
    schools = []
    for school in mongo_collection.find({"topics": topic}):
        schools.append(school)
    return schools

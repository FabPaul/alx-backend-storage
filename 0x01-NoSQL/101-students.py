#!/usr/bin/env python3
""" Script that returns all students sorted by average score """

import pymongo
from operator import itemgetter


def top_students(mongo_collection):
    """ returns all students sorted by average """
    all_students = mongo_collection.find()
    students = []
    for student in all_students:
        scores = []
        topics = student.get('topics')
        scores = [topic.get('score')for topic in topics]
        average_score = float(sum(scores) / len(scores))
        student['averageScore'] = average_score
        students.append(student)

    top_students = sorted(students,
                          key=itemgetter('averageScore'), reverse=True)
    return top_students

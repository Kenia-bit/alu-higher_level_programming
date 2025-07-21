#!/usr/bin/python3
"""A script that creates a Student class with serialization support"""


class Student:
    """
    Represents a student.

    Attributes:
        first_name (str)
        last_name (str)
        age (int)
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of a Student"""
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {
                k: getattr(self, k)
                for k in attrs
                if hasattr(self, k)
            }
        return self.__dict__

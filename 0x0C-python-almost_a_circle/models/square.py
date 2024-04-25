#!/usr/bin/python3
"""This module handles a square object"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This class represents a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes an instance"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return string representation of instance"""
        return f"[Square] ({self.id}) {self.x}/{self.y} \
- {self.width}"

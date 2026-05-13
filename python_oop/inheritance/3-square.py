#!/usr/bin/env python3
"""Square hérite de Rectangle."""

Rectangle = __import__('1-rectangle').Rectangle

class Square(Rectangle):
    """Carré basé sur Rectangle."""
    def __init__(self, size):
        """Init avec size."""
        super().__init__(size, size)

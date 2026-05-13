#!/usr/bin/env python3
"""Square hérite de Rectangle."""

BaseGeometry = __import__('base_geometry').BaseGeometry


class Square(Rectangle):
    """Carré basé sur Rectangle."""
    def __init__(self, size):
        """Init avec size."""
        super().__init__(size, size)

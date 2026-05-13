#!/usr/bin/env python3
"""Square avec str, hérite de Rectangle."""

BaseGeometry = __import__('base_geometry').BaseGeometry


class Square(Rectangle):
    """Carré basé sur Rectangle."""
    def __init__(self, size):
        """Init avec size."""
        super().__init__(size, size)

    def __str__(self):
        """Affiche le carré."""
        descr = f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
        return descr

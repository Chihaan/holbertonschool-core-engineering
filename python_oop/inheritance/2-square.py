#!/usr/bin/env python3
"""Square avec str, hérite de Rectangle."""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Carré basé sur Rectangle."""
    def __init__(self, size):
        """Init avec size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Affiche le carré."""
        descr = f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
        return descr

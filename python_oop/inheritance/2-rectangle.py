#!/usr/bin/env python3
"""Rectangle avec aire et str."""

BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle hérite de BaseGeometry."""
    def __init__(self, width, height):
        """Init avec largeur et hauteur."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Retourne l'aire."""
        return self.__width * self.__height

    def __str__(self):
        """Affiche le rectangle."""
        descr = f"[Rectangle] {self.__width}/{self.__height}"
        return descr

#!/usr/bin/env python3
"""Rectangle simple."""

from base_geometry import BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle hérite de BaseGeometry."""
    def __init__(self, width, height):
        """Init avec largeur et hauteur."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

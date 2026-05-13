#!/usr/bin/env python3
"""Module defining a Rectangle class with width and height attributes."""


class Rectangle:
    """Represents a rectangle with a width and a height."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.
        """
        self.__width = width
        self.__height = height

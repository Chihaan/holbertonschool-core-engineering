#!/usr/bin/env python3
"""Module defining an abstract BaseGeometry class."""


class BaseGeometry:
    """Represents a base geometry."""

    def area(self):
        """Compute the area of the geometry.

        Raises:
            Exception: Always, since this method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer.

        Args:
            name (str): The name of the parameter.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

#!/usr/bin/env python3


from base_geometry import BaseGeometry

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.width * self.height
        
    def __str__(self):
        descr = f"[Rectangle] {self.__width}/{self.__height}"
        return descr

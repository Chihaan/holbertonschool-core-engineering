#!/usr/bin/env python3


Rectangle = __import__('1-rectangle').Rectangle

class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)

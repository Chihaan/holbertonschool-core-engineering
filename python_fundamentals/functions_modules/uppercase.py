#!/usr/bin/env python3


def uppercase(str):
    new_str = ""
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            new_char = chr(ord(char) - 32)
        else:
            new_char = char
        new_str = new_str + new_char
    print(new_str)

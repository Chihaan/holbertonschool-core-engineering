#!/usr/bin/env python3


def append_write(filename="", text=""):
    """Append a string to a text file and return number characters added."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

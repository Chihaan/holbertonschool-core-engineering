#!/usr/bin/env python3
"""Module for appending text to files."""


def append_write(filename="", text=""):
    """Append a string to a text file and return number characters added.

    Args:
        filename (str): path to the file to append to.
        text (str): string to append to the file.

    Returns:
        int: number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

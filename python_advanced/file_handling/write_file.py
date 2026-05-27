#!/usr/bin/env python3
"""Module for writing text to files."""


def write_file(filename="", text=""):
    """Write a string to a text file and return number of characters written.

    Args:
        filename (str): path to the file to write to.
        text (str): string to write to the file.

    Returns:
        int: number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

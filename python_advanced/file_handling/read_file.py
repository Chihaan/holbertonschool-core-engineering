#!/usr/bin/env python3
"""Module for reading text files."""


def read_file(filename=""):
    """Read a text file (UTF-8) and print its content to stdout.

    Args:
        filename (str): path to the file to read.
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")

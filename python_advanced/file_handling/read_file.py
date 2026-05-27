#!/usr/bin/env python3


def read_file(filename=""):
    with open(filename, "r", encoding="utf-8") as f:
        file = f.read()
        print(file)

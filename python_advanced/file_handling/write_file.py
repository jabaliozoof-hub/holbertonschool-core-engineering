#!/usr/bin/env python3
"""Module containing a function to write text to a file."""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns characters written."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

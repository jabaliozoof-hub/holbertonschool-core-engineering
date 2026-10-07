#!/usr/bin/env python3
"""Module containing a function that appends a string to a file."""


def append_write(filename="", text=""):
    """Appends a string to a UTF8 file and returns chars added."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

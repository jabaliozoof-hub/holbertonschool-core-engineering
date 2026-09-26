#!/usr/bin/env python3
"""
Module verboselist
Defines a custom VerboseList class extending the built-in list class
to print notification messages on modifications (append, extend, remove, pop).
"""


class VerboseList(list):
    """Custom list class that prints notifications on modifications."""

    def append(self, item):
        """Add an item to the list and print a notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend the list with items from an iterable and print a notification."""
        items_list = list(iterable)
        count = len(items_list)
        super().extend(items_list)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """Remove an item from the list after printing a notification."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Pop an item from the list at the given index after printing a notification."""
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)

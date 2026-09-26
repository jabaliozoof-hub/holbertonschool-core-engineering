#!/usr/bin/env python3
"""
Module flyingfish
Demonstrates multiple inheritance using Fish and Bird classes,
and a FlyingFish class that inherits from both and overrides their methods.
"""


class Fish:
    """Class representing a fish."""

    def swim(self):
        """Print swimming behavior of a fish."""
        print("The fish is swimming")

    def habitat(self):
        """Print the habitat of a fish."""
        print("The fish lives in water")


class Bird:
    """Class representing a bird."""

    def fly(self):
        """Print flying behavior of a bird."""
        print("The bird is flying")

    def habitat(self):
        """Print the habitat of a bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Class representing a flying fish, inheriting from both Fish and Bird."""

    def fly(self):
        """Print flying behavior of a flying fish."""
        print("The flying fish is soaring!")

    def swim(self):
        """Print swimming behavior of a flying fish."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Print the habitat of a flying fish."""
        print("The flying fish lives both in water and the sky!")

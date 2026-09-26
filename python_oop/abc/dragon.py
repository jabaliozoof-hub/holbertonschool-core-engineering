#!/usr/bin/env python3
"""
Module dragon
Defines mixin classes SwimMixin and FlyMixin, and a Dragon class
that combines both behaviors along with its own roar method.
"""


class SwimMixin:
    """Mixin providing swimming behavior."""

    def swim(self):
        """Print swimming behavior message."""
        print("The creature swims!")


class FlyMixin:
    """Mixin providing flying behavior."""

    def fly(self):
        """Print flying behavior message."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Class representing a dragon, inheriting from both SwimMixin and FlyMixin."""

    def roar(self):
        """Print roaring behavior message."""
        print("The dragon roars!")

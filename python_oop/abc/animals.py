#!/usr/bin/env python3
"""
Module animals
Defines an abstract base class Animal and its concrete subclasses Dog and Cat.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing an animal."""

    @abstractmethod
    def sound(self):
        """Abstract method to get the sound of the animal."""
        pass


class Dog(Animal):
    """Concrete class representing a dog."""

    def sound(self):
        """Return the sound of a dog."""
        return "Bark"


class Cat(Animal):
    """Concrete class representing a cat."""

    def sound(self):
        """Return the sound of a cat."""
        return "Meow"

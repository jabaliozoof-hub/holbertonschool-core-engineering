#!/usr/bin/env python3
"""
Module 0-polymorphism_demo
Demonstrates the concepts of inheritance and polymorphism in Python.
"""


class Animal:
    """Base class representing a generic animal."""

    def speak(self):
        """Returns a generic sound."""
        return "Some sound"


class Dog(Animal):
    """Subclass Dog inheriting from Animal."""

    def speak(self):
        """Returns a dog bark."""
        return "Woof"


class Cat(Animal):
    """Subclass Cat inheriting from Animal."""

    def speak(self):
        """Returns a cat meow."""
        return "Meow"


if __name__ == "__main__":
    # Demonstrating polymorphism with a list of different objects
    animals = [Dog(), Cat(), Dog()]

    for animal in animals:
        print(animal.speak())

    # Checking class and object relationships
    dog = Dog()
    print(isinstance(dog, Dog))
    print(isinstance(dog, Animal))
    print(issubclass(Dog, Animal))

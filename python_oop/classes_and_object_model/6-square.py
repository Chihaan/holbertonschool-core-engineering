#!/usr/bin/env python3
"""
Module pour la classe Square.

Ce module définit la classe Square qui permet de gérer
la taille et la position d'un carré,
de calculer son aire, de l'afficher et de le convertir en
chaîne de caractères.
"""


class Square:
    """Classe représentant un carré avec
    gestion de la taille et de la position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialise un carré avec une taille et une position données.

        Args:
            size (int): La taille du côté du carré (par défaut 0).
            position (tuple): Position du carré (par défaut (0, 0)).
        """
        self.size = size
        self.position = position

    def area(self):
        """Retourne l'aire du carré."""
        return self.__size ** 2

    def __str__(self):
        """Retourne une représentation en chaîne du carré."""
        result = ""
        if self.size == 0:
            result += "\n"
            return result
        for i in range(self.position[1]):
            result += "\n"
        for length in range(self.size):
            result += " " * self.position[0] + "#" * self.size + "\n"
        result = result.rstrip("\n")
        return result

    @property
    def size(self):
        """Retourne la taille du carré."""
        return self.__size

    @size.setter
    def size(self, value):
        """Définit la taille du carré.

        Args:
            value (int): Nouvelle taille du carré.

        Raises:
            TypeError: Si value n'est pas un entier.
            ValueError: Si value est négatif.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Affiche le carré avec le caractère #
        en tenant compte de la position.
        """
        result = ""
        if self.size == 0:
            print()
            return
        for i in range(self.position[1]):
            print()
        for length in range(self.size):
            print(" " * self.position[0] + "#" * self.size)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not isinstance(value[0], int)
            or not isinstance(value[1], int)
            or value[0] < 0
            or value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

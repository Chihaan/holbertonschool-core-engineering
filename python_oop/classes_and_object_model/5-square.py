#!/usr/bin/env python3
"""
Module pour la classe Square.

Ce module définit la classe Square qui permet de gérer la taille d'un carré,
de calculer son aire et de l'afficher avec le caractère #.
"""


class Square:
    """Classe représentant un carré avec gestion de la taille et affichage."""

    def __init__(self, size=0):
        """Initialise un carré avec une taille donnée.

        Args:
            size (int): La taille du côté du carré (par défaut 0).
        """
        self.size = size

    def area(self):
        """Retourne l'aire du carré."""
        return self.__size ** 2

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
        """Affiche le carré avec le caractère #."""
        if self.size == 0:
            print()
            return
        for height in range(self.size):
            for length in range(self.size):
                print("#", end="")
            print()

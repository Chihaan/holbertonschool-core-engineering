#!/usr/bin/env python3
"""Module pour la classe Square.

Ce module définit la classe Square qui représente un carré avec une taille
et fournit une méthode pour calculer son aire.
"""


class Square:
    """Représente un carré.

    Attributes:
        __size (int): La taille du côté du carré.
    """

    def __init__(self, size=0):
        """Initialise un carré avec une taille donnée.

        Args:
            size (int): La taille du côté du carré. Valeur par défaut 0.

        Raises:
            TypeError: Si size n'est pas un entier.
            ValueError: Si size est inférieur à 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Retourne l'aire du carré.

        Returns:
            int: L'aire du carré.
        """
        return self.__size ** 2

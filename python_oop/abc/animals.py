#!/usr/bin/env python3



"""
Module pour la hiérarchie d'animaux utilisant les classes abstraites.

Ce module définit une classe abstraite Animal et ses sous-classes Dog et Cat.
"""

#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Classe abstraite représentant un animal.
    Les sous-classes doivent implémenter la méthode sound.
    """

    @abstractmethod
    def sound(self):
        """
        Retourne le cri de l'animal.
        Cette méthode doit être implémentée par les sous-classes.
        """
        pass


class Dog(Animal):
    """
    Classe représentant un chien.
    """

    def sound(self):
        """
        Retourne le cri du chien.
        Returns:
            str: "Bark"
        """
        return "Bark"
    

class Cat(Animal):
    """
    Classe représentant un chat.
    """

    def sound(self):
        """
        Retourne le cri du chat.
        Returns:
            str: "Meow"
        """
        return "Meow"
    

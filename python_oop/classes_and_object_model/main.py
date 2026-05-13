#!/usr/bin/env python3
"""
Script de test pour la classe Square.

Ce script importe la classe Square et affiche des exemples d'utilisation.
"""

Square = __import__('6-square').Square

my_square = Square(5, (0, 0))
print(my_square)

print("--")

my_square = Square(5, (4, 1))
print(my_square)

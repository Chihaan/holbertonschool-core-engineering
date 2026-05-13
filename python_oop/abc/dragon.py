#!/usr/bin/env python3
"""
Module pour la classe Dragon et les mixins SwimMixin et FlyMixin.

Ce module montre l'utilisation de l'héritage multiple avec des mixins pour ajouter des comportements.
"""

class SwimMixin:
    """Mixin ajoutant la capacité de nager."""
    def swim(self):
        print("The creature swims!")

class FlyMixin:
    """Mixin ajoutant la capacité de voler."""
    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """Classe représentant un dragon qui peut nager, voler et rugir."""
    def roar(self):
        print("The dragon roars!")
#!/usr/bin/env python3



class SwimMixin:
    def swim(self):
        print("The creature swims!")

class FlyMixin:
    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")



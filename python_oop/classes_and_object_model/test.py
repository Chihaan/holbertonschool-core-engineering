#!/usr/bin/env python3


class Voiture:
    def __init__(self, marque, couleur, carburant):
        self.marque = marque
        self.couleur = couleur
        self.carburant = carburant

    @property
    def marque(self):
        return self.__marque
    
    @property
    def couleur(self):
        return self.__couleur
    
    @property
    def carburant(self):
        return self.__carburant
    
    
    
    
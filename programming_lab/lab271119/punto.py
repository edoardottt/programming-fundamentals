#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 09:18:12 2019

@author: angelo
"""


class Punto:
    """un punto bidimensionale"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Punto({},{})".format(self.x, self.y)

    def __repr__(self):
        return "Punto(x={},y={})".format(self.x, self.y)

    def __sub__(self, altro_punto):
        return self.distanza(altro_punto)

    def distanza(self, altro_punto):
        if self.x == altro_punto.x:
            d = abs(self.y - altro_punto.y)
        elif self.y == altro_punto.y:
            d = abs(self.x - altro_punto.x)
        else:
            d = ((self.x - altro_punto.x) ** 2 + (self.y - altro_punto.y) ** 2) ** 0.5
        return d


class Quadrato:
    """un quadrato nel piano cartesiano"""

    def __init__(self, p, lato):
        #        if not isinstance(p, Punto):
        if type(p) != Punto:
            raise TypeError("l'oggetto Quadrato ha bisogno di un punto di origine")
        if not isinstance(lato, (int, float)):
            raise TypeError("l'oggetto Quadrato ha bisogno di un lato di tipo numerico")
        if lato == 0:
            raise ValueError("il lato del Quadrato non può essere 0")
        if lato < 0:
            lato = -lato
            p = Punto(p.x - lato, p.y - lato)
        self.vertice_as = Punto(p.x, p.y)
        self.vertice_ad = Punto(p.x + lato, p.y)
        self.vertice_bs = Punto(p.x, p.y + lato)
        self.vertice_bd = Punto(p.x + lato, p.y + lato)

    def perimetro(self):
        """ritorna il perimetro del quadrato"""
        return self.vertice_ad.distanza(self.vertice_as) * 4

    def area(self):
        """ritorna l'area del quadrato"""
        return self.vertice_ad.distanza(self.vertice_as) ** 2


class Rettangolo:
    """un rettangolo nel piano cartesiano"""

    def __init__(self, p1, p2):
        if type(p1) != Punto or type(p2) != Punto:
            raise TypeError("Il rettangolo ha due Punti come vertici")
        if p1.x == p2.x or p1.y == p2.y:
            raise ValueError("Il rettangolo ha una dimensione nulla")
        self.vertice_as = Punto(min(p1.x, p2.x), min(p1.y, p2.y))
        self.vertice_bd = Punto(max(p1.x, p2.x), max(p1.y, p2.y))
        self.vertice_ad = Punto(self.vertice_bd.x, self.vertice_as.y)
        self.vertice_bs = Punto(self.vertice_as.x, self.vertice_bd.y)

        self.base = self.vertice_bd - self.vertice_bs
        self.altezza = self.vertice_bs - self.vertice_as

    def perimetro(self):
        return self.base * 2 + self.altezza * 2

    def area(self):
        return self.base * self.altezza

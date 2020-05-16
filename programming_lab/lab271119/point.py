#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 13:06:47 2019

@author: angelo
"""

class Punto:
    def __init__(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError ('Non posso creare un punto con parametri non numerici')
        self.x = x
        self.y = y


    def __repr__(self):
        return 'Oggetto Punto(x={}, y={})'.format(self.x, self.y)


    def __str__(self):
        return 'Punto({},{})'.format(self.x, self.y)


    def distanza(self, carletto):
        if type(carletto) != Punto:
            raise TypeError ('Non posso calcolare la distanza con qualcosa che non è un punto')
        return ((carletto.x - self.x)**2+(carletto.y - self.y)**2)**0.5


class Rettangolo:
    def __init__(self, p1, p2):
        if type(p1) != Punto or type(p2) != Punto:
            raise TypeError('Un rettangolo è definito da due punti')
        if p1.x==p2.x or p1.y==p2.y:
            raise ValueError('I punti non definiscono un rettangolo')
        if p1.x > p2.x:
            xs, xd = p2.x, p1.x
        else:
            xs, xd = p1.x, p2.x
        if p1.y > p2.y:
            ya, yb = p2.y, p1.y
        else:
            ya, yb = p1.y, p2.y
        self.vas = Punto(xs, ya)
        self.vad = Punto(xd, ya)
        self.vbs = Punto(xs, yb)
        self.vbd = Punto(xd, yb)

        self.base = xd - xs
        self.altezza = yb - ya

    def __len__(self):
        return 4

    def calcola_base(self):
        return self.vbs.distanza(self.vbd)


    def calcola_altezza(self):
        return self.vas.distanza(self.vbs)


    def calcola_diagonale(self):
        return self.vas.distanza(self.vbd)


    def calcola_area(self):
        return self.calcola_base() * self.calcola_altezza()


    def calcola_perimetro(self):
        return self.base*2 + self.altezza*2











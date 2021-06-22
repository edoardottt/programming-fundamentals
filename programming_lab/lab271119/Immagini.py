#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 12:24:19 2019

@author: angelo
"""

from immagini import load, save
from punto import Rettangolo, Quadrato, Punto

nero = (0, 0, 0)
bianco = (255, 255, 255)
rosso = (255, 0, 0)
verde = (0, 255, 0)
blu = (0, 0, 255)
amazon = (59, 122, 87)


class Immagine:
    """La classe immagine"""

    def __init__(self, altezza=640, larghezza=480, colore_sfondo=bianco):
        self.imm = [[colore_sfondo] * larghezza for _ in range(altezza)]
        self.larghezza = larghezza
        self.altezza = altezza
        self.colore_sfondo = colore_sfondo

    def __str__(self):
        return "Immagine(h = {}, l = {}, sfondo = {})".format(
            self.altezza, self.larghezza, self.colore_sfondo
        )

    def __repr__(self):
        return self.__str__()

    def disegna_rettangolo(self, rettangolo, colore):
        if not isinstance(rettangolo, (Rettangolo, Quadrato)):
            raise TypeError("Disegna rettangolo disegna rettangoli")
        for y in range(rettangolo.vertice_as.y, rettangolo.vertice_bs.y + 1):
            for x in range(rettangolo.vertice_as.x, rettangolo.vertice_ad.x + 1):
                self.imm[y][x] = colore

    def salva(self, nome_file):
        if type(nome_file) != str or not nome_file.endswith(".png"):
            raise TypeError("Posso solo salvare su file .png")
        save(self.imm, nome_file)

    def __add__(self, r):
        self.disegna_rettangolo(r, nero)

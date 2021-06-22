#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 15:14:02 2019

@author: angelo
"""

from point import Punto, Rettangolo
from immagini import load, save

nero = (0, 0, 0)
bianco = (255, 255, 255)
rosso = (255, 0, 0)
verde = (0, 255, 0)
blu = (0, 0, 255)
amazon = (59, 122, 87)


class Disegno:
    def __init__(self, larghezza=1024, altezza=768, sfondo=nero):
        self.immagine = [[sfondo] * larghezza for _ in range(altezza)]
        self.altezza = altezza
        self.larghezza = larghezza
        self.sfondo = sfondo

    def salva(self, nome_immagine):
        save(self.immagine, nome_immagine)

    def __repr__(self):
        return "Disegno largo {} pixel e alto {} pixel, di colore {}".format(
            self.larghezza, self.altezza, self.sfondo
        )

    def disegna_rettangolo(self, rettangolo, colore):
        if type(rettangolo) != Rettangolo:
            raise TypeError("Disegno solo rettangoli")
        for y in range(rettangolo.vas.y, rettangolo.vbs.y + 1):
            for x in range(rettangolo.vas.x, rettangolo.vad.x + 1):
                self.immagine[y][x] = colore

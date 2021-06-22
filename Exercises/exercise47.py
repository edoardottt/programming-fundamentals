#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 15:14:37 2019

@author: edoardottt
https://www.edoardoottavianelli.it
https://www.github.com/edoardottt
"""

from untitled0 import Rettangolo
from immagini import save

nero = (0, 0, 0)
bianco = (255, 255, 255)
rosso = (255, 0, 0)
verde = (0, 255, 0)
blu = (0, 0, 255)


class Disegno:
    def __init__(self, altezza=768, larghezza=1024, sfondo=nero):
        self.immagine = [[sfondo] * larghezza for _ in range(altezza)]
        self.altezza = altezza
        self.larghezza = larghezza
        self.sfondo = sfondo

    def salva(self, titolo):
        save(self.immagine, titolo)

    def __repr__(self):
        return "Disegno largo {} e alto {} di colore {}".format(
            self.larghezza, self.altezza, self.sfondo
        )

    def disegna_rettangolo(self, rettangolo, colore):
        if not type(rettangolo) == Rettangolo:
            raise TypeError("Disegno solo rattengoli.")
        for y in range(rettangolo.vas.y, rettangolo.vbs.y + 1):
            for x in range(rettangolo.vas.x, rettangolo.vad.x + 1):
                self.immagine[y][x] = colore

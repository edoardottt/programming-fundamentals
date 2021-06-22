#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 12:43:37 2019

@author: angelo
"""
from immagini import *


nero = (0, 0, 0)
bianco = (255, 255, 255)
rosso = (255, 0, 0)
verde = (0, 255, 0)
blu = (0, 0, 255)

scacchiera = []
for i in range(10):
    riga = []
    for j in range(10):
        if (i + j) % 2 == 0:
            colore = nero
        else:
            colore = bianco
        riga.append(colore)
    scacchiera.append(riga)

quadrato = [[nero] * 10 for _ in range(10)]
save(quadrato, "quadnero.png")

save(scacchiera, "scacchiera.png")


def cornice(immagine, colore):
    """prende l'immagine e la modifica creando una cornice di un pixel colore colore"""
    for indice in range(len(immagine[0])):
        immagine[0][indice] = colore
        immagine[len(immagine) - 1][indice] = colore
    for indice in range(len(immagine)):
        immagine[indice][0] = colore
        immagine[indice][len(immagine[0]) - 1] = colore
    return

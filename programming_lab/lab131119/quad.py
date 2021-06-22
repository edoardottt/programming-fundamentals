#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 17:07:29 2019

@author: angelo

Scrivere una funzione
quad(imm, x, y, lato, colore)
che prende un'immagine e disegna nell'immagine un quadrato di lato lato del colore colore a partire dal pixel imm[x][y]
L'immagine presa come argomento DEVE RISULTARE MODIFICATA

00000000
00000000
00000000
00000000
00000000

00000000
01110000
01110000
01110000
00000000

"""
from immagini01 import *
from immagini import load, save


def quad(imm, x, y, lato, colore):
    for i in range(x, x + lato):
        for j in range(y, y + lato):
            imm[i][j] = colore


def quad_vuoto(imm, x, y, lato, colore):
    for i in range(lato):
        imm[x][y + i] = colore
        imm[x + lato - 1][y + i] = colore
        imm[x + i][y] = colore
        imm[x + i][y + lato - 1] = colore

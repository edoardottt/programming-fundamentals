#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 16:39:22 2019

@author: angelo
"""

rosso = (255,0,0)
verde = (0,255,0)
blue  = (0,0,255)
nero = (0,0,0)
bianco = (255,255,255)

def genera_immagine(altezza, larghezza, colore):
    imm = []
    for i in range(altezza):
        riga = [colore] * larghezza
        imm.append(riga)
    return imm


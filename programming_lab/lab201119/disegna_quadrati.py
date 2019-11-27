#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 11:31:37 2019

@author: angelo
Scrivere una funzione disegna_quadrato_colorato(imm, x1, y1, x2, y2, colore_bordo, colore_interno) che prende

    una immagine imm come lista di liste di tuple di colore
    due punti x1,y1 e x2,y2 corrispondenti a due spigoli di un rettangolo
    due tuple di colori colore_bordo e colore_interno
    e modifica la immagine imm disegnando il rettangolo individuato dai due punti x1,y1 e x2,y2, usando colore_bordo per il perimetro del rettangolo e colore_interno per l'area. La funzione ritorna il numero di pixel modificati in imm.
"""

from immagini import load, save

nero = (0,0,0)
bianco = (255,255,255)
rosso = (255,0,0)
verde = (0,255,0)
blu = (0,0,255)
amazon = (59,122,87)

imm = []
altezza = 50
larghezza = 120
for i in range(altezza):
    riga = [nero] * larghezza
    imm.append(riga)

save(imm, 'rettangolo_50_120.png')

for i in range(len(imm[0])):
    for j in range(5):
        imm[j][i]=rosso
        imm[-j-1][i]=rosso

for i in range(len(imm)):
    for j in range(5):
        imm[i][j]=rosso
        imm[i][-j-1]=rosso

save(imm, 'rettangolo_50_120_constriscia.png')

def disegna_quadrato_colorato(imm, x1, y1, x2, y2, colore_bordo, colore_interno):
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1
    for riga in range(y1+1, y2):
        imm[riga][x1] = colore_bordo
        imm[riga][x2] = colore_bordo
        for pixel in range(x1+1, x2):
            imm[riga][pixel] = colore_interno
    for riga in [y1, y2]:
        for pixel in range(x1, x2+1):
            imm[riga][pixel] = colore_bordo



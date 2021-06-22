# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 11:10:09 2019

@author: edoardottt
https://www.edoardoottavianelli.it
https://www.github.com/edoardottt
"""

"""
Write a function
disegna_quadrato_colorato(imm, x1, y1, x2, y2, colore_bordo, colore_interno)
that take as input an image imm as list of lists of color's tuples,
two points x1,y1 and x2,y2 as two vertex of a rectangle,
two tuples of colors colore_bordo and colore_interno and edits the image
imm drawing a rectangle identified by two points using colore_bordo
for perimeter and colore_interno for the internal area.
The function returns the number of pixels modified.
"""

import immagini

tigre = immagini.load("tigre.png")


def disegna_quadrato_colorato(imm, x1, y1, x2, y2, colore_bordo, colore_interno):
    imm, pixels = disegna_bordo(imm, x1, y1, x2, y2, colore_bordo, 0)
    altezza = y1 - y2
    larghezza = x2 - x1
    x1 += 1
    y2 += 1
    for i in range(altezza - 1):
        for j in range(larghezza - 1):
            imm[x1 + j][y2 + i] = colore_interno
            pixels += 1
    immagini.save(imm, "imm.png")
    return pixels


def disegna_bordo(imm, x1, y1, x2, y2, colore_bordo, p):
    altezza = y1 - y2
    larghezza = x2 - x1
    for i in range(altezza):
        imm[x2][y2 + i] = colore_bordo
        imm[x1][y2 + i] = colore_bordo
        p += 2
    for i in range(larghezza):
        imm[x1 + i][y2] = colore_bordo
        imm[x1 + i][y1] = colore_bordo
        p += 2
    return imm, p


print(disegna_quadrato_colorato(tigre, 30, 100, 80, 20, (255, 0, 0), (0, 255, 0)))

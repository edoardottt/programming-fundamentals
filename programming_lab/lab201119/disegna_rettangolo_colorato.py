#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 17:38:49 2019

@author: angelo
Scrivere una funzione disegna_rettangolo_colorato(imm, x1, y1, x2, y2, colore_bordo, colore_interno) che prende

    una immagine imm come lista di liste di tuple di colore
    due punti x1,y1 e x2,y2 corrispondenti a due spigoli di un rettangolo
    due tuple di colori colore_bordo e colore_interno
    e modifica la immagine imm disegnando il rettangolo individuato dai due punti x1,y1 e x2,y2, usando colore_bordo per il perimetro del rettangolo e colore_interno per l'area. La funzione ritorna il numero di pixel modificati in imm.

    """


def disegna_rettangolo_colorato(imm, x1, y1, x2, y2, colore_bordo, colore_interno):
    imm[y1][x1:x2] = [colore_bordo] * (x2 - x1)
    imm[y2][x1:x2] = [colore_bordo] * (x2 - x1)
    for riga in range(y1 + 1, y2):
        imm[riga][x1:x2] = (
            [colore_bordo] + [colore_interno] * (x2 - x1 - 2) + [colore_bordo]
        )

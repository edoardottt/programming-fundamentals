# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 11:53:11 2019

@author: edoardottt
https://www.edoardoottavianelli.it
https://www.github.com/edoardottt
"""

"""
Write a function scala_di_grigi(imm) that take as input an image imm
and edits it transforming it in grey scale, using the grey scale formula.
"""

import immagini


def grey(imm):
    altezza = len(imm)
    larghezza = len(imm[0])
    for i in range(altezza):
        for j in range(larghezza):
            imm[i][j] = grey_scale(imm[i][j])
    return imm


def to_int(Y):
    return int(Y * 255)


def grey_scale(t):
    r, g, b = t[0], t[1], t[2]
    if r != 0:
        r = r / 255
    if g != 0:
        g = g / 255
    if b != 0:
        b = b / 255
    if r < 0.04045:
        Cr = r / 12.92
    else:
        Cr = ((r + 0.055) / 1.055) ** 2.4
    if g < 0.04045:
        Cg = g / 12.92
    else:
        Cg = ((g + 0.055) / 1.055) ** 2.4
    if b < 0.04045:
        Cb = b / 12.92
    else:
        Cb = ((b + 0.055) / 1.055) ** 2.4
    Ylinear = 0.2126 * Cr + 0.7152 * Cg + 0.0722 * Cb
    if Ylinear <= 0.0031308:
        Yr, Yg, Yb = Ylinear * 12.92, Ylinear * 12.92, Ylinear * 12.92
    else:
        Yr, Yg, Yb = (
            1.055 * (Ylinear) ** (1 / 2.4) - 0.055,
            1.055 * (Ylinear) ** (1 / 2.4) - 0.055,
            1.055 * (Ylinear) ** (1 / 2.4) - 0.055,
        )
    return to_int(Yr), to_int(Yg), to_int(Yb)


tigre = immagini.load("tigre.png")
img = grey(tigre)
immagini.save(img, "imma.png")

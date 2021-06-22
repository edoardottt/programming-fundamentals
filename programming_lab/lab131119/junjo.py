#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 18:09:26 2019

@author: angelo
"""


# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 19:10:42 2019

@author: Juanjo
"""

import png

"""
Carica l'immagine PNG e torna una matrice con i pixel, in cui ogni pixel è una tupla RGB (boxed row boxed pixel)
"""


def load(fname):
    with open(fname, mode="rb") as f:
        reader = png.Reader(f)
        w, h, png_img, _ = reader.asRGB8()
        img = []
        for line in png_img:
            l = []
            for i in range(0, len(line), 3):
                l += [(line[i], line[i + 1], line[i + 2])]
            img += [l]
        return img


"""
Salva l'immagine img nel file filename in formato PNG8
"""


def save(img, filename):
    pngimg = png.from_array(img, "RGB")
    pngimg.save(filename)


"""
Crea un'immagine dati i valori height, width e tupla
"""


def crea(h, w, t=(0, 0, 0)):
    return [[t for i in range(w)] for j in range(h)]


"""
Ruota l'immagine intorno al suo asse orizzontale
"""


def ruota1(img):
    h, w = len(img), len(img[0])
    ret = crea(h, w, (0, 0, 0))
    for y in range(h):
        for x in range(w):
            ret[y][x] = img[h - 1 - y][x]
    return ret

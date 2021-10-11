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
Load the PNG image and return a matrix with pixels, where each pixel is an RGB (boxed row boxed pixel) tuple
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
Save the img image in the filename file in PNG8 format
"""


def save(img, filename):
    pngimg = png.from_array(img, "RGB")
    pngimg.save(filename)


"""
Create an image given the height, width and tuple values
"""


def create(h, w, t=(0, 0, 0)):
    return [[t for i in range(w)] for j in range(h)]


"""
Rotate the image around its horizontal axis
"""


def rotate(img):
    h, w = len(img), len(img[0])
    ret = create(h, w, (0, 0, 0))
    for y in range(h):
        for x in range(w):
            ret[y][x] = img[h - 1 - y][x]
    return ret

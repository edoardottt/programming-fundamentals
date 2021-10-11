#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 12:43:37 2019

@author: angelo
"""
from images import *


black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

chessboard = []
for i in range(10):
    row = []
    for j in range(10):
        if (i + j) % 2 == 0:
            color = black
        else:
            color = white
        row.append(color)
    chessboard.append(row)

square = [[black] * 10 for _ in range(10)]
save(square, "quadnero.png")

save(chessboard, "chessboard.png")


def frame(image, colore):
    """takes the image and modifies it by creating a frame of a color color pixel"""
    for index in range(len(image[0])):
        image[0][index] = color
        image[len(image) - 1][index] = color
    for index in range(len(image)):
        image[index][0] = color
        image[index][len(image[0]) - 1] = color
    return

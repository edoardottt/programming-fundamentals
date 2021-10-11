#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 17:07:29 2019

@author: angelo

Write a function
quad(pic, x, y, side, color)
which takes an image and draws in the image a square on the side of the color color starting from the pixel pic [x] [y] 
The image taken as argument MUST BE MODIFIED

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
from images01 import *
from images import load, save


def quad(pic, x, y, side, color):
    for i in range(x, x + side):
        for j in range(y, y + side):
            pic[i][j] = color


def quad_blank(pic, x, y, side, color):
    for i in range(side):
        pic[x][y + i] = color
        pic[x + side - 1][y + i] = color
        pic[x + i][y] = color
        pic[x + i][y + side - 1] = color

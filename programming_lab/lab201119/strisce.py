#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 16:05:46 2019

@author: angelo
"""

mango = (255, 119, 51)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
ultra = (255, 102, 255)

from images import load, save


def stripes(pic, col1, col2):
    """Fills the pic image with streaks of alternating colors col1, col2"""
    for i in range(0, len(pic), 2):
        pic[i] = [col1] * len(pic[0])
        pic[i + 1] = [col2] * len(pic[0])
    if len(pic) % 2 == 1:
        pic[-1] = [col1] * len(pic[0])


def stripes_ver(pic, col1, col2):
    for i in range(len(pic)):
        for j in range(len(pic[0])):
            if j % 2 == 0:
                pic[i][j] = col1
            else:
                pic[i][j] = col2


def stripes_ver2(pic, col1, col2):
    for i in range(len(pic)):
        pic[i][: len(pic[0])] = [col1, col2] * (len(pic[0]) // 2)
    if len(pic[0]) % 2 == 1:
        for i in range(len(pic)):
            pic[i][-1] = col1

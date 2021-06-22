#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 16:05:46 2019

@author: angelo
"""

mango = (255, 119, 51)
nero = (0, 0, 0)
bianco = (255, 255, 255)
rosso = (255, 0, 0)
verde = (0, 255, 0)
blu = (0, 0, 255)
ultra = (255, 102, 255)

from immagini import load, save


def strisce(imm, col1, col2):
    """Riempie l'immagine imm con strisce di colori alternati col1, col2"""
    for i in range(0, len(imm), 2):
        imm[i] = [col1] * len(imm[0])
        imm[i + 1] = [col2] * len(imm[0])
    if len(imm) % 2 == 1:
        imm[-1] = [col1] * len(imm[0])


def strisce_ver(imm, col1, col2):
    for i in range(len(imm)):
        for j in range(len(imm[0])):
            if j % 2 == 0:
                imm[i][j] = col1
            else:
                imm[i][j] = col2


def strisce_ver2(imm, col1, col2):
    for i in range(len(imm)):
        imm[i][: len(imm[0])] = [col1, col2] * (len(imm[0]) // 2)
    if len(imm[0]) % 2 == 1:
        for i in range(len(imm)):
            imm[i][-1] = col1

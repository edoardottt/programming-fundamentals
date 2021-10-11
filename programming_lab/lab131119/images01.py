#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 16:39:22 2019

@author: angelo
"""

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)


def generate_image(height, length, color):
    imm = []
    for i in range(height):
        row = [color] * length
        imm.append(row)
    return imm

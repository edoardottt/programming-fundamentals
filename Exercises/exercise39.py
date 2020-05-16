#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 16:40:08 2019

@author: edoardottt
https://www.edoardoottavianelli.it
https://www.github.com/edoardottt
"""
'''
Write a function that take as input a,l and c.
a is the height of an image, l is the length and c the color.
Returns an image with those specs.
'''
from immagini import save

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)
white = (255,255,255)

def generate_img(a,l,c):
    img = []
    for i in range(a):
        riga = [c]*l
        img.append(riga)
    return img

img = generate_img(290,600,green)
save(img,'imma.png')
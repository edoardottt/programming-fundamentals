#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 17:09:55 2019

@author: edoardottt
https://www.edoardoottavianelli.it
https://www.github.com/edoardottt
"""

'''
Write a function
quad(imm,x,y,lato,colore)
that take as input an image and builds a square with side named 'lato' and
color 'colore' from pixel imm[x][y].
'''
import immagini

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)

def quad(imm,x,y,lato,colore):
    for i in range(lato):
        imm[x][y+i] = colore
        imm[x+lato][y+i] = colore
        imm[x+i][y] = colore
        imm[x+i][y+lato] = colore
    return imm

def quadP(imm,x,y,lato,colore):
    for i in range(lato):
        for j in range(lato):
            imm[x+i][y+j] = colore
    return imm

def generate_img(lato,colore):
    img = []
    for i in range(lato):
        riga = [colore]*lato
        img.append(riga)
    return img

intermediate = quad(generate_img(1000,black),400,400,100,red)
intermediate = quadP(intermediate,550,550,100,white)
immagini.save(intermediate,'imma.png')
tigre = immagini.load('tigre.png')
l = len(tigre)
intermediate = quad(tigre,l//2,l//2,100,red)
intermediate = quadP(intermediate,l//2+(l//4),l//2+(l//4),100,white)
immagini.save(intermediate,'imma2.png')
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 12:19:36 2019

@author: edoardottt
https://www.edoardoottavianelli.it
https://www.github.com/edoardottt
"""

'''
Write a function disegna_quadrati(imm, lista) that take as input an image
imm as list of lists of colour's tuples and edits it drawing al th squares 
in the list. Every element of the list is composed by (x, y, lato, colore),
 where x,y is the vertex on top left,
 lato is the length of the edge,
 colore is the tuple fo color
Example of a square's list:
    [(20,20,40,(255,255,255)), 
    (30,30,30,(180,180,180)), 
    (40,40,20,(100,100,100))]
'''
import immagini
def disegna_quadrati(imm, lista):
    for i in lista:
        x,y,lato,colore = i[0],i[1],i[2],i[3]
        for i in range(i[2]):
            imm[x][y+i] = colore
            imm[x+lato][y+i] = colore
            imm[x+i][y] = colore
            imm[x+i][y+lato] = colore
    return imm

tigre = immagini.load('tigre.png')
imm = disegna_quadrati(tigre,[(20,20,40,(255,255,255)), 
    (30,30,30,(180,180,180)), 
    (40,40,20,(100,100,100))])
immagini.save(imm,'imma2.png')
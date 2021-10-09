#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 11:31:37 2019

@author: angelo
Write a draw_color_square function (pic, x1, y1, x2, y2, border_color, inner_color) that takes

    an image pic as a list of color tuple lists 10 two points x1, y1 and x2, y2 corresponding to two edges of a rectangle 11 two color tuples border_color and inner_color 12 and modify the image im by drawing the rectangle identified by the two points x1, y1 and x2, y2, using color_border for the perimeter of the rectangle and color_in for the area. The function returns the number of pixels modified in images.
"""

from images import load, save

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
amazon = (59,122,87)

pic = []
height = 50
length = 120
for i in range(height):
    row = [black] * length
    pic.append(row)

save(pic, 'rectangle_50_120.png')

for i in range(len(pic[0])):
    for j in range(5):
        pic[j][i]=red
        pic[-j-1][i]=red

for i in range(len(pic)):
    for j in range(5):
        pic[i][j]=red
        pic[i][-j-1]=red

save(pic, 'rectangle_50_120_construct.png')

def draw_colorful_square(pic, x1, y1, x2, y2, border_color, interior_color):
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1
    for row in range(y1+1, y2):
        pic[row][x1] = border_color
        pic[row][x2] = border_color
        for pixel in range(x1+1, x2):
            pic[row][pixel] = interior_color
    for row in [y1, y2]:
        for pixel in range(x1, x2+1):
            pic[row][pixel] = border_color



#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 17:38:49 2019

@author: angelo
Write a draw_colorful_rectangle function (pic, x1, y1, x2, y2, border_color, inner_color) that takes

    an image pic as a list of color tuple lists 10 two points x1, y1 and x2, y2 corresponding to two edges of a rectangle 11 two color tuples border_color and inner_color 12 and modify the image im by drawing the rectangle identified by the two points x1, y1 and x2, y2, using color_border for the perimeter of the rectangle and color_in for the area. The function returns the number of pixels modified in images.

    """


def draw_colorful_rectangle(pic, x1, y1, x2, y2, border_color, interior_color):
    pic[y1][x1:x2] = [border_color] * (x2 - x1)
    pic[y2][x1:x2] = [border_color] * (x2 - x1)
    for row in range(y1 + 1, y2):
        pic[row][x1:x2] = (
            [border_color] + [interior_color] * (x2 - x1 - 2) + [border_color]
        )

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 15:14:02 2019

@author: angelo
"""

from point import Punto, Rectangle
from images import load, save

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
amazon = (59, 122, 87)


class Drawing:
    def __init__(self, length=1024, height=768, background=black):
        self.image = [[background] * length for _ in range(height)]
        self.height = height
        self.length = length
        self.background = background

    def save(self, image_name):
        save(self.image, image_name)

    def __repr__(self):
        return "Design {} pixel wide and {} pixel high, color {}".format(
            self.length, self.height, self.background
        )

    def draw_rectangle(self, rectangle, color):
        if type(rectangle) != Rectangle:
            raise TypeError("I draw only rectangles")
        for y in range(rectangle.vas.y, rectangle.vbs.y + 1):
            for x in range(rectangle.vas.x, rectangle.vad.x + 1):
                self.image[y][x] = color

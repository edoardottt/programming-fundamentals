#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 12:24:19 2019

@author: angelo
"""

from images import load, save
from point import Rectangle, Square, Point

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
amazon = (59, 122, 87)


class Image:
    """The image class"""

    def __init__(self, height=640, length=480, background_color=white):
        self.imm = [[background_color] * length for _ in range(height)]
        self.length = length
        self.height = height
        self.background_color = background_color

    def __str__(self):
        return "Image (h = {}, l = {}, background = {})".format(
            self.height, self.length, self.background_color
        )

    def __repr__(self):
        return self.__str__()

    def draw_rectangle(self, rectangle, color):
        if not isinstance(rectangle, (Rectangle, Quadrato)):
            raise TypeError("Disegna rettangolo disegna rettangoli")
        for y in range(rectangle.vertice_as.y, rectangle.vertice_bs.y + 1):
            for x in range(rectangle.vertice_as.x, rectangle.vertice_ad.x + 1):
                self.imm[y][x] = color

    def sava(self, nome_file):
        if type(nome_file) != str or not nome_file.endswith(".png"):
            raise TypeError("I can only save to file .png")
        save(self.imm, file_name)

    def __add__(self, r):
        self.draw_rectangle(r, black)

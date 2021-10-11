#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 13:06:47 2019

@author: angelo
"""


class Punto:
    def __init__(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("I cannot create a point with non-numeric parameters")
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point object (x = {}, y = {})".format(self.x, self.y)

    def __str__(self):
        return "Point({},{})".format(self.x, self.y)

    def distance(self, carletto):
        if type(carletto) != Point:
            raise TypeError(
                "I cannot calculate the distance with something that is not a point"
            )
        return ((carletto.x - self.x) ** 2 + (carletto.y - self.y) ** 2) ** 0.5


class Rectangle:
    def __init__(self, p1, p2):
        if type(p1) != Point or type(p2) != Point:
            raise TypeError("A rectangle is defined by two points")
        if p1.x == p2.x or p1.y == p2.y:
            raise ValueError("The points do not define a rectangle")
        if p1.x > p2.x:
            xs, xd = p2.x, p1.x
        else:
            xs, xd = p1.x, p2.x
        if p1.y > p2.y:
            ya, yb = p2.y, p1.y
        else:
            ya, yb = p1.y, p2.y
        self.vas = Point(xs, ya)
        self.vad = Point(xd, ya)
        self.vbs = Point(xs, yb)
        self.vbd = Point(xd, yb)

        self.base = xd - xs
        self.height = yb - ya

    def __len__(self):
        return 4

    def calculate_base(self):
        return self.vbs.distance(self.vbd)

    def calculate_height(self):
        return self.vas.distance(self.vbs)

    def calculate_diagonal(self):
        return self.vas.distance(self.vbd)

    def calculate_area(self):
        return self.calculate_base() * self.calculate_height()

    def calculate_perimeter(self):
        return self.base * 2 + self.height * 2

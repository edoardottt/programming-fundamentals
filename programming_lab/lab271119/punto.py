#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 09:18:12 2019

@author: angelo
"""


class Point:
    """A two-dimensional point"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Point({},{})".format(self.x, self.y)

    def __repr__(self):
        return "Point(x={},y={})".format(self.x, self.y)

    def __sub__(self, other_Point):
        return self.distance(other_Point)

    def distance(self, other_Point):
        if self.x == other_Point.x:
            d = abs(self.y - other_Point.y)
        elif self.y == other_Point.y:
            d = abs(self.x - other_Point.x)
        else:
            d = ((self.x - other_Point.x) ** 2 + (self.y - other_Point.y) ** 2) ** 0.5
        return d


class Square:
    """A square in the Cartesian plane"""

    def __init__(self, p, side):
        #        if not isinstance(p, Point):
        if type(p) != Point:
            raise TypeError("The Square object needs an origin point")
        if not isinstance(side, (int, float)):
            raise TypeError("The Square object needs a side of the numeric type")
        if side == 0:
            raise ValueError("The side of the Square cannot be 0")
        if side < 0:
            side = -side
            p = Point(p.x - side, p.y - side)
        self.vertice_as = Point(p.x, p.y)
        self.vertice_ad = Point(p.x + side, p.y)
        self.vertice_bs = Point(p.x, p.y + side)
        self.vertice_bd = Point(p.x + side, p.y + side)

    def perimeter(self):
        """Returns the perimeter of the square"""
        return self.vertice_ad.distance(self.vertice_as) * 4

    def area(self):
        """Returns the area of the square"""
        return self.vertice_ad.distance(self.vertice_as) ** 2


class Rectangle:
    """A rectangle in the Cartesian plane"""

    def __init__(self, p1, p2):
        if type(p1) != Point or type(p2) != Point:
            raise TypeError("The rectangle has two points as vertices")
        if p1.x == p2.x or p1.y == p2.y:
            raise ValueError("The rectangle has a zero size")
        self.vertice_as = Point(min(p1.x, p2.x), min(p1.y, p2.y))
        self.vertice_bd = Point(max(p1.x, p2.x), max(p1.y, p2.y))
        self.vertice_ad = Point(self.vertice_bd.x, self.vertice_as.y)
        self.vertice_bs = Point(self.vertice_as.x, self.vertice_bd.y)

        self.base = self.vertice_bd - self.vertice_bs
        self.height = self.vertice_bs - self.vertice_as

    def perimeter(self):
        return self.base * 2 + self.height * 2

    def area(self):
        return self.base * self.height

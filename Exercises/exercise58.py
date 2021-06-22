#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 16:26:37 2019

@author: edoardottt
https://edoardoottavianelli.it
"""


class Nodo:
    def __init__(self, v):
        self.valore = v
        self.sx = None
        self.dx = None

    def __str__(self, livello=0):
        risultato = ""
        if self.sx:
            risultato += "\n" + "\t" * livello + self.sx.__str__(livello + 1)
        risultato += "\n" + "\t" * livello + f"{self.valore}"
        if self.dx:
            risultato += "\n" + "\t" * livello + self.dx.__str__(livello + 1)
        return risultato


"""
Write a function that returns the number of vertex into the tree
"""


def count_vertex(r):
    if not r:
        return 0
    return 1 + count_vertex(r.sx) + count_vertex(r.dx)


"""
Write a function that find the max value in the input tree
"""


def find_max(r):
    if not r.sx and not r.sx:
        return r.valore
    if not r.sx:
        return find_max(r.dx)
    if not r.dx:
        return find_max(r.sx)
    return max(r.valore, find_max(r.sx), find_max(r.dx))


"""
Write a function that returns the height of a tree
"""


def height_tree(r):
    if not r.sx and not r.dx:
        return 0
    if not r.sx:
        return 1 + height_tree(r.dx)
    if not r.dx:
        return 1 + height_tree(r.sx)
    return 1 + max(height_tree(r.sx), height_tree(r.dx))

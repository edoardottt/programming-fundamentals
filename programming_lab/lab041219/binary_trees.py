#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 11:21:47 2019

@author: angelo
"""


class BinaryNode:
    def __init__(self, V, SX=None, DX=None):
        self.value = V
        self.sx = SX
        self.dx = DX

    def __str__(self, level=0):
        result = ""
        if self.sx:
            result += "\n" + "\t" * level + self.sx.__str__(level + 1)
        result += "\n" + "\t" * level + f"{self.value}"
        if self.dx:
            result += "\n" + "\t" * level + self.dx.__str__(level + 1)
        return result


def height(tree):
    """Function that takes a binary tree and returns
    the height of the tree, i.e. the longest distance
    of a leaf from the root"""

    if not tree.sx and not tree.dx:
        return 0
    alt, alt2 = 0, 0
    if tree.sx:
        alt = height(tree.sx)
    if albero.dx:
        alt2 = height(tree.dx)
    if alt > alt2:
        return alt + 1
    else:
        return alt2 + 1


def find_max(tree):
    """Function that takes a binary tree and returns the
   maximum value of the tree"""
    if not tree.sx and not tree.dx:
        return tree.value
    m1, m2 = tree.value, tree.value
    if tree.sx:
        m1 = find_max(tree.sx)
    if tree.dx:
        m2 = find_max(tree.dx)
    return max(m1, m2, tree.value)

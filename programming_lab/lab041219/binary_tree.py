#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 16:25:58 2019

@author: angelo
Write a recursive function that counts the number
of nodes of a tree.

"""


class Node:
    def __init__(self, v):
        self.value = v
        self.left = None
        self.right = None

    def __str__(self, level=0):
        result = ""
        if self.left:
            result += "\n" + "\t" * level + self.left.__str__(level + 1)
        result += "\n" + "\t" * level + f"{self.value}"
        if self.right:
            result += "\n" + "\t" * level + self.right.__str__(level + 1)
        return result

    def counter_node(self):
        if not self.left and not self.right:
            return 1
        c = 1
        if self.left:
            c += self.left.counter_node()
        if self.right:
            c += self.right.counter_node()
        return c


def counter_node(tree):
    """base case = None return 0
    recursive case = return 1 + the number of children of left + the number of children of right"""
    if tree == None:
        return 0
    return 1 + counter_node(tree.left) + counter_node(tree.right)


def counter_node2(tree):
    """base case = leaf node -> return 1
    recursive case = return 1 + the number of children of left + the number of children of right
    """
    if not tree.left and not tree.right:
        return 1
    c = 1
    if tree.left:
        c += counter_node(tree.left)
    if tree.right:
        c += counter_node(tree.right)
    return c


def find_max(tree):
    """base case: leaf node -> leaf.value
    recursive case: tree with left child and right child
        return the greater of leaf value and max (left) and max (right)
    """
    if not tree.left and not tree.right:
        return tree.value
    m, m1, m2 = tree.value, tree.value, tree.value
    if tree.left:
        m1 = find_max(tree.left)
    if albero.right:
        m2 = find_max(tree.right)
    return max(m, m1, m2)


def calculate_height(tree):
    """The greatest length of the path from root to leaf

    base case: leaf node: 0
    recursive case: 1 + maximum_height between left child and right child
    """
    if not tree.left and not tree.right:
        return 0
    m1, m2 = 0, 0
    if tree.left:
        m1 = calculate_height(tree.left)
    if albero.right:
        m2 = calculate_height(tree.right)
    return max(m1, m2) + 1

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 17:44:29 2019

@author: angelo
"""


class Node:
    def __init__(self, v):
        self.value = v
        self.sons = []


def counter_node(tree):
    """Case base: leaf -> tree.sons == [] -> 1
    Case recursive:  sum(counter_node for son in sons)  +1
    """
    if tree.sons == []:
        return 1
    node = 1
    for son in tree.sons:
        node += counter_node(son)
    return node

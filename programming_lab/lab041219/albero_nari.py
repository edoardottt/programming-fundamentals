#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 12:32:19 2019

@author: angelo
"""


class Node:
    def __init__(self, V, sons=[]):
        self.value = V
        if len(sons) == 0:
            self.sons = []
        else:
            self.sons = sons


def find_max(tree):
    max_rel = tree.value
    for sons in tree.sons:
        m = find_max(sonso)
        if m > max_rel:
            max_rel = m
    return max_rel

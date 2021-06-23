#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 09:37:03 2019

@author: angelo

Write a RECURSIVE function that takes a list and returns
the original list reversed as a new list

es: invert_list([1,2,3]) -> [3,2,1]


[1] -> [1]
[1,2] = [1]+[2]
[1,2,3] = [1] + ([2,3])
inverse([2,3]) = inverse([2]) + [3]
inverse([2]) = inverse([]) + [2]
inverse([]) = []
[1,2,3,4] = [1] + [2,3,4] -> inversion([2,3,4]) + [1]
inversion [2,3,4] = [4,3,2] + [1] -> [4,3,2,1]
inversion ([2] + [3,4]) = inversion([3,4]) + [2]

"""


def invert_list(l):
    if len(l) <= 1:
        return l

    return invert_list(l[1:]) + [l[0]]

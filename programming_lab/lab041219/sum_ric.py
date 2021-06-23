#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 14:44:28 2019

@author: angelo

Write a recursive function that sums all numbers in a list

es: sum_ric([1,2,3]) -> 6

case base: the list has only one element ->
            sum same l[0] (the only element)

case recursive: the list has n elements:
    the first element returned + the sum of the remainder
    n-1 element (return l[0] + sum_ric(l[1:]))

"""


def sum_ric(l):
    if len(l) == 1:
        return l[0]
    return l[0] + sum_ric(l[1:])

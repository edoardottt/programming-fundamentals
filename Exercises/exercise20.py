#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 16:53:17 2019

@author: edoardottt
https://www.edoardoottavianelli.it
https://www.github.com/edoardottt
"""

# Write a function that returns True if the list in input is sorted.


def is_sorted(l):
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            return False
    return True


# with while
def is_sorted2(l):
    i = 0
    while i < len(l) - 1:
        if l[i] > l[i + 1]:
            return False
        i += 1
    return True

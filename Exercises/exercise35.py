#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 16:24:25 2019

@author: edoardottt
https://www.edoardoottavianelli.it
https://www.github.com/edoardottt
"""

"""
Write a function that take as input a filename and returns the number
of characters in every lines except the newline character.
"""


def foo(n):
    with open(n, "r") as f:
        s = f.readlines()
        result = [len(line) - 1 for line in s]
    return result


print(foo("pippo.txt"))

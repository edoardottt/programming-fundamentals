#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 19:22:45 2019

@author: edoardottt
https://www.edoardoottavianelli.it
https://www.github.com/edoardottt
"""

"""
Write a function that take as input a name of a file and print into it all the 
numbers for 0 to 9 on different lines.
It returns 0.
"""


def foo(n):
    f = open(n, "w")
    for i in range(10):
        f.write(str(i) + "\n")
    f.close()
    return 0


# another version
def foo2(n):
    l = [str(i) + "\n" for i in range(10)]
    f = open(n, "w")
    f.writelines(l)
    f.close()
    return 0


# another version with 'with open'
def foo3(n):
    with open(n, "w") as f:
        for i in range(10):
            f.write(str(i) + "\n")
    return 0

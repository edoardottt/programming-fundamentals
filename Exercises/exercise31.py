# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 19:49:06 2019

@author: edoardottt
https://www.edoardoottavianelli.it
https://www.github.com/edoardottt
"""

"""
Write a function that take as input a dictionary (like key:integer list)
and returns a new dictionary with same keys but having as value
the average of the value's elements.
"""


def foo(d):
    return {k: sum(v) / len(v) for k, v in d.items()}

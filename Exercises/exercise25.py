#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 15:58:59 2019

@author: edoardottt
https://www.edoardoottavianelli.it
https://www.github.com/edoardottt
"""

"""
Write a function that take as input a string and WITHOUT USING LOOPS returns 
the set of characters that make the string.
"""
s = "edoardo loves programming"


def char_string(s):
    alphabet = set(
        [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "x",
            "w",
            "y",
            "z",
        ]
    )
    string = set(s.replace("", " ").split())
    return alphabet & string

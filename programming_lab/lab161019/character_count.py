#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 12:43:21 2019

@author: angelo

Write a function that takes a string and returns a dictionary in which the keys are the characters present in the string and the values the number of times the corresponding character is present in the string.

es: character_count("pippo") returns the dictionary
{'p':3, 'i':1, 'o':1}
"""


def character_count(word):
    d = dict()
    for character in word:
        if character not in d:
            d[character] = 1
        else:
            d[character] += 1
    return d


def character_count2(word):
    d = dict()
    for character in word:
        count = d.get(character, 0)
        d[character] = count + 1
    return d


def character_count3(word):
    # A count is invoked for each character
    # Cost is quadratic (i.e. len * len)
    d = dict()
    for character in word:
        d[character] = word.count(character)
    return d


# test with Beowulf (292951 characters):
#    %timeit character_count(a)
# 33.9 ms ± 723 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)

#    %timeit character_count2(a)
# 44.1 ms ± 2.29 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)

#    %timeit character_count3(a)
# 1min 42s ± 3 s per loop (mean ± std. dev. of 7 runs, 1 loop each)

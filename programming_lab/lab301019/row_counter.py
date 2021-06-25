#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 12:26:54 2019

@author: angelo

write a function that takes the name of a file, opens it and returns the number of lines of which the file is composed


"""


def row_counter(filename):
    counter = 0
    with open(filename) as f:
        for line in f:
            counter += 1
    return counter


def row_counter2(filename):
    counter = 0
    with open(filename) as f:
        for line in f.readlines():
            counter += 1
    return counter


def row_counter3(filename):
    with open(filename) as f:
        return len(f.readlines())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 17:26:42 2019

@author: angelo
Write a function that takes a string which is the name of a file and prints the number of characters found in each line, excluding the newline character """


def print_characters_line(filename):
    with open(filename) as f:
        for line in f:
            print(len(line.rstrip("\n")))

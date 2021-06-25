#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 16:25:54 2019

@author: angelo
We write a function that takes the name of a file as a parameter and prints all the numbers from 0 to 9 on different lines. Returns 0.
"""


def file_10(filename):
    f = open(filename, "w")
    string = ""
    for i in range(10):
        string += str(i) + "\n"
    f.write(string)
    f.close()
    return 0


def file_102(filename):
    f = open(filename, "w")
    for i in range(10):
        f.write(str(i) + "\n")
    f.close()
    return 0


def file_103(filename):
    with open(filename, "w") as f:
        list = [str(i) + "\n" for i in range(10)]
        f.writelines(list)
    return 0

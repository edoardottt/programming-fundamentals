#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 10:38:24 2019

@author: angelo

Write a function that takes a list of integers as input and returns the list with the 10's complements of the integers of the input list.
"""


def complement_a_10(number):
    n = len(str(number))
    return 10 ** n - number


def list_complement(list_full):
    list = []
    for number in list_full:
        list.append(complement_a_10(number))
    return list


def list_complement2(list_full):
    list = []
    for i in range(len(list_full)):
        list.append(complement_a_10(list_full[i]))
    return list


def list_complement3(list_full):
    list = []
    i = 0
    while i < len(list_full):
        list.append(complement_a_10(list_full[i]))
        i += 1
    return list

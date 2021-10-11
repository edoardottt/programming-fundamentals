#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 14:57:29 2019

@author: angelo
Write a function that takes as input a list of integers and returns the list with the 10's complements of the integers of the input list
"""


def calculate_complement(number):
    n = len(str(number))
    complement = 10 ** n - number
    return complement


def calculate_complement2(number):
    n = 1
    a = number
    while a // 10 > 0:
        n += 1
        a //= 10
    complement = 10 ** n - number
    return complement


def list_complement(lista):
    complementi = []
    for number in list:
        complement = calculate_complement(number)
        complements.append(complement)
    return complements


def list_complement2(list):
    complements = []
    for i in range(len(list)):
        complement = calculate_complement(list[i])
        complements.append(complement)
    return complements


def list_complement3(list):
    complements = []
    i = 0
    while i < len(list):
        complement = calculate_complement(list[i])
        complements.append(complement)
        i = i + 1
    return complements


def list_complement4(list):
    complements = []
    for number in list:
        complement = calculate_complement2(number)
        complements.append(complement)
    return complements

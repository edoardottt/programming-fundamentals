#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 11:25:16 2019

@author: angelo
"""

""" Write a function that takes a list of integers and returns a new list with only the even elements of the original list """

def even_items(list):
    list_pair = []
    for i in list:
        if i % 2 == 0:
            list_pair.append(i)
    return list_pair


def even_index_items(list):
    list_pair =[]
    for i in range(len(list)):
        if list[i] % 2 == 0:
            list_pair.append(list[i])
    return list_pair

""" Write a function that takes a list of integers and returns an integer corresponding to the sum of all the values in the original list """

def sum_list(list):
    sum= 0
    for i in list:
        sum += i
    return sum


""" Write a function that takes a list of strings and returns a list with only the strings that are a vowel """

def search_vowels(list):

def search_index_vowels(list):

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 10:20:20 2019

@author: angelo
Write a function that takes a string of words separated by spaces and returns a dictionary where the key is the number of letters and the value is the number of words in the string that have a number of letters equal to the key

ex: "pippo re ciao asdrubale te" {2:2, 4:1, 5:1, 9:1}
"""


def dic_length(s):
    diz = {}
    list = s.split()
    for word in list:
        word_length = len(word)
        if not word_length in dic:
            dic[word_length] = 1
        else:
            dic[word_length] = dic[word_length] + 1
    return dic


def dic_length2(s):
    dic = {}
    for parola in s.split():
        dic[len(word)] = dic.get(len(word), 0) + 1
    return dic

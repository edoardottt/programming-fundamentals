#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 09:52:14 2019

@author: angelo
Write a function that takes a list and returns a new list made up of tuples. 
Each element of the tuple has the first element which is an element of the input list and the second which is the number of times the element repeats starting from that position. 
The same elements must be in the same order as the input list.

ex: [1,2,2,2,"b","a","a",2.0,2.0,2.0,"home","home",2.0]
returns
[(1,1),(2,3),("b",1),("a",2),(2.0,4),("home",2)]
"""


def count_elements_list(list):
    dic = {}
    for element in list:
        dic[element] = list.count(element)
    return list(dic.items())


def count_elements_list2(list):
    dic = {}
    for element in list:
        if element not in dic:
            dic[element] = list.count(element)
    return list(dic.items())


def count_elements_list3(list):
    dic = {}
    for element in list:
        if element not in dic:
            dic[element] = 1
        else:
            dic[element] += 1
    return list(dic.items())


def count_elements_list4(list):
    dic = {}
    for element in list:
        t = element, type(element)
        if t not in dic:
            dic[t] = 1
        else:
            dic[t] += 1
    list_ret = []
    for tuple, repetitions in dic.items():
        list_ret.append((tuple[0], repetitions))
    return list_ret


def count_elements_list5(list):
    dic = {(element, type(element)): 0 for element in list}
    for element in list:
        t = element, type(element)
        dic[t] += 1
    return [(tuple[0], dic[tuple]) for tuple in dic]


def count_elements_list6(list):
    dic = {}
    for element in list:
        try:
            dic[element] += 1
        except:
            dic[element] = 1
    return list(dic.items())


def count_elements_list7(list):
    dic = {}
    for element in list:
        dic[element] = dic.get(element, 0) + 1
    return list(dic.items())

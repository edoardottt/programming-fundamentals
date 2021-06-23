#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 14:13:16 2019

@author: angelo

maximum([a,b,c])
???
maximum (a, maximum([b,c]))
maximum([b,c]) = maximum(b, maximum([c]))
maximum([c])


"""


def f(l):
    c = l
    return c


def g(l):
    b = l[0]
    m = f(l[1])
    if b > m:
        return b
    return m


def h(l):
    a = l[0]
    m = g(l[1:3])
    if a > m:
        return a
    return m


a, b, c = 3, 5, 7
j = h([a, b, c])
print(j)


def find_max(l):
    if len(l) == 1:
        return l[0]
    m = find_max(l[1:])
    if l[0] > m:
        return l[0]
    return m


"""
case_base: the list has only one element -> is the max

recursive_case: the list has n elements: return the
       greater between the first element and the max of
       remaining n-1 elements


find_max([56,33,567,224,6,774,3,22245,66765,43])
56 > find_max([33,567,224,6,774,3,22245,66765,43]) ?
56 > 66765? 66765

33 > find_max([567,224,6,774,3,22245,66765,43]) ?
33 > 66765? 66765

567 > find_max([224,6,774,3,22245,66765,43]) ?
567 > 66765? -> 66765

224 > find_max([6,774,3,22245,66765,43]) ?
224 > 66765? -> 66765

6 > find_max([774,3,22245,66765,43])  ?
6 > 66765? -> 66765

774 > find_max([3,22245,66765,43]) ?
774 > 66765? -> 66765

3 > find_max([22245,66765,43]) ?
3 > 66765? -> 66765

22245 > find_max([66765,43]) ?
22245 > 66765 ? -> 66765

66765 > find_max([43]) ?
66765 > 43? -> 66765

find_max([43]) -> 43

"""

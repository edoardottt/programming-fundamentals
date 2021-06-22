#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 14:13:16 2019

@author: angelo

massimo([a,b,c])
???
massimo (a, massimo([b,c]))
massimo([b,c]) = massimo(b, massimo([c]))
massimo([c])


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


def trova_max(l):
    if len(l) == 1:
        return l[0]
    m = trova_max(l[1:])
    if l[0] > m:
        return l[0]
    return m


"""
caso_base : la lista ha un solo elemento -> è il max

caso_ricorsivo: la lista ha n elementi: ritorno il
       maggiore fra il primo elemento e il max dei
       restanti n-1 elemnti


trova_max([56,33,567,224,6,774,3,22245,66765,43])
56 > trova_max([33,567,224,6,774,3,22245,66765,43]) ?
56 > 66765? 66765

33 > trova_max([567,224,6,774,3,22245,66765,43]) ?
33 > 66765? 66765

567 > trova_max([224,6,774,3,22245,66765,43]) ?
567 > 66765? -> 66765

224 > trova_max([6,774,3,22245,66765,43]) ?
224 > 66765? -> 66765

6 > trova_max([774,3,22245,66765,43])  ?
6 > 66765? -> 66765

774 > trova_max([3,22245,66765,43]) ?
774 > 66765? -> 66765

3 > trova_max([22245,66765,43]) ?
3 > 66765? -> 66765

22245 > trova_max([66765,43]) ?
22245 > 66765 ? -> 66765

66765 > trova_max([43]) ?
66765 > 43? -> 66765

trova_max([43]) -> 43

"""

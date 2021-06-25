#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 09:33:38 2019

@author: angelo
"""


def es1(S, m):
    l = S.split(",")
    le = len(l)
    l = list(map(int, l))
    c = 0
    for j in range(le):
        t = 0
        for i in range(j, le):
            t += l[i]
            if t > m:
                break
            elif t == m:
                c += 1
    return c

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 15:46:17 2019

@author: angelo
Write a function that takes two arrays of numbers as lists of lists and calculates a third which is the product of rows and columns
"""


def column_line_product(A, i, B, j):
    row = A[i]
    column = [r[j] for r in B]
    return sum([row[i] * column[i] for i in range(len(row))])


def product_lines_columns(A, B):
    if not len(A[0]) == len(B):
        raise Exception
    matrix = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            row.append(column_line_product(A, i, B, j))
        matrix.append(row)
    return matrix

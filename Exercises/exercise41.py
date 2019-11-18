# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 10:25:23 2019

@author: edoardottt
https://www.edoardoottavianelli.it
https://www.github.com/edoardottt
"""

'''
Write a function that take as input two matrices of numbers as lists of lists
and it calculates a third matrix that is the product-rows-columns.
'''

m1 = [[1,0,2],
      [0,3,-1]]
m2 = [[4,1],
      [-2,2],
      [0,3]]
def prod_rows_cols(m1,m2):
    if len(m1[0])!=len(m2):
        print("The length of m1's cols have to be equal to m2's rows.")
        return 0
    else:
        n_rows = len(m1)
        n_cols = len(m2[0])
        m3=[[0]*n_rows]*n_cols
        for i in range(n_rows):
            for j in range(n_cols):
                col = extract_col(m2,j)
                m3[i][j] = calc(m1[i],col)
        return m3
        
def calc(l1,l2):
    i,j = 0,0
    summ = 0
    while i<len(l1) and j<len(l2):
        c = l1[i]*l2[j]
        summ += c
        i+=1
        j+=1
    return summ

def extract_col(m,i):
    col = [m[j][i] for j in range(len(m))]
    return col

print(prod_rows_cols(m1,m2))
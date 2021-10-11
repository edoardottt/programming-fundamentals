#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 11:23:44 2019

@author: angelo

Write a function that takes a list and checks if the list can be considered an array of numbers (int or float). 
Specifically: the number of elements in each row must be the same for each row.

"""

def check_matrix(A):
    column = len(A[0])
    for row in A:
        if len(row) != column:
            return False
        for element in row:
#            if type(element) != float and type(element) != int:
#                return False
            if not isinstance(element, (int, float)):
                return False
    return True

def prod_scalare(s, A):
    """ returns the matrix resulting from the product of matrix A by the scalar s
    eg:
        s = 4
        A = [[1,2,3],[4,5,6]]

        A' = [[4,8,12],[16,20,24]]
    """
    new_matrix = []
    for row in A:
        new_row = [s*el for el in row]
#        for element in row:
#            new_row.append(s*element)
        new_matrix.append(new_row)
    return new_matrix

def prod_vector_matrice(v, A):
    """ returns the matrix resulting from the product of matrix A by the vector v
    eg:
        v = [4, 2, 1]
        A = [[1,2,3],[4,5,6]]

        A' = [[4,4,3],[16,10,6]]
    """
    new_matrix = []
    for row in A:
        new_row = [row[i]*v[i] for i in range(len(row))]
#        for index in range(len(riga)):
#            new_row.append(A[index] * v[index])
        new_matrix.append(new_row)
    return new_matrix



def sum_matrices(A, B):
    """ returns the matrix resulting from the sum of the matrices
    eg: element i, j will beA[i,j]+B[i,j]

    """
    new_matrix = []
    for index_row in range(len(A)):
        new_row = [A[index_row][i]+B[index_row][i] for i in range(len(A[index_row]))]
#        for index_column in range(len(A[index_row])):
#            new_row.append(A[index_row][index_column] + B[index_row][index_column])
        new_matrix.append(new_row)
    return new_matrix

def product_matrices (A,B):
    """ to do at home """

if __name__=='__main__':
    A = [[5, 6, 7], [3, 6, 1], [9, -1, -2], [1.3,5,-0.5]]
    print(check_matrix(A))

    B = [[5, 6, 7], [3, 6, 1], [9, -1, -2], [1.3,5,"-0.5"]]
    print(check_matrix(B))

    C = [[5, 6, 7], [3, 6, 1], [9, -1, -2], [1.3,5,"-0.5"],[5,6]]
    print(check_matrix(C))





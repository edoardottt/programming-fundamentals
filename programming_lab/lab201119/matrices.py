    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
    """
    Created on Wed Nov 20 09:30:38 2019

    @author: angelo

    Write a function that takes two arrays of numbers as lists of lists and calculates a third which is the product of rows and columns.


    C = A.B

    cij = ai * bj -> product "vector"

     that is a*b= a1*b1+a2*b2+a3*b3...

    """


    def prod_vectors(x, y):
        """x = [1,2,3] y= [0,1,2]
        prod_vectors = 0 + 2 + 6 = 8"""
        return sum([x[i] * y[i] for i in range(len(x))])


    def prod_right_columns(A, B):
        if len(A) != len(B[0]):
            raise Exception
        mat = []
        for i in range(len(A)):
            row = []
            for j in range(len(B[0])):
                column_j_B = [B[k][j] for k in range(len(B))]
                #            column_j_B = [rowB[j] for rowB in B]
                row.append(prod_vectors(A[i], column_j_B))
            mat.append(row)
        return mat


    def matrix_full(nrows, ncolumns):
        """This function creates a matrix with n lines and n columns containing all the numbers from 1 to n lines * n columns"""
        mat = []
        for i in range(nrows):
            row = []
            for j in range(ncolumns):
                row.append(1 + j + ncolumns * i)
            mat.append(row)
        return mat

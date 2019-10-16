# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 10:04:08 2019

@author: edoardottt
https://www.edoardoottavianelli.it
https://www.github.com/edoardottt
"""

#Write a function 'invest' that take as input a capital, an annual interest and the years number and it
#prints the matured capital after n years of investment with the interest i.
# Use the formula: matured = capital * (1+interest/100)**years.

from invest import invest

test_list = {(1000,10,2):1210,
             (5000,1.10,20):6222,
             (3500,0.9,30):4579}

if __name__ == '__main__':
    for test_case, result in test_list.items():
        val = invest(*test_case)
        if  val == result:
            print('Test case: {}\tOK'.format(test_case))
        else:
            print('Test case: {}\tNOK, risultato atteso {}, risultato fornito {}'.format(test_case, result, val))

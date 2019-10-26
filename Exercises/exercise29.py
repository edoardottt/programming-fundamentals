# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 19:23:13 2019

@author: edoardottt
https://www.edoardoottavianelli.it
https://www.github.com/edoardottt
"""

'''
Scrivere una funzione che prende una stringa contenente una serie di parole 
separate da spazi e costruisce un dizionario in cui le chiavi sono le 
ultime lettere delle parole della stringa e i valori ad esse associati 
sono liste con le parole che terminano con quella lettera.
Le liste devono essere ordinate lessicograficamente.
Ad esempio, per la stringa "in verità non mi par vero affatto" deve restituire
{'o':['affatto','vero'], 'n':['in','non'], 'à':['verità'], 'i':['mi'], 'r':['par']}


Write a function that take as input a string containing a word serie
separated by commas and build(and returns) a dictionary having as keys the
last words of the string's words and as values the lists with the words 
that endwith that letter.
The lists have to be sorted lexicographically.
For example, for the input "in verità non mi par vero affatto" -->
{'o':['affatto','vero'], 'n':['in','non'], 'à':['verità'], 'i':['mi'], 'r':['par']}
'''
def foo(s):
    end = [i[-1] for i in s.split()]
    end = set(end)
    diz = {}
    for item in end:
        diz[item] = [i for i in s.split() if i[-1]==item]
    for k,v in diz.items():
        v.sort()
    return diz
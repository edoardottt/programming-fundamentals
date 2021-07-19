#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 11:31:48 2019

@author: angelo
Write a function that takes a string of words separated by spaces and returns a dictionary where the keys are the vowels of the alphabet present in the word string. The values ​​associated with the keys are lists with the words of the original string that contain the vowel one.

ex: "odio et amo" {'o':['odio','amo'], 'i':['odio'], 'e':['et'], 'a':['amo']}
"""


def vowel_words(s):
    dic = {}
    words = s.split()
    for word in words:
        for vowel in "aeiou":
            if vowel in word:
                if vowel in dic:
                    dic[vowel].append(word)
                else:
                    dic[vowel] = [word]
    return dic


def vowel_words2(s):
    dic = {}
    words = s.split()
    for word in words:
        for vowel in "aeiou":
            if vowel in word:
                dic[vowel] = dic.get(vowel, []) + [word]
    return dic


vocal_words("odio et amo aaaaaaaa")

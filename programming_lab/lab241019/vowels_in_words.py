#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 16:48:05 2019

@author: angelo

Writing a function that takes as an argument a string containing words separated by spaces and returns a dictionary in which the keys are the vowels present in the string and the values associated with each key are a list with the words that contain that key.


ex: "the wolf howls" {'i':['the'], 'u':['wolf','howls'], 'a':['howls'], 'o':['wolf']}
"""


def vowels_in_words(S):
    dic = {vowel: [] for vowel in "aeiou"}
    for vowel in dic:
        for word in S.split():
            if vowel in word:
                dic[vowel].append(word)
    l = []
    for vowel, list in dic.items():
        if list == []:
            l.append(vowel)
    for vowel in l:
        del dic[vowel]
    return dic


def vowels_in_words2(S):
    dic = {}
    for vowel in "aeiou":
        for word in S.split():
            if vowel in word:
                dic[vowel] = dic.get(vowel, []) + [word]
    #                if vowel not in dic:
    #                    dic[vowel] = [word]
    #                else:
    #                    dic[vowel].append(word)
    return dic


vowels_in_words2("the wolf howls")

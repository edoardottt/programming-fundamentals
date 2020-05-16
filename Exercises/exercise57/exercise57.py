#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 15:50:01 2019

@author: edoardottt
https://edoardoottavianelli.it
"""

import json

'''
Write a function that take as input test.json and returns the set of users
(userId) that have at least a todo
'''
def usersId(fname):
    with open(fname) as f:
        lista = json.load(f)
    users = set()
    for user in lista:
        users.add(user['userId'])
    return users

'''
Return the users that have the max number of todo 
'''
def max_todo(fname):
    with open(fname) as f:
        lista = json.load(f)
    users = usersId(fname)
    d = {user:0 for user in users}
    for elem in lista:
        if elem['completed']==False:
            d[elem['userId']] +=1
    d2 = {}
    for k,v in d.items():
        if v in d2: d2[v].append(k)
        else: d2[v] = [k]
    return d2[max(d2)]

'''
Return the users that have the max number of todo completed 
'''
def max_todo_completed(fname):
    with open(fname) as f:
        lista = json.load(f)
    users = usersId(fname)
    d = {user:0 for user in users}
    for elem in lista:
        if elem['completed']==True:
            d[elem['userId']] +=1
    d2 = {}
    for k,v in d.items():
        if v in d2: d2[v].append(k)
        else: d2[v] = [k]
    return d2[max(d2)]
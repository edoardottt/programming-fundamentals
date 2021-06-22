#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 15:50:58 2019

@author: angelo
Scrivere una funzione che prende todos.json e
ritorna l'insieme degli utenti (userId) che anno
almeno un todo

Scrivere user_with_max_todos che ritorna
l'userId dell'utente che ha il maggior numero
di todo. Se ce ne sono più di uno con lo stesso
numero, ritorna la lista.
"""
import json


def userIds(fname):
    with open(fname) as f:
        lista = json.load(f)
    users = set()
    for todo in lista:
        users.add(todo["userId"])
    return users


def user_with_max_todos(fname):
    with open(fname) as f:
        lista = json.load(f)
    d = {}
    for todo in lista:
        d[todo["userId"]] = d.get(todo["userId"], 0) + 1
    d_freq = {}
    for user, freq in d.items():
        d_freq[freq] = d_freq.get(freq, []) + [user]
    max_freq = max(d_freq.keys())
    return d_freq[max_freq]


def user_with_max_todos_completed(fname):
    with open(fname) as f:
        lista = json.load(f)
    d = {}
    for todo in lista:
        if todo["completed"]:
            d[todo["userId"]] = d.get(todo["userId"], 0) + 1
    d_freq = {}
    for user, freq in d.items():
        d_freq[freq] = d_freq.get(freq, []) + [user]
    max_freq = max(d_freq.keys())
    return d_freq[max_freq]

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 12:26:54 2019

@author: angelo

scrivere una funzione che prende il nome di un file, lo apre e ritorna il numero di righe di cui il file è composto


"""
def conta_righe(filename):
    contatore = 0
    with open(filename) as f:
      for line in f:
        contatore +=1
    return contatore

def conta_righe2(filename):
    contatore = 0
    with open(filename) as f:
      for line in f.readlines():
        contatore +=1
    return contatore

def conta_righe3(filename):
    with open(filename) as f:
        return len(f.readlines())

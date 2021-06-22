#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 16:13:25 2019

@author: angelo
"""


class Nodo:
    def __init__(self, val):
        self.val = val
        self.figliosx = None
        self.figliodx = None

    def aggiungi_nodo(self, val):
        if self.val > val:
            if not self.figliosx:
                self.figliosx = Nodo(val)
            else:
                self.figliosx.aggiungi_nodo(val)
        else:
            if not self.figliodx:
                self.figliodx = Nodo(val)
            else:
                self.figliodx.aggiungi_nodo(val)

    def stampa(self, l=[]):
        l.append(self.val)
        if self.figliosx:
            print("Nodi ricorsioni sx", l)
            self.figliosx.stampa(l)
        print(self.val, end=" ")
        if self.figliodx:
            print("Nodi ricorsioni dx", l)
            self.figliodx.stampa(l)
        l.pop()

    def crea_albero_da_lista(l):
        radice = Nodo(l[0])
        for i in l[1:]:
            radice.aggiungi_nodo(i)
        return radice

    def trova(self, val):
        if self.val == val:
            return True
        if val < self.val:
            seguente = self.figliosx
        else:
            seguente = self.figliodx
        if seguente:
            return seguente.trova(val)
        return False

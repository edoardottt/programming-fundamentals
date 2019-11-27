#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 16:13:37 2019

@author: edoardottt
https://www.edoardoottavianelli.it
https://www.github.com/edoardottt
"""

class Nodo:
    def __init__(self,val):
        self.val = val
        self.figliosx = None
        self.figliodx = None
        
    def __repr__(self):
        return 'Oggetto Nodo: val={},figliosx={},figliodx={}'.format(self.val,self.figliosx,self.figliodx)

    def stampa(self):
        if self.figliosx: self.figliosx.stampa()
        print(self.val, end=' ')
        if self.figliodx:self.figliodx.stampa()
        
    def aggiungi_nodo(self,val):
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
    
    def crea_albero_da_lista(l):
        radice = Nodo(l[0])
        for elem in l[1:]:
            radice.aggiungi_nodo(elem)
        return radice
    
    def trova(self,val):
        if val==self.val:
            print('Trovato!')
        elif val>self.val:
            if self.figliodx:
                return self.figliodx.trova(val)
            else: 
                print('Non Trovato!')
        else:
            if self.figliosx:
                return self.figliosx.trova(val)
            else: 
                print('Non Trovato!')
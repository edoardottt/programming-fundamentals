#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 13:55:38 2019

@author: edoardottt
https://www.edoardoottavianelli.it
https://www.github.com/edoardottt
"""

class Punto:
    def __init__(self,x,y):
        if not isinstance(x,(int,float)) or not isinstance(y,(int,float)):
            raise TypeError('I parametri devono essere numerici')
        self.x = x
        self.y = y
    
    def __repr__(self):
        return 'Oggetto Punto(x={},y={})'.format(self.x,self.y)
    
    def __str__(self):
        return 'Punto({},{})'.format(self.x,self.y)
    
    def distanza(self,altro):
        if type(altro) != Punto:
            raise TypeError('Non posso calcolare la distanza con qualcosa che non è un Punto')
        primo = altro.x - self.x
        secondo = altro.y - self.y
        return ((primo)**2+(secondo)**2)**0.5
    
class Rettangolo:
    def __init__(self,p1,p2):
        if not isinstance(p1,Punto) or not isinstance(p2,Punto):
            raise TypeError('Un rettangolo è definito da due punti.')
        elif p1.x==p2.x or p1.y==p2.y:
            raise ValueError('I punti non definiscono un rettangolo.')
        if p1.x > p2.x: xs,xd = p2.x,p1.x
        else: xd,xs = p2.x,p1.x 
        if p1.y > p2.y: ya,yb = p2.y,p1.y
        else: yb,ya = p2.y,p1.y
        self.vas = Punto(xs,ya)
        self.vad = Punto(xd,ya)
        self.vbs = Punto(xs,yb)
        self.vbd = Punto(xd,yb)
        self.base = xd - xs
        self.altezza = yb - ya
        
    def __repr__(self):
        return 'Oggetto Rettangolo(vas={},vad={},vbs={},vbd={})'.format(self.vas,self.vad,self.vbs,self.vbd)
        
    def __str__(self):
        return 'vas={},vad={},vbs={},vbd={}'.format(self.vas,self.vad,self.vbs,self.vbd)
        
    def calcolo_base(self):
        return self.vbd.distanza(self.vbs)
        
    def calcolo_altezza(self):
        return self.vas.distanza(self.vbs)
    
    def calcolo_area(self):
        return self.base*self.altezza
    
    def calcolo_perimetro(self):
        return self.base*2+self.altezza*2
    
    def calcolo_area_2(self):
        return self.calcolo_base() * self.calcolo_altezza()
    
    def calcola_perimetro_2(self):
        return self.calcolo_base*2 + self.calcolo_altezza*2
    
    def calcolo_diagonale(self):
        return self.vas.distanza(self.vbd)
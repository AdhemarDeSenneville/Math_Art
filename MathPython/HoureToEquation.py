# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 14:13:38 2021

@author: adhem
"""

import numpy as np

class Hour():
    
    def __init__(self,a=0,b=0,c=0,d=0):
        self.h1=a
        self.h2=b
        self.min1=c
        self.min2=d
    
    def NextMin(self):
        if self.min2<9:
            self.min2=1+self.min2
        elif self.min1<5:
            self.min2=0
            self.min1=1+self.min1
        elif self.h2<9 and 10*self.h1+self.h2<24:
            self.min1=0
            self.min2=0
            self.h2=1+self.h2
        elif 10*self.h1+self.h2<24:
            self.min1=0
            self.min2=0
            self.h1=0
            self.h1=1+self.h1
        else:
            self.h1=0
            self.h2=0
            self.min1=0
            self.min2=0
    
    def Affichage(self):
        print(self.h1,self.h2,":",self.min1,self.min2)
        
        
class Equation():
    
    def __init__(self,Mat):
        self.sign1=Mat[0]
        self.sign2=Mat[1]
        self.sign3=Mat[2]
        self.sign4=Mat[3]
        
        self.oprt1=Mat[4]
        self.oprt2=Mat[5]
        #self.oprt3=Mat[6]
        
        #self.order=Mat[7]
    
    def Affichage():
        pass
    
    def sign(a,n):
        """0 rien // 1 - // 2 sqrt """
        if n==0:
            return a
        if n==1:
            return -a
        if n==2:
            return sqrt(a)
        if n==3:
            return -sqrt(a)
    
    def oprt(a,b,n):
        
        if n==1:
            return a+b
        if n==2:
            return a*b
        if n==3:
            return a/b
        if n==4:
            return pow(a,b)
        if n==5:
            return 10*a+b
    
    def IsGood(self,Hour):
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
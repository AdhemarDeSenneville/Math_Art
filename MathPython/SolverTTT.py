# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 17:40:30 2021

@author: Adhemar
"""
import numpy as np
#from MainTTT import Affichage
import MainTTT


class TTT:
    def __init__(self,Mat):
        self.Board=Mat
        self.Turn=self.GetTurn()
    
    def GetTurn(self):
        return np.sum(np.absolute(self.Board))
    
    def IsWin(self):
        if max(np.sum(self.Board[0,:]),np.sum(self.Board[1,:]),np.sum(self.Board[2,:]))==3:
            return 1
        if max(np.sum(self.Board[:,0]),np.sum(self.Board[:,1]),np.sum(self.Board[:,2]))==3:
            return 1
        if min(np.sum(self.Board[0,:]),np.sum(self.Board[1,:]),np.sum(self.Board[2,:]))==-3:
            return -1
        if min(np.sum(self.Board[:,0]),np.sum(self.Board[:,1]),np.sum(self.Board[:,2]))==-3:
            return -1
        if self.Board[0,0]+self.Board[1,1]+self.Board[2,2]==3 or self.Board[2,0]+self.Board[1,1]+self.Board[0,2]==3:
            return 1
        if self.Board[0,0]+self.Board[1,1]+self.Board[2,2]==-3 or self.Board[2,0]+self.Board[1,1]+self.Board[0,2]==-3:
            return -1
        return 0 #A oppti de ouf(Ultra utiliser sur le final)
    
    
    def AffichageBoard(self):
        MainTTT.Affichage(self.Board)
    
    def MinMax(self):
        T=self.GetTurn()
        if T==9 or self.IsWin()!=0:
            return self.IsWin()
        
        if T%2==0:
            MaxEval=-1
            for i in range(3):
                for j in range(3):
                    if self.Board[i,j]==0:
                        Children=self.Board[:,:]
                        Children[i,j]=1
                        C=TTT(Children)
                        MaxEval=max(MaxEval,C.MinMax())
                    else:
                        pass
                
            return MaxEval
        else:
            MinEval=1
            for i in range(3):
                for j in range(3):
                    if self.Board[i,j]==0:
                        Children=self.Board[:,:]
                        Children[i,j]=-1
                        C=TTT(Children)
                        MinEval=min(MinEval,C.MinMax())
                    else:
                        pass
                    
            return MinEval
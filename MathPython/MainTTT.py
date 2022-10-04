# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 00:33:22 2021

@author: Adhemar
"""


"""Import"""
import numpy as np
import pylab as plt
import math
from PIL import Image
#import matplotlib


"""Defining main parametres"""
InitialGame=np.array([[1,0,0],
                      [0,0,0],
                      [0,0,0]])

deapth=4
MinResolution=5
ResolutionAffichage=7
GenerationType=False #True: Color mode / False: Game mode
PaletNumber=2
path='C:\\Users\\adhem\\Documents\\Algo\\Marth\\MathPython\\'

"""Generating the color palet"""

"""Palet 1"""
if PaletNumber==1: 
    Saturation=0
    Green=np.array([144+Saturation,190+Saturation,109+Saturation])
    Orange=np.array([248+Saturation, 150+Saturation, 30+Saturation])
    Red=np.array([249+Saturation,65+Saturation,68+Saturation])
    Green[Green>255]=255
    Orange[Orange>255]=255
    Red[Red>255]=255

"""Palet 2"""
if PaletNumber==2:
    Green=np.array([76,201,240])
    Orange=np.array([72,12,168])
    Red=np.array([247,37,133])

if PaletNumber==3:
    Green=np.array([76,201,240])
    Orange=np.array([67,97,239])
    Red=np.array([247,37,133])


ColorPalet=[1-Red/255,1-Orange/255,1-Green/255]


"""Defining TicTacToe solving algorithm"""

def IsWinOUT(A):
        if np.sum(A[0,:])==3 or np.sum(A[1,:])==3 or np.sum(A[2,:])==3:
            return 1
        if np.sum(A[:,0])==3 or np.sum(A[:,1])==3 or np.sum(A[:,2])==3:
            return 1
        if np.sum(A[0,:])==-3 or np.sum(A[1,:])==-3 or np.sum(A[2,:])==-3:
            return -1
        if np.sum(A[:,0])==-3 or np.sum(A[:,1])==-3 or np.sum(A[:,2])==-3:
            return -1
        if A[0,0]+A[1,1]+A[2,2]==3 or A[2,0]+A[1,1]+A[0,2]==3:
            return 1
        if A[0,0]+A[1,1]+A[2,2]==-3 or A[2,0]+A[1,1]+A[0,2]==-3:
            return -1
        return 0 #A oppti de ouf(Ultra utiliser sur le final)

def MinMaxOUT(A,alpha=-2,beta=2):
        T=np.sum(np.absolute(A))
        if T==9 or IsWinOUT(A)!=0:
            return IsWinOUT(A)
        if T%2==0:
            MaxEval=-1
            for i in range(3):
                for j in range(3):
                    if A[i,j]==0:
                        
                        Children=np.zeros((3,3))
                        for k in range(3):
                            for l in range(3):
                                Children[k,l]=A[k,l]
                        Children[i,j]=1
                        
                        Eval=MinMaxOUT(Children,alpha,beta)
                        MaxEval=max(MaxEval,Eval)
                        
                        alpha = max(alpha, Eval)
                        if beta <= alpha:
                            break
                        
                    else:
                        pass
                
            return MaxEval
        else:
            MinEval=1
            for i in range(3):
                for j in range(3):
                    if A[i,j]==0:
                        
                        Children=np.zeros((3,3))
                        for k in range(3):
                            for l in range(3):
                                Children[k,l]=A[k,l]
                        Children[i,j]=-1
                        
                        Eval=MinMaxOUT(Children,alpha,beta)
                        MinEval=min(MinEval,Eval)
                        
                        beta =min(beta,Eval)
                        if beta<=alpha:
                            break
                    else:
                        pass
                    
            return MinEval


"""Defining Grafic functions"""

def Affichage(mat):
    
    t=[[0,0,0],[0,0,0],[0,0,0]]
    
    for i in range(3):
        for j in range(3):
            
            if mat[i,j]==1:
                t[i][j]=CreatCross(ResolutionAffichage)
            elif mat[i,j]==-1:
                t[i][j]=CreatRound(ResolutionAffichage)
            else:
                t[i][j]=np.zeros((ResolutionAffichage,ResolutionAffichage))
                #print("ddddd")
            
    
    Line=np.ones(((t[0][0]).shape[0],1))
    
    A=np.concatenate([t[0][0],Line,t[0][1],Line,t[0][2]],axis=1)
    B=np.concatenate([t[1][0],Line,t[1][1],Line,t[1][2]],axis=1)
    C=np.concatenate([t[2][0],Line,t[2][1],Line,t[2][2]],axis=1)
    
    Line2=np.ones((1,A.shape[1]))
    
    FinalFrame=np.concatenate([A,Line2,B,Line2,C],axis=0)
    im = plt.imshow(1-FinalFrame, cmap='hot')
    plt.show()

def CreatCross(n):
    
    
    Sickness=(n)//8+1
    
    Cross=np.zeros((n,n))
    
    for i in range(n):
        for j in range(n):
            if abs(i-j)<Sickness or abs(i+j-n+1)<Sickness:
                Cross[i,j]=1
    return Cross

def CreatRound(n):
    
    
    if n==3:
        return np.array([[0,1,0],[1,0,1],[0,1,0]])
    if n==5:
        return np.array([[0,1,1,1,0],
                         [1,1,0,1,1],
                         [1,0,0,0,1],
                         [1,1,0,1,1],
                         [0,1,1,1,0]])
    
    Sickness=(n)//8+1
    
    Cross=np.zeros((n,n))
    
    for i in range(n):
        for j in range(n):
            r=(i-(n-1)/2)*(i-(n-1)/2)+(j-(n-1)/2)*(j-(n-1)/2)
            if (n)/2*(4/7)<math.sqrt(r)<n/2:
                Cross[i,j]=1
    return Cross

def CreatColor(n,State):
    Acreat=np.zeros((3**n,3**n,3))
    Acreat[:,:,:3]=ColorPalet[State]
    return Acreat


"""Generating parametres link to black lines thickness"""

DimNotCheat=[1,2,4,8,16,32,64,128,256,512]

def CreatDimCheat(U0):
    DimCheat=[]
    for i in range(deapth+1):
        DimCheat.append(U0)
        U0=U0*3+2*DimNotCheat[i]
    return DimCheat

DimCheat=CreatDimCheat(MinResolution)

def To3D(A):
    return np.concatenate([np.atleast_3d(A),np.atleast_3d(A),np.atleast_3d(A)],axis=2)


"""Defining the 2 main functions"""

def CreatFrame(mat):
    
    rank=np.sum(np.absolute(mat))
    
    if rank<3:
        print("#",end="")
    #print(mat[0,:],mat[1,:],mat[2,:])
    t=[[0,0,0],[0,0,0],[0,0,0]]
    
    for i in range(3):
        for j in range(3):
            
            if mat[i,j]==1:
                
                mat2=np.zeros((3,3))
                for k in range(3):
                    for l in range(3): 
                        mat2[k,l]=mat[k,l]
                mat2[i,j]=1
                
                t[i][j]=CreatColor(int(deapth-rank),MinMaxOUT(mat2)+1) 
                
            elif mat[i,j]==-1:
                
                mat2=np.zeros((3,3))
                for k in range(3):
                    for l in range(3): 
                        mat2[k,l]=mat[k,l]
                mat2[i,j]=-1
                
                t[i][j]=CreatColor(int(deapth-rank),MinMaxOUT(mat2)+1)
                
            elif rank==deapth:
                
                mat2=np.zeros((3,3))
                for k in range(3):
                    for l in range(3): 
                        mat2[k,l]=mat[k,l]
                mat2[i,j]=(-1)**rank
                
                t[i][j]=CreatColor(int(deapth-rank),MinMaxOUT(mat2)+1)
                #print("ddddd")
            else:
                mat2=np.zeros((3,3))
                for k in range(3):
                    for l in range(3): 
                        mat2[k,l]=mat[k,l]
                mat2[i,j]=(-1)**rank
                #print(mat2)
                t[i][j]=CreatFrame(mat2)
    
    #print(t[0][0],t[0][1],t[0][2])
    A=np.concatenate([t[0][0],t[0][1],t[0][2]],axis=1)
    B=np.concatenate([t[1][0],t[1][1],t[1][2]],axis=1)
    C=np.concatenate([t[2][0],t[2][1],t[2][2]],axis=1)
    BNW=np.concatenate([A,B,C],axis=0)
    # State=MinMaxOUT(mat)+1
    # BNW[:,:,:3][(BNW[:,:,1]==0)]=ColorPalet[State]
    
    return BNW

def CreatFrameLineColor(mat):
    
    rank=np.sum(np.absolute(mat))
    
    #print(mat[0,:],mat[1,:],mat[2,:])
    t=[[0,0,0],[0,0,0],[0,0,0]]
    
    if rank<3:
        print("#",end="")
    
    for i in range(3):
        for j in range(3):
            
            if mat[i,j]==1:
                t[i][j]=To3D(CreatCross(DimCheat[int(deapth-rank)]))
            elif mat[i,j]==-1:
                t[i][j]=To3D(CreatRound(DimCheat[int(deapth-rank)]))
            elif rank==deapth:
                t[i][j]=To3D(np.zeros((MinResolution,MinResolution)))
                #print("ddddd")
            else:
                mat2=np.zeros((3,3))
                for k in range(3):
                    for l in range(3): 
                        mat2[k,l]=mat[k,l]
                mat2[i,j]=(-1)**rank
                t[i][j]=CreatFrameLineColor(mat2)
    
    Line=np.ones(((t[0][0]).shape[0],int(DimNotCheat[int(deapth-rank)]),3))
    
    A=np.concatenate([t[0][0],Line,t[0][1],Line,t[0][2]],axis=1)
    B=np.concatenate([t[1][0],Line,t[1][1],Line,t[1][2]],axis=1)
    C=np.concatenate([t[2][0],Line,t[2][1],Line,t[2][2]],axis=1)
    
    Line2=np.ones((int(DimNotCheat[int(deapth-rank)]),A.shape[1],3))
    BNW=np.concatenate([A,Line2,B,Line2,C],axis=0)
    
    
    State=MinMaxOUT(mat)+1
    BNW[:,:,:3][(BNW[:,:,1]==0)]=ColorPalet[State]
    
    return BNW



for i in range(9*9+1):
    print("_",end="")
print("100%")

if GenerationType:
    A1=CreatFrame(InitialGame) #cree ta propre mat
    im = plt.imshow(1-A1, cmap='hot')
    plt.show() 
    im = Image.fromarray(((1-A1)*255).astype(np.uint8))
    im.save(path+'TTT (Color, Deapth='+str(deapth)+', P='+str(PaletNumber)+').bmp')

else:
    A4=CreatFrameLineColor(InitialGame)
    im = plt.imshow(1-A4, cmap='hot')
    plt.show() 
    im = Image.fromarray(((1-A4)*255).astype(np.uint8))
    im.save(path+'TTT (Game, Deapth='+str(deapth)+', Res='+str(MinResolution)+', P='+str(PaletNumber)+').bmp')

print("100%")
print("MainTTT : DONE")









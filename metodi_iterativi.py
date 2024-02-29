# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 09:28:22 2023

@author: Antonio
"""

import numpy as np

def jacobi(A, b, x0, toll, kmax):
    k=0
    n=np.size(b)
    stimaerrore = 1.0
    ier=0
    x = np.zeros([n,1])
    
    for i in range(n):
        if A[i,i]==0:
            print("Attenzione elemento nullo sulla diagonale")
            x=[]
            ier=2
            return x,k,stimaerrore,ier
    
    while k<kmax and stimaerrore>=toll:
        for i in range(n):
            somma1 = 0
            for j in range(i):
                somma1 += A[i, j]*x0[j]
                
            somma2 = 0
            for j in range(i+1, n):
                somma2 += A[i, j]*x0[j]
            
            x[i]=(b[i]-somma1-somma2)/A[i, i]
            
        stimaerrore=np.linalg.norm(x-x0, 2)/np.linalg.norm(x, 2)
            
        k+=1
        
        x0=np.copy(x)
        
    if stimaerrore>toll:
        ier=1
    return x,k,stimaerrore,ier
    
def gauss_seidel(A, b, x0, toll, kmax):
    k=0
    n=np.size(b)
    stimaerrore = 1.0
    ier=0
    x = np.zeros([n,1])
        
    for i in range(n):
        if A[i,i]==0:
            print("Attenzione elemento nullo sulla diagonale")
            x=[]
            ier=2
            return x,k,stimaerrore,ier
        
    while k<kmax and stimaerrore>=toll:
        for i in range(n):
            somma1 = 0
            for j in range(i):
                somma1 += A[i, j]*x[j]
                    
            somma2 = 0
            for j in range(i+1, n):
                somma2 += A[i, j]*x0[j]
                
            x[i]=(b[i]-somma1-somma2)/A[i, i]
                
        stimaerrore=np.linalg.norm(x-x0, 2)/np.linalg.norm(x, 2)
                
        k+=1
            
        x0=np.copy(x)
            
    if stimaerrore>toll:
        ier=1
    return x,k,stimaerrore,ier
            
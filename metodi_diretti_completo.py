# -*- coding: utf-8 -*-
"""
Created on Mon May  8 15:42:42 2023

@author: Antonio
"""

import sys
import numpy as np

def backsubst(A,b):
    n=np.size(A, 1)
    x=np.zeros((n, 1))

    x[n-1] = b[n-1]/A[n-1, n-1]

    for i in range(n-2, -1, -1):
        somma = 0.0
        for j in range(i+1, n):
            somma = somma+A[i,j]*x[j]
        
            x[i]=(b[i]-somma)/A[i,i]
   
    return x

def gaussNaive(A,b):
    
    U=np.copy(A)
    c=np.copy(b)
    
    n=np.size(A,0)
    C=np.linalg.norm(A, np.inf)
    deter =1
    
    for k in range(n-1):
        if U[k][k]==0:
            print("Attenzione elemento nullo sulla diagonale")
            deter=[]
            return U, c, deter
        
        if abs(U[k][k])<sys.float_info.epsilon*C:
            print("Attenzione possibile elemento nullo sulla diagonale")
            
        deter=deter*U[k][k]
        for i in range(k+1, n):
            m=-U[i][k]/U[k][k]
            U[i,k:]=U[i,k:]+m*U[k,k:]
            c[i]=c[i]+m*c[k]

    deter=deter*U[n-1][n-1]
    
    if U[n-1][n-1]==0:
        print("Attenzione det(A)=0")
    if abs(U[n-1][n-1])<sys.float_info.epsilon*C:
        print("Attenzione il determinante di A potrebbe essere zero!")
    return U, c, deter

def gaussPiv(A,b):
    U = np.copy(A)
    c = np.copy(b)
    
    n = np.size(A,0)
    C = np.linalg.norm(A, np.inf)
    deter=1
    pivot=np.arange(n)

    for k in range(n-1):
        r = np.argmax(abs((U[k:n, k])))
        r = r+k
        
        if r>k:
            U[[k,r],k:] = U[[r,k],k:]
            c[[k,r]] = c[[r,k]]
            pivot[[k,r]] = pivot[[r,k]]
            deter = -deter

        if U[k][k] == 0:
            print("Attenzione det(A)=0")
            deter=[]
            return U, c, deter
        
        if abs(U[k][k])<sys.float_info.epsilon*C:
               print("Attenzione il determinante di A potrebbe essere zero")
               
		
        deter=deter*U[k][k]
        for i in range (k+1,n):
            m = -U[i][k]/U[k][k]
            U[i, k:] = U[i,k:]+m*U[k,k:]
            c[i] = c[i]+m*c[k]
        
        deter = deter*U[n-1][n-1]

        if U[n-1][n-1]==0:
            print("Attenzione det(A)=0")
            

        if abs(U[n-1][n-1])<sys.float_info.epsilon*C:
            print("Attenzione il determinante di A potrebbe essere zero!")


    return U, c, deter
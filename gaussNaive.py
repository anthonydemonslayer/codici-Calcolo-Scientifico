# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 13:02:13 2023

@author: Antonio
"""

import sys
import numpy as np

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
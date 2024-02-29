# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 11:47:04 2023

@author: Antonio
"""
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
        
        
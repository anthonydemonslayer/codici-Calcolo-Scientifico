# -*- coding: utf-8 -*-
"""
Created on Mon May 15 15:53:52 2023

@author: Antonio
"""

import numpy as np

def metodo_potenze(A: np.array, toll:float, n_iter_max:int, y0: np.array, verbose=False):
    n_iter=0
    stima_errore=1.0
    lambdan0=0.0
    
    while n_iter<n_iter_max and stima_errore>=toll:
        w=np.dot(A,y0)
        k=np.argmax(np.abs(w))
        
        lambdaa = w[k]/y0[k]
        stima_errore=abs(lambdaa-lambdan0)/abs(lambdaa)
        lambdan0 = lambdaa
        
        y = w/np.linalg.norm(w, ord=1)
        y0 = np.copy(y)
        n_iter += 1
        
        if verbose:
            print("n_iter = ", n_iter, ", lambda =", lambdaa)
            print(y.T)
        
    return lambdaa, stima_errore, n_iter, y
    
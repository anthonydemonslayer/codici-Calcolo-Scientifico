# -*- coding: utf-8 -*-
"""
Created on Mon May  8 16:16:15 2023

@author: Antonio
"""

import sys
import numpy as np
import metodi_iterativi as metiter

A = np.array([[66, 26, -1, 9],
             [26, 14, -2, 7],
             [-1, 2, 5, 2],
             [-9, 7, 2, 54]])

b = np.array([[303/2],
              [209/2],
              [7],
              [84]])

xEsatta = np.array([[2],
                    [3],
                    [0],
                    [3/2]])

epsilon = sys.float_info.epsilon
x0 = np.zeros((np.size(b, 0),1))
toll = 1e-3
kmax = 100
print("Soluzione esatta ")
print(xEsatta)

np.set_printoptions(precision=16)
xJacobi, niterJ, stimaerrJ, ierJ  = metiter.jacobi(A, b, x0, toll, kmax)
print("Soluzione con metodo di Jacobi: ")
print(xJacobi)
errRelJacobi = np.linalg.norm(xJacobi-xEsatta, 2)/np.linalg.norm(xJacobi, 2)
print("Errore relativo Jacobi: %e" % errRelJacobi)
print("stima errore Jacobi: %e" % stimaerrJ)
print("Numero di iterazioni Jacobi: ", niterJ)
print("indicatore di errore Jacobi: ")
print(ierJ)

xGaussSeidel, niterGS, stimaerrGS, ierGS = metiter.gauss_seidel(A, b, x0, toll, kmax)
print("Soluzione con metodo di Gauss Seidel: ")
print(xGaussSeidel)
errRelGaussSeidel = np.linalg.norm(xGaussSeidel-xEsatta, 2)/np.linalg.norm(xGaussSeidel, 2)
print("Errore relativo Gauss Seidel: %e" % errRelGaussSeidel)
print("stima errore Gauss Seidel %e: " % stimaerrGS)
print("Numero di iterazioni Gauss Seidel: ", niterGS)
print("indicatore di errore Gauss Seidel: ")
print(ierGS)

indice_condizionamento = np.linalg.cond(A)
print("Indice di condizionamento matrice A: ", indice_condizionamento)

print("epsilon: ", epsilon)
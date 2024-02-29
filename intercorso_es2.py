# -*- coding: utf-8 -*-
"""
Created on Thu May 11 11:36:32 2023

@author: Antonio
"""

import numpy as np
import metodi_diretti_completo as metdir

epsilon = 1e-12
A = np.array([[10, 2, 3],
      [-3, 0, 1],
      [4+epsilon, 2+epsilon, 5+epsilon]])

b = np.array([[95],
              [-25],
              [45+16*epsilon]])

xEsatta = ([[8],
            [9],
            [-1]])

U, c, deterNaive = metdir.gaussNaive(A, b)
xNaive = metdir.backsubst(U, c)
errNaive = np.linalg.norm(xNaive-xEsatta, 2)/np.linalg.norm(xEsatta, 2)

U, c, deterPiv = metdir.gaussPiv(A, b)
xPivoting = metdir.backsubst(U, c)
errPivoting = np.linalg.norm(xPivoting-xEsatta, 2)/np.linalg.norm(xEsatta, 2)

xNumpy = np.linalg.solve(A,b)
errNumpy = np.linalg.norm(xNumpy-xEsatta, 2)/np.linalg.norm(xEsatta, 2)
detNumpy = np.linalg.det(A)

indice_condizionamento_matrice = np.linalg.cond(A)

np.set_printoptions(precision=16)

print("\nSoluzione esatta: ")
print(xEsatta)

print("\nSoluzione con Gauss Naive: ")
print(xNaive)
print("\nerrore Gauss Naive: %e" % errNaive)
print("\nDeterminante Gauss Naive: %20.15e" % deterNaive)

print("\nSoluzione con Gauss Pivoting: ")
print(xPivoting)
print("\nerrore Gauss Pivoting: %e" % errPivoting)
print("\nDeterminante Gauss Pivoting: %20.15e" % deterPiv)

print("\nsoluzione Numpy: ")
print(xNumpy)
print("\nerrore relativo Numpy: %e" % errNumpy)
print("\nDeterminante Numpy: %20.15e" % detNumpy)

print("indice condizionamento matrice A: %e" % indice_condizionamento_matrice)

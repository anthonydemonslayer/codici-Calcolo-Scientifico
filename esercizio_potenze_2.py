# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 18:23:11 2023

@author: Antonio
"""

import numpy as np
import metodo_potenze as metpot

np.set_printoptions(precision=16)
A = np.array([[65/9, 10/9, -155/9],
              [10/9, -85/9, -145/9],
              [-155/9, -145/9, -5/18]])


tollA = 1e-3;
tollB = 1e-6;
nmax = 9999;
x0 = np.array([[1],
               [1],
               [1]])

lambdaaA, stimaerroreA, niterA, vA = metpot.metodo_potenze(A, tollA, nmax, x0)
lambdaaB, stimaerroreB, niterB, vB = metpot.metodo_potenze(A, tollB, nmax, x0)
#lambdaaB, stimaerroreB, niterB, vB = metpot.metodo_potenze(B, toll, nmax, x0)

print("tolleranza 10 a -3:")
print("lambda A: ", lambdaaA)
print("stima errore matrice A: ", stimaerroreA)
print("numero iterazioni A: ", niterA)

print("con tolleranza 10 a -6:")
print("lambda B: ", lambdaaB)
print("stima errore matrice A: ", stimaerroreB)
print("numero iterazioni B: ", niterB)
eigvaluesA = np.linalg.eigvals(A)

iA = np.argmax(np.abs(eigvaluesA))
#iB = np.argmax(np.abs(eigvaluesB))
lambdaa_npA = eigvaluesA[iA]
errRelA = np.abs(lambdaa_npA-lambdaaA)/abs(lambdaa_npA)
#lambdaa_npB = eigvaluesB[iB]
#errRelB = np.abs(lambdaa_npB-lambdaaB)/abs(lambdaa_npB)
print("errore relativo matrice A: ", errRelA)
#print("errore relativo matrice B: ", errRelB)
print("soluzione esatta A: ", lambdaa_npA)
#print("soluzione esatta B: ", lambdaa_npB)

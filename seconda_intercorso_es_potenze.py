# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 10:11:08 2023

@author: Antonio
"""

import numpy as np
import metodo_potenze as metpot

np.set_printoptions(precision=16)

A = np.array([[-317/624, 757/780, -1147/1560],
              [913/780, -317/624, 523/1560],
              [-523/1560, 1147/1560, 23/78]])

B = np.array([[-544/195, -16/3, -1028/195],
              [-16/3, -2092/195, -2068/195],
              [-1028/195, -2068/195, -2098/195]])

toll = 1e-5
nitermax = 999

x0 = np.array([[1],
               [1],
               [1]])

lambdaaA, stimaerroreA, niterA, vA = metpot.metodo_potenze(A, toll, nitermax, x0)
lambdaaB, stimaerroreB, niterB, vB = metpot.metodo_potenze(B, toll, nitermax, x0)

print("lambda matrice A: ", lambdaaA)
print("stima errore matrice A: ", stimaerroreA)
print("numero di iterazioni sulla matrice A: ", niterA)

print("lambda matrice B: ", lambdaaB)
print("stima errore B: ", stimaerroreB)
print("numero di iterazioni sulla matrice B: ", niterB)

eigvaluesA = np.linalg.eigvals(A)
eigvaluesB = np.linalg.eigvals(B)

iA = np.argmax(np.abs(eigvaluesA))
iB = np.argmax(np.abs(eigvaluesB))
lambdaa_npA = eigvaluesA[iA]
lambdaa_npB = eigvaluesB[iB]

errRelA = np.abs(lambdaa_npA-lambdaaA)/abs(lambdaa_npA)
errRelB = np.abs(lambdaa_npB-lambdaaB)/abs(lambdaa_npB)

print("errore relativo matrice A: ", errRelA)
print("soluzione esatta A: ", lambdaa_npA)

print("errore relativo matrice B: ", errRelB)
print("soluzione esatta B: ", lambdaa_npB)

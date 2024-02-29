# -*- coding: utf-8 -*-
"""
Created on Mon May 29 12:55:45 2023

@author: Antonio
"""

import numpy as np
import metodo_potenze as metpot

np.set_printoptions(precision=16)

A = np.array([[-58.0/9, -32.0/9, 16.0/9],
              [-32.0/9, -58.0/9, -16.0/9],
              [16.0/9, -16.0/9, -82.0/9]],
             dtype=float)

B = np.array([[-56.0/45, -20.0/9, -97.0/45],
              [-20.0/9, -203.0/45, -197.0/45],
              [-97.0/45, -197.0/45, -409.0/90]],
             dtype=float)

toll = 1e-5;
nMax = 50;
x0 = np.array([[1.0],
               [1.0],
               [1.0]],
              dtype=float)


lambdaaA, stimaErroreA, niterA, vA = metpot.metodo_potenze(A, toll, nMax, x0)

print("Lambda: ")
print(lambdaaA)
print("Stima errore: ")
print(stimaErroreA)
print("Numero di iterazioni: ")
print(niterA)
print("Autovettore: ")
print(vA)

eigvalues = np.linalg.eigvals(A)
i = np.argmax(np.abs(eigvalues))
lambdaa_np = eigvalues[i]
errRelA = np.abs(lambdaa_np-lambdaaA)/abs(lambdaa_np)
print("Errore relativo matrice A: ")
print(errRelA)

lambdaaB, stimaErroreB, niterB, vB = metpot.metodo_potenze(B, toll, nMax, x0)

print("Lambda: ")
print(lambdaaB)
print("Stima errore: ")
print(stimaErroreB)
print("Numero di iterazioni: ")
print(niterB)
print("Autovettore: ")
print(vB)

eigvalues = np.linalg.eigvals(B)
i = np.argmax(np.abs(eigvalues))
lambdaa_np = eigvalues[i]
errRelB = np.abs(lambdaa_np-lambdaaB)/abs(lambdaa_np)
print("Errore relativo matrice B: ")
print(errRelB)
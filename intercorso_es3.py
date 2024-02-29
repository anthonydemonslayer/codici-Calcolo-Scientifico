# -*- coding: utf-8 -*-
"""
Created on Thu May 11 11:36:34 2023

@author: Antonio
"""

import sys
import numpy as np
import metodi_iterativi as metiter

A = np.array([[-352/3, -88/3, -88/3],
              [-176/3, 264, 0],
              [0, 704/3, 176]])

b = np.array([[12],
              [-14],
              [28]])

xEsatta = ([[-87/583],
            [-201/2332],
            [639/2332]])

x0 = np.zeros((np.size(b, 0),1))
eps = sys.float_info.epsilon
toll = eps
kmax = 99999

np.set_printoptions(precision=16)
print("Soluzione carta e penna: ")
print(xEsatta)
xJacobi, niterJacobi, stimaErroreJacobi, ierJacobi = metiter.jacobi(A, b, x0, toll, kmax)
print("Solzuione con metodo di Jacobi: ", xJacobi)
errRelJacobi = np.linalg.norm(xJacobi-xEsatta, 2)/np.linalg.norm(xJacobi, 2)
print("errore Relativo Jacobi: %e" % errRelJacobi)
print("\nStima dell'errore Jacobi: %e" % stimaErroreJacobi)
print("\nNumero di iterazioni Jacobi: ", niterJacobi)
print("\nIndicatore di errore Jacobi: ", ierJacobi)

xGaussSeidel, niterGaussSeidel, stimaErroreGaussSeidel, ierGS = metiter.gauss_seidel(A, b, x0, toll, kmax)
print("Solzuione con metodo di Gauss Seidel: ", xGaussSeidel)
errRelGaussSeidel = np.linalg.norm(xGaussSeidel-xEsatta, 2)/np.linalg.norm(xGaussSeidel, 2)
print("errore Relativo Gauss Seidel: %e" % errRelGaussSeidel)
print("\nStima dell'errore Gauss Seidel: %e" % stimaErroreGaussSeidel)
print("\nNumero di iterazioni Gauss Seidel: ", niterGaussSeidel)
print("\nIndicatore di errore Gauss Seidel: ", ierGS)

indice_condizionamento = np.linalg.cond(A)
print("indice di condizionamento matrice A: %e" % indice_condizionamento)

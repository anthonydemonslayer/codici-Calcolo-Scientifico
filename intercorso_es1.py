# -*- coding: utf-8 -*-
"""
Created on Thu May 11 11:36:28 2023

@author: Antonio
"""

import numpy as np
np.set_printoptions(precision=16)

#punto 1
a = 472.01602090
b = -472.01602080
cvero = 1e-7
c = a+b
print("soluzione: ", c)
errRel = np.abs(c-cvero)/np.abs(c)
print("errore: ", errRel)

#punto 2
a = 1
b = 1e-14
cvero = 1.00000000000001
c = a+b
print("soluzione: ", c)
errRel = np.abs(c-cvero)/np.abs(c)
print("errore: ", errRel)

#punto 3
#a = 0.145891e-14
#b = 4.44741e4
#cvero = 4447,41000000000000145891
#c = a+b
#print("soluzione: ", c)
#errRel = np.abs(c-cvero)/np.abs(c)
#print("errore: ", errRel)

##punto 4
a = 9.89174e-99
b = 2.28105e-229
c = 4.51325e71
d1 = (a*b)*c
d2 = a*(b*c)
print("soluzione 1: ", d1)
print("soluzione 2: ", d2)

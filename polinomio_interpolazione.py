# -*- coding: utf-8 -*-
"""
Created on Mon May 22 11:50:59 2023

@author: Antonio
"""

import numpy as np
import matplotlib.pyplot as plt

a = 1921
b = 2001

anno = np.array([1921, 1931, 1951, 1961, 1971, 1981, 1991, 2001])
popolazione = 1e3*np.array([39944, 41652, 47516, 50624, 54137, 56557, 56778, 56305])

plt.plot(anno,popolazione,marker = 'o', color = 'red', linestyle = 'none', label='dati')

x = np.linspace(a,b,1000)

p = np.polyfit(anno,popolazione,8)

y_polinomio = np.polyval(p,x)
plt.plot(x,y_polinomio,color = 'blue', label = 'polinomio di interpolazione')

plt.title("Fitting dati discreti")
plt.xlabel("Anno")
plt.ylabel("Popolazione")
plt.legend()
plt.savefig('ex_dati_discreti.png')
plt.show()


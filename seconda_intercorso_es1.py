# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 09:31:11 2023

@author: Antonio
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

arrayX = np.array([2.4, 4.2, 6.6, 7.9, 11, 12.3, 13.5, 16.7, 19])
arrayY = np.array([24.62, 35.96, 51.08, 59.27, 78.8, 86.99, 94.55, 114.71, 129.2])

a = -10
b = 30

plt.plot(arrayX,arrayY,marker = 'o', color = 'green', linestyle = 'None', label = 'Dati')

x = np.linspace(a,b,1000)

p1 = np.polyfit(arrayX,arrayY,1)
p2 = np.polyfit(arrayX,arrayY,2)
p3 = np.polyfit(arrayX,arrayY,3)
p4 = np.polyfit(arrayX,arrayY,4)

y_p1 = np.polyval(p1,x)
y_p2 = np.polyval(p2,x)
y_p3 = np.polyval(p3,x)
y_p4 = np.polyval(p4,x)

plt.plot(x,y_p1,color = 'red', label = 'retta di regressione')
plt.plot(x,y_p2,color = 'orange', label = 'minimi quadrati grado 2')
plt.plot(x,y_p3,color = 'yellow', label = 'minimi quadrati grado 3')
plt.plot(x,y_p4,color = 'blue', label = 'polinomio di interpolazione')

#spline cubica
f = CubicSpline(arrayX,arrayY,bc_type='natural')
x_new = np.linspace(0,9,100)
y_new = f(x_new)
plt.plot(x_new,y_new, color = 'purple', label='spline cubica')

plt.legend()
plt.title('Esercizio 1')
plt.xlabel('asse x')
plt.ylabel('asse y')
plt.savefig('Esercizio_1.png')
plt.show()

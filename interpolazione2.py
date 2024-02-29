# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 18:04:20 2023

@author: Antonio
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

a = 1.9
b = 16.6

arrayX = np.array([1.9, 2.9, 8, 9.2, 10.9, 12.2, 16.6])
arrayY = np.array([23.43, 41.83, 229, 295.72, 405.03, 500.32, 898.08])

#grafico
plt.plot(arrayX, arrayY, marker = 'o', color='purple', linestyle='None', label='grafico funzione')

x = np.linspace(a,b,1000)

#calcolo minimi quadrati
p1 = np.polyfit(arrayX,arrayY,1)
p2 = np.polyfit(arrayX,arrayY,2)
p3 = np.polyfit(arrayX,arrayY,3)

y_p1 = np.polyval(p1,x)
y_p2 = np.polyval(p2,x)
y_p3 = np.polyval(p3,x)

plt.plot(x,y_p1,color= 'yellow', label='retta di regressione')
plt.plot(x,y_p2,color = 'green', label='minimi quadrati grado 2')
plt.plot(x,y_p3,color = 'red', label='interpolazione')

#spline cubica
f = CubicSpline(arrayX,arrayY,bc_type='natural')
x_new = np.linspace(0,7,100)
y_new = f(x_new)
plt.plot(x_new,y_new, color = 'blue', label='spline cubica')

plt.legend()
plt.title('Esercizio interpolazione')
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('esercizio_interpolazione2.png')
plt.show()
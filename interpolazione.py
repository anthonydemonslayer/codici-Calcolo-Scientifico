# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 18:53:11 2023

@author: Antonio
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline


a = 0.6
b = 8.9

ascisse = np.array([0.6, 0.7, 3.3, 4.3, 4.4, 4.9, 5.2, 5.5, 8.3, 8.9])
ordinate = np.array([9.128, 10.299, 158.681, 316.191, 336.232, 449.577, 528.744, 616.875, 1960.231, 2393.137])

#grafico funzione sul piano cartesiano
plt.plot(ascisse, ordinate, marker = 'o', color = 'green', linestyle='None', label='Dati')


x = np.linspace(a,b,1000)

#calcolo minimi quadrati
p1 = np.polyfit(ascisse,ordinate,1)
p2 = np.polyfit(ascisse,ordinate,2)
p3 = np.polyfit(ascisse,ordinate,3)
p4 = np.polyfit(ascisse,ordinate,4)

y_p1 = np.polyval(p1,x)
y_p2 = np.polyval(p2,x)
y_p3 = np.polyval(p3,x)
y_p4 = np.polyval(p4,x)

plt.plot(x,y_p1,color= 'yellow', label='retta di regressione')
plt.plot(x,y_p2,color = 'green', label='minimi quadrati grado 2')
plt.plot(x,y_p3,color = 'red', label='minimi quadrati grado 3')
plt.plot(x,y_p4,color = 'orange', label='interpolazione')

f = CubicSpline(ascisse,ordinate,bc_type='natural')
x_new = np.linspace(0,10,100)
y_new = f(x_new)
plt.plot(x_new,y_new, color = 'blue', label='spline cubica')

#visualizzazione grafico
plt.legend()
plt.title('Esercizio interpolazione')
plt.xlabel('ascisse')
plt.ylabel('ordinate')
plt.savefig('esercizio_interpolazione.png')
plt.show()


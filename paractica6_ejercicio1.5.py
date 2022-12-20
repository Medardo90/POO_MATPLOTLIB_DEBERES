# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 01:18:43 2022

@author: Pablo Estrada
"""
#ejemplo 2d
import numpy as np
 
import matplotlib.pyplot as plt
 
plt.figure()
 
x = np.arange(-5, 5, 0.01)
 
y = np.arange(-5, 5, 0.01)
 
X, Y = np.meshgrid(x, y)
 
# Definimos cos (x^3 + y^2)
 
fxy = np.cos(X**3+Y**2)
 
plt.imshow(fxy);
 
plt.colorbar();
 
plt.show()


#https://unipython.com/matplotlib-funciones-principales/
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 01:22:46 2022

@author: Pablo Estrada
"""
# histogramas
import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
x = np.random.normal(5, 1.5, size=1000)
ax.hist(x, np.arange(0, 11))
plt.show()
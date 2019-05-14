# -*- coding: utf-8 -*-
"""WEEK_6_Micro_Project_Matrix.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14aQdC9XfNedN7MptQisIehzhH3xg20FG
"""

!pip install scipy

from scipy.linalg import expm
import numpy as np
import matplotlib.pyplot as plt

x = np.array([[-3,3],[5,-5]])

t = np.arange(0, 1, 0.01)
m = np.zeros((len(t),2,2))
m1_1= np.zeros(len(t))
m1_2= np.zeros(len(t))
m2_1= np.zeros(len(t))
m2_2= np.zeros(len(t))

expm(x*t[0])

for i in range(0, len(t)):
    m[i] = expm(x*t[i])
    m1_1[i] = m[i,0,0]
    m1_2[i] = m[i,0,1]
    m2_1[i] = m[i,1,0]
    m2_2[i] = m[i,1,1]

plt.plot (t,m1_1)
plt.plot (t,m1_2)
plt.plot (t,m2_1)
plt.plot (t,m2_2)
plt.show()



#WEEK_6_Micro_Project_Matrix_in_R 

# Matrix using R
### https://rextester.com/NFDB13385


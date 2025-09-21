# -*- coding: utf-8 -*-
"""
Created on Sun Sep 21 21:20:32 2025

@author: spoor
"
"""
#variation of P with p

import matplotlib.pyplot as plt
import numpy as np

n=5

p = np.linspace(0, 1, 200)

P1 = (1-(1-p**n)**n)**n 

P2 = 1-(1-p**n)**(n**2)

plt.figure()
plt.plot(p, P1, label ="P1", color= 'blue')
plt.plot(p, P2, label="P2", color = 'red')
plt.xlabel("p")
plt.ylabel("Probability of the bulb glowing")
plt.title("P1 and P2 vs p")
plt.show()

#variation of P with n

t=0.5

n = np.linspace(2, 50)

T1 = (1-(1-t**n)**n)**n 

T2 = 1-(1-t**n)**(n**2)
plt.figure()
plt.plot(n, T1, label ="P1", color= 'black')
plt.plot(n, T2, label="P2", color = 'green')
plt.xlabel("p")
plt.ylabel("Probability of the bulb glowing")
plt.title("P1 and P2 vs p")
plt.show()
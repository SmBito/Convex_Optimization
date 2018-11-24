#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 15:40:08 2018

@author: Bilto
"""

import numpy as np
import matplotlib.pyplot as plt

iteration = np.linspace(0, 99, num = 100)

def my_fun(x):
    output = x**2 + 3*x
    return output


x_grid = np.linspace(-10, 10, num = 100)
my_plot = plt.plot(x_grid, my_fun(x_grid))
plt.show()

print ('*********  Random Search  ***********')

# Plot function
my_plot = plt.plot(x_grid, my_fun(x_grid))
plt.figure(figsize=(18,10))

# Initial guess
x_0 = 8
best_point = x_0

for i in range(50):
    # Generate a random number between -10 and +10
    x_k = np.random.rand()*20 - 10    
    if my_fun(x_k)<= my_fun(best_point):
        best_point = x_k
        plt.plot(best_point,my_fun(best_point) ,marker = 'x', markersize = 14, markeredgewidth = 3, color = 'red')
    else:
        plt.plot(x_k,my_fun(x_k) ,marker = 'x', markersize = 14, markeredgewidth = 3, color = 'black')

    # Annotate the axis to show iteration number
    plt.annotate('iter '+ str(i), xy=(x_k,my_fun(x_k) ), xytext=(x_k+1,my_fun(x_k)+1 ),textcoords='offset points', ha='right', va='bottom',
            arrowprops=dict(arrowstyle = '->', connectionstyle='arc3,rad=0'), bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5))
plt.show()

print ('*********  Best solution  ***********')
plt.plot(x_grid, my_fun(x_grid))
plt.plot(best_point,my_fun(best_point) ,marker = 'x', markersize = 14, markeredgewidth = 3)
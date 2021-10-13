# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 05:41:54 2021

@author: denis
"""


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from math import floor, log

def g(x, y):
    return (np.cos(4.5*x + 0.3) - x * (x + 0.2) - 1.01 + np.sin(y+2))

low = -3
high = 3
step = 0.2
p = np.arange(low, high, step)
n = len(p)
z = np.zeros((n, n), dtype=float)
valores=[]
paso = 0.5

digitos = floor(log(100, 10)) + 1
guardar = 0
for i in range(n):
    x = p[i]
    for j in range(n): 
        y = p[n - j - 1] # voltear
        z[i, j] = g(x, y)
        valores.append(g(x, y))
maximo=max(valores)

r = [15, 30, 45]
xi1 = 0.33
xi2 = 0.99
for re in r:
    
    df1 = pd.read_csv('resultados_{0:}.csv'.format(re))
    df2 = pd.read_csv('resultados_{0:}_T10_xi3.csv'.format(re))
    df3 = pd.read_csv('resultados_{0:}_T100_xi1.csv'.format(re))


    p1 = df1[str(re)+' con 100'],df2['T 10'+' xi '+str(xi1) +' '+str(re)+' con 100'],df3['T 100'+' xi '+ str(xi2)+ ' '+str(re)+' con 100']
    p2 = df1[str(re)+' con 1000'],df2['T 10'+' xi '+str(xi1) + ' '+str(re)+' con 1000'],df3['T 100'+' xi '+ str(xi2)+ ' '+str(re)+' con 1000']
    p3 = df1[str(re)+' con 10000'],df2['T 10'+' xi '+str(xi1) +' '+str(re)+' con 10000'],df3['T 100'+' xi '+ str(xi2)+ ' '+str(re)+' con 10000']
    medianprops = dict(linestyle='solid', linewidth=2.5, color='red')
    
    xticks=['s/T','T=10','T=100']
    p=[x for x in range(1,4)] 
    
    
    plt.boxplot(p1,medianprops=medianprops)
    plt.ylabel('Maximos')
    plt.xticks(p, xticks)
    plt.xlabel('replicas '+str(re))
    plt.axhline(maximo, color = 'green',label='Maximo estimado') 
    # plt.legend()
    plt.savefig('p7_p100_r'+str(re)+'.png', dpi=300)
    plt.show()
    plt.close()
    
    plt.boxplot(p2,medianprops=medianprops)
    plt.ylabel('Maximos')
    plt.xticks(p, xticks)
    plt.xlabel('replicas '+str(re))
    plt.axhline(maximo, color = 'green',label='Maximo estimado') 
    # plt.legend() 
    plt.savefig('p7_p1000_r'+str(re)+'.png', dpi=300)
    plt.show()
    plt.close()
    
    plt.boxplot(p3,medianprops=medianprops)
    plt.ylabel('Maximos')
    plt.xticks(p, xticks)
    plt.xlabel('replicas '+str(re))
    plt.axhline(maximo, color = 'green',label='Maximo estimado') 
    # plt.legend() 
    plt.savefig('p7_p10000_r'+str(re)+'.png', dpi=300)
    plt.show()
    plt.close()
from random import randint, random
from math import fabs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = []
data2 = []
data3 = []
largos = [10, 1000, 10000]

for dimension in range(1, 4):
    for duracion in largos:
    	for replica in range(50):
            pos = [0] * dimension
            mayor = 0
            for t in range(duracion):
                cambiar = randint(0, dimension - 1)
                cambio = 1
                if random() < 0.5:
                    cambio = -1
                pos[cambiar] += cambio
                d = sum([fabs(p) for p in pos])
                if d > mayor:
                    mayor = d
            resultado = [dimension, duracion, replica, mayor]
            data.append(resultado)

datos = pd.DataFrame(data, columns = ['Dim', 'Dur', 'Rep', 'Dist'])

for dimension in range(1, 7):
    for duracion in largos:
    	for replica in range(50):
            pos = [0] * dimension
            mayor = 0
            for t in range(duracion):
                cambiar = randint(0, dimension - 1)
                cambio = 1
                if random() < 0.5:
                    cambio = -1
                pos[cambiar] += cambio
                d = sum([fabs(p) for p in pos])
                if d > mayor:
                    mayor = d
            resultado = [dimension, duracion, replica, mayor]
            data.append(resultado)

datos2 = pd.DataFrame(data, columns = ['Dim', 'Dur', 'Rep', 'Dist'])


for dimension in range(1, 16):
    for duracion in largos:
    	for replica in range(50):
            pos = [0] * dimension
            mayor = 0
            for t in range(duracion):
                cambiar = randint(0, dimension - 1)
                cambio = 1
                if random() < 0.5:
                    cambio = -1
                pos[cambiar] += cambio
                d = sum([fabs(p) for p in pos])
                if d > mayor:
                    mayor = d
            resultado = [dimension, duracion, replica, mayor]
            data.append(resultado)

datos3 = pd.DataFrame(data, columns = ['Dim', 'Dur', 'Rep', 'Dist'])

g1 = datos[datos['Dur'] == 10]
g2 = datos[datos['Dur'] == 1000]
g3 = datos[datos['Dur'] == 10000]


g16 = datos2[datos2['Dur'] == 10]
g26 = datos2[datos2['Dur'] == 1000]
g36 = datos2[datos2['Dur'] == 10000]

g115 = datos3[datos3['Dur'] == 10]
g215 = datos3[datos3['Dur'] == 1000]
g315 = datos3[datos3['Dur'] == 10000]


plt.boxplot([g1['Dist'], g16['Dist'], g115['Dist'], g2['Dist'], g26['Dist'], g215['Dist'], g3['Dist'], g36['Dist'], g315['Dist']], patch_artist=True, boxprops=dict(facecolor=c, color=c))


plt.yscale('log')
plt.title('Resultados distancia Manhattan', fontsize = '18')
plt.ylabel('Largo de caminata', loc = 'top')
plt.xlabel('Dimensiones/\nPasos 10 100 10000\nReplicas = 50', loc = 'center')

xvalues = ['  ', '3', '6', '15', '3', '6', '15', '3', '6', '15']
plt.xticks(np.arange(10), xvalues, )
plt.savefig('figurap1.png', dpi = 400)
plt.show()


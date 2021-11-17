from random import randint
from math import floor, log
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def simu(N, G, B):
    modelos = pd.read_csv('digits.txt', sep=' ', header = None)
    modelos = modelos.replace({'n': N, 'g': G, 'b': B})
    r, c = 5, 3
    dim = r * c

    tasa = 0.15
    tranqui = 0.99
    tope = 9
    k = tope + 1 # incl. cero
    contadores = np.zeros((k, k + 1), dtype = int)
    n = floor(log(k-1, 2)) + 1
    neuronas = np.random.rand(n, dim) # perceptrones

    for t in range(4000): # entrenamiento
        d = randint(0, tope)
        pixeles = 1 * (np.random.rand(dim) < modelos.iloc[d])
        correcto = '{0:04b}'.format(d)
        for i in range(n):
            w = neuronas[i, :]
            deseada = int(correcto[i]) # 0 o 1
            resultado = sum(w * pixeles) >= 0
            if deseada != resultado:
                ajuste = tasa * (1 * deseada - 1 * resultado)
                tasa = tranqui * tasa
                neuronas[i, :] = w + ajuste * pixeles

    for t in range(100): # prueba
        d = randint(0, tope)
        pixeles = 1 * (np.random.rand(dim) < modelos.iloc[d])
        correcto = '{0:04b}'.format(d)
        salida = ''
        for i in range(n):
            salida += '1' if sum(neuronas[i, :] * pixeles) >= 0 else '0'
        r = min(int(salida, 2), k)
        contadores[d, r] += 1
    c = pd.DataFrame(contadores)
    c.columns = [str(i) for i in range(k)] + ['NA']
    c.index = [str(i) for i in range(k)]

    f1 = []

    for x in range(len(contadores)):
        for y in range(len(contadores[0])):
            if x == y:
                tp = contadores[x][y]
                precision = tp / sum(list(c.iloc[x]))
                recall = tp / sum(list(c.iloc[:, x]))
                f1.append(2 * ((precision * recall) / (precision + recall)))


    F1 = np.nansum(f1) / len(f1)

    return F1




N = [0.95,0.6,0.3]
G = [0.92,0.5,0.2]
B = [0.002,0.4,0.1]

rep = 3

simus = []
simus2 = []
simus3 = []
simus4 = []
simus5 = []
simus6 = []

for r in range(rep):
    SIMU = []
    for n in N:
        for g in G:
            for b in B:
                SIMU = simu(n,g,b)
                if r == 0:
                    simus.append(SIMU)
                if r == 1:
                    simus2.append(SIMU)
                if r == 2:
                    simus3.append(SIMU)
                if r == 3:
                    simus4.append(SIMU)
                if r == 4:
                    simus5.append(SIMU)
                if r == 5:
                    simus6.append(SIMU)

sms = pd.DataFrame()
sms['rep'] = simus
sms['rep2'] = simus2
sms['rep3'] = simus3
sms['rep4'] = simus4
sms['rep5'] = simus5
sms['rep6'] = simus6



xlabel = []
for n in N:
    for g in G:
        for b in B:
            xlabel.append(str(n) + ',' + str(g) + ',' + str(b))

sms.index = xlabel

smsT = sms.T




ax = sns.boxplot(data=smsT)
plt.setp(ax.get_xticklabels(), rotation=45)
plt.subplots_adjust(bottom=0.2, top=0.95)
plt.ylabel("F-score",fontsize = 15)
plt.xlabel("Combinaciones (n,g,b)", fontsize = 15)
plt.show()
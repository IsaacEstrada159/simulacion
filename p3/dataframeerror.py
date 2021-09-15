from time import time
from math import sqrt, ceil
from random import randint, random, shuffle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def primo(n):
    if n < 4: # 1 2 3
        return True
    if n % 2 == 0:
        return False
    for d in range(3, int(ceil(sqrt(n)))):
        if n % d == 0:
            return False
    return True

dificiles = []
data = []
datos = []
meta = 10
faciles = [randint(1000, 15000) for i in range(meta)]
while len(dificiles) < meta:
    n = randint(50000000, 700000000) 
    if n % 2 == 0:
        n += 1
    if primo(n):
        dificiles.append(n)

from multiprocessing import Pool

if __name__ == "__main__":
    c1 = faciles + dificiles
    c2 = dificiles + faciles
    cr = c2.copy()
    shuffle(cr)
    ordenes = {'fp': c1, 'dp': c2, 'oa': cr}
    for trabajadores in range(1, 9):
        with Pool(trabajadores) as p:
            for o in ordenes:
                label = o
                datos = ordenes[o]
                for replica in range(100):
                    start = time()
                    p.map(primo, datos)
                    tiempo = 1000 * (time() - start)
                resultado = [trabajadores, replica, tiempo,]
                data.append(resultado)
    datos = pd.DataFrame(data, columns = ['replica','trabajadores','tiempo'])                


plt.boxplot([datos['replica']],[datos['tiempo'])
plt.show()

                        




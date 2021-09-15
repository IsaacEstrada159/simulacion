from time import time
from math import sqrt, ceil
from random import randint, random, shuffle
import pandas as pd
import numpy as np
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
    for trabajadores in range(1, 5):
        with Pool(trabajadores) as p:
            for o in ordenes:
                label = o
                datos = ordenes[o]
                for replica in range(100):
                    start = time()
                    p.map(primo, datos)
                    tiempo = 1000 * (time() - start)
                    if replica > 0:
                        #print(f'{replica},{trabajadores},{tiempo}')
        datos = pd.DataFrame(data, columns = [f'tiempo'])
        #print(datos) 
                        




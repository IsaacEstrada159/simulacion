# Based code from E. Schaeffer URL: https://github.com/satuelisa/Simulation/blob/master/QueuingTheory/ordering.py
from math import ceil, sqrt
from scipy.stats import describe 
from random import shuffle
import multiprocessing
from time import time

def factor(n):
    if n < 4:
        return -1
    if n % 2 == 0:
        return 2
    for i in range(3, int(ceil(sqrt(n))), 2):
        if n % i == 0:
            return i
    return -1
 
if __name__ == "__main__":

    with open('dataprimes.txt', 'r') as input:
        linea = input.readline()

    datos = [int(valor) for valor in linea.split(',')]
    faciles = []
    dificiles = []
    largo = len(datos)

    for rep in range(largo):
        for cand in range(datos[0],datos[rep]):
            if factor(cand) < 0:
                dificiles += [cand]
            if factor(cand) >= 2:
                faciles += [cand]

    invertido = dificiles[::-1]
    aleatorio = dificiles.copy()
    replicas = 10
    tiempos = {"ot": [], "it": [], "at": []}
    with multiprocessing.Pool(1) as pool:
        for r in range(replicas):
            t = time()
            pool.map(factor, dificiles)
            tiempos["ot"].append(time() - t)
            t = time()
            pool.map(factor, invertido)
            tiempos["it"].append(time() - t)
            shuffle(aleatorio)
            t = time()
            pool.map(factor, aleatorio)
            tiempos["at"].append(time() - t)
    for tipo in tiempos:
        print(describe(tiempos[tipo]))

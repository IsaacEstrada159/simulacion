import numpy as np # instalar numpy con pip
from random import random
import matplotlib.cm as cm
import matplotlib.pyplot as plt

dim = 30
num = dim**2
p = 0.5
valores = [1 * (random() < p) for i in range(num)]
actual = np.reshape(valores, (dim, dim))

def mapeo(pos):
    fila = pos // dim
    columna = pos % dim
    return actual[fila, columna]

assert all([mapeo(x) == valores[x]  for x in range(num)])

def paso(pos):
    fila = pos // dim
    columna = pos % dim
    vecindad = actual[max(0, fila - 1):min(dim, fila + 2),
                      max(0, columna - 1):min(dim, columna + 2)]
    return 1 * (np.sum(vecindad) - actual[fila, columna] == 3)

dur = 40
lim = 9
seq = 0

if __name__ == "__main__":
   for i in range(4):
       for iteracion in range(dur):
           valores = [paso(x) for x in range(num)]
           vivos = sum(valores)
           #print(iteracion, 'vivos')
           if vivos == 0:
               print('muertos')
               break; # nadie vivo
           actual = np.reshape(valores, (dim, dim))
       seq = seq + 1
       print(seq)
    


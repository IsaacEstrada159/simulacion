# Based code from E. Schaeffer modified by I. Estrada
import numpy as np
from random import random
import matplotlib.cm as cm
import matplotlib.pyplot as plt

def prob():
    return 0 if random() > 0.3 else 1     #0.1 to 0.9

dim = 50
num = dim**2
valores = [prob() for i in range(num)]
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

print(actual)        
if __name__ == "__main__":
    fig = plt.figure()
    plt.imshow(actual, interpolation='nearest', cmap=cm.Greys)
    fig.suptitle('Estado inicial')
    plt.savefig('p2_t0_p.png')
    plt.close()
    for iteracion in range(50):
        print("Iter", iteracion)
        valores = [paso(x) for x in range(num)]
        vivos = sum(valores)
        print(iteracion, vivos)
        if vivos == 0:
            print('# Ya no queda nadie vivo.')
            break;
        actual = np.reshape(valores, (dim, dim))
        #print(actual)        
        fig = plt.figure()
        plt.imshow(actual, interpolation='nearest', cmap=cm.Greys)
        fig.suptitle('Paso {:d}'.format(iteracion + 1))
        plt.savefig('p2_t{:d}_p.png'.format(iteracion + 1))
        plt.close()

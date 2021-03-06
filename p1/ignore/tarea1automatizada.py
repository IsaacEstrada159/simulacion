from random import random, randint
import pandas as pd
import numpy as np

corridas = 50
pasitos = 0
milis = 0
r = [0]

def paso(pos, dim):
    d = randint(0, dim-1)
    pos[d]+= -1 if random() < 0.5 else 1
    return pos

def experimento(largo, dim, pasitos, milis):
    pos = [0] * dim
    for t in range(largo):
        pos = paso(pos, dim)
        pasitos = pasitos + 1
        if  all([p == 0 for p in pos]):
            milis = pasitos
            pasitos = 0
            break
    return milis

for dim in range(1,9):
    largo = [32, 64, 128, 256, 512, 1024]
    for largo in largo:
        for replicas in range (corridas):
            r += [[largo],[dim,[experimento(largo, dim, pasitos, milis)]]]



print(r)


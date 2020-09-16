
from random import random, randint

dim = 3
largo = 1024
corridas = 50

def paso(pos, dim):
    d = randint(0, dim-1)
    pos[d]+= -1 if random() < 0.5 else 1
    return pos

def experimento(largo, dim,):
    pos = [0] * dim
    for t in range(largo):
        pos = paso(pos, dim)
        if  all([p == 0 for p in pos]):
            return t+1
    return None

for replicas in range (corridas):
    resultado =  experimento(largo, dim)
    if resultado is not None:
        print(resultado)
    else:
        print ("infinito")

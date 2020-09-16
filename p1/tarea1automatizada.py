from random import random, randint

dim = 1
largo = 1024
pasitos = 0
milis = 0
corridas = 50

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
            print(milis)
            pasitos = 0
    return milis

for replicas in range (corridas):
    experimento(largo, dim, pasitos, milis)
    print ("fin")

      

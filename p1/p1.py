from random import random, randint 
import pandas as  pd
dimenciones = 0
replicas = 1
v = []


for lop in range(1, replicas + 1):

    for dimenciones in range(1, 9 + 1):

        for dim in range(1,dimenciones+2):
            pos = [0] * dim
            dur = 7000

            def paso(pos, dim):
                d = randint(0, dim-1)
                pos[d] += -1 if random() < 0.5 else 1
                return pos
        
            for t in range(dur):
                pos = paso(pos, dim)

        pd.DataFrame[abs(sum(pos))] 
   
   


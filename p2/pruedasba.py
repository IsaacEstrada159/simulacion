from math import sqrt
from random import randint
from multiprocessing import Pool
import pandas as pd
import matplotlib.pyplot as plt
datos = []
data = []



muchos = 2000000
interior = 0

if __name__ == "__main__":
    with Pool(3) as p:

        for r in range(muchos): 
            x = randint(-2000, 2000)
            y = randint(-2000, 2000)
            d = sqrt(x*x + y*y)
            if (d < 2000):
                interior = interior + 1
                tasa = interior / muchos
                pi = 4 * tasa
        data.append(pi)
        datos = pd.DataFrame(data, columns = 'replicas') 
print(pi)
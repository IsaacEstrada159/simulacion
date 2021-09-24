from multiprocessing import Pool
from math import sqrt
from random import randint
import pandas as pd
import matplotlib.pyplot as plt
    
datos = []
data = []
datos2 = []
data2 = []
datos3 = []
data3 = []

if __name__ == "__main__":
    with Pool(3) as p:

        for replicas in range(300):

            muchos = 1000
            interior = 0
            for r in range(muchos): 
                x = randint(-1000,1000)
                y = randint(-1000,1000)
                d = sqrt(x*x + y*y)
                if (d < 1000):
                    interior = interior + 1
                tasa = interior / muchos
                pi = 4 * tasa
            data.append(pi)
            datos = pd.DataFrame(data, columns = ['replica1'])  


        for replicas in range(400):

            muchos = 1000
            interior = 0
            for r in range(muchos): 
                x = randint(-1000,1000)
                y = randint(-1000,1000)
                d = sqrt(x*x + y*y)
                if (d < 1000):
                    interior = interior + 1
                tasa = interior / muchos
                pi = 4 * tasa
            data2.append(pi)
            datos2 = pd.DataFrame(data2, columns = ['replica2'])  

    plt.boxplot([datos,datos2])
    plt.show()
        
            
from math import exp, pi
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


sns.set_theme(style="ticks")
def g(x):
    return (2  / (pi * (exp(x) + exp(-x))))
 
vg = np.vectorize(g)
X = np.arange(-8, 8, 0.05) # ampliar y refinar
Y = vg(X) # mayor eficiencia
wolf = str(0.0488340)  
from GeneralRandom import GeneralRandom
generador = GeneralRandom(np.asarray(X), np.asarray(Y))
desde = 3
hasta = 7
pedazo = 1000
cuantos = 500
def parte(replica):
    V = generador.random(pedazo)[0]
    return ((V >= desde) & (V <= hasta)).sum() 
primero = []
segundo = []
tercero = []
cuarto = []
quinto = []
sexto = []
septimpo = []
replica = 1000
data = []
import multiprocessing
if __name__ == "__main__":
    with multiprocessing.Pool() as pool:
        for t in range(1, replica):
            uno = 0
            dos = 0
            tres = 0
            cuatro = 0
            cinco = 0
            seis = 0
            siete = 0

            montecarlo = pool.map(parte, range(1000))
            integral = sum(montecarlo) / (1000 * pedazo)
            numn = (pi / 2) * integral
            num = str(numn)
            #print(numn)
            if num[0] == wolf[0] and num[1] == wolf[1] and num[2] == wolf[2]: # 1er Decimal
                
                uno = uno + 1
            if num[0] == wolf[0] and num[1] == wolf[1] and num[2] == wolf[2] and num[3] == wolf[3]: # 2do Decimal
                dos = dos + 1
            if num[0] == wolf[0] and num[1] == wolf[1] and num[2] == wolf[2] and num[3] == wolf[3] and num[4] == wolf[4]: # 3er Decimal
                tres = tres + 1
            if num[0] == wolf[0] and num[1] == wolf[1] and num[2] == wolf[2] and num[3] == wolf[3] and num[4] == wolf[4] and num[5] == wolf[5]: # 4to Decimal
                cuatro = cuatro + 1
            if num[0] == wolf[0] and num[1] == wolf[1] and num[2] == wolf[2] and num[3] == wolf[3] and num[4] == wolf[4] and num[5] == wolf[5] and num[6] == wolf[6]: # 5to Decimal
                cinco = cinco + 1
            if num[0] == wolf[0] and num[1] == wolf[1] and num[2] == wolf[2] and num[3] == wolf[3] and num[4] == wolf[4] and num[5] == wolf[5] and num[6] == wolf[6] and num[7] == wolf[7]: # 6to Decimal
                seis = seis + 1
            if num[0] == wolf[0] and num[1] == wolf[1] and num[2] == wolf[2] and num[3] == wolf[3] and num[4] == wolf[4] and num[5] == wolf[5] and num[6] == wolf[6] and num[7] == wolf[7] and num[8] == wolf[8] : # 7mo Decimal
                siete = siete + 1
            primero.append(uno)
            primero.append(dos)
            primero.append(tres)
            primero.append(cuatro)
            primero.append(cinco)
            primero.append(seis)
            primero.append(siete)
            decimales = uno + dos + tres + cuatro + cinco + seis + siete
            resultados = decimales
            data.append(resultados)
        #datos = pd.DataFrame(data, columns = ['replica', 'decimales'])
        plt.boxplot(data)
        plt.show()
        print(data)


        uno = 0
        dos = 0
        tres = 0
        cuatro = 0
        cinco = 0
        seis = 0
        siete = 0



        for t in range(1, 50):
            montecarlo = pool.map(parte, range(1000))
            integral = sum(montecarlo) / (1000 * pedazo)
            numn = (pi / 2) * integral
            num = str(numn)
            #print(numn)
            if num[0] == wolf[0] and num[1] == wolf[1] and num[2] == wolf[2]: # 1er Decimal
                
                uno = uno + 1
            if num[0] == wolf[0] and num[1] == wolf[1] and num[2] == wolf[2] and num[3] == wolf[3]: # 2do Decimal
                dos = dos + 1
            if num[0] == wolf[0] and num[1] == wolf[1] and num[2] == wolf[2] and num[3] == wolf[3] and num[4] == wolf[4]: # 3er Decimal
                tres = tres + 1
            if num[0] == wolf[0] and num[1] == wolf[1] and num[2] == wolf[2] and num[3] == wolf[3] and num[4] == wolf[4] and num[5] == wolf[5]: # 4to Decimal
                cuatro = cuatro + 1
            if num[0] == wolf[0] and num[1] == wolf[1] and num[2] == wolf[2] and num[3] == wolf[3] and num[4] == wolf[4] and num[5] == wolf[5] and num[6] == wolf[6]: # 5to Decimal
                cinco = cinco + 1
            if num[0] == wolf[0] and num[1] == wolf[1] and num[2] == wolf[2] and num[3] == wolf[3] and num[4] == wolf[4] and num[5] == wolf[5] and num[6] == wolf[6] and num[7] == wolf[7]: # 6to Decimal
                seis = seis + 1
            if num[0] == wolf[0] and num[1] == wolf[1] and num[2] == wolf[2] and num[3] == wolf[3] and num[4] == wolf[4] and num[5] == wolf[5] and num[6] == wolf[6] and num[7] == wolf[7] and num[8] == wolf[8] : # 7mo Decimal
                siete = siete + 1
            segundo.append(uno)
            segundo.append(dos)
            segundo.append(tres)
            segundo.append(cuatro)
            segundo.append(cinco)
            segundo.append(seis)
            segundo.append(siete)



        uno = 0
        dos = 0
        tres = 0
        cuatro = 0
        cinco = 0
        seis = 0
        siete = 0



        for t in range(1, 50):
            montecarlo = pool.map(parte, range(10000))
            integral = sum(montecarlo) / (10000 * pedazo)
            numn = (pi / 2) * integral
            num = str(numn)
            #print(numn)
            replica = 0 
            if num[0] == wolf[0] and num[1] == wolf[1] and num[2] == wolf[2]: # 1er Decimal
                
                uno = uno + 1
            if num[0] == wolf[0] and num[1] == wolf[1] and num[2] == wolf[2] and num[3] == wolf[3]: # 2do Decimal
                dos = dos + 1
            if num[0] == wolf[0] and num[1] == wolf[1] and num[2] == wolf[2] and num[3] == wolf[3] and num[4] == wolf[4]: # 3er Decimal
                tres = tres + 1
            if num[0] == wolf[0] and num[1] == wolf[1] and num[2] == wolf[2] and num[3] == wolf[3] and num[4] == wolf[4] and num[5] == wolf[5]: # 4to Decimal
                cuatro = cuatro + 1
            if num[0] == wolf[0] and num[1] == wolf[1] and num[2] == wolf[2] and num[3] == wolf[3] and num[4] == wolf[4] and num[5] == wolf[5] and num[6] == wolf[6]: # 5to Decimal
                cinco = cinco + 1
            if num[0] == wolf[0] and num[1] == wolf[1] and num[2] == wolf[2] and num[3] == wolf[3] and num[4] == wolf[4] and num[5] == wolf[5] and num[6] == wolf[6] and num[7] == wolf[7]: # 6to Decimal
                seis = seis + 1
            if num[0] == wolf[0] and num[1] == wolf[1] and num[2] == wolf[2] and num[3] == wolf[3] and num[4] == wolf[4] and num[5] == wolf[5] and num[6] == wolf[6] and num[7] == wolf[7] and num[8] == wolf[8] : # 7mo Decimal
                siete = siete + 1
            tercero.append(uno)
            tercero.append(dos)
            tercero.append(tres)
            tercero.append(cuatro)
            tercero.append(cinco)
            tercero.append(seis)
            tercero.append(siete)
            replica += 1



        uno = 0
        dos = 0
        tres = 0
        cuatro = 0
        cinco = 0
        seis = 0
        siete = 0



        for t in range(1, 50):
            montecarlo = pool.map(parte, range(100000))
            integral = sum(montecarlo) / (100000 * pedazo)
            numn = (pi / 2) * integral
            num = str(numn)
            #print(numn)
            if num[0] == wolf[0] and num[1] == wolf[1] and num[2] == wolf[2]: # 1er Decimal
                uno = uno + 1
            if num[0] == wolf[0] and num[1] == wolf[1] and num[2] == wolf[2] and num[3] == wolf[3]: # 2do Decimal
                dos = dos + 1
            if num[0] == wolf[0] and num[1] == wolf[1] and num[2] == wolf[2] and num[3] == wolf[3] and num[4] == wolf[4]: # 3er Decimal
                tres = tres + 1
            if num[0] == wolf[0] and num[1] == wolf[1] and num[2] == wolf[2] and num[3] == wolf[3] and num[4] == wolf[4] and num[5] == wolf[5]: # 4to Decimal
                cuatro = cuatro + 1
            if num[0] == wolf[0] and num[1] == wolf[1] and num[2] == wolf[2] and num[3] == wolf[3] and num[4] == wolf[4] and num[5] == wolf[5] and num[6] == wolf[6]: # 5to Decimal
                cinco = cinco + 1
            if num[0] == wolf[0] and num[1] == wolf[1] and num[2] == wolf[2] and num[3] == wolf[3] and num[4] == wolf[4] and num[5] == wolf[5] and num[6] == wolf[6] and num[7] == wolf[7]: # 6to Decimal
                seis = seis + 1
            if num[0] == wolf[0] and num[1] == wolf[1] and num[2] == wolf[2] and num[3] == wolf[3] and num[4] == wolf[4] and num[5] == wolf[5] and num[6] == wolf[6] and num[7] == wolf[7] and num[8] == wolf[8] : # 7mo Decimal
                siete = siete + 1
            cuarto.append(uno)
            cuarto.append(dos)
            cuarto.append(tres)
            cuarto.append(cuatro)
            cuarto.append(cinco)
            cuarto.append(seis)
            cuarto.append(siete)

    print(df)
   


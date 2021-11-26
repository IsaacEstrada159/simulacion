from random import randint
from math import floor, log
import pandas as pd
import numpy as np
from multiprocessing import Pool
import matplotlib.pyplot as plt
import seaborn as sns
s = []
s2 = []
s3 = []
s4 = []
s5 = []
s6 = []
s7 = []
replicas = 25
if __name__ == '__main__':
     with Pool(4) as p:

        for replica in range(replicas): 
            modelos = pd.read_csv('digits.txt', sep=' ', header = None)
            modelos = modelos.replace({'n': 0.99, 'g': 0.88, 'b': 0.2})
            r, c = 5, 3
            dim = r * c
            
            tasa = 0.15
            tranqui = 0.99
            tope = 9
            k = tope + 1 # incl. cero
            contadores = np.zeros((k, k + 1), dtype = int)
            n = floor(log(k-1, 2)) + 1
            neuronas = np.random.rand(n, dim) # perceptrones
            
            for t in range(5000): # entrenamiento
                d = randint(0, tope)
                pixeles = 1 * (np.random.rand(dim) < modelos.iloc[d])
                correcto = '{0:04b}'.format(d)
                for i in range(n):
                    w = neuronas[i, :]
                    deseada = int(correcto[i]) # 0 o 1
                    resultado = sum(w * pixeles) >= 0
                    if deseada != resultado: 
                        ajuste = tasa * (1 * deseada - 1 * resultado)
                        tasa = tranqui * tasa 
                        neuronas[i, :] = w + ajuste * pixeles
            
            for t in range(300): # prueba
                d = randint(0, tope)
                pixeles = 1 * (np.random.rand(dim) < modelos.iloc[d])
                correcto = '{0:04b}'.format(d)
                salida = ''
                for i in range(n):
                    salida += '1' if sum(neuronas[i, :] * pixeles) >= 0 else '0'
                r = min(int(salida, 2), k)
                contadores[d, r] += 1
            c = pd.DataFrame(contadores)
            c.columns = [str(i) for i in range(k)] + ['NA']
            c.index = [str(i) for i in range(k)]
            p = s.append(sum(c['NA']))

        for replica in range(replicas): 
            modelos = pd.read_csv('digits.txt', sep=' ', header = None)
            modelos = modelos.replace({'n': 0.95, 'g': 0.85, 'b': 0.2})
            r, c = 5, 3
            dim = r * c
            
            tasa = 0.15
            tranqui = 0.99
            tope = 9
            k = tope + 1 # incl. cero
            contadores = np.zeros((k, k + 1), dtype = int)
            n = floor(log(k-1, 2)) + 1
            neuronas = np.random.rand(n, dim) # perceptrones
            
            for t in range(5000): # entrenamiento
                d = randint(0, tope)
                pixeles = 1 * (np.random.rand(dim) < modelos.iloc[d])
                correcto = '{0:04b}'.format(d)
                for i in range(n):
                    w = neuronas[i, :]
                    deseada = int(correcto[i]) # 0 o 1
                    resultado = sum(w * pixeles) >= 0
                    if deseada != resultado: 
                        ajuste = tasa * (1 * deseada - 1 * resultado)
                        tasa = tranqui * tasa 
                        neuronas[i, :] = w + ajuste * pixeles
            
            for t in range(300): # prueba
                d = randint(0, tope)
                pixeles = 1 * (np.random.rand(dim) < modelos.iloc[d])
                correcto = '{0:04b}'.format(d)
                salida = ''
                for i in range(n):
                    salida += '1' if sum(neuronas[i, :] * pixeles) >= 0 else '0'
                r = min(int(salida, 2), k)
                contadores[d, r] += 1
            c = pd.DataFrame(contadores)
            c.columns = [str(i) for i in range(k)] + ['NA']
            c.index = [str(i) for i in range(k)]
            p2 = s2.append(sum(c['NA']))

        for replica in range(replicas): 
            modelos = pd.read_csv('digits.txt', sep=' ', header = None)
            modelos = modelos.replace({'n': 0.9, 'g': 0.8, 'b': 0.2})
            r, c = 5, 3
            dim = r * c
            
            tasa = 0.15
            tranqui = 0.99
            tope = 9
            k = tope + 1 # incl. cero
            contadores = np.zeros((k, k + 1), dtype = int)
            n = floor(log(k-1, 2)) + 1
            neuronas = np.random.rand(n, dim) # perceptrones
            
            for t in range(5000): # entrenamiento
                d = randint(0, tope)
                pixeles = 1 * (np.random.rand(dim) < modelos.iloc[d])
                correcto = '{0:04b}'.format(d)
                for i in range(n):
                    w = neuronas[i, :]
                    deseada = int(correcto[i]) # 0 o 1
                    resultado = sum(w * pixeles) >= 0
                    if deseada != resultado: 
                        ajuste = tasa * (1 * deseada - 1 * resultado)
                        tasa = tranqui * tasa 
                        neuronas[i, :] = w + ajuste * pixeles
            
            for t in range(300): # prueba
                d = randint(0, tope)
                pixeles = 1 * (np.random.rand(dim) < modelos.iloc[d])
                correcto = '{0:04b}'.format(d)
                salida = ''
                for i in range(n):
                    salida += '1' if sum(neuronas[i, :] * pixeles) >= 0 else '0'
                r = min(int(salida, 2), k)
                contadores[d, r] += 1
            c = pd.DataFrame(contadores)
            c.columns = [str(i) for i in range(k)] + ['NA']
            c.index = [str(i) for i in range(k)]
            p3 = s3.append(sum(c['NA']))

        for replica in range(replicas): 
            modelos = pd.read_csv('digits.txt', sep=' ', header = None)
            modelos = modelos.replace({'n': 0.8, 'g': 0.7, 'b': 0.2})
            r, c = 5, 3
            dim = r * c
            
            tasa = 0.15
            tranqui = 0.99
            tope = 9
            k = tope + 1 # incl. cero
            contadores = np.zeros((k, k + 1), dtype = int)
            n = floor(log(k-1, 2)) + 1
            neuronas = np.random.rand(n, dim) # perceptrones
            
            for t in range(5000): # entrenamiento
                d = randint(0, tope)
                pixeles = 1 * (np.random.rand(dim) < modelos.iloc[d])
                correcto = '{0:04b}'.format(d)
                for i in range(n):
                    w = neuronas[i, :]
                    deseada = int(correcto[i]) # 0 o 1
                    resultado = sum(w * pixeles) >= 0
                    if deseada != resultado: 
                        ajuste = tasa * (1 * deseada - 1 * resultado)
                        tasa = tranqui * tasa 
                        neuronas[i, :] = w + ajuste * pixeles
            
            for t in range(300): # prueba
                d = randint(0, tope)
                pixeles = 1 * (np.random.rand(dim) < modelos.iloc[d])
                correcto = '{0:04b}'.format(d)
                salida = ''
                for i in range(n):
                    salida += '1' if sum(neuronas[i, :] * pixeles) >= 0 else '0'
                r = min(int(salida, 2), k)
                contadores[d, r] += 1
            c = pd.DataFrame(contadores)
            c.columns = [str(i) for i in range(k)] + ['NA']
            c.index = [str(i) for i in range(k)]
            p4 = s4.append(sum(c['NA']))

        for replica in range(replicas): 
            modelos = pd.read_csv('digits.txt', sep=' ', header = None)
            modelos = modelos.replace({'n': 0.75, 'g': 0.65, 'b': 0.2})
            r, c = 5, 3
            dim = r * c
            
            tasa = 0.15
            tranqui = 0.99
            tope = 9
            k = tope + 1 # incl. cero
            contadores = np.zeros((k, k + 1), dtype = int)
            n = floor(log(k-1, 2)) + 1
            neuronas = np.random.rand(n, dim) # perceptrones
            
            for t in range(5000): # entrenamiento
                d = randint(0, tope)
                pixeles = 1 * (np.random.rand(dim) < modelos.iloc[d])
                correcto = '{0:04b}'.format(d)
                for i in range(n):
                    w = neuronas[i, :]
                    deseada = int(correcto[i]) # 0 o 1
                    resultado = sum(w * pixeles) >= 0
                    if deseada != resultado: 
                        ajuste = tasa * (1 * deseada - 1 * resultado)
                        tasa = tranqui * tasa 
                        neuronas[i, :] = w + ajuste * pixeles
            
            for t in range(300): # prueba
                d = randint(0, tope)
                pixeles = 1 * (np.random.rand(dim) < modelos.iloc[d])
                correcto = '{0:04b}'.format(d)
                salida = ''
                for i in range(n):
                    salida += '1' if sum(neuronas[i, :] * pixeles) >= 0 else '0'
                r = min(int(salida, 2), k)
                contadores[d, r] += 1
            c = pd.DataFrame(contadores)
            c.columns = [str(i) for i in range(k)] + ['NA']
            c.index = [str(i) for i in range(k)]
            p5 = s5.append(sum(c['NA']))

        for replica in range(replicas): 
            modelos = pd.read_csv('digits.txt', sep=' ', header = None)
            modelos = modelos.replace({'n': 0.7, 'g': 0.6, 'b': 0.2})
            r, c = 5, 3
            dim = r * c
            
            tasa = 0.15
            tranqui = 0.99
            tope = 9
            k = tope + 1 # incl. cero
            contadores = np.zeros((k, k + 1), dtype = int)
            n = floor(log(k-1, 2)) + 1
            neuronas = np.random.rand(n, dim) # perceptrones
            
            for t in range(5000): # entrenamiento
                d = randint(0, tope)
                pixeles = 1 * (np.random.rand(dim) < modelos.iloc[d])
                correcto = '{0:04b}'.format(d)
                for i in range(n):
                    w = neuronas[i, :]
                    deseada = int(correcto[i]) # 0 o 1
                    resultado = sum(w * pixeles) >= 0
                    if deseada != resultado: 
                        ajuste = tasa * (1 * deseada - 1 * resultado)
                        tasa = tranqui * tasa 
                        neuronas[i, :] = w + ajuste * pixeles
            
            for t in range(300): # prueba
                d = randint(0, tope)
                pixeles = 1 * (np.random.rand(dim) < modelos.iloc[d])
                correcto = '{0:04b}'.format(d)
                salida = ''
                for i in range(n):
                    salida += '1' if sum(neuronas[i, :] * pixeles) >= 0 else '0'
                r = min(int(salida, 2), k)
                contadores[d, r] += 1
            c = pd.DataFrame(contadores)
            c.columns = [str(i) for i in range(k)] + ['NA']
            c.index = [str(i) for i in range(k)]
            p6 = s6.append(sum(c['NA']))

        for replica in range(replicas): 
            modelos = pd.read_csv('digits.txt', sep=' ', header = None)
            modelos = modelos.replace({'n': 0.65, 'g': 0.75, 'b': 0.2})
            r, c = 5, 3
            dim = r * c
            
            tasa = 0.15
            tranqui = 0.99
            tope = 9
            k = tope + 1 # incl. cero
            contadores = np.zeros((k, k + 1), dtype = int)
            n = floor(log(k-1, 2)) + 1
            neuronas = np.random.rand(n, dim) # perceptrones
            
            for t in range(5000): # entrenamiento
                d = randint(0, tope)
                pixeles = 1 * (np.random.rand(dim) < modelos.iloc[d])
                correcto = '{0:04b}'.format(d)
                for i in range(n):
                    w = neuronas[i, :]
                    deseada = int(correcto[i]) # 0 o 1
                    resultado = sum(w * pixeles) >= 0
                    if deseada != resultado: 
                        ajuste = tasa * (1 * deseada - 1 * resultado)
                        tasa = tranqui * tasa 
                        neuronas[i, :] = w + ajuste * pixeles
            
            for t in range(300): # prueba
                d = randint(0, tope)
                pixeles = 1 * (np.random.rand(dim) < modelos.iloc[d])
                correcto = '{0:04b}'.format(d)
                salida = ''
                for i in range(n):
                    salida += '1' if sum(neuronas[i, :] * pixeles) >= 0 else '0'
                r = min(int(salida, 2), k)
                contadores[d, r] += 1
            c = pd.DataFrame(contadores)
            c.columns = [str(i) for i in range(k)] + ['NA']
            c.index = [str(i) for i in range(k)]
            p7 = s7.append(sum(c['NA']))

c = 'red'
data = [s, s2, s3, s4, s4, s6, s7]       
#plt.boxplot(data, patch_artist=True, boxprops=dict(facecolor=c, color=c))

ax = sns.violinplot(data=data, scale='count', inner="box"  ,cut = 0)


plt.ylabel('Sumatoria de digitos negados')
plt.xlabel('Criterios \n variando la probabilidad de generación de dígitos\nReplicas = 25', loc = 'center')
plt.savefig('figurap1.png', dpi = 400)
plt.show()


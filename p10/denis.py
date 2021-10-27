# -*- coding: utf-8 -*-
"""
Created on Sun May  2 20:56:13 2021

@author: denis
"""

import numpy as np
import pandas as pd
from random import random, randint, sample, choices
from time import time
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import expon


 
def knapsack(peso_permitido, pesos, valores):
    assert len(pesos) == len(valores)
    peso_total = sum(pesos)
    valor_total = sum(valores)
    if peso_total < peso_permitido: 
        return valor_total
    else:
        V = dict()
        for w in range(peso_permitido + 1):
            V[(w, 0)] = 0
        for i in range(len(pesos)):
            peso = pesos[i]
            valor = valores[i]
            for w in range(peso_permitido + 1):
                cand = V.get((w - peso, i), -float('inf')) + valor
                V[(w, i + 1)] = max(V[(w, i)], cand)
        return max(V.values())
 
def factible(seleccion, pesos, capacidad):
    return np.inner(seleccion, pesos) <= capacidad
  
def objetivo(seleccion, valores):
    return np.inner(seleccion, valores)
 
def normalizar(data):
    menor = min(data)
    mayor = max(data)
    rango  = mayor - menor
    data = data - menor # > 0
    return data / rango # entre 0 y 1
  
def generador_pesos(cuantos, low, high):
    return np.round(normalizar(np.random.normal(size = cuantos)) * (high - low) + low)
 
def generador_valores(pesos, low, high):
    return np.round(normalizar(np.random.normal(size = pesos)) * (high - low) + low)

def generador_pesos2(valores, low, high):
    cant = 1 / valores
    return np.round(((normalizar(cant))) * (high - low) + low)
 
def generador_valores2(pesos, low, high):
    cant = np.arange(0, pesos)  
    return np.round(normalizar(expon.pdf(cant))  * (high - low) + low)

def generador_valores3(pesos, low, high):
    return np.round((pesos**2) * (high - low) + low)
 
def poblacion_inicial(n, tam):
    pobl = np.zeros((tam, n))
    for i in range(tam):
        pobl[i] = (np.round(np.random.uniform(size = n))).astype(int)
    return pobl
 
def mutacion(sol, n):
    pos = randint(0, n - 1)
    mut = np.copy(sol)
    mut[pos] = 1 if sol[pos] == 0 else 0
    return mut
  
def reproduccion(x, y, n):
    pos = randint(2, n - 2)
    xy = np.concatenate([x[:pos], y[pos:]])
    yx = np.concatenate([y[:pos], x[pos:]])
    return (xy, yx)



n = 50
iteraciones = 20
for n in range(100, 401, 100):
    
#*******************#
#****Instancia 1****#
#*******************#

    countr = 0
    count = 0
    mejor_total_r = []
    mejor_total = []
    mejort = []
    for repeticion in range(iteraciones):
        pesos = generador_pesos(n, 15, 80)
        valores = generador_valores(n, 10, 500)
        capacidad = int(round(sum(pesos) * 0.65))
        top1 = time()
        optimo = knapsack(capacidad, pesos, valores)
        top2 = time()
        top = top2-top1
        optimo_r = optimo
        print(top)
        optimo_t = optimo/top
        init = 200
        p = poblacion_inicial(n, init)
        tam = p.shape[0]
        assert tam == init
        pm = 0.05
        rep = 50
        tmax = 150
        mejor_r = None
        mejores_r = []
        tin_r = time()
        tiempo_r = True
    
        # Con Ruleta
        while tiempo_r:
            obj = [objetivo(p[i], valores) for i in range(tam)]
            fac = [factible(p[i], pesos, capacidad) for i in range(tam)]
            peso_p = [((fac[i] + 1)*obj[i]) for i in range(tam)]
            peso_m = [(1/((fac[i] + 1)*(obj[i]))) for i in range(tam)]
            km = int(tam*pm)
            pop = [i for i in range(tam)]
            mut = choices(population=pop, weights=peso_m, k=km)
            pad = choices(population=pop, weights=peso_p, k=rep)
        
            for i in (mut): # mutarse con probabilidad pm
                p = np.vstack([p, mutacion(p[i], n)])
                    
            for i in range(0,rep,2):  # reproducciones
                hijos = reproduccion(p[pad[i]], p[pad[i+1]], n)
                p = np.vstack([p, hijos[0], hijos[1]])
        
            tam = p.shape[0]
            d = []
            for i in range(tam):
                d.append({'idx': i, 'obj': objetivo(p[i], valores),
                          'fact': factible(p[i], pesos, capacidad)})
            d = pd.DataFrame(d).sort_values(by = ['fact', 'obj'], ascending = False)
            mantener = np.array(d.idx[:init])
            p = p[mantener, :]
            tam = p.shape[0]
            assert tam == init
            factibles = d.loc[d.fact == True,]
            mejor_r = max(factibles.obj)
            mejores_r.append(mejor_r)
            tfin = time()
            tm = tfin - tin_r
            tmu = tm / top
            mejor_v = mejor_r/optimo
            mejor_t = mejor_v/tmu
            mejor_total_r.append(mejor_t)
            if top < tm:
                tiempo_r = False
            countr += 1
        
        pesos = generador_pesos(n, 15, 80)
        valores = generador_valores(n, 10, 500)
        capacidad = int(round(sum(pesos) * 0.65))
        top1 = time()
        optimo = knapsack(capacidad, pesos, valores)
        top2 = time()
        top = top2-top1
        # print(top)
        optimo_t = optimo/top
        init = 200
        p = poblacion_inicial(n, init)
        tam = p.shape[0]
        assert tam == init
        pm = 0.05
        rep = 50
        tmax = 150
        mejor = None
        mejores = []
        tiempo = True
        #sin ruleta
        tin = time()
        while tiempo:
            for i in range(tam): # mutarse con probabilidad pm
                if random() < pm:
                    p = np.vstack([p, mutacion(p[i], n)])
            for i in range(rep):  # reproducciones
                padres = sample(range(tam), 2)
                hijos = reproduccion(p[padres[0]], p[padres[1]], n)
                p = np.vstack([p, hijos[0], hijos[1]])
            tam = p.shape[0]
            d = []
            for i in range(tam):
                d.append({'idx': i, 'obj': objetivo(p[i], valores),
                          'fact': factible(p[i], pesos, capacidad)})
            d = pd.DataFrame(d).sort_values(by = ['fact', 'obj'], ascending = False)
            mantener = np.array(d.idx[:init])
            p = p[mantener, :]
            tam = p.shape[0]
            assert tam == init
            factibles = d.loc[d.fact == True,]
            mejor = max(factibles.obj)
            mejores.append(mejor)
            tfin = time()
            tm = tfin - tin
            tmu = tm / top
            mejor_v = mejor/optimo
            mejor_t = mejor_v/tmu
            mejor_total.append(mejor_t)
            if top < tm:
                tiempo = False
            count += 1
            
    
        if repeticion == 0:    
            plt.figure(figsize=(7, 3), dpi=300)
            plt.plot(range(len(mejor_total_r)), mejor_total_r, 'ks--', linewidth=1, markersize=2)
            plt.axhline(y = 1, color = 'green', linewidth=3)
            plt.xlabel('Iteración')
            plt.ylabel('Valor / Tiempo')
            plt.savefig('p10p_R_Prim_{:d}.png'.format(n), dpi = 300)
            plt.show() 
            plt.close()
              
            plt.figure(figsize=(7, 3), dpi=300)
            plt.plot(range(len(mejor_total)), mejor_total, 'ks--', linewidth=1, markersize=2)
            plt.axhline(y = 1, color = 'green', linewidth=3)
            plt.xlabel('Iteración')
            plt.ylabel('Valor / Tiempo')
            plt.savefig('p10p_Prim_{:d}.png'.format(n), dpi = 300)
            plt.show() 
            plt.close()
            
            plt.figure(figsize=(7, 3), dpi=300)
            plt.plot(range(len(mejores_r)), mejores_r, 'ks--', linewidth=1, markersize=2)
            plt.axhline(y = optimo_r, color = 'green', linewidth=3)
            plt.xlabel('Paso')
            plt.ylabel('Mayor valor')
            plt.ylim(0.95 * min(mejores_r), 1.05 * optimo_r)
            plt.savefig('p10e_R_Prim_{:d}.png'.format(n), bbox_inches='tight') 
            plt.show()
            plt.close()
            
            plt.figure(figsize=(7, 3), dpi=300)
            plt.plot(range(len(mejores)), mejores, 'ks--', linewidth=1, markersize=2)
            plt.axhline(y = optimo, color = 'green', linewidth=3)
            plt.xlabel('Paso')
            plt.ylabel('Mayor valor')
            plt.ylim(0.95 * min(mejores), 1.05 * optimo)
            plt.savefig('p10e_Prim_{:d}.png'.format(n), bbox_inches='tight') 
            plt.show()
            plt.close()

    mejort.extend(mejor_total_r)
    mejort.extend(mejor_total)
    df = pd.DataFrame(
        {"Instancia": ["Primera"] * countr + ["Primera"] * count,
          "Tipo" : ["Con Ruleta"] * countr + ["Sin Ruleta"] * count,
          "Valor / Tiempo": mejort}
          )
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    ax = sns.boxplot(x='Instancia', y='Valor / Tiempo', data=df, whis=np.inf, palette="Set1", hue="Tipo")
    plt.savefig('p10p_Box_Prim_{:d}.png'.format(n), dpi=300)
    plt.show()
    plt.close()

#*******************#
#****Instancia 2****#
#*******************#

    countr = 0
    count = 0
    mejor_total_r = []
    mejor_total = []
    mejort = []
    for repeticion in range(iteraciones):
        valores = generador_valores2(n, 10, 500)
        pesos = generador_pesos2(valores, 15, 80)
        capacidad = int(round(sum(pesos) * 0.65))
        top1 = time()
        optimo = knapsack(capacidad, pesos, valores)
        top2 = time()
        top = top2-top1
        optimo_r = optimo
        print(top)
        optimo_t = optimo/top
        init = 200
        p = poblacion_inicial(n, init)
        tam = p.shape[0]
        assert tam == init
        pm = 0.05
        rep = 50
        tmax = 150
        
        mejor_r = None
        mejores_r = []
        tin_r = time()
        tiempo_r = True
    
        # Con Ruleta
        while tiempo_r:
            obj = [objetivo(p[i], valores) for i in range(tam)]
            fac = [factible(p[i], pesos, capacidad) for i in range(tam)]
            peso_p = [((fac[i] + 1)*obj[i]) for i in range(tam)]
            peso_m = [(1/((fac[i] + 1)*(obj[i]))) for i in range(tam)]
            km = int(tam*pm)
            pop = [i for i in range(tam)]
            mut = choices(population=pop, weights=peso_m, k=km)
            pad = choices(population=pop, weights=peso_p, k=rep)
        
            for i in (mut): # mutarse con probabilidad pm
                p = np.vstack([p, mutacion(p[i], n)])
                    
            for i in range(0,rep,2):  # reproducciones
                hijos = reproduccion(p[pad[i]], p[pad[i+1]], n)
                p = np.vstack([p, hijos[0], hijos[1]])
        
            tam = p.shape[0]
            d = []
            for i in range(tam):
                d.append({'idx': i, 'obj': objetivo(p[i], valores),
                          'fact': factible(p[i], pesos, capacidad)})
            d = pd.DataFrame(d).sort_values(by = ['fact', 'obj'], ascending = False)
            mantener = np.array(d.idx[:init])
            p = p[mantener, :]
            tam = p.shape[0]
            assert tam == init
            factibles = d.loc[d.fact == True,]
            mejor_r = max(factibles.obj)
            mejores_r.append(mejor_r)
            tfin = time()
            tm = tfin - tin_r
            tmu = tm / top
            mejor_v = mejor_r/optimo
            mejor_t = mejor_v/tmu
            mejor_total_r.append(mejor_t)
            if top < tm:
                tiempo_r = False
            countr += 1
        
        valores = generador_valores2(n, 10, 500)
        pesos = generador_pesos2(valores, 15, 80)
        capacidad = int(round(sum(pesos) * 0.65))
        top1 = time()
        optimo = knapsack(capacidad, pesos, valores)
        top2 = time()
        top = top2-top1
        optimo_t = optimo/top
        init = 200
        p = poblacion_inicial(n, init)
        tam = p.shape[0]
        assert tam == init
        pm = 0.05
        rep = 50
        tmax = 150
        mejor = None
        mejores = []
        tiempo = True
        tin = time()
        while tiempo:
            for i in range(tam): # mutarse con probabilidad pm
                if random() < pm:
                    p = np.vstack([p, mutacion(p[i], n)])
            for i in range(rep):  # reproducciones
                padres = sample(range(tam), 2)
                hijos = reproduccion(p[padres[0]], p[padres[1]], n)
                p = np.vstack([p, hijos[0], hijos[1]])
            tam = p.shape[0]
            d = []
            for i in range(tam):
                d.append({'idx': i, 'obj': objetivo(p[i], valores),
                          'fact': factible(p[i], pesos, capacidad)})
            d = pd.DataFrame(d).sort_values(by = ['fact', 'obj'], ascending = False)
            mantener = np.array(d.idx[:init])
            p = p[mantener, :]
            tam = p.shape[0]
            assert tam == init
            factibles = d.loc[d.fact == True,]
            mejor = max(factibles.obj)
            mejores.append(mejor)
            tfin = time()
            tm = tfin - tin
            tmu = tm / top
            mejor_v = mejor/optimo
            mejor_t = mejor_v/tmu
            mejor_total.append(mejor_t)
            if top < tm:
                tiempo = False
            count += 1            
    
        if repeticion == 0:    
            plt.figure(figsize=(7, 3), dpi=300)
            plt.plot(range(len(mejor_total_r)), mejor_total_r, 'ks--', linewidth=1, markersize=2)
            plt.axhline(y = 1, color = 'green', linewidth=3)
            plt.xlabel('Iteración')
            plt.ylabel('Valor / Tiempo')
            plt.savefig('p10p_R_Seg_{:d}.png'.format(n), dpi = 300)
            plt.show() 
            plt.close()
              
            plt.figure(figsize=(7, 3), dpi=300)
            plt.plot(range(len(mejor_total)), mejor_total, 'ks--', linewidth=1, markersize=2)
            plt.axhline(y = 1, color = 'green', linewidth=3)
            plt.xlabel('Iteración')
            plt.ylabel('Valor / Tiempo')
            plt.savefig('p10p_Seg_{:d}.png'.format(n), dpi = 300)
            plt.show() 
            plt.close()
            
            plt.figure(figsize=(7, 3), dpi=300)
            plt.plot(range(len(mejores_r)), mejores_r, 'ks--', linewidth=1, markersize=2)
            plt.axhline(y = optimo_r, color = 'green', linewidth=3)
            plt.xlabel('Paso')
            plt.ylabel('Mayor valor')
            plt.ylim(0.95 * min(mejores_r), 1.05 * optimo_r)
            plt.savefig('p10e_R_Seg_{:d}.png'.format(n), bbox_inches='tight') 
            plt.show()
            plt.close()
            
            plt.figure(figsize=(7, 3), dpi=300)
            plt.plot(range(len(mejores)), mejores, 'ks--', linewidth=1, markersize=2)
            plt.axhline(y = optimo, color = 'green', linewidth=3)
            plt.xlabel('Paso')
            plt.ylabel('Mayor valor')
            plt.ylim(0.95 * min(mejores), 1.05 * optimo)
            plt.savefig('p10e_Seg_{:d}.png'.format(n), bbox_inches='tight') 
            plt.show()
            plt.close()

    mejort.extend(mejor_total_r)
    mejort.extend(mejor_total)
    dfnew = pd.DataFrame(
        {"Instancia": ["Segunda"] * countr + ["Segunda"] * count,
          "Tipo" : ["Con Ruleta"] * countr + ["Sin Ruleta"] * count,
          "Valor / Tiempo": mejort}
          )
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    ax = sns.boxplot(x='Instancia', y='Valor / Tiempo', data=dfnew, whis=np.inf, palette="Set1", hue="Tipo")
    plt.savefig('p10p_Box_Seg_{:d}.png'.format(n), dpi=300)
    plt.show()
    plt.close()
    
    df = df.append(dfnew, ignore_index=True)

#*******************#
#****Instancia 3****#
#*******************#

    countr = 0
    count = 0
    mejor_total_r = []
    mejor_total = []
    mejort = []
    for repeticion in range(iteraciones):
        pesos = generador_pesos(n, 15, 80)
        valores = generador_valores3(pesos, 10, 500)
        capacidad = int(round(sum(pesos) * 0.65))
        top1 = time()
        optimo = knapsack(capacidad, pesos, valores)
        top2 = time()
        top = top2-top1
        optimo_r = optimo
        optimo_t = optimo/top
        init = 200
        p = poblacion_inicial(n, init)
        tam = p.shape[0]
        assert tam == init
        pm = 0.05
        rep = 50
        tmax = 150
        
        mejor_r = None
        mejores_r = []
        tin_r = time()
        tiempo_r = True

        # Con Ruleta
        while tiempo_r:
            
            obj = [objetivo(p[i], valores) for i in range(tam)]
            fac = [factible(p[i], pesos, capacidad) for i in range(tam)]
            peso_p = [((fac[i] + 1)*obj[i]) for i in range(tam)]
            peso_m = [(1/((fac[i] + 1)*(obj[i]))) for i in range(tam)]
            km = int(tam*pm)
            pop = [i for i in range(tam)]
            mut = choices(population=pop, weights=peso_m, k=km)
            pad = choices(population=pop, weights=peso_p, k=rep)
        
            for i in (mut): # mutarse con probabilidad pm
                p = np.vstack([p, mutacion(p[i], n)])
                    
            for i in range(0,rep,2):  # reproducciones
                hijos = reproduccion(p[pad[i]], p[pad[i+1]], n)
                p = np.vstack([p, hijos[0], hijos[1]])
        
            tam = p.shape[0]
            d = []
            for i in range(tam):
                d.append({'idx': i, 'obj': objetivo(p[i], valores),
                          'fact': factible(p[i], pesos, capacidad)})
            d = pd.DataFrame(d).sort_values(by = ['fact', 'obj'], ascending = False)
            mantener = np.array(d.idx[:init])
            p = p[mantener, :]
            tam = p.shape[0]
            assert tam == init
            factibles = d.loc[d.fact == True,]
            mejor_r = max(factibles.obj)
            mejores_r.append(mejor_r)
            tfin = time()
            tm = tfin - tin_r
            tmu = tm / top
            mejor_v = mejor_r/optimo
            mejor_t = mejor_v/tmu
            mejor_total_r.append(mejor_t)
            if top < tm:
                tiempo_r = False
            countr += 1
        
        pesos = generador_pesos(n, 15, 80)
        valores = generador_valores3(pesos, 10, 500)
        capacidad = int(round(sum(pesos) * 0.65))
        top1 = time()
        optimo = knapsack(capacidad, pesos, valores)
        top2 = time()
        top = top2-top1
        optimo_t = optimo/top
        init = 200
        p = poblacion_inicial(n, init)
        tam = p.shape[0]
        assert tam == init
        pm = 0.05
        rep = 50
        tmax = 150
        mejor = None
        mejores = []
        tiempo = True
        tin = time()
        while tiempo:
            for i in range(tam): # mutarse con probabilidad pm
                if random() < pm:
                    p = np.vstack([p, mutacion(p[i], n)])
            for i in range(rep):  # reproducciones
                padres = sample(range(tam), 2)
                hijos = reproduccion(p[padres[0]], p[padres[1]], n)
                p = np.vstack([p, hijos[0], hijos[1]])
            tam = p.shape[0]
            d = []
            for i in range(tam):
                d.append({'idx': i, 'obj': objetivo(p[i], valores),
                          'fact': factible(p[i], pesos, capacidad)})
            d = pd.DataFrame(d).sort_values(by = ['fact', 'obj'], ascending = False)
            mantener = np.array(d.idx[:init])
            p = p[mantener, :]
            tam = p.shape[0]
            assert tam == init
            factibles = d.loc[d.fact == True,]
            mejor = max(factibles.obj)
            mejores.append(mejor)
            tfin = time()
            tm = tfin - tin
            tmu = tm / top
            mejor_v = mejor/optimo
            mejor_t = mejor_v/tmu
            mejor_total.append(mejor_t)
            if top < tm:
                tiempo = False
            count += 1
            
    
        if repeticion == 0:    
            plt.figure(figsize=(7, 3), dpi=300)
            plt.plot(range(len(mejor_total_r)), mejor_total_r, 'ks--', linewidth=1, markersize=2)
            plt.axhline(y = 1, color = 'green', linewidth=3)
            plt.xlabel('Iteración')
            plt.ylabel('Valor / Tiempo')
            plt.savefig('p10p_R_Ter_{:d}.png'.format(n), dpi = 300)
            plt.show() 
            plt.close()
              
            plt.figure(figsize=(7, 3), dpi=300)
            plt.plot(range(len(mejor_total)), mejor_total, 'ks--', linewidth=1, markersize=2)
            plt.axhline(y = 1, color = 'green', linewidth=3)
            plt.xlabel('Iteración')
            plt.ylabel('Valor / Tiempo')
            plt.savefig('p10p_Ter_{:d}.png'.format(n), dpi = 300)
            plt.show() 
            plt.close()
            
            plt.figure(figsize=(7, 3), dpi=300)
            plt.plot(range(len(mejores_r)), mejores_r, 'ks--', linewidth=1, markersize=2)
            plt.axhline(y = optimo_r, color = 'green', linewidth=3)
            plt.xlabel('Paso')
            plt.ylabel('Mayor valor')
            plt.ylim(0.95 * min(mejores_r), 1.05 * optimo_r)
            plt.savefig('p10e_R_Ter_{:d}.png'.format(n), bbox_inches='tight') 
            plt.show()
            plt.close()
            
            plt.figure(figsize=(7, 3), dpi=300)
            plt.plot(range(len(mejores)), mejores, 'ks--', linewidth=1, markersize=2)
            plt.axhline(y = optimo, color = 'green', linewidth=3)
            plt.xlabel('Paso')
            plt.ylabel('Mayor valor')
            plt.ylim(0.95 * min(mejores), 1.05 * optimo)
            plt.savefig('p10e_Ter_{:d}.png'.format(n), bbox_inches='tight') 
            plt.show()
            plt.close()

    mejort.extend(mejor_total_r)
    mejort.extend(mejor_total)
    dfnew = pd.DataFrame(
        {"Instancia": ["Tercera"] * countr + ["Tercera"] * count,
          "Tipo" : ["Con Ruleta"] * countr + ["Sin Ruleta"] * count,
          "Valor / Tiempo": mejort}
          )
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    ax = sns.boxplot(x='Instancia', y='Valor / Tiempo', data=dfnew, whis=np.inf, palette="Set1", hue="Tipo")
    plt.savefig('p10p_Box_Ter_{:d}.png'.format(n), dpi=300)
    plt.show()
    plt.close()
    
    df = df.append(dfnew, ignore_index=True)

    pd.set_option("display.max_rows", None, "display.max_columns", None)
    ax = sns.boxplot(x='Instancia', y='Valor / Tiempo', data=df, whis=np.inf, palette="Set1", hue="Tipo")
    plt.savefig('p10p_Box_Comp_{:d}.png'.format(n), dpi=300)
    plt.show()
    plt.close()
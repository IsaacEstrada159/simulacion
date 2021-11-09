
import numpy as np
import pandas as pd
from random import randint, random
import seaborn as sns
import matplotlib.pyplot as plt
 
def poli(maxdeg, varcount, termcount):
    f = []
    for t in range(termcount):
        var = randint(0, varcount - 1)
        deg = randint(0, maxdeg)
        f.append({'var': var, 'coef': randint(0, 1000), 'deg': deg})
    return pd.DataFrame(f)
  
def evaluate(pol, var):
    return sum([t.coef * var[pol.at[i, 'var']]**t.deg for i, t in pol.iterrows()])
 
 
def domin_by(target, challenger):
    if np.any(np.greater(target, challenger)):
        return False
    return np.any(np.greater(challenger, target))
 
 
iteracion = 30 # cuantas iteraciones
porcentajes = []
for k in range(1, 10): # cuantas funciones objetivo

    for it in range(iteracion): 
        vc = 4
        md = 3
        tc = 5
        obj = [poli(md, vc, tc) for i in range(k)]
        minim = np.random.rand(k) > 0.5
        n = 280 # cuantas soluciones aleatorias
        sol = np.random.rand(n, vc)
        val = np.zeros((n, k))
        for i in range(n): # evaluamos las soluciones
            for j in range(k):
                val[i, j] = evaluate(obj[j], sol[i])
        sign = [1 + -2 * m for m in minim]
        
        no_dom = []
        for i in range(n):
            d = [domin_by(sign * val[i], sign * val[j]) for j in range(n)]
            no_dom.append(not np.any(d)) # si es cierto que ninguno es verdadero
        frente = val[no_dom, :]
        porcentaje = (len(frente)/n)*100
        porcentajes.append(porcentaje)
        
df = pd.DataFrame(
    {"Funciones Objetivo": ["1"] * iteracion + ["2"] * iteracion + ["3"] * iteracion + ["4"] * iteracion + ["5"] * iteracion + ["6"] * iteracion + ["7"] * iteracion + ["8"] * iteracion + ["9"] * iteracion,
     "Porcentaje Pareto": porcentajes}
     )
#pd.set_option("display.max_rows", None, "display.max_columns", None)
#ax = sns.violinplot(x='Funciones Objetivo', y='Porcentaje Pareto', data=df, scale='count', inner="box"  ,cut = 0)
#plt.savefig('p11p.png', dpi=300)
#plt.show()
print(mean(df[1])
#plt.close()

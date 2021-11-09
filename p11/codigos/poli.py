import numpy as np
import pandas as pd
from random import randint, random
 
def poli(maxdeg, varcount, termcount):
    f = []
    for t in range(termcount):
        var = randint(0, varcount - 1)
        deg = randint(0, maxdeg)
        f.append({'var': var, 'coef': randint(-1000, 1000), 'deg': deg})
    return pd.DataFrame(f)
  
def evaluate(pol, var):
    return sum([t.coef * var[pol.at[i, 'var']]**t.deg for i, t in pol.iterrows()])
  
vc = 4
md = 3
tc = 8
f = poli(md, vc, tc)
print(f)
print(evaluate(f, np.random.uniform(size =  vc)))
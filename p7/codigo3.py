import matplotlib.colorbar as colorbar
import matplotlib.pyplot as plt
import numpy as np
 
def g(x, y):
    return ((x + 0.7)**4 - 12 * x**2 - 30 * x + (y + 0.7)**4 - 15 * y**2 - 30 * y)/300
 
low = -6
high = 5
paso = 0.25
cuantos = 10

x = np.arange(low, high, 0.02)
vg = np.vectorize(g)
y = vg(x)

 

p = np.arange(low, high, cuantos)
n = len(p)
z = np.zeros((n, n), dtype=float)
for i in range(n):
    x = p[i]
    for j in range(n): 
        y = p[n - j - 1] # voltear
        z[i, j] = g(x, y)
        delta = np.random.uniform(0, paso, cuantos)
        xizq = x - delta # a la izq
        xder = x + delta # a la der
        fizq = vg(xizq) # altura a la izq
        fder = vg(xder) # altura a la der        
 
t = range(0, n, 5)
l = ['{:.1f}'.format(low + i * step) for i in t]
fig, ax = plt.subplots(figsize=(6, 5), ncols=1)
pos = ax.imshow(z) 
plt.xticks(t, l)
plt.yticks(t, l[::-1]) # arriba-abajo
fig.colorbar(pos, ax=ax)
plt.savefig('p7p_flat_2.png')
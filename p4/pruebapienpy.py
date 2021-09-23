from math import sqrt
from random import randint
muchos = 2000000

interior = 0

for r in range(muchos): 
    x = randint(-2000, 2000)
    y = randint(-2000, 2000)
    d = sqrt(x*x + y*y)
    if (d < 2000):
        interior = interior + 1
    

tasa = interior / muchos
pi = 4 * tasa
print(pi)
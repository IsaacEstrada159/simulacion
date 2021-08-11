from random import random
from numpy.random import rand
from numpy.random import uniform
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 200)
y = uniform(0, 1000, size = 200)

plt.plot(x, y)
plt.title('Numeros pseudoaliatorios')
plt.xlabel('Numero de muetras')
plt.ylabel('Numeros pseudoaliatorios del 0 al 1000')
plt.show()

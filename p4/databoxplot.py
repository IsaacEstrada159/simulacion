import matplotlib.pyplot as plt
import numpy as np
data1 = (146, 121, 55, 81)
data2 = (103, 113, 131, 172)
data3 = (58, 87, 99,137)
data4 = (74, 48, 93, 81)
data = [data1, data2, data3, data4]
plt.boxplot(data, patch_artist=True, )
plt.xlabel('  semilla n=40             semilla n=90            semilla n=180          semilla=250')
plt.ylabel('distancia manhattan', loc = 'top')
plt.show()
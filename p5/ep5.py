from math import exp, pi
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import seaborn as sns


data = {'muestra1':[1, 2, 3,0,0,0,0], 'muestra2' : [49, 49, 4, 0, 0, 0, 0],  'muestra3' : [49, 49, 0, 0, 0, 0, 0], 'muestra4' : [49, 49, 0, 0, 0, 0, 0] ,'decimales':[1, 2, 3, 4, 5, 6, 7]} #datos del data.frame

# Create DataFrame
df = pd.DataFrame(data) #comando para el data frame

# Print the output.
print(df)


df.boxplot(by = 'decimales', grid = False) #boxplot by= eje x, column = eje y
plt.ylabel('decimales', loc = 'center')
plt.xlabel('replicas', loc = 'center')
plt.savefig('figurap5.png', dpi = 400) #gnerar imagen y guardar
plt.show() #mostrar imagen generada
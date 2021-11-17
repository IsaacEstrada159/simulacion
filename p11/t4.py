from matplotlib import pyplot as plt 
import numpy as np  
   
a = np.array([7]) 

plt.hist(a, bins = [1,1,2,3,4,4,5]) 
plt.title("histogram") 
plt.show()
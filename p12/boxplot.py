import matplotlib.pyplot as plt
s = [1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,34,4,4,555,5,5,5,6,6,6,6,6,67,7,7]
s2 = [1,1,1,55,55,55,55,55,66,66,66,66,77,8,9,11,11,11,23]
data = [s, s2]
plt.boxplot(data)
plt.savefig('figurap1.png', dpi = 400)
plt.show()
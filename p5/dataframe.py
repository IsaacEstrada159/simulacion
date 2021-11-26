import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# intialise data of lists.
data = {'muestra1':[99, 83, 9, 4, 0, 0, 0], 'decimales':[1, 2, 3, 4, 5, 6, 7]}

# Create DataFrame
df = pd.DataFrame(data)

# Print the output.
print(df)
ax = sns.violinplot(data=df, scale='count', inner="box"  ,cut = 0)
plt.savefig('figurap5.png', dpi = 400)
plt.show()
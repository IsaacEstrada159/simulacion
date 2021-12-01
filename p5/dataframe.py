import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# intialise data of lists.
data = {'muestra1':[99, 83, 9, 4, 0, 0, 0]}

# Create DataFrame
df = pd.DataFrame(data)

# Print the output.
print(df)
plt.boxplot(df)

plt.savefig('figurap5.png', dpi = 400)
plt.show()
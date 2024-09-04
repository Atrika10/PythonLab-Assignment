from ucimlrepo import fetch_ucirepo
import matplotlib.pyplot as plt
iris = fetch_ucirepo(id=53)
df = iris.data.original
print(df.shape)
print(df.head())
print(df)
print(df['class'].value_counts())

# 4 Visualizing the dataset

#Univariate plots
numeric_data = df.drop(columns=['class'])
#Box plot
numeric_data.plot(kind='box', subplots=True, sharex=False, sharey=False)
plt.show()
# Histogram
numeric_data.hist(figsize=(10, 8))
plt.show()
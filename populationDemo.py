import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_population = pd.read_csv('data/population_total.csv')

print(df_population.head())

# reshaping the dataframe
#dropping null values
df_population = df_population.dropna()

#convert float values to integers
df_population["year"] = df_population["year"].apply(np.int64)
df_population["population"] = df_population["population"].apply(np.int64)
print (df_population.head())

df_population = df_population.pivot(index='year', columns='country',
                                    values='population')# selecting 5 countries
df_population = df_population[['United States', 'India', 'China', 
                               'Indonesia', 'Brazil']]

df_population.plot()
plt.show()

df_population.plot.pie( y="India", figsize=(8,8), legend=False) #, labels="country", subplots = True, title="Population in 2020 (%)")
plt.show()

#boxplot of United States
df_population["United States"].plot(kind="box", color="green", title="Population")
plt.show()

#boxplot of all countries
df_population.plot(kind="box", color="green", title="Population")
plt.show()

#histogram comparing United States and Indonesia
df_population[["United States", "Indonesia"]].plot(kind="hist", title="Population")
plt.show()

df_population_2020 = df_population[df_population.index.isin([2020])]
df_population_2020 = df_population_2020.T

#transforming data
df_population_2020 = df_population_2020.reset_index()
df_population_2020 = df_population_2020.rename(columns={2020:"2020"})

df_population_2020.plot(kind="bar", x="country", color="lightgreen", title="Population in 2020", legend=True, figsize=(8,8))
plt.show()

# filter years out
df_population_sample = df_population[df_population.index.isin([1980, 1990, 2000, 2010, 2020])]
df_population_sample.plot(kind="bar", title="Population in Years", figsize=(8,8))
plt.show()

#Interactive graph has AttributeError: module 'plotly.offline' has no attribute '__PLOTLY_OFFLINE_INITIALIZED'
# df_population.iplot(kind='line',xTitle='Years', yTitle='Population', title='Population (1955-2020)')
# df_population_2020.iplot(kind='bar', color='lightgreen',
#                          xTitle='Years', yTitle='Population',
#                          title='Population in 2020')
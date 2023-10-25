import pandas as pd

df = pd.read_csv("Life_Expectancy_Data.csv")

print(df.info())
print(df.describe())

num_linhas = df.shape[0]

print(num_linhas)

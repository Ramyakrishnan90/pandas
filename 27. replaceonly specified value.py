




import pandas as pd

df = pd.read_csv('data1.csv')

df["Calories"].fillna(130, inplace = True)


print(df.to_string())
#calculate the MODE, and replace any empty values with it

#mode = the value that appears most frequently


import pandas as pd

df = pd.read_csv('data1.csv')

x = df["Calories"].mode(0) #select the first value if multiple values will be appears

df["Calories"].fillna(x, inplace =True)
print(df.to_string())
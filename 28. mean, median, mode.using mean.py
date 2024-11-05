#replace using Mean, Median, or mode
#replace using mean
#mean = the average value
#(the sum of all values divided by number of values



#calculate the MEAN

import pandas as pd

df = pd.read_csv('data1.csv')

x = df["Calories"].mean()

df["Calories"].fillna(x, inplace =True)
print(df.to_string)
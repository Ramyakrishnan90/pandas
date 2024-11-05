#calculate the MEDIAN, and replace any emptyvalues with it

#Median = the value in the middle
#after you have sorted all values accending`



import pandas as pd

df = pd.read_csv('data1.csv')

x = df["Calories"].median()

df["Calories"].fillna(x, inplace =True)
print(df.to_string)
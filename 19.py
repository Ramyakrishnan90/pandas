#if the number of rows is not specified
#the head() method will return the top 5 rows

#print the first 5 rows of the Dataframe

import  pandas as pd

df = pd.read_csv('data.csv')
print(df.head())
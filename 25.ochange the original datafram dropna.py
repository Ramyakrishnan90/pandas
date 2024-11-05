#if you want to change the origibnal dataframe
#use the inplace = true argument:


#remove all rows with NULL values
import pandas as pd

df = pd.read_csv('data1.csv')

df.dropna(inplace = True)


print(df.to_string())

#note: now, the dropna(inplace = True)
#will NOT return a newDataframe,
#but it will remove all rows containing NULL values
#from the original dataframe
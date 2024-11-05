#there is also a tail()  method
#for viewing the last rows of tghe Dataframe

#the tail() method returns the headers and a spcified number of rows

#print rhe last 5 rows of the data frane

import  pandas as pd

df = pd.read_csv('data.csv')

print(df.tail())
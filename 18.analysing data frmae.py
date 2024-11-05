#pandas - Analuysing data frame

#viewing the datA

#the head() method returns the header and a spcified number of rows

#print the first 10 rows and headers of csv file as dataframe

import pandas as pd

df = pd.read_csv('data.csv')

print(df.head(10))
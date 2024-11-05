#pandas - cleaning data

#data cleaning

#data cleaning means fixing bad data in your data set

#
#bad data could be
#empty cells
#data in wrong format
#wrong data
#duplicates

import pandas as pd

df = pd.read_csv('data.csv')

print(df.to_string())
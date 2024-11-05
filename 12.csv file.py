#load files into a dataframes
#if your data sets are stored in a file
#pandas can load them into a dataframe


#if we using this fime all the dats will be arranged like using comma

import  pandas as pd
df = pd.read_csv('data.csv')
print(df)
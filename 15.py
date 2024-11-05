#increase  the number of rowa to display the entire dataframe

import  pandas as pd

#set display option to show maximum rowa and columns

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


df = pd.read_csv('big.csv') #load your csv file

print(df.to_string()) #print the entire Dataframe
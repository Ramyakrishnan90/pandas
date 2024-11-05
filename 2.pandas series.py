#pandas series

#a pandas series is like a column in a table
#it is onr-dimentional array holding data of any type
#label and column based

#create a simple pandas series from a list




import pandas as pd
a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)
print(myvar[0]) #return the first value of te series
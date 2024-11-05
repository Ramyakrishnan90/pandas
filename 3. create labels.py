create lables
#with the index argument, you can name your own lable
#create your own lable




import pandas as pd
a = [1, 7, 8]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)

print(myvar["y"])

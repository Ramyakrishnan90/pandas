



import pandas as pd

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}
df = pd.DataFrame(data) #load the data into a dataframe object

print(df.loc[[0, 1]])
#note: whwn using [], the result is a pandas dataframes
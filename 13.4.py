#deleting a column



import pandas as pd
data = {
    'Name': ['alice', 'bob', 'charlie', 'david', 'eva'],
    'Age': [24, 27, 22, 32, 29],
    'City': ['chennai', 'goa', 'kerala', 'madurai', 'trichy'],
     'salary': [50000, 60000, 55000, 65000, 70000]
}
df = pd.DataFrame(data)

df.drop('salary', axis=1, inplace=True)

print(df)

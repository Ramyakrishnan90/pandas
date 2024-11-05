



import pandas as pd
data = {
    'Name': ['alice', 'bob', 'charlie', 'david', 'eva'],
    'Age': [24, 27, 22, 32, 29],
    'City': ['chennai', 'goa', 'kerala', 'madurai', 'trichy']
}
df = pd.DataFrame(data)

print(df['Name'])
print(df[['Name', 'Age']])
print(df.iloc[0:3])
print(df[df['Age'] > 25])
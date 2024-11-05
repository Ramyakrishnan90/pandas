#adding a new column




import pandas as pd
data = {
    'Name': ['alice', 'bob', 'charlie', 'david', 'eva'],
    'Age': [24, 27, 22, 32, 29],
    'City': ['chennai', 'goa', 'kerala', 'madurai', 'trichy']
}
df = pd.DataFrame(data)

df['salary'] = [50000, 60000, 55000, 65000, 70000]

print(df)

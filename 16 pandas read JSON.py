#pandas read JSON

#load the JSON file into a Dataframe


import pandas as pd

df = pd.read_json('jhai.json')

print(df.to_string())

#tip use to string() to print the entire DataFrame
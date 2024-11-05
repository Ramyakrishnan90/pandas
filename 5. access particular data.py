



import pandas as pd

calories = {"day1": 234, "day2": 345, "day3": 456}

myvar = pd.Series(calories, index = ["day1", "day2"])

print(myvar)
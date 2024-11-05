#keyvalue/ object as series
#you can alose use a key/value object
#like a dictionary, when creating a series
#create a simpole serie from a dictionary

import pandas as pd
calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)
print(myvar)
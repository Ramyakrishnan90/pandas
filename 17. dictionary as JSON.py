#dictionaary as JSON

#JSON = python dictionary

#JSON objects have the same format as python dictionaries

#load a python Dictionary into a Dataframe

import  pandas as pd
data = {
     "duration":{
         "0":60,
         "1":60,
         "2":60,
         "3":45,
         "4":45,
         "5":60
     },
     "pulse":{
         "0":110,
         "1":117,
         "2":120,
         "3":125,
         "4":145,
         "5":123
     },
     "Maxpulse":{
         "0":110,
         "1":145,
         "2":135,
         "3":175,
         "4":148,
         "5":127
     },
     "Calories":{
         "0":110,
         "1":409,
         "2":479,
         "3":340,
         "4":283,
         "5":300

     }
 }
df = pd.DataFrame(data)
print(df)
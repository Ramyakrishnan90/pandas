#pandas read csv
#if you have large file it can be read bz of the large file
#if we use print(df) then thw output will we get like 1st 4 rows and last 4 rows
#so avoiding that error we can use to_string() it will help to rrange all the datas



import  pandas as pd
df = pd.read_csv('big.csv')
print(df.to_string())
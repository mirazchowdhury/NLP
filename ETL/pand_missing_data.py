import pandas as pd
data = {'id':[1,2,3,None,5], 'score':[10,20,30,40,None]}
df = pd.DataFrame(data)

print(df)

rm_row = df.dropna()
rm_col = df.dropna(axis=1)

print(rm_row)
print(rm_col)
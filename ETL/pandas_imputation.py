import pandas as pd

data = {'id': [1, 2, 3, 4, 5, None, 7, 8, 9, 10], 
        'score': [10, 20, 20, 40, 50, 50, 60, 90, 90, 100]}
df = pd.DataFrame(data)
print(df)

df_copy = df.copy()

for col in df_copy.columns:
    if df_copy[col].isnull().any():
        df_copy[col] = df_copy[col].fillna(df_copy[col].mean())

print(df_copy)



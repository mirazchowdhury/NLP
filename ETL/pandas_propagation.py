import pandas as pd

data = {'id': [1, 2, 3, 4, 5, None, 7, 8, 9, 10], 
        'score': [10, 20, 20, 40, 50, 50, 60, 90, 90, 100]}
df = pd.DataFrame(data)
print(df)

# new_df = df.fillna(method = 'ffill')
new_df = df.fillna(method = 'bfill')
print(new_df)
import pandas as pd

data = {'text':['This $is @Bangladesh!','^I *love &my #country']}

df = pd.DataFrame(data)


print(df.columns)

df['tokens'] = df['text'].apply(lambda x: x.split())
print(df['tokens'])

import pandas as pd

data = {'text':['This $is @Bangladesh!','^I *love &my #country']}

df = pd.DataFrame(data)

df['text'] = df['text'].str.replace(r'[^a-zA-Z\s]','',regex=True)
print(df)
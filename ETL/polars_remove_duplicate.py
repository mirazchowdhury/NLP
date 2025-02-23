import polars as pl

data = {'text': ['This $is @Bangladesh!', '^I *love &my #country']}

df = pl.DataFrame(data)

print("Before:", df)

df = df.with_columns(pl.col('text').str.replace_all(r'[^a-zA-Z\s]', '').alias('text'))

print("After:", df)

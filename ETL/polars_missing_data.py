import polars as pl
data = {'id':[1,2,3,None,5], 'score':[10,20,30,40,None]}
df = pl.DataFrame(data)

print(df)

# for col in df.columns:
#     print(col)

rm_row = df.drop_nulls()
rm_col = df.select(col for col in df.columns if df[col].is_not_null().all())

# print(rm_row)
# print(rm_col)
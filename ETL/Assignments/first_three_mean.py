import pandas as pd

# Create DataFrame
data = {'id': [1, 2, 3, 4, 5, None, 7, 8, None, 10], 
        'score': [10, 20, 20, 40, 50, 50, 60, None, 90, 100]}
df = pd.DataFrame(data)

# Iterate through each column in the DataFrame
for col in df.columns:
    nan_indices = df[df[col].isna()].index  # Get indices where NaN values exist

    for idx in nan_indices:
        # Ensure there are at least 3 previous values before NaN
        if idx >= 3:
            prev_values = df.loc[idx - 3:idx - 1, col]  # Get previous 3 values
            mean_value = prev_values.mean()  # Calculate mean
            df.loc[idx, col] = mean_value  # Replace NaN with mean
        else:
            print(f"Not enough previous values to compute mean for index {idx} in column '{col}'.")

# Print modified DataFrame
print(df)


# # Filter rows where both 'id' and 'score' are NaN
# nan_rows = df[df['id'].isna() | df['score'].isna()]
# print(nan_rows)

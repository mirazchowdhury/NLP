import pandas as pd

# Create DataFrame
data = {'id': [1, 2, 3, 4, 5, None, 7, 8, 9, 10], 
        'score': [10, 20, 20, 40, 50, 50, 60, None, 90, 100]}
df = pd.DataFrame(data)

# Iterate through each column in the DataFrame
for col in df.columns:
    nan_indices = df[df[col].isna()].index  # Get indices where NaN values exist

    for idx in nan_indices:
        # Get all previous values dynamically (all rows before the current NaN index)
        prev_values = df.loc[:idx - 1, col]  # All previous values (up to current row)
        mean_value = prev_values.mean()  # Compute mean of previous values
        
        # Replace NaN with computed mean
        df.at[idx, col] = mean_value

# Print modified DataFrame
print(df)
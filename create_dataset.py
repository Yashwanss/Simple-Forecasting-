import pandas as pd

# Create a larger dataset with 50 observations to avoid ARIMA errors
data = {
    'date': pd.date_range(start='2023-01-01', periods=50, freq='D'),  # 50 days of data
    'values': [100, 105, 103, 108, 112, 115, 120, 125, 128, 130, 135, 138, 140, 145, 148, 150, 152, 155, 158, 160,
               162, 165, 167, 170, 173, 175, 178, 180, 183, 185, 188, 190, 193, 195, 198, 200, 203, 205, 208, 210,
               213, 215, 218, 220, 223, 225, 228, 230, 233, 235]
}

# Convert into DataFrame
df = pd.DataFrame(data)

# Save the dataframe to a CSV file
df.to_csv('data.csv', index=False)

print("CSV file saved as 'fixed_forecasting_dataset.csv'")
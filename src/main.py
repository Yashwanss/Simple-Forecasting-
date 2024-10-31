from src.data_processing import load_data, preprocess_data
from src.arima_model import ARIMAModel
import pandas as pd


def main():
    # Load and preprocess data
    # file_path = 'data.csv'  # Replace with your data file
    # data = load_data(file_path)
    # processed_data = preprocess_data(data)
    # data = {
    # 'Date': pd.date_range(start='2023-01-01', periods=100, freq='D'),
    # 'Sales': [100 + i + (i//10)*2 for i in range(100)]  # Example trend + seasonality
    # }
    
    # if not isinstance(data.index, pd.DatetimeIndex):
    #     data.index = pd.to_datetime(data.index)  # Convert to DatetimeIndex

    # # Ensure data has a frequency (e.g., daily 'D'). Adjust 'D' depending on your needs (e.g., 'M' for monthly).
    # if data.index.freq is None:
    #     data.index = data.index.asfreq('D')  # Adjust 'D' if needed, depending on your frequency.
    #     print(f"Assigned frequency: {data.index.freq}")
    data = pd.read_csv('data.csv', index_col=0, parse_dates=True)

    if not isinstance(data.index, pd.DatetimeIndex):
        data.index = pd.to_datetime(data.index)

    # Apply frequency to the entire DataFrame, not just the index
    data = data.asfreq('D') 
    
    
    # # Ensure the index is a DatetimeIndex
    # if not isinstance(data.index, pd.DatetimeIndex):
    #     data.index = pd.to_datetime(data.index)

    # # Set the frequency
    # if data.index.freq is None:
    #     data.index = data.index.asfreq('D')
    #     print(f"Assigned frequency: {data.index.freq}")
    
    processed_data = data    
    
    # df = pd.DataFrame(data)
    # df.set_index('Date', inplace=True)
    # processed_data = dfl
    model = ARIMAModel()
    model.train(processed_data)
    model.send_forecast_email(steps=10) # Forecasting the next 5 steps

if __name__ == '__main__':
    main()

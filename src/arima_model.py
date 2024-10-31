import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from src.config import Config
from src.email_service import send_email
from statsmodels.tsa.stattools import adfuller

class ARIMAModel:
    def __init__(self, order=(5, 1, 0)):
        self.order = order
        self.model_fit = None

    def check_stationarity(self, data):
        result = adfuller(data)
        if result[1] > 0.05:
            print("Data is not stationary. Differencing data...")
            data = data.diff().dropna()  
            return self.check_stationarity(data)
        return data

    def train(self, data):
        if not isinstance(data, (pd.DataFrame, pd.Series)):
            raise ValueError("Input data must be a Pandas DataFrame or Series.")

        if not hasattr(data.index, 'freq'):
            data.index = pd.DatetimeIndex(data.index).asfreq('D')

        data = self.check_stationarity(data)

        try:
            self.model = ARIMA(data, order=self.order)
            self.model_fit = self.model.fit()
            print("Model trained successfully.")
        except Exception as e:
            print(f"An error occurred while fitting the model: {e}")

    def forecast(self, steps=10):
        if self.model_fit is None:
            raise RuntimeError("Model has not been trained yet.")
        return self.model_fit.forecast(steps=steps)

    def send_forecast_email(self, steps=10):
        forecast = self.forecast(steps)
        subject = "Forecast Results"
        body = f"Forecast for the next {steps} steps: {forecast.tolist()}"
        send_email(subject, body)

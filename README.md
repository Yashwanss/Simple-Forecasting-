# Simple Data Forecasting Project

## Overview
This project provides a simple automated data forecasting solution using ARIMA. It loads data, trains an ARIMA model, forecasts future values, and sends the results via email.

## Project Structure
- src/: Source code
- .env: Environment variables for SMTP configuration
- data.csv: Example CSV file containing date and value columns

## Requirements
- Python 3.10
- pandas
- statsmodels
- python-dotenv

## Setup
1. Create a .env file with your SMTP configurations.
2. Place your CSV data file in the project directory and ensure it has a date and value column.

## Running the Project
Run the main script:
```bash
python src/main.py 
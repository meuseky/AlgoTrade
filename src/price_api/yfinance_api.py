import yfinance as yf
from statsmodels.tsa.arima.model import ARIMA
import pandas as pd

# Get data for one company for last day
google = yf.Ticker("UK100")
df = google.history(period='1d', interval="1m")

# Get the LOW price during that period
df = df[['Low']]
df['date'] = pd.to_datetime(df.index).time
df.set_index('date', inplace=True)


X = df.index.values
y = df['Low'].values
# The split point is the 10% of the dataframe length
offset = int(0.10*len(df))
X_train = X[:-offset]
y_train = y[:-offset]
X_test = X[-offset:]
y_test = y[-offset:]

# Use an ARIMA model to train the data
model = ARIMA(y_train, order=(5,0,1)).fit()
forecast = model.forecast(steps=1)[0]

a = 1
import yfinance as yf
import pandas as pd

from src.market_instruments.tickers.crypto_tickers import crypto_ticker_definition
from src.market_instruments.tickers.currency_tickers import currency_ticker_definition
from src.market_instruments.tickers.etf_tickers import etf_ticker_definition
from src.market_instruments.tickers.stock_tickers import stock_ticker_definition
from src.utils.date_time import get_start_end_last_month
from src.utils.resources import get_historical_data_filename


def get_historical_prices_by_period(ticker_symbol, period="1d", interval="1m"):
    ticker = yf.Ticker(ticker_symbol)
    history_df = ticker.history(period=period, interval=interval)
    pass


def get_historical_prices_by_date(ticker_symbol, start_date, end_date):
    ticker = yf.Ticker(ticker_symbol)
    history_df = ticker.history(start=start_date, end=end_date, interval="1m")
    return history_df


instruments_to_process = {
    "crypto": crypto_ticker_definition,
    "currency": currency_ticker_definition,
    "etf": etf_ticker_definition,
    "stock": stock_ticker_definition,
}

start_end_dates = get_start_end_last_month()

for instrument_type, instrument_definitions in instruments_to_process.items():
    definition_len = len(instrument_definitions)
    for i, instrument_definition in enumerate(instrument_definitions.values()):
        ticker_symbol = instrument_definition["default_ticker"]
        print("{}: {} {} of {}".format(instrument_type, ticker_symbol, i + 1, definition_len))

        historical_df_list = list()
        for d in start_end_dates:
            history_df = get_historical_prices_by_date(ticker_symbol, d[0], d[1])
            historical_df_list.append(history_df)

        full_history_df = pd.concat(historical_df_list)
        full_history_df.sort_index(inplace=True)

        historical_data_path = get_historical_data_filename(instrument_type, ticker_symbol)
        full_history_df.to_csv(historical_data_path)

import json

from src.market_instruments.etoro.etoro_instruments import etoro_market_instruments
from src.market_instruments.tickers.currency_tickers import currency_ticker_definition

# Get an update of the currency definition comparing what's available on etoro and yfinance
# Use the output to update the currency_tickers module

relevant_currencies = dict()
for k, v in currency_ticker_definition.items():
    if k in etoro_market_instruments["currencies"]:
        currency_ticker_definition[k]["etoro"] = etoro_market_instruments["currencies"][k]["symbol"]

with open('find_currencies.json', 'w') as fp:
    json.dump(currency_ticker_definition, fp, indent=4)

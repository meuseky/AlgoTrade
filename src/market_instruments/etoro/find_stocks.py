import json
from time import sleep

import yfinance as yf

from src.market_instruments.etoro.etoro_instruments import etoro_market_instruments

stock_list = etoro_market_instruments["stocks"]
stock_list_len = len(stock_list)

stock_details = dict()
for i, (k, v) in enumerate(stock_list.items()):
    print("{} of {}".format(i + 1, stock_list_len))

    ticker_info = None
    while ticker_info is None:
        try:
            ticker = yf.Ticker(v["symbol"])
            ticker_info = ticker.get_info()
        except:
            sleep(30)

    if "quoteType" in ticker_info:
        stock_details[ticker_info["shortName"]] = {
            "default_ticker": ticker_info.get("symbol", ""),
            "etoro": ticker_info.get("symbol", ""),
            "long_name": ticker_info.get("longName", ""),
            "tz_name": ticker_info.get("exchangeTimezoneName", ""),
            "tz_short_name": ticker_info.get("exchangeTimezoneShortName", ""),
            "quote_type": ticker_info.get("quoteType", ""),
            "sector": ticker_info.get("sector", ""),
            "market": ticker_info.get("market", ""),
            "average_volume": ticker_info.get("averageVolume", ""),
        }

with open('find_stocks.json', 'w') as fp:
    json.dump(stock_details, fp, indent=4)

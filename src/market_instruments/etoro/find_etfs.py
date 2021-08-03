import json
from time import sleep

import yfinance as yf

from src.market_instruments.etoro.etoro_instruments import etoro_market_instruments

etf_list = etoro_market_instruments["etf"]
etf_list_len = len(etf_list)

etf_details = dict()
for i, (k, v) in enumerate(etf_list.items()):
    print("{} of {}".format(i + 1, etf_list_len))

    ticker_info = None
    while ticker_info is None:
        try:
            ticker = yf.Ticker(v["symbol"])
            ticker_info = ticker.get_info()
        except:
            sleep(30)

    if "quoteType" in ticker_info:
        etf_details[ticker_info["shortName"]] = {
            "default_ticker": ticker_info.get("symbol", ""),
            "etoro": ticker_info.get("symbol", ""),
            "long_name": ticker_info.get("longName", ""),
            "tz_name": ticker_info.get("exchangeTimezoneName", ""),
            "tz_short_name": ticker_info.get("exchangeTimezoneShortName", ""),
            "quote_type": ticker_info.get("quoteType", ""),
            "market": ticker_info.get("market", ""),
            "fund_family": ticker_info.get("fundFamily", ""),
        }

with open('find_etfs.json', 'w') as fp:
    json.dump(etf_details, fp, indent=4)

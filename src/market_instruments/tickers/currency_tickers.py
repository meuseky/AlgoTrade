# Originally generated from https://finance.yahoo.com/currencies/

currency_ticker_definition = {
    "AUD/USD": {
        "default_ticker": "AUDUSD=X",
        "etoro": "AUDUSD"
    },
    "EUR/CAD": {
        "default_ticker": "EURCAD=X",
        "etoro": "EURCAD"
    },
    "EUR/CHF": {
        "default_ticker": "EURCHF=X",
        "etoro": "EURCHF"
    },
    "EUR/GBP": {
        "default_ticker": "EURGBP=X",
        "etoro": "EURGBP"
    },
    "EUR/HUF": {
        "default_ticker": "EURHUF=X",
        "etoro": "EURHUF"
    },
    "EUR/JPY": {
        "default_ticker": "EURJPY=X",
        "etoro": "EURJPY"
    },
    "EUR/SEK": {
        "default_ticker": "EURSEK=X",
        "etoro": "EURSEK"
    },
    "EUR/USD": {
        "default_ticker": "EURUSD=X",
        "etoro": "EURUSD"
    },
    "GBP/JPY": {
        "default_ticker": "GBPJPY=X",
        "etoro": "GBPJPY"
    },
    "GBP/USD": {
        "default_ticker": "GBPUSD=X",
        "etoro": "GBPUSD"
    },
    "NZD/USD": {
        "default_ticker": "NZDUSD=X",
        "etoro": "NZDUSD"
    },
    "USD/CNY": {
        "default_ticker": "CNY=X"
    },
    "USD/HKD": {
        "default_ticker": "HKD=X",
        "etoro": "USDHKD"
    },
    "USD/IDR": {
        "default_ticker": "IDR=X"
    },
    "USD/INR": {
        "default_ticker": "INR=X"
    },
    "USD/JPY": {
        "default_ticker": "JPY=X",
        "etoro": "USDJPY"
    },
    "USD/MXN": {
        "default_ticker": "MXN=X",
        "etoro": "USDMXN"
    },
    "USD/MYR": {
        "default_ticker": "MYR=X"
    },
    "USD/PHP": {
        "default_ticker": "PHP=X"
    },
    "USD/RUB": {
        "default_ticker": "RUB=X",
        "etoro": "USDRUB"
    },
    "USD/SGD": {
        "default_ticker": "SGD=X",
        "etoro": "USDSGD"
    },
    "USD/THB": {
        "default_ticker": "THB=X"
    },
    "USD/ZAR": {
        "default_ticker": "ZAR=X",
        "etoro": "USDZAR"
    }
}

etoro_currency = {k: v for k, v in currency_ticker_definition.items() if "etoro" in v}

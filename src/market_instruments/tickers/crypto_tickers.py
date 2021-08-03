# Originally generated from https://finance.yahoo.com/cryptocurrencies/

crypto_ticker_definition = {
    "Bitcoin": {
        "default_ticker": "BTC-USD",
        "etoro": "BTC",
    },
    "Ethereum": {
        "default_ticker": "ETH-USD",
        "etoro": "ETH",
    },
    "Tether": {
        "default_ticker": "USDT-USD"
    },
    "BinanceCoin": {
        "default_ticker": "BNB-USD",
        "etoro": "BNB",
    },
    "Cardano": {
        "default_ticker": "ADA-USD",
        "etoro": "ADA",
    },
    "XRP": {
        "default_ticker": "XRP-USD",
        "etoro": "XRP",
    },
    "USDCoin": {
        "default_ticker": "USDC-USD"
    },
    "Dogecoin": {
        "default_ticker": "DOGE-USD",
        "etoro": "DOGE",
    },
    "HEX": {
        "default_ticker": "HEX-USD"
    },
    "Polkadot": {
        "default_ticker": "DOT1-USD"
    },
    "Uniswap": {
        "default_ticker": "UNI3-USD",
        "etoro": "UNI",
    },
    "Chainlink": {
        "default_ticker": "LINK-USD",
        "etoro": "LINK",
    },
    "BitcoinCash": {
        "default_ticker": "BCH-USD"
    },
    "Solana": {
        "default_ticker": "SOL1-USD"
    },
    "Litecoin": {
        "default_ticker": "LTC-USD",
        "etoro": "LTC",
    },
    "MaticNetwork": {
        "default_ticker": "MATIC-USD"
    },
    "EthereumClassic": {
        "default_ticker": "ETC-USD"
    },
    "Stellar": {
        "default_ticker": "XLM-USD",
        "etoro": "XLM",
    },
    "THETA": {
        "default_ticker": "THETA-USD"
    },
    "Terra": {
        "default_ticker": "LUNA1-USD"
    },
    "VeChain": {
        "default_ticker": "VET-USD"
    },
    "InternetComputer": {
        "default_ticker": "ICP1-USD"
    },
    "FilecoinFutures": {
        "default_ticker": "FIL-USD"
    },
    "TRON": {
        "default_ticker": "TRX-USD",
        "etoro": "TRX",
    },
    "Monero": {
        "default_ticker": "XMR-USD"
    },
}

etoro_crypto = {k: v for k, v in crypto_ticker_definition.items() if "etoro" in v}

from src.market_instruments.tickers.crypto_tickers import etoro_crypto
from src.market_instruments.tickers.currency_tickers import etoro_currency

# Get market instruments for given trading platform

market_instruments = {
    "crypto": etoro_crypto,
    "currency": etoro_currency,
}

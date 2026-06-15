from django.conf import settings
import requests

STOCK_ENDPOINT = 'https://www.alphavantage.co/query'


class AlphaVantageError(Exception):
    pass


def get_daily_prices(symbol: str) -> list[dict]:
    params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': symbol.upper(),
        'apikey': settings.ALPHA_VANTAGE_API_KEY,
    }
    response = requests.get(STOCK_ENDPOINT, params=params, timeout=15)
    response.raise_for_status()
    payload = response.json()

    if 'Time Series (Daily)' not in payload:
        raise AlphaVantageError(f'Unexpected Alpha Vantage response: {payload}')

    prices = []
    for date, values in payload['Time Series (Daily)'].items():
        prices.append({
            'date': date,
            'open': float(values['1. open']),
            'high': float(values['2. high']),
            'low': float(values['3. low']),
            'close': float(values['4. close']),
            'volume': int(values['5. volume']),
        })
    return prices


def calculate_percentage_change(prices: list[dict]) -> dict:
    latest = prices[0]
    previous = prices[1]
    difference = latest['close'] - previous['close']
    percentage = abs(difference) / previous['close'] * 100
    return {
        'latest_close': latest['close'],
        'previous_close': previous['close'],
        'difference': difference,
        'percentage': percentage,
        'direction': 'up' if difference > 0 else 'down',
    }

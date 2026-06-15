from django.conf import settings
import requests

NEWS_ENDPOINT = 'https://newsapi.org/v2/everything'


class NewsAPIError(Exception):
    pass


def get_company_news(company_name: str, limit: int = 3) -> list[dict]:
    params = {
        'apiKey': settings.NEWS_API_KEY,
        'q': company_name,
        'searchIn': 'title,description',
        'language': 'en',
        'sortBy': 'publishedAt',
    }
    response = requests.get(NEWS_ENDPOINT, params=params, timeout=15)
    response.raise_for_status()
    payload = response.json()

    if payload.get('status') != 'ok':
        raise NewsAPIError(f'Unexpected NewsAPI response: {payload}')

    return payload.get('articles', [])[:limit]

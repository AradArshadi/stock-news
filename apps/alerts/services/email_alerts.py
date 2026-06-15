from django.conf import settings
from django.core.mail import send_mail


def send_stock_news_email(symbol: str, percentage: float, direction: str, articles: list[dict]) -> None:
    arrow = '🔺' if direction == 'up' else '🔻'
    subject = f'{symbol.upper()} stock alert: {arrow} {percentage:.2f}%'

    body_parts = []
    for article in articles:
        body_parts.append(
            f"Headline: {article.get('title', 'No title')}\n"
            f"Brief: {article.get('description', 'No description')}\n"
            f"URL: {article.get('url', '')}"
        )

    body = f'{symbol.upper()} moved {arrow} {percentage:.2f}%\n\n' + '\n\n---\n\n'.join(body_parts)

    send_mail(
        subject=subject,
        message=body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[settings.ALERT_RECIPIENT_EMAIL],
        fail_silently=False,
    )

import json
from django.contrib import messages
from django.shortcuts import render
from .models import Company, StockSearch
from .services.alpha_vantage import get_daily_prices, calculate_percentage_change
from .services.news_api import get_company_news
from apps.alerts.services.email_alerts import send_stock_news_email


DEFAULT_SYMBOL = "TSLA"
DEFAULT_COMPANY = "Tesla Inc."


def dashboard(request):
    companies = Company.objects.filter(is_active=True).order_by("symbol")

    selected_symbol = request.GET.get("symbol", DEFAULT_SYMBOL).upper().strip()
    selected_company = None

    if selected_symbol:
        selected_company = companies.filter(symbol=selected_symbol).first()

    if selected_company:
        company_name = selected_company.name
    else:
        company_name = request.GET.get("company_name", DEFAULT_COMPANY).strip()

    context = {
        "companies": companies,
        "symbol": selected_symbol,
        "company_name": company_name,
        "prices": [],
        "articles": [],
        "change": None,
        "chart_labels": "[]",
        "chart_prices": "[]",
    }

    try:
        prices = get_daily_prices(selected_symbol)
        chart_prices = list(reversed(prices[:30]))
        change = calculate_percentage_change(prices)
        articles = get_company_news(company_name, limit=3)

        StockSearch.objects.create(symbol=selected_symbol, company_name=company_name)

        if request.GET.get("send_email") == "1":
            send_stock_news_email(selected_symbol, change["percentage"], change["direction"], articles)
            messages.success(request, "Email alert sent successfully.")

        context.update({
            "prices": prices[:10],
            "articles": articles,
            "change": change,
            "chart_labels": json.dumps([item["date"] for item in chart_prices]),
            "chart_prices": json.dumps([item["close"] for item in chart_prices]),
        })
    except Exception as exc:
        messages.error(request, f"Could not load stock data: {exc}")

    return render(request, "stocks/dashboard.html", context)

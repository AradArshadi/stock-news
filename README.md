# StockWise — Django Stock Intelligence App

A clean Django web app upgraded from the stock/news alert bootcamp project.

## Features in this version

- Default dropdown with 100 large-cap companies
- Fetch daily stock prices from Alpha Vantage
- Render a 30-day line chart with Chart.js
- Fetch latest company news from NewsAPI
- Send an email alert with the latest articles
- Keep secrets in `.env`
- Clean Django structure with separate apps, migrations, service modules, and a seed command

## Project structure

```text
stockwise-django/
├── apps/
│   ├── alerts/
│   │   ├── migrations/
│   │   ├── services/
│   │   │   └── email_alerts.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   └── views.py
│   └── stocks/
│       ├── management/
│       │   └── commands/
│       │       └── seed_companies.py
│       ├── migrations/
│       ├── services/
│       │   ├── alpha_vantage.py
│       │   └── news_api.py
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       ├── urls.py
│       └── views.py
├── config/
├── static/
├── templates/
├── .env.example
├── .gitignore
├── manage.py
└── requirements.txt
```

## Setup

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
python manage.py migrate
python manage.py seed_companies
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## Reset database during development

```bash
del db.sqlite3
python manage.py migrate
python manage.py seed_companies
python manage.py runserver
```

## Git safety

Do not commit `.env`.

```bash
git add .
git commit -m "Add default company dropdown to stock dashboard"
```

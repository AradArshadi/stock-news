from django.core.management.base import BaseCommand
from config.apps.stocks.models import Company


COMPANIES = [
    ("AAPL", "Apple Inc.", "NASDAQ", "Technology"),
    ("MSFT", "Microsoft Corporation", "NASDAQ", "Technology"),
    ("NVDA", "NVIDIA Corporation", "NASDAQ", "Technology"),
    ("AMZN", "Amazon.com Inc.", "NASDAQ", "Consumer Cyclical"),
    ("GOOGL", "Alphabet Inc. Class A", "NASDAQ", "Communication Services"),
    ("GOOG", "Alphabet Inc. Class C", "NASDAQ", "Communication Services"),
    ("META", "Meta Platforms Inc.", "NASDAQ", "Communication Services"),
    ("BRK.B", "Berkshire Hathaway Inc.", "NYSE", "Financial Services"),
    ("LLY", "Eli Lilly and Company", "NYSE", "Healthcare"),
    ("AVGO", "Broadcom Inc.", "NASDAQ", "Technology"),
    ("TSLA", "Tesla Inc.", "NASDAQ", "Consumer Cyclical"),
    ("JPM", "JPMorgan Chase & Co.", "NYSE", "Financial Services"),
    ("WMT", "Walmart Inc.", "NYSE", "Consumer Defensive"),
    ("V", "Visa Inc.", "NYSE", "Financial Services"),
    ("UNH", "UnitedHealth Group Incorporated", "NYSE", "Healthcare"),
    ("XOM", "Exxon Mobil Corporation", "NYSE", "Energy"),
    ("MA", "Mastercard Incorporated", "NYSE", "Financial Services"),
    ("ORCL", "Oracle Corporation", "NYSE", "Technology"),
    ("COST", "Costco Wholesale Corporation", "NASDAQ", "Consumer Defensive"),
    ("JNJ", "Johnson & Johnson", "NYSE", "Healthcare"),
    ("HD", "The Home Depot Inc.", "NYSE", "Consumer Cyclical"),
    ("PG", "The Procter & Gamble Company", "NYSE", "Consumer Defensive"),
    ("ABBV", "AbbVie Inc.", "NYSE", "Healthcare"),
    ("BAC", "Bank of America Corporation", "NYSE", "Financial Services"),
    ("KO", "The Coca-Cola Company", "NYSE", "Consumer Defensive"),
    ("NFLX", "Netflix Inc.", "NASDAQ", "Communication Services"),
    ("CRM", "Salesforce Inc.", "NYSE", "Technology"),
    ("CVX", "Chevron Corporation", "NYSE", "Energy"),
    ("MRK", "Merck & Co. Inc.", "NYSE", "Healthcare"),
    ("AMD", "Advanced Micro Devices Inc.", "NASDAQ", "Technology"),
    ("PEP", "PepsiCo Inc.", "NASDAQ", "Consumer Defensive"),
    ("ADBE", "Adobe Inc.", "NASDAQ", "Technology"),
    ("TMO", "Thermo Fisher Scientific Inc.", "NYSE", "Healthcare"),
    ("WFC", "Wells Fargo & Company", "NYSE", "Financial Services"),
    ("ACN", "Accenture plc", "NYSE", "Technology"),
    ("CSCO", "Cisco Systems Inc.", "NASDAQ", "Technology"),
    ("MCD", "McDonald's Corporation", "NYSE", "Consumer Cyclical"),
    ("ABT", "Abbott Laboratories", "NYSE", "Healthcare"),
    ("IBM", "International Business Machines Corporation", "NYSE", "Technology"),
    ("LIN", "Linde plc", "NASDAQ", "Basic Materials"),
    ("GE", "GE Aerospace", "NYSE", "Industrials"),
    ("QCOM", "QUALCOMM Incorporated", "NASDAQ", "Technology"),
    ("INTU", "Intuit Inc.", "NASDAQ", "Technology"),
    ("TXN", "Texas Instruments Incorporated", "NASDAQ", "Technology"),
    ("AMGN", "Amgen Inc.", "NASDAQ", "Healthcare"),
    ("NOW", "ServiceNow Inc.", "NYSE", "Technology"),
    ("PM", "Philip Morris International Inc.", "NYSE", "Consumer Defensive"),
    ("DIS", "The Walt Disney Company", "NYSE", "Communication Services"),
    ("ISRG", "Intuitive Surgical Inc.", "NASDAQ", "Healthcare"),
    ("CAT", "Caterpillar Inc.", "NYSE", "Industrials"),
    ("VZ", "Verizon Communications Inc.", "NYSE", "Communication Services"),
    ("GS", "The Goldman Sachs Group Inc.", "NYSE", "Financial Services"),
    ("NEE", "NextEra Energy Inc.", "NYSE", "Utilities"),
    ("RTX", "RTX Corporation", "NYSE", "Industrials"),
    ("SPGI", "S&P Global Inc.", "NYSE", "Financial Services"),
    ("PFE", "Pfizer Inc.", "NYSE", "Healthcare"),
    ("LOW", "Lowe's Companies Inc.", "NYSE", "Consumer Cyclical"),
    ("UBER", "Uber Technologies Inc.", "NYSE", "Technology"),
    ("HON", "Honeywell International Inc.", "NASDAQ", "Industrials"),
    ("BKNG", "Booking Holdings Inc.", "NASDAQ", "Consumer Cyclical"),
    ("T", "AT&T Inc.", "NYSE", "Communication Services"),
    ("BLK", "BlackRock Inc.", "NYSE", "Financial Services"),
    ("MS", "Morgan Stanley", "NYSE", "Financial Services"),
    ("AMAT", "Applied Materials Inc.", "NASDAQ", "Technology"),
    ("SCHW", "The Charles Schwab Corporation", "NYSE", "Financial Services"),
    ("TJX", "The TJX Companies Inc.", "NYSE", "Consumer Cyclical"),
    ("C", "Citigroup Inc.", "NYSE", "Financial Services"),
    ("UNP", "Union Pacific Corporation", "NYSE", "Industrials"),
    ("SYK", "Stryker Corporation", "NYSE", "Healthcare"),
    ("PGR", "The Progressive Corporation", "NYSE", "Financial Services"),
    ("VRTX", "Vertex Pharmaceuticals Incorporated", "NASDAQ", "Healthcare"),
    ("ETN", "Eaton Corporation plc", "NYSE", "Industrials"),
    ("LRCX", "Lam Research Corporation", "NASDAQ", "Technology"),
    ("BSX", "Boston Scientific Corporation", "NYSE", "Healthcare"),
    ("PANW", "Palo Alto Networks Inc.", "NASDAQ", "Technology"),
    ("COP", "ConocoPhillips", "NYSE", "Energy"),
    ("ADP", "Automatic Data Processing Inc.", "NASDAQ", "Industrials"),
    ("DE", "Deere & Company", "NYSE", "Industrials"),
    ("MDT", "Medtronic plc", "NYSE", "Healthcare"),
    ("GILD", "Gilead Sciences Inc.", "NASDAQ", "Healthcare"),
    ("CB", "Chubb Limited", "NYSE", "Financial Services"),
    ("ADI", "Analog Devices Inc.", "NASDAQ", "Technology"),
    ("PLD", "Prologis Inc.", "NYSE", "Real Estate"),
    ("MMC", "Marsh & McLennan Companies Inc.", "NYSE", "Financial Services"),
    ("SBUX", "Starbucks Corporation", "NASDAQ", "Consumer Cyclical"),
    ("MU", "Micron Technology Inc.", "NASDAQ", "Technology"),
    ("KLAC", "KLA Corporation", "NASDAQ", "Technology"),
    ("NKE", "NIKE Inc.", "NYSE", "Consumer Cyclical"),
    ("BA", "The Boeing Company", "NYSE", "Industrials"),
    ("SO", "The Southern Company", "NYSE", "Utilities"),
    ("ICE", "Intercontinental Exchange Inc.", "NYSE", "Financial Services"),
    ("MO", "Altria Group Inc.", "NYSE", "Consumer Defensive"),
    ("DUK", "Duke Energy Corporation", "NYSE", "Utilities"),
    ("ELV", "Elevance Health Inc.", "NYSE", "Healthcare"),
    ("MCK", "McKesson Corporation", "NYSE", "Healthcare"),
    ("APH", "Amphenol Corporation", "NYSE", "Technology"),
    ("REGN", "Regeneron Pharmaceuticals Inc.", "NASDAQ", "Healthcare"),
    ("SHW", "The Sherwin-Williams Company", "NYSE", "Basic Materials"),
    ("WM", "Waste Management Inc.", "NYSE", "Industrials"),
    ("FI", "Fiserv Inc.", "NYSE", "Technology"),
    ("EQIX", "Equinix Inc.", "NASDAQ", "Real Estate"),
]


class Command(BaseCommand):
    help = "Seed the database with 100 large-cap companies for the dashboard dropdown."

    def handle(self, *args, **options):
        created_count = 0
        updated_count = 0

        for symbol, name, exchange, sector in COMPANIES:
            company, created = Company.objects.update_or_create(
                symbol=symbol,
                defaults={
                    "name": name,
                    "exchange": exchange,
                    "sector": sector,
                    "is_active": True,
                },
            )
            if created:
                created_count += 1
            else:
                updated_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Seed complete: {created_count} created, {updated_count} updated."
            )
        )

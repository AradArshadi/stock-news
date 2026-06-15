from django.contrib import admin
from .models import Company, StockSearch


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("symbol", "name", "exchange", "sector", "is_active")
    list_filter = ("exchange", "sector", "is_active")
    search_fields = ("symbol", "name")


@admin.register(StockSearch)
class StockSearchAdmin(admin.ModelAdmin):
    list_display = ("symbol", "company_name", "searched_at")
    search_fields = ("symbol", "company_name")
    list_filter = ("searched_at",)

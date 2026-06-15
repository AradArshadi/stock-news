from django.contrib import admin
from .models import PriceAlert


@admin.register(PriceAlert)
class PriceAlertAdmin(admin.ModelAdmin):
    list_display = ('symbol', 'direction', 'target_price', 'email', 'active', 'created_at')
    list_filter = ('direction', 'active')
    search_fields = ('symbol', 'email')

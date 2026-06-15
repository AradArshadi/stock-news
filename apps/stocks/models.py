from django.db import models


class Company(models.Model):
    symbol = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=255)
    exchange = models.CharField(max_length=50, blank=True)
    sector = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["symbol"]
        verbose_name_plural = "companies"

    def __str__(self):
        return f"{self.symbol} - {self.name}"


class StockSearch(models.Model):
    symbol = models.CharField(max_length=20)
    company_name = models.CharField(max_length=255, blank=True)
    searched_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-searched_at"]

    def __str__(self):
        return self.symbol

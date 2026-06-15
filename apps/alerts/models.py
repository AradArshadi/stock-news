from django.db import models


class PriceAlert(models.Model):
    DIRECTION_CHOICES = [
        ('above', 'Above'),
        ('below', 'Below'),
    ]

    symbol = models.CharField(max_length=20)
    target_price = models.DecimalField(max_digits=12, decimal_places=2)
    direction = models.CharField(max_length=10, choices=DIRECTION_CHOICES)
    email = models.EmailField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.symbol} {self.direction} {self.target_price}'

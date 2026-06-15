# Generated manually for the StockWise starter project.
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PriceAlert",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("symbol", models.CharField(max_length=20)),
                ("target_price", models.DecimalField(decimal_places=2, max_digits=12)),
                ("direction", models.CharField(choices=[("above", "Above"), ("below", "Below")], max_length=10)),
                ("email", models.EmailField(max_length=254)),
                ("active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
    ]

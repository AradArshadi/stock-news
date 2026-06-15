# Generated manually for the StockWise starter project.
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("symbol", models.CharField(max_length=20, unique=True)),
                ("name", models.CharField(max_length=255)),
                ("exchange", models.CharField(blank=True, max_length=50)),
                ("sector", models.CharField(blank=True, max_length=100)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "ordering": ["symbol"],
                "verbose_name_plural": "companies",
            },
        ),
        migrations.CreateModel(
            name="StockSearch",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("symbol", models.CharField(max_length=20)),
                ("company_name", models.CharField(blank=True, max_length=255)),
                ("searched_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ["-searched_at"],
            },
        ),
    ]

# Generated by Django 4.2.5 on 2023-11-17 16:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0005_remove_order_tags_product_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

# Generated by Django 4.2.5 on 2023-11-25 11:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0006_alter_product_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="notes",
            field=models.CharField(max_length=200, null=True),
        ),
    ]
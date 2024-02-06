# Generated by Django 4.2.5 on 2023-11-17 16:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0004_tag_order_tags"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="tags",
        ),
        migrations.AddField(
            model_name="product",
            name="tags",
            field=models.ManyToManyField(to="accounts.tag"),
        ),
    ]

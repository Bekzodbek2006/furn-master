# Generated by Django 4.0.6 on 2022-07-07 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furn', '0008_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='products_url',
            field=models.URLField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
# Generated by Django 4.0.6 on 2022-07-07 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furn', '0010_rename_arrivals_arrival_rename_products_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
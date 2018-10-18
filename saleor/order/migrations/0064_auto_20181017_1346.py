# Generated by Django 2.1.2 on 2018-10-17 18:46

from django.db import migrations
import django_prices.models
import saleor.core


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0063_auto_20180926_0446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='discount_amount',
            field=django_prices.models.MoneyField(currency='USD', decimal_places=2, default=saleor.core.zero_money, max_digits=12),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_gross',
            field=django_prices.models.MoneyField(currency='USD', decimal_places=2, default=saleor.core.zero_money, max_digits=12),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_net',
            field=django_prices.models.MoneyField(currency='USD', decimal_places=2, default=saleor.core.zero_money, max_digits=12),
        ),
    ]
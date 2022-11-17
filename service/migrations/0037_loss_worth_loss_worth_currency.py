# Generated by Django 4.1.1 on 2022-10-25 19:16

from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0036_ltype_color_ltype_size_rtype_color_rtype_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='loss',
            name='worth',
            field=djmoney.models.fields.MoneyField(currency_choices=[('EUR', 'EUR'), ('RUB', 'RUB'), ('USD', 'USD'), ('UZS', 'UZS')], decimal_places=2, default_currency='UZS', max_digits=50, null=True),
        ),
        migrations.AddField(
            model_name='loss',
            name='worth_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('EUR', 'EUR'), ('RUB', 'RUB'), ('USD', 'USD'), ('UZS', 'UZS')], default='UZS', editable=False, max_length=3, null=True),
        ),
    ]
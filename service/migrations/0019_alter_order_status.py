# Generated by Django 4.1.1 on 2022-10-01 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0018_order_total_sum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, choices=[("To'lovni kutmoqda", "To'lovni kutmoqda"), ('Qabul qilindi', 'Qabul qilindi'), ('Chop etilmoqda', 'Chop etilmoqda'), ('Tayyor', 'Tayyor')], default="To'lovni kutmoqda", max_length=50, null=True),
        ),
    ]
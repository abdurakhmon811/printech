# Generated by Django 4.1.1 on 2022-09-17 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_alter_complaint_book_alter_complaint_time_bought_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='custom_category',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]

# Generated by Django 4.1.1 on 2022-09-28 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0016_news_publisher_tw_blogpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='date_published',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]

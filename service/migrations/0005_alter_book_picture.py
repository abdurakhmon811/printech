# Generated by Django 4.1.1 on 2022-09-17 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_complaint_custom_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='picture',
            field=models.ImageField(blank=True, default='static/media/user_loaded_images/open.png', null=True, upload_to='user_loaded_images/'),
        ),
    ]
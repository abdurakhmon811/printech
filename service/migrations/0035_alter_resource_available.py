# Generated by Django 4.1.1 on 2022-10-16 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0034_rename_ptype_loss_type_rename_ptype_resource_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='available',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

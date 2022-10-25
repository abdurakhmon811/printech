# Generated by Django 4.1.1 on 2022-10-16 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0033_ltype_rtype_resource_loss'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loss',
            old_name='ptype',
            new_name='type',
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='ptype',
            new_name='type',
        ),
        migrations.RemoveField(
            model_name='loss',
            name='bottles',
        ),
        migrations.RemoveField(
            model_name='loss',
            name='boxes',
        ),
        migrations.RemoveField(
            model_name='loss',
            name='gram',
        ),
        migrations.RemoveField(
            model_name='loss',
            name='packs',
        ),
        migrations.RemoveField(
            model_name='loss',
            name='pieces',
        ),
        migrations.RemoveField(
            model_name='loss',
            name='sheets',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='bottles',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='boxes',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='gram',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='packs',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='pieces',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='sheets',
        ),
        migrations.AddField(
            model_name='loss',
            name='amount',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='loss',
            name='color',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='resource',
            name='amount',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='resource',
            name='color',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
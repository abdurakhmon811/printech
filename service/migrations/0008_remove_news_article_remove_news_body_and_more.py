# Generated by Django 4.1.1 on 2022-09-18 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0007_alter_book_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='article',
        ),
        migrations.RemoveField(
            model_name='news',
            name='body',
        ),
        migrations.RemoveField(
            model_name='news',
            name='picture',
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.CharField(blank=True, choices=[('F', 'Fantastika'), ('SF', 'Ilmiy Fantastika'), ('CF', 'Zamonaviy Fantastika'), ('HF', 'Tarixiy Fantastika'), ('AA', 'Sarguzashtlar'), ('M', 'Detektiv'), ('R', 'Romantika'), ('N', 'Roman'), ('SS', 'Qisqa hikoyalar'), ('DS', 'Aniq fanlar'), ('L', 'Tilga oid'), ('P', 'Axborot Texnologiyalariga oid')], default=None, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='body_1',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='body_2',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='body_3',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='picture_1',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='user_loaded_images/'),
        ),
        migrations.AddField(
            model_name='news',
            name='picture_2',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='user_loaded_images/'),
        ),
        migrations.AddField(
            model_name='news',
            name='picture_3',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='user_loaded_images/'),
        ),
        migrations.AddField(
            model_name='news',
            name='publisher_gm',
            field=models.EmailField(blank=True, default=None, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='publisher_li',
            field=models.URLField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='publisher_tg',
            field=models.URLField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='short_body',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='subtitle_1',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='subtitle_2',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='subtitle_3',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='title',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='delivered',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, choices=[('TK', "To'lovni kutmoqda..."), ('QQ', 'Qabul qilindi'), ('CE', 'Chop etilmoqda...'), ('T', 'Tayyor')], default='TK', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='book',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='service.book'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='custom_category',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='time_bought',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='createsite',
            name='age',
            field=models.IntegerField(blank=True, default=18, null=True),
        ),
        migrations.AlterField(
            model_name='createsite',
            name='f_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='createsite',
            name='l_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='createsite',
            name='person',
            field=models.CharField(blank=True, choices=[('JS', 'Jismoniy shaxs'), ('YS', 'Yuridik shaxs')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment',
            field=models.CharField(choices=[('CL', 'Click'), ('CSH', 'Naqd'), ('V', 'VISA')], default=None, max_length=3),
        ),
        migrations.AlterField(
            model_name='order',
            name='place_to_get',
            field=models.CharField(choices=[('KA', 'Kamandi MFY'), ('GL', "Eski Ko'z kasalliklari shifoxonasi"), ('II', 'Qarshi Muhandislik-Iqtisodiyot Instituti')], max_length=2),
        ),
    ]

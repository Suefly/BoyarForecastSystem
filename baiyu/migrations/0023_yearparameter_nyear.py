# Generated by Django 2.0.3 on 2019-06-27 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baiyu', '0022_auto_20190626_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='yearparameter',
            name='nYear',
            field=models.IntegerField(default=2009, verbose_name='年份'),
        ),
    ]

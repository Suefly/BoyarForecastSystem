# Generated by Django 2.0.3 on 2019-05-25 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baiyu', '0004_auto_20190525_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speciesinfo',
            name='BirdType',
            field=models.CharField(max_length=16, verbose_name='家禽种类'),
        ),
    ]

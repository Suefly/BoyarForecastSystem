# Generated by Django 2.0.3 on 2019-06-27 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baiyu', '0023_yearparameter_nyear'),
    ]

    operations = [
        migrations.AddField(
            model_name='yeartcjirouparam',
            name='nYear',
            field=models.IntegerField(default=2019, verbose_name='年份'),
        ),
    ]

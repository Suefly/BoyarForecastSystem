# Generated by Django 2.0.3 on 2019-10-31 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baiyu', '0046_introducedinfo_liveperiod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='introducedinfo',
            name='LivePeriod',
            field=models.IntegerField(default=0, verbose_name='生存周期'),
        ),
    ]

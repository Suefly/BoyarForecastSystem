# Generated by Django 2.0.3 on 2019-10-31 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baiyu', '0045_auto_20191027_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='introducedinfo',
            name='LivePeriod',
            field=models.IntegerField(default=65, verbose_name='生存周期'),
        ),
    ]

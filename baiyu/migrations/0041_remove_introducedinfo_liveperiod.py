# Generated by Django 2.0.3 on 2019-08-04 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baiyu', '0040_introducedinfodetail_huanyuinterval'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='introducedinfo',
            name='LivePeriod',
        ),
    ]

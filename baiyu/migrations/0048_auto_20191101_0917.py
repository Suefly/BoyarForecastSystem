# Generated by Django 2.0.3 on 2019-11-01 01:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baiyu', '0047_auto_20191031_1607'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weekstandardtable',
            name='SpeciesId',
        ),
        migrations.RemoveField(
            model_name='weekstandardtable',
            name='feedWayId',
        ),
    ]
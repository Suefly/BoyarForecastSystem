# Generated by Django 2.0.3 on 2019-06-25 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baiyu', '0020_progenitorintroduceddetail_feedwayid'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProgenitorIntroduced',
            new_name='IntroducedInfo',
        ),
        migrations.RenameModel(
            old_name='ProgenitorIntroducedDetail',
            new_name='IntroducedInfoDetail',
        ),
    ]

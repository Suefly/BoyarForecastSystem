# Generated by Django 2.0.3 on 2019-05-25 02:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baiyu', '0003_progenitorintroduced'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companyinfo',
            old_name='remark',
            new_name='Remark',
        ),
    ]

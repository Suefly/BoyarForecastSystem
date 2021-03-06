# Generated by Django 2.0.3 on 2019-10-27 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baiyu', '0044_auto_20190821_2132'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZudaiIntroducedFile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='序号')),
                ('fileName', models.CharField(blank=True, max_length=64, null=True, verbose_name='文件名')),
                ('Remark', models.CharField(blank=True, max_length=64, null=True, verbose_name='备注')),
            ],
        ),
        migrations.AlterField(
            model_name='introducedinfodetail',
            name='qzhyPeriod',
            field=models.IntegerField(default=0, verbose_name='强制换羽周期'),
        ),
    ]

# Generated by Django 2.0.3 on 2019-05-26 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baiyu', '0009_dailystandardtable'),
    ]

    operations = [
        migrations.CreateModel(
            name='WholeParameter',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='序号')),
                ('YuChengPeriod', models.IntegerField(verbose_name='育成期')),
                ('MaxLivePeriod', models.IntegerField(verbose_name='最大生存周期')),
                ('XuanYongRate', models.FloatField(verbose_name='选用率')),
                ('nGeneration', models.IntegerField(verbose_name='代次')),
                ('nBirdsType', models.IntegerField(verbose_name='家禽种类')),
                ('Remark', models.CharField(blank=True, max_length=64, null=True, verbose_name='备注')),
            ],
        ),
    ]

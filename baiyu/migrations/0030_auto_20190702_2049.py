# Generated by Django 2.0.3 on 2019-07-02 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baiyu', '0029_weeklyintroducedmedian_shengchanzhou'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weeklyintroducedmedian',
            name='CompanyId',
            field=models.IntegerField(blank=True, null=True, verbose_name='公司名'),
        ),
        migrations.AlterField(
            model_name='weeklyintroducedmedian',
            name='SpeciesId',
            field=models.IntegerField(blank=True, default=1, null=True, verbose_name='品种'),
        ),
        migrations.AlterField(
            model_name='weeklyintroducedmedian',
            name='TaoTaiJiNum',
            field=models.IntegerField(blank=True, null=True, verbose_name='淘汰鸡数目'),
        ),
        migrations.AlterField(
            model_name='weeklyintroducedmedian',
            name='TotalChanDanCunLan',
            field=models.IntegerField(blank=True, null=True, verbose_name='总产蛋期存栏'),
        ),
        migrations.AlterField(
            model_name='weeklyintroducedmedian',
            name='TotalChuJi',
            field=models.IntegerField(blank=True, null=True, verbose_name='雏鸡总数'),
        ),
        migrations.AlterField(
            model_name='weeklyintroducedmedian',
            name='TotalDan',
            field=models.IntegerField(blank=True, null=True, verbose_name='总产蛋数'),
        ),
        migrations.AlterField(
            model_name='weeklyintroducedmedian',
            name='TotalFactSaleChuJi',
            field=models.IntegerField(blank=True, null=True, verbose_name='实际销售雏鸡总数'),
        ),
        migrations.AlterField(
            model_name='weeklyintroducedmedian',
            name='TotalYuChengCunLan',
            field=models.IntegerField(blank=True, null=True, verbose_name='总育成期存栏'),
        ),
        migrations.AlterField(
            model_name='weeklyintroducedmedian',
            name='dTaoTaiJiRou',
            field=models.FloatField(blank=True, null=True, verbose_name='淘汰鸡肉'),
        ),
        migrations.AlterField(
            model_name='weeklyintroducedmedian',
            name='endDate',
            field=models.DateField(blank=True, null=True, verbose_name='结束日期'),
        ),
        migrations.AlterField(
            model_name='weeklyintroducedmedian',
            name='feedWayId',
            field=models.IntegerField(blank=True, default=1, null=True, verbose_name='饲养方式'),
        ),
        migrations.AlterField(
            model_name='weeklyintroducedmedian',
            name='nBirdsType',
            field=models.IntegerField(blank=True, null=True, verbose_name='家禽种类'),
        ),
        migrations.AlterField(
            model_name='weeklyintroducedmedian',
            name='nDraftOrOriginal',
            field=models.IntegerField(blank=True, null=True, verbose_name='存储类型'),
        ),
        migrations.AlterField(
            model_name='weeklyintroducedmedian',
            name='nGeneration',
            field=models.IntegerField(blank=True, null=True, verbose_name='代次'),
        ),
        migrations.AlterField(
            model_name='weeklyintroducedmedian',
            name='shengchanZhou',
            field=models.IntegerField(blank=True, default=1, null=True, verbose_name='生产周编号'),
        ),
        migrations.AlterField(
            model_name='weeklyintroducedmedian',
            name='startDate',
            field=models.DateField(blank=True, null=True, verbose_name='开始日期'),
        ),
    ]
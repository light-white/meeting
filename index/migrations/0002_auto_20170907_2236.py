# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-07 14:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='快递地址'),
        ),
        migrations.AddField(
            model_name='user',
            name='invoicenum',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='纳税人识别号'),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='手机号'),
        ),
        migrations.AddField(
            model_name='user',
            name='postal',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='邮政编码'),
        ),
        migrations.AddField(
            model_name='user',
            name='title',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='发票抬头'),
        ),
    ]

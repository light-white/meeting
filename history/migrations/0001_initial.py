# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-07 03:22
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='内容')),
                ('time', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '历届文章',
                'verbose_name_plural': '历届文章',
            },
        ),
    ]

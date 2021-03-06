# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-07 12:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='標題')),
                ('content', models.TextField(verbose_name='內容')),
            ],
            options={
                'verbose_name_plural': '關於聖森',
                'verbose_name': '關於聖森',
                'db_table': 'about',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='公司名')),
                ('zipcode', models.IntegerField(default=0, verbose_name='郵遞區號')),
                ('address', models.CharField(max_length=200, verbose_name='地址')),
            ],
            options={
                'verbose_name_plural': '公司資訊',
                'verbose_name': '公司資訊',
                'db_table': 'company',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('email', models.EmailField(max_length=200, verbose_name='信箱')),
                ('url', models.URLField(blank=True, null=True, verbose_name='網址')),
                ('message', models.TextField(verbose_name='訊息')),
            ],
            options={
                'verbose_name_plural': '聯絡我們',
                'verbose_name': '聯絡我們',
                'db_table': 'contact',
            },
        ),
        migrations.CreateModel(
            name='Management_Philosophy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='標題')),
                ('content', models.TextField(verbose_name='內容')),
            ],
            options={
                'verbose_name_plural': '經營理念',
                'verbose_name': '經營理念',
                'db_table': 'management_philosophy',
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(default='./no-profile-pic-img.gif', upload_to='./', verbose_name='圖示')),
                ('title', models.CharField(max_length=50, verbose_name='標題')),
                ('url', models.URLField(verbose_name='網址')),
            ],
            options={
                'verbose_name_plural': '合作伙伴',
                'verbose_name': '合作伙伴',
                'db_table': 'partner',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='標題')),
                ('content', models.CharField(max_length=100, verbose_name='內容')),
            ],
            options={
                'verbose_name_plural': '首頁滑塊',
                'verbose_name': '首頁滑塊',
                'db_table': 'slider',
            },
        ),
    ]

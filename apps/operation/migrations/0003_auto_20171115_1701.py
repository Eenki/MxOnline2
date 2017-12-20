# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 09:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0002_auto_20171115_1519'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermessage',
            name='has_read',
            field=models.CharField(choices=[('yes', '已读'), ('no', '没读')], default='no', max_length=10, verbose_name='消息是否读过'),
        ),
        migrations.AlterField(
            model_name='userfavourite',
            name='fav_type',
            field=models.IntegerField(choices=[(1, '课程'), (2, '机构'), (3, '教师')], verbose_name='类型'),
        ),
    ]
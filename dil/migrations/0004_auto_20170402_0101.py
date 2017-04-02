# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-02 01:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dil', '0003_auto_20170401_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_user_profile', related_query_name='to_user_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]

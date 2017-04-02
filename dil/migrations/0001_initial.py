# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 21:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('dob', models.DateTimeField(verbose_name='Date Of Birth')),
                ('branch', models.CharField(max_length=200)),
                ('red_rose', models.IntegerField(default=0)),
                ('yellow_rose', models.IntegerField(default=0)),
                ('year', models.IntegerField(default=1)),
            ],
        ),
        migrations.AddField(
            model_name='messages',
            name='frm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user_profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='messages',
            name='to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_user_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]

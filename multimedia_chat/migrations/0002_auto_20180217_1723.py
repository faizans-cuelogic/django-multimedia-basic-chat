# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-17 17:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multimedia_chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='message_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]

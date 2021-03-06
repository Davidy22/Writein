# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-29 03:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0002_auto_20171228_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='IP',
            field=models.GenericIPAddressField(help_text='Recipient IP address'),
        ),
        migrations.AlterUniqueTogether(
            name='entry',
            unique_together=set([('pollID', 'IP')]),
        ),
    ]

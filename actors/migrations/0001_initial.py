# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Actor Name')),
                ('description', models.TextField(verbose_name='Actor Description')),
                ('file', models.ImageField(upload_to=b'', max_length=255, verbose_name='Actor Banner')),
                ('career_start_date', models.DateField(verbose_name='Actor Career Start Date')),
            ],
        ),
    ]

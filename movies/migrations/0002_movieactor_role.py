# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movieactor',
            name='role',
            field=models.CharField(default=None, max_length=255, verbose_name='Movie Role'),
            preserve_default=False,
        ),
    ]

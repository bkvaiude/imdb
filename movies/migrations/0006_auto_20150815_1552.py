# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_auto_20150815_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviescreenshot',
            name='file',
            field=models.ImageField(upload_to=b'movie/banner/', verbose_name='Movie Banner'),
        ),
        migrations.AlterField(
            model_name='movievideo',
            name='file',
            field=models.FileField(upload_to=b'movie/trailer/', verbose_name='Movie Trailer'),
        ),
    ]

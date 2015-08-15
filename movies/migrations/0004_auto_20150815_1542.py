# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20150815_0734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieactor',
            name='actor_id',
            field=models.ForeignKey(related_name='actor_object', to='actors.Actor'),
        ),
        migrations.AlterField(
            model_name='movieactor',
            name='movie_id',
            field=models.ForeignKey(related_name='movie_actors', to='movies.Movie'),
        ),
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

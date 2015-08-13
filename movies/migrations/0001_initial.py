# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('actors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Movie Name')),
                ('description', models.TextField(verbose_name='Movie Description')),
                ('release_date', models.DateField(verbose_name='Movie Release Date')),
            ],
        ),
        migrations.CreateModel(
            name='MovieActor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('actor_id', models.ForeignKey(related_name='mva_actor', to='actors.Actor')),
                ('movie_id', models.ForeignKey(related_name='mva_movie', to='movies.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='MovieAward',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('award_id', models.ForeignKey(related_name='award_for_movie', to='awards.Award')),
                ('movie_id', models.ForeignKey(related_name='movie_for_award', to='movies.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='MovieRating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.CharField(max_length=3, verbose_name='Movie Rating')),
                ('movie_id', models.ForeignKey(related_name='mr_movie', to='movies.Movie')),
                ('user_id', models.ForeignKey(related_name='mr_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MovieScreenshot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.ImageField(upload_to=b'', verbose_name='Movie Banner')),
                ('is_cover_photo', models.TextField(verbose_name="Is this movie's cover photo?")),
                ('launched_date', models.DateField(verbose_name='Movie Release Date')),
                ('priority', models.IntegerField(verbose_name='Movie Screenshot Order')),
                ('movie_id', models.ForeignKey(related_name='movie_screenshots', to='movies.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='MovieVideo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(upload_to=b'', verbose_name='Movie Trailer')),
                ('launched_date', models.DateField(verbose_name='Movie Release Date')),
                ('movie_id', models.ForeignKey(related_name='movie_trailers', to='movies.Movie')),
            ],
        ),
    ]

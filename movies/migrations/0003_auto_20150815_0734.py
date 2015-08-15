# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movieactor_role'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ('updated',)},
        ),
        migrations.AlterModelOptions(
            name='movieactor',
            options={'ordering': ('updated',)},
        ),
        migrations.AlterModelOptions(
            name='movieaward',
            options={'ordering': ('updated',)},
        ),
        migrations.AlterModelOptions(
            name='movierating',
            options={'ordering': ('updated',)},
        ),
        migrations.AlterModelOptions(
            name='moviescreenshot',
            options={'ordering': ('updated',)},
        ),
        migrations.AlterModelOptions(
            name='movievideo',
            options={'ordering': ('updated',)},
        ),
        migrations.AddField(
            model_name='movie',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 15, 7, 34, 18, 493320, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 15, 7, 34, 21, 325219, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movieactor',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 15, 7, 34, 26, 541380, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movieactor',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 15, 7, 34, 28, 77539, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movieaward',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 15, 7, 34, 29, 397502, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movieaward',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 15, 7, 34, 30, 653334, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movierating',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 15, 7, 34, 32, 156923, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movierating',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 15, 7, 34, 34, 356929, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='moviescreenshot',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 15, 7, 34, 35, 845244, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='moviescreenshot',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 15, 7, 34, 37, 317231, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movievideo',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 15, 7, 34, 38, 677325, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movievideo',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 15, 7, 34, 40, 197249, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]

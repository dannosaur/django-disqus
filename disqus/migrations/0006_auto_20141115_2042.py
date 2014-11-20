# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disqus', '0005_auto_20141115_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='approved',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='deleted',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='dislikes',
            field=models.IntegerField(default=0, max_length=11),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='edited',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='flagged',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='highlighted',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.IntegerField(default=0, max_length=11),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='spam',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]

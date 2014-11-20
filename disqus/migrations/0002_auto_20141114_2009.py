# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disqus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='object_id',
            field=models.BigIntegerField(max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='thread',
            name='thread_id',
            field=models.BigIntegerField(max_length=20),
            preserve_default=True,
        ),
    ]

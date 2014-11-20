# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disqus', '0002_auto_20141114_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='thread_id',
            field=models.BigIntegerField(unique=True, max_length=20),
            preserve_default=True,
        ),
    ]

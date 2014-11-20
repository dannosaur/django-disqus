# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disqus', '0004_author_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='reputation',
            field=models.DecimalField(default=1, max_digits=9, decimal_places=5),
            preserve_default=True,
        ),
    ]

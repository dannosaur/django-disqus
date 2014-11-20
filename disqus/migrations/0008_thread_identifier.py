# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disqus', '0007_comment_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='identifier',
            field=models.CharField(default=b'', max_length=255),
            preserve_default=True,
        ),
    ]

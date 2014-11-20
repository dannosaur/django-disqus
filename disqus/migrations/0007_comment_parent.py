# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disqus', '0006_auto_20141115_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(default=None, blank=True, to='disqus.Comment', null=True),
            preserve_default=True,
        ),
    ]

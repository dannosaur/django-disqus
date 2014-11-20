# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disqus', '0003_auto_20141114_2009'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author_id', models.BigIntegerField(unique=True, max_length=20)),
                ('username', models.CharField(max_length=255)),
                ('date_joined', models.DateTimeField()),
                ('anonymous', models.BooleanField(default=False)),
                ('primary', models.BooleanField(default=True)),
                ('private', models.BooleanField(default=False)),
                ('profile_url', models.URLField()),
                ('avatar_large', models.URLField()),
                ('avatar_small', models.URLField()),
                ('reputation', models.DecimalField(max_digits=9, decimal_places=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment_id', models.BigIntegerField(unique=True, max_length=20)),
                ('date_created', models.DateTimeField()),
                ('raw_message', models.TextField()),
                ('html_message', models.TextField()),
                ('author', models.ForeignKey(to='disqus.Author')),
                ('thread', models.ForeignKey(to='disqus.Thread')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

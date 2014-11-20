from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models
from django.contrib.contenttypes.models import ContentType


class Thread(models.Model):
    thread_id = models.BigIntegerField(max_length=20, unique=True)
    object_type = models.ForeignKey(ContentType)
    object_id = models.BigIntegerField(max_length=20)
    content_object = GenericForeignKey('object_type', 'object_id')
    identifier = models.CharField(max_length=255, null=False, default="")


class Author(models.Model):
    author_id = models.BigIntegerField(max_length=20, unique=True)
    username = models.CharField(max_length=255)
    date_joined = models.DateTimeField(auto_now=False)
    anonymous = models.BooleanField(default=False)
    primary = models.BooleanField(default=True)
    private = models.BooleanField(default=False)
    profile_url = models.URLField()
    avatar_large = models.URLField()
    avatar_small = models.URLField()
    reputation = models.DecimalField(max_digits=9, decimal_places=5, default=1)


class Comment(models.Model):
    comment_id = models.BigIntegerField(max_length=20, unique=True)
    parent = models.ForeignKey('Comment', default=None, blank=True, null=True)
    thread = models.ForeignKey(Thread)
    author = models.ForeignKey(Author)
    date_created = models.DateTimeField(auto_now=False)
    raw_message = models.TextField()
    html_message = models.TextField()
    approved = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    edited = models.BooleanField(default=False)
    flagged = models.BooleanField(default=False)
    highlighted = models.BooleanField(default=False)
    spam = models.BooleanField(default=False)
    likes = models.IntegerField(max_length=11, default=0)
    dislikes = models.IntegerField(max_length=11, default=0)




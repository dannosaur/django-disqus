import calendar
import dateutil.parser
from django.contrib.contenttypes.models import ContentType
from django.core.management import BaseCommand
from disqus.api import Client
from disqus.models import Thread, Comment, Author
import pytz


class Command(BaseCommand):
    client = None

    def handle(self, *args, **options):
        self.client = Client()

        post_kwargs = {
            'order': 'asc',
            'limit': 1,
        }

        try:
            last_comment = Comment.objects.latest('id')
            post_kwargs['since'] = calendar.timegm(
                last_comment.date_created.utctimetuple()
            ) + 1
        except Comment.DoesNotExist:
            pass

        data = self.client.list_posts(**post_kwargs)

        while data['cursor']['more']:
            self.process_response(data['response'])

            post_kwargs['cursor'] = data['cursor']['next']
            data = self.client.list_posts(**post_kwargs)
        else:
            self.process_response(data['response'])

    def process_response(self, response):
        for post in response:
            # get thread
            try:
                thread = Thread.objects.get(thread_id=post['thread'])
            except Thread.DoesNotExist:
                thread = self.client.thread_details(post['thread'])['response']

                for identifier in thread['identifiers']:
                    s = identifier.split(".")
                    if len(s) < 3:
                        continue

                    ct = ContentType.objects.get(
                        app_label=s[0],
                        model=s[1]
                    )

                    model = ct.get_object_for_this_type(id=s[2])

                    thread = Thread.objects.create(
                        content_object=model,
                        thread_id=post['thread'],
                        identifier=identifier
                    )

                    break

            # get author
            try:
                author = Author.objects.get(
                    author_id=post['author']['id']
                )
            except Author.DoesNotExist:
                author = Author.objects.create(
                    author_id=post['author']['id'],
                    username=post['author']['username'],
                    date_joined=pytz.utc.localize(
                        dateutil.parser.parse(
                            post['author']['joinedAt']
                        )
                    ),
                    anonymous=post['author']['isAnonymous'],
                    primary=post['author']['isPrimary'],
                    private=post['author']['isPrivate'],
                    profile_url=post['author']['profileUrl'],
                    avatar_large=
                    post['author']['avatar']['large']['permalink'],
                    avatar_small=
                    post['author']['avatar']['small']['permalink'],
                )

            author.reputation = post['author']['reputation']
            author.save()

            # get or create comment
            try:
                Comment.objects.get(comment_id=post['id'])
                # we've seen this one before...
                break
            except Comment.DoesNotExist:
                comment = Comment.objects.create(
                    comment_id=post['id'],
                    thread=thread,
                    author=author,
                    date_created=pytz.utc.localize(
                        dateutil.parser.parse(post['createdAt'])
                    ),
                    raw_message=post['raw_message'],
                    html_message=post['message'],
                    approved=post['isApproved'],
                    deleted=post['isDeleted'],
                    edited=post['isEdited'],
                    flagged=post['isFlagged'],
                    spam=post['isSpam'],
                )

                if post['parent'] is not None:
                    parent = Comment.objects.get(comment_id=post['parent'])
                    comment.parent = parent
                    comment.save()

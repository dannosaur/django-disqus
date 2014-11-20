from disqus.models import Thread, Comment
from django import template
from django.conf import settings
from django.template.defaulttags import URLNode, url

register = template.Library()


class DisqusURLNode(URLNode):
    def render(self, context):
        path = super(DisqusURLNode, self).render(context)

        return "http://%s%s" % (
            settings.SITE_URL,
            path
        )


@register.tag
def disqus_url(parser, token):
    url_instance = url(parser, token)

    return DisqusURLNode(
        view_name=url_instance.view_name,
        args=url_instance.args,
        kwargs=url_instance.kwargs,
        asvar=url_instance.asvar
    )


@register.inclusion_tag("disqus/comments_widget.html", takes_context=True)
def disqus_widget(context, app, model, model_id, title):
    context['shortname'] = settings.DISQUS_WEBSITE_SHORTNAME
    context['identifier'] = "%s.%s.%s" % (app, model, model_id)
    context['title'] = title

    return context


class DisqusCommentsCountNode(template.Node):
    def render(self, context):
        # print context
        pass

@register.simple_tag
def disqus_comments_count(
    app, model, model_id, as_string=False,
    string_template="{count} comment{plural}"
):
    thread_id = "%s.%s.%s" % \
                (app, model, model_id)

    count = 0

    try:
        thread = Thread.objects.get(identifier=thread_id)
        count = thread.comment_set.count()
    except Thread.DoesNotExist:
        pass

    if not as_string:
        return count
    else:
        return string_template.format(**{
            "count": count,
            "plural": "s" if count != 1 else "",
        })


@register.inclusion_tag("disqus/recent_comments.html", takes_context=True)
def disqus_recent_comments(context, max_comments=5):
    context['comments'] = Comment.objects.filter(approved=True) \
        .order_by("-id")[:max_comments]

    return context

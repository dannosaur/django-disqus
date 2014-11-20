import json
import pprint
import urllib
import urllib2
from django.conf import settings


class Client(object):
    api_url = "https://disqus.com/api/3.0"

    def list_posts(self, **kwargs):
        response = self.request(
            endpoint="forums/listPosts",
            data=kwargs
        )

        # pprint.pprint(response)
        return response

    def thread_details(self, thread_id):
        request_kwargs = {}

        if thread_id.isdigit():
            request_kwargs['thread'] = thread_id
        else:
            request_kwargs['thread:ident'] = thread_id

        response = self.request(
            endpoint="threads/details",
            data=request_kwargs
        )

        # pprint.pprint(response)
        return response

    def request(self, endpoint, method="GET", data=None):
        data['forum'] = settings.DISQUS_WEBSITE_SHORTNAME
        data['api_key'] = settings.DISQUS_API_KEY

        url = "%s/%s.json" % (self.api_url, endpoint)

        if method == "POST":
            request = urllib2.Request(url, data)
        else:
            params = urllib.urlencode(data)
            url = "%s?%s" % (url, params)

            print url

            request = urllib2.Request(url)

        response = urllib2.urlopen(request).read()

        return json.loads(response)

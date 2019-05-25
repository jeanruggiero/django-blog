from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import Post


class LatestEntriesFeed(Feed):
    title = "Latest blog posts"
    link = ""
    description = "Latest posts published to my blog"

    def items(self):
        return Post.objects.all().order_by('-published_date')[:5]

    def item_title(self, item):
        return item.title

    def item_content(self, item):
        return item.content

    def item_link(self, item):
        return reverse('blog_detail', args=[item.pk])

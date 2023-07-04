from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from blog.models import Post,Category
from django.urls import reverse
from django.utils.feedgenerator import Atom1Feed

class LatestPostsFeed(Feed):
	title="WeBlog"
	link=""
	description="New blog posts"
	feed_type = Atom1Feed

	def items(self):
		return Post.objects.filter(status=Post.PUBLISHED)

	def item_title(self,item):
		return item.title

	def item_description(self,item):
		return truncatewords(item.intro,50)
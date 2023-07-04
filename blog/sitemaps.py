from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from blog.models import Post,Category

class CategorySiteMap(Sitemap):
	def items(self):
		return Category.objects.all()


class PostSiteMap(Sitemap):
	def items(self):
		return Post.objects.filter(status=Post.PUBLISHED)

	def lastmod(self, obj):
		return obj.updated


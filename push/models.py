from django.db import models
from certify.models import Account

# Create your models here.


class About(models.Model):
	title=models.CharField(max_length=100)
	author_of_the_book=models.CharField(max_length=100)
	publisher=models.CharField(max_length=)
	isbn=models.CharField(max_length=100)
	year_of_publication=models.IntegerField()
	number_of_pages=models.IntegerField()





class Main(models.Model):
	student=models.ForeignKey(Account.get_ful_name(), related_name='user', on_delete=models.CASCADE)
	about=models.ForeignKey(About,related_name='about',on_delete=models.CASCADE)


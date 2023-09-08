from django.db import models
from certify.models import Account
from ckeditor.fields import RichTextField
from jsignature.fields import JSignatureField
# Create your models here.


class About(models.Model):
	title=models.CharField(max_length=100)
	author_of_the_book=models.CharField(max_length=100)
	publisher=models.CharField(max_length=)
	isbn=models.CharField(max_length=100)
	year_of_publication=models.IntegerField()
	number_of_pages=models.IntegerField()


class Recommendation(models.Model):
	parent_comment=RichTextField(max_length=1000)
	parent_signature=JSignatureField()
	teacher_comment=RichTextField(max_length=1000)
	teacher_signature=JSignatureField()

# In your form template

# {{ form.media }}
# <form action="" method="post">
#     {{ form }}
#     <input type="submit" value="Save" />
#     {% csrf_token %}
# </form>
# Render image from db value in your display template:

# {# yourtemplate.html #}
# {% load jsignature_filters %}

# <img src="{{ obj.signature|signature_base64 }}" alt="{{ obj }}" />


class Main(models.Model):
	student=models.ForeignKey(Account.get_ful_name(), related_name='user', on_delete=models.CASCADE)
	about=models.ForeignKey(About,related_name='about',on_delete=models.CASCADE)
	summary=RichTextField(max_length=500)
	moral_lessons_learnt=RichTextField(max_length=1000)
	part_i_like_best_and_why=RichTextField(max_length=1000)
	main_character_in_the_story=models.CharField(max_length=100)
	is_the_story_fiction=models.BooleanField(default=None)
	why_fiction_or_non_fiction=RichTextField(max_length=1000)
	literally_devices_used_in_the_story=RichTextField(max_length=1000)
	new_words_learnt_with_their_meaning=RichTextField(max_length=5000)
	three_synonym_words_each_to_the_words_learnt=RichTextField(max_length=5000)
	three_antonym_words_each_to_the_words_learnt=RichTextField(max_length=5000)
	date_started=models.DateTimeField(default=None)
	date_completed=models.DateTimeField(default=None) 
	recommendation=models.ForeignKey(Recommendation,related_name='recommendation',on_delete=models.CASCADE)
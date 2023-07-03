from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from django.utils import timezone
import uuid
from django.contrib.auth import get_user_model

#initializing user with django contrib auth
User=get_user_model()
# ---------------Create your models here.--------------------
#-------------The Category Model---------------------------------
class Category(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title
    
    #sitemap for blog category
    def get_absolute_url(self):
        return '/%s/' % self.slug



#-------------The Post Model---------------------------------
class Post(models.Model):

    #blog post  status option's key and value 
    PUBLISHED = 'PUBLISHED'
    DRAFT = 'DRAFT'

    CHOICES_STATUS = (
        (PUBLISHED, 'PUBLISHED'),
        (DRAFT, 'DRAFT')
    )
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = RichTextField(max_length=400)
    body = RichTextUploadingField()
    author=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=PUBLISHED)
    thumbnail=models.ImageField(upload_to='uploads/thumbnail')
    class Meta:
        ordering = ('created_at',)
    
    def __str__(self):
        return self.title

    #sitemap for blog post
    def get_absolute_url(self):
        return '/%s/%s/' % (self.category.slug, self.slug)


#---------------------------------------Comment-------------------------
class Comment(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    #email = models.EmailField()
    message =  RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)
    #reply=models.ForeignKey("self",on_delete=models.CASCADE,null=True)
    

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return 'Comment {} by {}'.format(self.message1[1:30], self.title)

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class BlogInfo(models.Model):
    logo = models.ImageField(upload_to='blog_info', blank=True, null=True)
    about = models.TextField(blank=True)
    facebook_link = models.URLField(blank=True)
    twitter_link = models.URLField(blank=True)
    instagram_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)
    youtube_link = models.URLField(blank=True)
    pinterest_link = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    class Meta:
        verbose_name_plural = 'Blog info'


class UserDescription(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='description')
    profile_image = models.ImageField(upload_to='profile_images', blank=True, null=True)
    position = models.CharField(max_length=100, blank=True)
    about_me = models.TextField(blank=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    instagram_link = models.URLField(blank=True)
    facebook_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)
    twitter_link = models.URLField(blank=True)
    def __str__(self):
        return self.user.get_full_name()


class Category(models.Model):
    thumbnail = models.ImageField(upload_to='Category', default=None)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name    

class Image(models.Model):
    name = models.CharField(max_length=50, default=None)
    image = models.ImageField(upload_to='Article', default=None)
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    

class Article(models.Model):
    thumbnail = models.ImageField(upload_to='Article', default=None)
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    headline = models.CharField(max_length=200)
    content = RichTextUploadingField(blank=True,null=True)
    categories = models.ForeignKey(
        Category, on_delete=models.CASCADE, default=True, null=False)
    read_time = models.CharField(max_length=100, blank=True)
    tags = models.ManyToManyField(Tag)
  
    
    def __str__(self):
        return self.headline
  

class Comment(models.Model):
    post = models.ForeignKey(Article,on_delete=models.CASCADE,related_name='comments')
    website = models.URLField(blank=True)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
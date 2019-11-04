from django.db import models
from django.conf import settings
# Create your models here.
class Keyword(models.Model) :
    name=models.CharField(max_length=30)
    key_image=models.TextField()
    like_users=models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='like_keywords')
class Movie(models.Model):
    title=models.TextField()
    #user 의 N개의 post
    baged_users=models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='bagging_movies', blank=True)
    keywords=models.ManyToManyField(Keyword,blank=True, related_name='movies')
    code=models.TextField()
    imageUrl=models.TextField()
    is_like=models.TextField(blank=True,default=False)
    @property
    def like_count(self) :
        return self.baged_users.count()
        
class Image(models.Model) :
    mv_key_img = models.TextField()
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)

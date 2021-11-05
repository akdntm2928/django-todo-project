from django.db import models
from django.urls import reverse

from photo.fields import ThumbnailImageField
from django.contrib.auth.models import User

class Album(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField('One Line Description',max_length=100,blank=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)

    class Meta:
        ordering=('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('photo:album_detail',args=(self.id,))

class Publication(models.Model):
    title = models.CharField(max_length=30)
    albums = models.ManyToManyField(Album,null=True)

class Photo(models.Model):
    album =models.ForeignKey(Album,on_delete=models.CASCADE)
    title =models.CharField('TITLE',max_length=30)
    description =models.TextField('Photo Description',blank=True)
    image =ThumbnailImageField(upload_to='photo/%Y/%m')
    upload_dt = models.DateTimeField('Upload Date',auto_now_add=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)

    class Meta:
        ordering= ('title',)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('photo:photo_detail',args=(self.id,))
# Create your models here.

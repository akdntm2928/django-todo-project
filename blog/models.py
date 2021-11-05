from django.db import models

# Create your models here.

from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(verbose_name='TITLE',max_length=50)
    slug  = models.SlugField('SLUG',unique=True, allow_unicode=True , help_text='one word for title alias.')
    description =models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text.')
    content =models.TextField('CONTENT')
    create_dt =models.DateTimeField('CREATE DATE',auto_now_add=True)
    modify_dt =models.DateTimeField('MODIFY DATE',auto_now =True)
    tags =TaggableManager(blank=True)
    owner =models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)

    class Meta:
        verbose_name ='post'
        verbose_name_plural ='posts'
        db_table ='blog_posts'
        ordering =("-modify_dt",)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse( 'blog:post_detail' ,args=(self.slug,))
    
    def get_previous(self):
        return self.get_previous_by_modify_dt()
    
    def get_next(self):
        return self.get_next_by_modify_dt()
    def save(self,*args,**kwargs):# 모델에 객체내용을 저장하는 메소드
        self.slug = slugify(self.title,allow_unicode=True) #title을 slugify에서 변환시켜 slug필드에 객체에 채워넣음
        super().save(*args, **kwargs) # 객체을 모델에 저장



    
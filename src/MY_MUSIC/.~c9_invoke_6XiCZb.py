# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.
class Album(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    artist=models.CharField(max_length=120)
    album_title=models.CharField(max_length=120)
    genre=models.CharField(max_length=120)
    album_logo=models.ImageField(upload_to='photos/%Y/%m/%d/%s', null=True,blank=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    def __unicode__(self):
        return self.album_title
    def get_absolute_url(self):
        return reverse("detail",kwargs={"id":self.id})
        
class Songs(models.Model):
    album=models.ForeignKey(Album,on_delete=models.CASCADE)
    song_title=models.CharField(max_length=120,null=True,blank=True)
    audio_file=models.FileField(upload_to='audio/%Y/%m/%d')
    is_favourite=models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    def __unicode__(self):
        return self.song_title
        
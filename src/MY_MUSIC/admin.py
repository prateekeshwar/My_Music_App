# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Album, Songs
# Register your models here.
class AlbumModelAdmin(admin.ModelAdmin):
    list_display=["album_title","timestamp","updated"]
    list_filter=["updated","timestamp"]
    search_fields=["album_title","artist"]
    class Meta:
        model = Album
class SongsModelAdmin(admin.ModelAdmin):
    list_display=["song_title","timestamp","updated"]
    list_filter=["updated","timestamp"]
    search_fields=["song_title"]
    class Meta:
        model = Songs        
admin.site.register(Album,AlbumModelAdmin)
admin.site.register(Songs,SongsModelAdmin)
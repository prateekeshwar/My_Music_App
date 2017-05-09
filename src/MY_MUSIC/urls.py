from django.conf.urls import url

from MY_MUSIC import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^create/', views.create, name='create'),
    url(r'^(?P<id>\d+)/', views.detail, name='detail'),
    url(r'^add_songs/', views.add_songs, name='add_songs'),
    url(r'^update/(?P<id>\d+)/', views.update, name='update'),
    url(r'^delete/(?P<id>\d+)/', views.delete, name='delete'),
    url(r'^register/', views.register, name='register'),
    url(r'^login/', views.user_login, name='login'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^logout/', views.user_logout, name='logout'),
    url(r'^song_player/(?P<id>\d+)/', views.song_player, name='song_player'),
    ]
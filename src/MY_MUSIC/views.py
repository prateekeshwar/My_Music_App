# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404,redirect
from .models import Album, Songs
from .forms import AlbumForm,UserForm,SongsForm
# Create your views here.
def home(request):
    queryset_list=Album.objects.all()
    paginator = Paginator(queryset_list, 5) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context={
        'title':'Album List',
        'album_list':queryset,
    }    
   
    return render(request, "home.html", context)
    
def detail(request,id=None):
    instance=get_object_or_404(Album ,id=id)
    song_list = instance.songs_set.all()
    context={
        'title':'Album Detail',
        'instance':instance,
        'song_list':song_list,
    }
    return render(request, "album_detail.html", context)

def create(request):
    if not request.user.is_authenticated():
        raise Http404
    form1=AlbumForm(request.POST or None, request.FILES or None)
    if form1.is_valid():
        instance=form1.save(commit=False)
        instance.user = request.user
        # instance.album_logo = form1.cleaned_data['album_logo']
        instance.save()
        messages.success(request,"Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request,"Not Successfully Created")
    context={
        "form1":form1,
    }
    return render(request, "form1.html", context)
    
def update(request,id=None):
    if not request.user.is_authenticated():
        raise Http404
    instance=get_object_or_404(Album ,id=id)
    song_list = instance.songs_set.all()
    form1=AlbumForm(request.POST or None,request.FILES or None,instance=instance)
    if form1.is_valid():
        instance=form1.save(commit=False)
        instance.user = request.user
        instance.album_logo = form1.cleaned_data['album_logo']
        instance.save()
        messages.success(request,"Updated")
        return HttpResponseRedirect(instance.get_absolute_url())
    context={
        'title':'Album Update',
        'instance':instance,
        'song_list':song_list,
        'form1':form1
        
    }
    return render(request, "form1.html", context)  
    
def add_songs(request):
    if not request.user.is_authenticated():
        raise Http404
    form2=SongsForm(request.POST or None, request.FILES or None)
    if form2.is_valid():
        # import ipdb; ipdb.set_trace()
        instance=form2.save(commit=False)
        # instance.album = request.album
        # instance.album_logo = form1.cleaned_data['album_logo']
        instance.save()
        messages.success(request,"Successfully Created")
        # return HttpResponseRedirect(instance.get_absolute_url())
        return HttpResponseRedirect(reverse("MY_MUSIC:detail", kwargs={'id': instance.album.id}))
    else:
        messages.error(request,"Not Successfully Created")
    context={
        "form2":form2,
    }
    return render(request, "form2.html", context)



    
def delete(request,id=None):
    if not request.user.is_authenticated():
        raise Http404
    instance=get_object_or_404(Album ,id=id)
    instance.delete()
    messages.success(request,"Deleted")
    return redirect("MY_MUSIC:home")
    
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print user_form.errors
    else:
        user_form = UserForm()
    return render(request,'register.html',{'user_form': user_form,'registered': registered} )
    
    
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Your MY_MUSIC account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'login.html', {})

@login_required    
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")
    
    
    
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/logout/')
    
    
    
def song_player(request, id=None):

    
    instance = Songs.objects.get(id=id)
    context = {
        "instance":instance,
    }
    return render(request, 'player.html', context)
    

    
    
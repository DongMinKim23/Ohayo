from django.shortcuts import render,redirect,get_object_or_404
from .models import Keyword,Movie
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
import requests, pprint
# Create your views here.

def index(request) :
    keywords=Keyword.objects.all()
    movies=Movie.objects.all()
    if request.user.is_authenticated :
        user=request.user
        if user.like_keywords.all() :
            return redirect('movies:content')
    context={
        'keywords':keywords,
        'movies':movies
    }
    return render(request,'movies/index.html',context)
    
def main(request):
    return render(request, 'movies/main.html')
    
# def show_movies(request) :
#     user=request.user
#     movies=Movie.objects.all()
#     movie_list=[]
#     if user.like_keywords.all() :
#         for user_keyword in user.like_keywords.all() :
#             for movies in user_keyword.movies.all() :
#                 if movies not in movie_list :
#                     movie_list.append(movies)
#         print(movie_list)
#         return render(request,'movies/show_movies.html',{'user_keywords':user.like_keywords.all(),'movies':movie_list})
#     else :
#         return redirect('movies:index')

def like_keyword(request,keyword_pk) :
    keyword=get_object_or_404(Keyword,pk=keyword_pk)
    user=request.user
    print(keyword)
    print(user)
    if keyword not in user.like_keywords.all() :
        user.like_keywords.add(keyword)
        is_like=True
        
    else :
        user.like_keywords.remove(keyword)
        is_like=False
    return JsonResponse({'is_like':is_like})
    
def select(request):
    keywords = Keyword.objects.all()
    context = {'keywords': keywords}
    return render(request, 'movies/select.html', context)
    
def clear(request):
    request.user.like_keywords.clear()
    return redirect('movies:index')

@login_required
def like_movie(request,movie_pk) :
    movie=get_object_or_404(Movie,pk=movie_pk)
    user=request.user
    if user in movie.baged_users.all():
        movie.baged_users.remove(user)
        movie.is_like = False
        movie.save()
        
    else :
        movie.baged_users.add(user)
        movie.is_like = True
        movie.save()
    return JsonResponse({})
    
def content(request):
    user=request.user
    movies=Movie.objects.all()
    movie_list=[]
    if user.like_keywords.all() :
        for user_keyword in user.like_keywords.all() :
            for movies in user_keyword.movies.all() :
                if movies not in movie_list :
                    movie_list.append(movies)
        print(movie_list)
        return render(request,'movies/content.html',{'user_keywords':user.like_keywords.all(),'movies':movie_list})
    else :
        return redirect('movies:index')
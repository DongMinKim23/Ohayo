from django.urls import path
from . import views

app_name ='movies'

urlpatterns = [
    path('',views.index, name='index'),
    path('main', views.main, name='main'),
    path('select/', views.select, name='select'),
    path('clear/', views.clear, name='clear'),
    # path('show_movies/',views.show_movies,name='show_movies'),
    path('<int:keyword_pk>/like/',views.like_keyword,name='like_keyword'),
    path('<int:movie_pk>/movie_like/',views.like_movie,name='like_movie'),
    path('content/', views.content, name='content'),
    
]
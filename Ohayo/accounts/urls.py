from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('my_movie/',views.my_movie,name='my_movie'),
    path('my_movie/<int:movie_pk>/delete/',views.my_movie_delete,name='my_movies_delete'),
]
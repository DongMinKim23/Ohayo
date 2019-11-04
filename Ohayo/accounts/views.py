from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import UserCustomCreationForm
# Create your views here.

def signup(request):
    if request.method == "POST":
        signup_form = UserCustomCreationForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            auth_login(request,user)
            return redirect('accounts:login')
    else:
        signup_form = UserCustomCreationForm()
    context = {'signup_form': signup_form}
    return render(request, 'accounts/signup2.html', context)

def login(request):
    if request.method == "POST":
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
            return redirect('movies:main')
    else:
        login_form = AuthenticationForm()
    context = {'login_form': login_form}
    return render(request, 'accounts/login2.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('movies:main')
    
@login_required
def my_movie(request) :
    User=request.user
    my_movies=User.bagging_movies.all()
    return render(request,'accounts/my_movie.html',{'my_movies':my_movies})
    
@login_required
def my_movie_delete(request,movie_pk) :
    User=request.user
    movie=User.bagging_movies.get(pk=movie_pk)
    movie.delete()
    return redirect('accounts:my_movie')

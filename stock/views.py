from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

def index(request):
    return render(request, 'frontend/index.html')
def games(request):
    return render(request, 'frontend/games.html')
def about(request):
    return render(request, 'frontend/about.html')
def login(request):
    return render(request, 'frontend/login.html')
def signup(request):
    return render(request, 'frontend/signup.html')
def account(request):
    return render(request, 'frontend/myaccount.html')
def about(request):
    return render(request, 'frontend/about.html')
def change_password(request):
    return render(request, 'frontend/change_password.html')

def adduser(request):
    username=request.POST['username']
    email=request.POST['email']
    password=request.POST['password']
    pwd_confirm=request.POST['pwd_confirm']

    if password == pwd_confirm :
        if User.objects.filter(username=username).exists():
            messages.info(request,'This username has been used.')
            return redirect('/signup')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'This email has been used.')
            return redirect('/signup')
        else :
            user=User.objects.create_user(
            username=username,
            email=email,
            password=password,
            )
            user.save()
            return redirect('/')
    else :
        messages.info(request, 'Passwords do not match.')
        return redirect('/signup')

def userin(request):
    username=request.POST['username']
    password=request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None :
        auth.login(request,user)
        return redirect('/')
    else :
        messages.info(request,'Username or Password is wrong.')
        return redirect('/login')

def userout(request):
    auth.logout(request)
    return redirect('/')
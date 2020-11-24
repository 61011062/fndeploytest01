from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('games', views.games, name='games'),
    path('about-fngame', views.about, name='about-fngame'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('myaccount', views.account, name='myaccount'),
    path('adduser', views.adduser, name='adduser'),
    path('userin', views.userin, name='userin'),
    path('userout', views.userout, name='userout'),
    path('change_password', views.change_password, name='change_password'),
]

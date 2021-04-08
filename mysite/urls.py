from django.urls import path

from mysite import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.userSignup, name='Usersignup'),
]
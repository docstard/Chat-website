from django.urls import path

from mysite import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.userSignup, name='Usersignup'),
    path('login/', views.login, name='Login'),
    path('volsignup/', views.volSignup, name='Volsignup'),
    path('logout/',views.logout,name='logout'),
]
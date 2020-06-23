from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('', views.render_home, name='luna-home'),
    path('botpage/',views.render_botpage,name='luna-bot-welcome'),
    path('botpage/login/',auth_views.LoginView.as_view(template_name='luna/login.html'),name='luna-bot-login'),
    path('botpage/signup/',views.render_signup,name='luna-bot-signup'),
    path('botpage/logout/',auth_views.LogoutView.as_view(template_name='luna/logout.html'),name='luna-bot-logout'),
   
]

from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.render_home, name='luna-home'),
    path('botpage/',views.render_botpage,name='luna-bot-welcome'),
    path('botpage/login/',views.render_login,name='luna-bot-login'),
    path('botpage/signup/',views.render_signup,name='luna-bot-signup')
   
]

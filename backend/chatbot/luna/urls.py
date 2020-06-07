from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.render_home, name='luna-home'),
    path('botpage/',views.render_botpage,name='luna-bot-welcome')
   
]

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def SayHello(request):
    return HttpResponse('<h1>Hello Bitches</h1> ')

def render_home(request):
    return render(request,'luna/index.html')

def render_botpage(request):
    return render(request,'luna/botpage.html')
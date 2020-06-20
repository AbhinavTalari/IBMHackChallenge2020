from django.shortcuts import render
from django.http import HttpResponse

from .forms import UserRegisterForm
# Create your views here.
def SayHello(request):
    return HttpResponse('<h1>Hello Bitches</h1> ')

def render_home(request):
    return render(request,'luna/index.html')

def render_botpage(request):
    return render(request,'luna/greet.html')

def render_login(request):
    return render(request,'luna/login.html')


def render_signup(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            
    else:
        form=UserRegisterForm()
    return render(request,'luna/signup.html',{'form':form})
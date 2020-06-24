from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate,login

from .forms import UserRegisterForm
from django.template.context import RequestContext
# Create your views here.
def SayHello(request):
    return HttpResponse('<h1>Hello Bitches</h1> ')

def render_home(request):
    return render(request,'luna/index.html')

def render_botpage(request):
    return render(request,'luna/greet.html')


def render_welcome(request):
    return render(request,'luna/profile.html')

def render_login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
                login(request, user)
                return HttpResponseRedirect('/profile.html')
     
        else:
            state = "Your email and/or password were incorrect."

        state = "Please log in below..."

    context = RequestContext(request, {
        'state': state   })
    return render('luna/login.html',{},context)
    



def render_signup(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home.html')
        
            
    else:
        form=UserRegisterForm()
    return render(request,'luna/signup.html',{'form':form})





    
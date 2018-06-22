from django.shortcuts import render
from .forms import login,signup
# Create your views here.
def index(request):
    return render(request,'app1/index.html')
def contact(request):
    return render(request,'app1/contact.html')

def Login(request):
    form = login()
    return render(request,'app1/login.html',{ 'form':form,})
def Signup(request):
    form = signup()
    return render(request,'app1/signup.html',{ 'form':form,})

from django.shortcuts import render
from .forms import login,signup
from django.http import HttpResponse
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
def mklogin(request):
    form = login(request.POST)
    if form.is_valid() :
        name = form.cleaned_data['User_Name']
        password = form.cleaned_data['Password']
        return render(request,'app1/mklogin.html',{ 'name':name,'password':password })
    else :
        return HttpResponse("Invalid Form ")

def mksignup(request):
    form = signup(request.POST)
    if form.is_valid() :
        data = {
        'Name' : form.cleaned_data['User_Name'],
        'First-Name' : form.cleaned_data['First_Name'],
        'Last_Name' : form.cleaned_data['Last_Name'],
        'Email' : form.cleaned_data['Email'],
        #Profile_Pic = forms.ImageField()
        'Password' : form.cleaned_data['Password'],
        }
        return render(request,'app1/mksignup.html',{ 'data':data})
    else :
        return HttpResponse("Invalid Form ")

from django.shortcuts import render,redirect
from .forms import login,signup
from django.http import HttpResponse
from .models import Users
def index(request):
    if request.session.get('is_login') :
        return render(request,'app1/index.html',{'flag':1,})
    else :
        return render(request,'app1/index.html',{'flag':0,})
def contact(request):
    if request.session.get('is_login') :

        return render(request,'app1/contact.html',{'flag':1})
    else :
        return render(request,'app1/contact.html',{'flag':0})

def Login(request):
    if request.session.get('is_login') :
        return redirect('http://localhost/',{ 'flag':1})
    else :
        form = login()
        return render(request,'app1/login.html',{ 'form':form,})
def Signup(request):
    if request.session.get('is_login') :
        return redirect('http://localhost/',{ 'flag':1})
    else :
        form = signup()
        return render(request,'app1/signup.html',{ 'form':form,})
def mklogin(request):
    form = login(request.POST)
    if form.is_valid() :
        name = form.cleaned_data['User_Name']
        password = form.cleaned_data['Password']
        try :
            ob1 = Users.objects.get(User_Name=name)
            p = ob1.Password
            if p == password :
                request.session['is_login'] = 1
                return render(request,'app1/index.html',{ 'flag':1})
            else :
                form = login()
                error = "Incorrect Password Please Try Again".format(name)
                return redirect('/login/',{'form':form,'nouser':error,})
        except Exception as e :
            form = login()
            error = "No such User with Name {} Exist in Our System".format(name)
            return redirect('/login/',{'form':form,'nouser':error,})
        #return render(request,'app1/mklogin.html',{ 'name':name,'password':password })
    else :
        return HttpResponse("Invalid Form ")

def mksignup(request):
    form = signup(request.POST)
    if form.is_valid() :
        data = {
        'User_Name' : form.cleaned_data['User_Name'],
        'First_Name' : form.cleaned_data['First_Name'],
        'Last_Name' : form.cleaned_data['Last_Name'],
        'Email' : form.cleaned_data['Email'],
        #Profile_Pic = forms.ImageField()
        'Password' : form.cleaned_data['Password'],
        }
        ob1 = Users.objects.create(**data)
        return render(request,'app1/mksignup.html',{ 'data':data})
    else :
        return HttpResponse("Invalid Form ")
def about(request):
    if request.session.get('is_login') :
        return render(request,'app1/index.html',{ 'flag' : 1})
    else :
        return render(request,'app1/index.html',{ 'flag' : 0})
def profile(request):
    return render(request,'app1/profile.html')
def logout(request):
    del request.session['is_login']
    return redirect('http://localhost',{ 'flag':0 })
    

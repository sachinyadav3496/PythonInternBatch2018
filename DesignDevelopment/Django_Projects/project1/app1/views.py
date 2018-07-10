from django.shortcuts import render
from django.http import HttpResponse
from .forms import Login
# Create your views here.
def index(request):
    form = Login()
    return render(request,'app1/index.html',{'form':form})
    #return HttpResponse("<h1 style='color:green'>Welcome App1</h1>")
def hello(request):
    return render(request,'app1/hello.html')
    #return HttpResponse("<h1 style='color:yellowgreen'>Hello World by App1 </h1>")
def login(request):
    form = Login(request.POST)
    if form.is_valid():
        name = form.cleaned_data['UserName']
        password = form.cleaned_data['Password']
        return HttpResponse('Welcome {} with {}'.format(name,password))
    else :
        return "Error!!!Form is in not proper format."
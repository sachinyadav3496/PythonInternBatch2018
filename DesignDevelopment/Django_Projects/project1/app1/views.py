from django.shortcuts import render
from django.http import HttpResponse
from .forms import Login,SignUp
from .models import Users
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
        try :
            u = Users.objects.get(UserName=name)
            p = u.Password
            if password == p :
                data = {
                'User Name' : u.UserName,
                'First Name' : u.FirstName,
                'Last Name' : u.LastName,
                'Email' : u.Email,
                }
                return  render(request,'app1/index.html',{'flag':True,'data':data,})

            else :
                error = "Error!!!Invalid Password"
                form = Login()
                return render(request,'app1/index.html',{'error':error,'form':form})


        except Exception as e :
            error = "Error!!!No such User Exists Please SignUP"
            form = Login()
            return render(request,'app1/index.html',{'error':error,'form':form})

        #return HttpResponse('Welcome {} with {}'.format(name,password))
    else :
        return "Error!!!Form is in not proper format."

def signup(request):

    form = SignUp()
    return render(request,'app1/signup.html',{ 'form':form })

def adduser(request):
    form = SignUp(request.POST)
    if form.is_valid():
        return HttpResponse('Sucess')
    else :
        return HttpResponse('Something Wrong')


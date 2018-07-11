from django import forms

class Login(forms.Form):

    UserName = forms.CharField(max_length=100)
    Password = forms.CharField(max_length=100,widget=forms.PasswordInput)

class SignUp(forms.Form):
    UserName = forms.CharField(max_length=100)
    Password = forms.CharField(max_length=100,widget=forms.PasswordInput)
    FirstName = forms.CharField(max_length=100)
    LastName = forms.CharField(max_length=100)
    Email = forms.EmailField(widget=forms.EmailInput)
    Pic = forms.ImageField()

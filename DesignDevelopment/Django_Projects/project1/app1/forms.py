from django import forms

class Login(forms.Form):

    UserName = forms.CharField(max_length=100)
    Password = forms.CharField(max_length=100,widget=forms.PasswordInput)

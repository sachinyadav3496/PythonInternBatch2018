from django.urls import path
from . import views
urlpatterns = [
path('',views.index,name='home'),
path('contact/',views.contact,name='contact'),
path('login/',views.Login,name='login'),
path('signup/',views.Signup,name='signup'),
]

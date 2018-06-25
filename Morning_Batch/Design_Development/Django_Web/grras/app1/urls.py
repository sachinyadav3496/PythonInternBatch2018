from django.urls import path
from . import views
urlpatterns = [
path('',views.index,name='home'),
path('contact/',views.contact,name='contact'),
path('login/',views.Login,name='login'),
path('signup/',views.Signup,name='signup'),
path('mklogin/',views.mklogin,name='mklogin'),
path('mksignup/',views.mksignup,name='mksignup'),
path('profile/',views.profile,name='profile'),
path('about/',views.about,name='about'),
path('logout/',views.logout,name='logout'),
]

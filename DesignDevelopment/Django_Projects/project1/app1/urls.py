from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    path('hello/',views.hello,name='hello'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('adduser/',views.adduser,name='adduser'),

]
from django.urls import path
from .views import *
urlpatterns = [
     path('',home,name="home"),
    path('home/',home,name="home"),
    path('blog/',blog,name="blog"),
    path('About/',About,name="About"),
    path('cart/',cart,name="cart"),
    path('contact/',contact,name="contact"),
    path('shop/',shop,name="shop"),  
    path('login/',log_in,name="log_in"),
    path('register/',register,name="register"),
    path('logout/',log_out,name="log_out"),
    path('change_password/',change_password,name="change_password"),
]
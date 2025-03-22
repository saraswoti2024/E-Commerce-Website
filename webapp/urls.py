from django.urls import path
from django.contrib.auth import views as auth_views
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
    path('profileboard/',profileboard,name="profileboard"),
    path('profile_edit/',profileedit,name="profile_edit"),
    #for forgot password when password is not known end
    path('change_password/',change_password,name="change_password"),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = "auth/password_reset_complete.html"), name='password_reset_complete'),
       #for forgot password when password is not known end
]
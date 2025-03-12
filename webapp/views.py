from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product,Users
from django.contrib import messages 
from django.contrib import messages
from django.db.models import Q
from django.core.mail import send_mail,EmailMessage
from django.template.loader import render_to_string
from datetime import datetime
from django.contrib.auth.models import User
from .models import *
import phonenumbers

# Create your views here.
def home(request):
    return render(request,'webapp/home.html')

def blog(request):
    return render(request,'webapp/blog.html')

def About(request):
    return render(request,'webapp/About.html')

def contact(request):
    if request.method=='POST':
        data = request.POST
        email = data.get('email')
        phone = data.get('ph')
        address = data.get('address')
        message = data.get('message')

        try:
             user = Users(email=email,number=phone,address=address,messages=message)
             user.full_clean() ##models ma vako validate garxa herxa ,thikxa vane save hunxa
             user.save()
             messages.success(request,f" your form submitted successfully")
             return redirect('contact')
        except Exception as e:
            messages.error(request,f"Error: {str(e)}")
            return redirect('contact')
    return render(request,'webapp/contact.html')

def cart(request):
    return render(request,'webapp/cart.html')

def shop(request):
    data = Product.objects.all()
    categoryy = Category.objects.all()

    cateid = request.GET.get('Categ') 
    searched = request.GET.get('searches')  
    if cateid :
        data = Product.objects.filter(Category1=cateid)
 
    elif searched:
        data = Product.objects.filter(title__icontains=searched)

    else:
          data = Product.objects.all()

    context={
        'cate': categoryy,
        'cateid' : cateid,
        'data1' : data,
    }
    return render(request,'webapp/shop.html',context)  ##admin lai use garna abc-> admin page ma hernu

def log_in (request):
    return render(request,'auth/log_in.html')

# def register(request):
#     if request.method=='POST':
#         fname = request.POST['fname']
#         lname = request.POST['lname']
#         uname = request.POST['uname']
#         password = request.POST['password']
#         password1 = request.POST['password1']
#         if password == password1:
#             User.objects.create_user(first_name=fname,last_name=lname,username=uname,password=password)
#             messages.success(request,'Registered Successfully')
#             return redirect('log_in')
#         else:
#             messages.error(request,'password and confirm password should be similar') 
#             return redirect('register')           

#     return render(request,'auth/register.html')
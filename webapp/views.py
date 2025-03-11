from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product,Users
from django.contrib import messages 
from django.contrib import messages
from django.db.models import Q
from django.core.mail import send_mail,EmailMessage
from django.template.loader import render_to_string
from datetime import datetime
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
    # data = product.objects.filter(title="belt")
    # data = product.objects.all()
    searched = request.GET.get('searches')
    if searched:
        data = Product.objects.filter(title__icontains=searched)
    else:
        data = Product.objects.all()
    return render(request,'webapp/shop.html',{'abc':data})  ##admin lai use garna abc-> admin page ma hernu

def log_in (request):
    return render(request,'auth/log_in.html')

def register(request):
    return render(request,'auth/register.html')
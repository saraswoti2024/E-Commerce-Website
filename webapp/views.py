from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product,Users
from django.contrib import messages 


# Create your views here.
def home(request):
    return render(request,'home.html')

def blog(request):
    return render(request,'blog.html')

def About(request):
    return render(request,'About.html')

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
    return render(request,'contact.html')

def cart(request):
    return render(request,'cart.html')

def shop(request):
    # data = product.objects.filter(title="belt")
    # data = product.objects.all()
    searched = request.GET.get('searches')
    if searched:
        data = Product.objects.filter(title__icontains=searched)
    else:
        data = Product.objects.all()
    return render(request,'shop.html',{'abc':data})  ##admin lai use garna abc-> admin page ma hernu


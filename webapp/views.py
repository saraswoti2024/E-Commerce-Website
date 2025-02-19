from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Users

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
    
        user = Users(email=email,number=phone,address=address,messages=message)
        user.save()
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


from django.shortcuts import render
from django.http import HttpResponse
from .models import product

# Create your views here.
def home(request):
    return render(request,'home.html')

def blog(request):
    return render(request,'blog.html')

def About(request):
    return render(request,'About.html')

def contact(request):
    return render(request,'contact.html')

def cart(request):
    return render(request,'cart.html')

def shop(request):
    data = product.objects.all()
    return render(request,'shop.html',{'abc':data})  ##admin lai use garna abc-> admin page ma hernu


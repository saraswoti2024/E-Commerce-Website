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
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
import re
from django.contrib.auth.decorators import login_required
from datetime import datetime
import phonenumbers

# Create your views here.
def home(request):
    return render(request,'webapp/home.html')

@login_required(login_url='log_in')
def blog(request):
    return render(request,'webapp/blog.html')

@login_required(login_url='log_in')
def About(request):
    return render(request,'webapp/About.html')

def contact(request):
    if request.method=='POST':
        data = request.POST
        email = data.get('email')
        phone = data.get('ph')
        address = data.get('address')
        message = data.get('message')
        sliced_email = email[:5]

        try:
             user = Users(email=email,number=phone,address=address,messages=message)
             user.full_clean() ##models ma vako validate garxa herxa ,thikxa vane save hunxa
             user.save()

             ##gmail starts
             subject = "Thank you for Getting in Touch!"
             message = render_to_string('webapp/gmail.html',{'email': sliced_email,'date':datetime.now()})
             from_email = 'saraswotikhadka2k2@gmail.com'
             recipient_list = [email]
             emailmsg = EmailMessage(subject,message,from_email,recipient_list)
             emailmsg.attach_file('webapp/static/images/knit-mitten-top.png')
             emailmsg.send(fail_silently=True)
             ##gmail ends

             messages.success(request,f" your form submitted successfully")
             return redirect('contact')
        except Exception as e:
            messages.error(request,f"Error: {str(e)}")
            return redirect('contact')
    return render(request,'webapp/contact.html')

@login_required(login_url='log_in') #log_in -> url (name="log_in")
def cart(request):
    return render(request,'webapp/cart.html')

@login_required(login_url='log_in')
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

def register(request):
    if request.method=='POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['uname']
        password = request.POST['password']
        password1 = request.POST['password1']
        email = request.POST['email']
        error_messages = []
        if password != password1:
            error_messages.append('password and confirm password should be similar')
        try:
            validate_password(password) ##password's policy
        except ValidationError as e:
            for error in e.messages:
                error_messages.append(error)

        if password == uname:
            error_messages.append('username and password must be different')
           
        # if not re.search(r'[A-Z]',password): #capital letter
        #     error_messages.append('Password must contain at least one capital letter')
           
        # if not re.search(r'\W',password): #specialcharacter
        #     error_messages.append('Password must contain at least one Special character')
       
        if not re.search(r'\d',password): #numbers
            error_messages.append('Password Should at least contain one number')
            
        if not re.search(r'\d',uname):
            error_messages.append('Username should at least contain one numeric value')
            
        if User.objects.filter(username=uname).exists():
            error_messages.append('Username already exists')
           
        if User.objects.filter(email=email).exists():
            error_messages.append('email already exists')
        
        if not error_messages:
            User.objects.create_user(first_name=fname,last_name=lname,username=uname,password=password,email=email)
            messages.success(request,'Registered Successfully,Redirecting to Login page...')
            return redirect('register')
        
        else:
            for error in error_messages:
                messages.error(request,error)
            return redirect('register')           
    return render(request,'auth/register.html')
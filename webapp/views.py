from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
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
from django.contrib.auth import authenticate,login,logout
import phonenumbers
from django.contrib.auth.forms import PasswordChangeForm
from .forms import ContactForms

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
    form = ContactForms()
    if request.method=='POST':
        form = ContactForms(request.POST)
        if form.is_valid(): 
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            address = form.cleaned_data['address']
            phone = form.cleaned_data['phonenumber']
            sliced_email = email[:5]
        try:
             Users.objects.create(email=email,number=phone,address=address,messages=message)
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
    return render(request,'webapp/contact.html',{'form':form})

@login_required(login_url='log_in') #log_in -> url (name="log_in")
def cart(request):
    return render(request,'webapp/cart.html')

@login_required(login_url='log_in')
def shop(request):
    data = Product.objects.all()
    categoryy = Category.objects.all()

    cateid = request.GET.get('Categ') 
    searched = request.GET.get('searches')   #sa
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
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        remember = request.POST.get('remember')

        if not User.objects.filter(username=username).exists():
            messages.error(request,'username doesnot exist')
            return redirect('log_in')
        userauth = authenticate(username=username,password=password)
        if userauth is not None:
            login(request,userauth) ##creates session gives login access
            if remember:
                request.session.set_expiry(120000000)
            else:
                request.session.set_expiry(0)   
            next1 = request.POST.get('next','')
            if next1 and next1 != 'None' and next1 != '':  
                return redirect(next1)  # Redirect to the 'next' URL if it's valid
            else:
                return redirect('home')
        else:
            messages.error(request,'invalid password')
            return redirect('log_in')
    next = request.GET.get('next')
    return render(request,'auth/log_in.html',{'next': next})

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

# logout(request):
# Clears the session.
# Logs out the user.
def log_out(request):
    logout(request)
    return redirect('home')


##password change

@login_required(login_url='log_in')
def change_password(request):
    form = PasswordChangeForm(user=request.user) #empty form is created oldp,newp,confp blank
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user,data = request.POST) #user-> tyo user lai lyauxa, data-> oldp,conp,newp lekoeko lai data ma store garxa value in dict form which is as below 
#         request.POST = {
#     'old_password': 'current_password_123', #lee12, 
#     'new_password1': 'new_password_123',
#     'new_password2': 'new_password_123',
# } 
        if form.is_valid(): #oldp and newp matches, length complexity of password herxa
            form.save() #saves the newp  in database
            return redirect('log_in')
    return render(request,'auth/change_password.html',{'form': form})

def profileboard(request):
    return render(request,'profile/profileboard.html')

def profileedit(request):
    return render(request,'profile/profile_edit.html')
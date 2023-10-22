from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login
from django.contrib import messages
from .models import userProfile
from django.core.mail import send_mail
from django.conf import settings
import random
from django.contrib.auth import update_session_auth_hash

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('Username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            auth_login(request,user)
            messages.success(request, 'User Login')
            return redirect('home')
        else:
            messages.warning(request, 'User Not Found')
            return redirect('login')
    return render(request,'accounts/index.html')

def sinup(request):
    
    if request.method =='POST':
        Firstname=request.POST.get('name')
        Username=request.POST.get('Username')
        email=request.POST.get('email')
        Password=request.POST.get('Password')
        ConfirmPassword=request.POST.get('password2')
        if len(Password)<8:
            messages.success(request, "Profile pass must be 8 character.")
        else:
            if Password:
                a = []
                b = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
                c = []
                d = ['&', '$', '#', '@', '*', '!', '_', '/', '-']
                for i in b:
                    if i in Password:
                        a.append(i)
                for i in d:
                    if i in Password:
                        c.append(i)
                if len(a)!=0 and len(c)!= 0:
                    if Password==ConfirmPassword:
                        if User.objects.filter(username=Username).exists():
                            messages.success(request, "Profile Username Already Taken.")
                        elif User.objects.filter(email=email).exists():
                            messages.success(request, "Profile Email Already Taken.")
                        else:
                            user=User.objects.create_user(first_name=Firstname,username=Username,email=email,password=Password)
                            user.set_password(Password)
                            user.save()
                            messages.success(request, "Profile Created.")
                            return redirect('login')
                    else:
                        messages.warning(request, "Profile Password not Matched.")
                else:
                    messages.warning(request, "enter minimum 1 number and 1 special character in your password.(1-9,@,$,/)")
                
    return render(request,'accounts/sinup.html')


def signout(request):
    logout(request)
    return redirect('login')

def forget_pass(request):
    otp = random.randint(1111111,9999999)
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            if email:
                send_mail_registration(email, otp)
                user = User.objects.get(email=email)
                if user:
                    try:
                        prof = userProfile.objects.get(user=user)
                        if prof:
                            prof.otp=otp
                            prof.save()
                            return redirect('verify_otp')
                    except:
                        prof =userProfile.objects.create(user=user,otp=otp)
                        prof.save()
                        return redirect ('verify_otp') 
        except:
            messages.warning(request,"User Not Found.")  
            return redirect('forget_pass')             
    return render(request, 'accounts/forget_pass.html')

def verify_otp(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('pass')
        otp = request.POST.get('otp')
        user = User.objects.get(email=email)
        if user:
            prof = userProfile.objects.get(user = user)
            if prof.otp == otp:
                if len(password)<8:
                    messages.success(request, "Profile pass must be 8 character.")
                else:
                    if password:
                        a = []
                        b = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
                        c = []
                        d = ['&', '$', '#', '@', '*', '!', '_', '/', '-']
                        for i in b:
                            if i in password:
                                a.append(i)
                        for i in d:
                            if i in password:
                                c.append(i)
                        if len(a)!=0 and len(c)!= 0:
                            user.set_password(password)
                            user.save()
                            update_session_auth_hash(request, user)
                            messages.success(request, "User Password Changed.")
                            return redirect('login')
                        else:
                            messages.warning(request, "enter minimum 1 number and 1 special character in your password.(1-9,@,$,/)")
            else:
                messages.warning(request, "Otp not matched Try again.")
                    
                        
                
    return render(request, 'accounts/verify_otp.html')

def resetpassword(request):
    
    if request.method == 'POST':
        oldpass = request.POST.get('oldpass')
        newpass = request.POST.get('newpass')
        conpass = request.POST.get('conpass')
        user =User.objects.get(id=request.user.id)
        check =user.check_password(oldpass)
        if check:
            user.set_password(newpass)
            user.save()
            messages.success(request, " Password Changed Successfully")
            return redirect('home')
        else:
            messages.success(request, " your old password not caret")
    return render(request,'accounts/password_chang.html')

def send_mail_registration(email, otp):
    subject = "Account Verification otp"
    message = f'hi your verify otp is :  {otp}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
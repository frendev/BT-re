from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from contacts.models import Contact
# Create your views here.

def register(request):

    if request.method=="POST":
        #GET FORM VALUES
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']

        #check if passwords match

        if password==password2:
            #check username
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username is already taken!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'Email is in Use!')
                    return redirect('register')
                else:
                    #everything is passed
                    user=User.objects.create_user(username=username,email=email,password=password,first_name=first_name,last_name=last_name)
                    user.save()
                    messages.success(request,'You are now registered and can Login!')
                    return redirect('login')

        else:
            messages.error(request,'Passwords Do Not Match!')
            return redirect('register')

    else:
        return render(request,'accounts/register.html')

def login(request):
    if request.method=="POST":
        #Login User
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request,"You are logged in successfully")
            return redirect('dashboard')

        else:
             messages.error(request,"Invalid credentials")
             return redirect('login')
            
    else:
        return render(request,'accounts/login.html')

def dashboard(request):
    user_contacts=Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context={
        'contacts':user_contacts
    }
    return render(request,'accounts/dashboard.html',context)

def logout(request):
    if request.method=='POST':
        auth.logout(request)
        messages.success(request,'You are now logged out')
        return redirect('index')